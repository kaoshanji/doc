## 第2章：编码器

### 什么是编码器

编码器负责将事件转换为字节数组，并将该字节数组写入 OutputStream。编码器在0.9.19版本的对战版本中引入。在以前的版本中，大多数appender依赖于布局来将事件转换为字符串，并使用a写入java.io.Writer。在以前版本的logback中，用户将嵌套PatternLayout在内 FileAppender。由于logback 0.9.19， FileAppender子类期望编码器不再进行布局。

为什么突然变化?

如下一章详细讨论的布局只能将事件转换为String。此外，由于`layout`不能控制事件何时写出，`layout`不能将事件聚合成批。与编码器对比，编码器不仅可以完全控制写入字节的格式，还可以控制何时（如果）这些字节被写出。

目前，`PatternLayoutEncoder`唯一真正有用的编码器。它只是包裹了`PatternLayout`大部分的工作。因此，除了不必要的复杂性，编码器似乎不会带来太多的影响。但是，我们希望随着新的和强大的编码器的出现，这种印象将会改变。

### 编码器接口

编码器负责将传入事件转换为字节数组，并将生成的字节数组写入适当的数组`OutputStream`。因此，编码器可以完全控制什么和什么时候字节被写入`OutputStream`由所有的追加者维护。这是编码器接口：

    package ch.qos.logback.core.encoder;

        public interface Encoder<E> extends ContextAware, LifeCycle {

        /**
        * This method is called when the owning appender starts or whenever output
        * needs to be directed to a new OutputStream, for instance as a result of a
        * rollover.
        */
        void init(OutputStream os) throws IOException;

        /**
        * Encode and write an event to the appropriate {@link OutputStream}.
        * Implementations are free to defer writing out of the encoded event and
        * instead write in batches.
        */
        void doEncode(E event) throws IOException;


        /**
        * This method is called prior to the closing of the underling
        * {@link OutputStream}. Implementations MUST not close the underlying
        * {@link OutputStream} which is the responsibility of the owning appender.
        */
        void close() throws IOException;
    }

您可以看到，该Encoder接口由几种方法组成，但令人惊奇的是，这些方法可以实现许多有用的功能。
 
### LayoutWrappingEncoder

直到logback版本0.9.19，许多`appender`依赖于`Layout`实例来控制日志输出的格式。由于基于布局界面存在大量的代码，我们需要一种编码器与布局进行互操作的方式。`LayoutWrappingEncoder` 桥接了编码器和布局之间的差距。它实现编码器接口并包装一个布局，它将委托将事件转换成字符串的工作。

下面是`LayoutWrappingEncoder`类的摘录，说明如何完成对包装布局实例的委托。

    package ch.qos.logback.core.encoder;

    public class LayoutWrappingEncoder<E> extends EncoderBase<E> {

        protected Layout<E> layout;
        private Charset charset;
        
        // encode a given event as a byte[]
        public byte[] encode(E event) {
            String txt = layout.doLayout(event);
            return convertToBytes(txt);
        }

        private byte[] convertToBytes(String s) {
            if (charset == null) {
            return s.getBytes();
            } else {
            return s.getBytes(charset);
            }
        } 
    }

`doEncode（）`方法是通过使包装的布局将传入的事件转换为字符串来启动的。生成的文本字符串根据用户选择的字符集编码转换为字节。

### PatternLayoutEncoder

鉴于这`PatternLayout`是最常用的布局，logback适用于这种常见的用例` PatternLayoutEncoder`，扩展 `LayoutWrappingEncoder`限制为包装实例`PatternLayout`。

从logback 0.9.19开始，只要一个 `FileAppender`或一个子类配置了`PatternLayout`，则`PatternLayoutEncoder`必须使用。这将在loaback错误代码的相关条目中进行说明。

#### immediateFlush属性

对于`LOGBACK 1.2.0`， `immediateFlush`属性是附加的Appender的一部分.

#### 输出模式字符串作为标题

为了方便解析日志文件，logback可以在日志文件的顶部插入用于日志输出的模式。默认情况下禁用此功能。可以通过将`outputPatternAsHeader` 属性设置为`true`，使其相关 `PatternLayoutEncoder`。这是一个例子：

    <appender name="FILE" class="ch.qos.logback.core.FileAppender"> 
        <file>foo.log</file>
        <encoder>
            <pattern>%d %-5level [%thread] %logger{0}: %msg%n</pattern>
            <outputPatternAsHeader>true</outputPatternAsHeader>
        </encoder> 
    </appender>

这将导致输出类似于日志文件中的以下内容：

    ＃logback.classic pattern：%d [%thread]%-5level%logger {36}  - %msg％n
    2012-04-26 14：54：38,461 [main] DEBUG com.foo.App  -  Hello world
    2012-04-26 14：54：38,461 [main] DEBUG com.foo.App  - 嗨 again
    ...

以“＃logback.classic pattern”开头的行是新插入的模式行。
