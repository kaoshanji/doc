## 第6章：Layouts

## 什么是Layout?

Layout是负责将传入事件转换为字符串的logback组件。 接口中的 `format()`方法Layout接受一个表示事件（任何类型）的对象，并返回一个String。Layout 接口简介如下所示:

    public interface Layout<E> extends ContextAware, LifeCycle {

        String doLayout(E event);
        String getFileHeader();
        String getPresentationHeader();
        String getFileFooter();
        String getPresentationFooter();
        String getContentType();
    }

该接口相当简单，但对于许多格式化需求来说足够。来自德克萨斯州的德克萨斯州的开发人员，你可能从约瑟夫·海勒的“ Catch-22”可能知道，可能会惊叹：实施布局只需要五种方法！

### Logback-classic

Logback-classic连接到只处理类型的事件`ch.qos.logback.classic.spi.ILoggingEvent`,这个事实在本节将会很明显。

### 编写自己的自定义Layout

让我们为logback-classic模块实现一个简单而有功能的布局，该模块打印自应用程序启动以来的时间，记录事件的级别，括号之间的调用者线程，其记录器名称，事件消息后面的破折号和一条新线。

示例输出可能如下所示：

    10489 DEBUG [main] com.marsupial.Pouch - Hello world.

这是一个可能的实施，由德克萨斯州的开发人员撰写：

示例：Layout的示例实现 （logback-examples / src / main / java / chapters / layouts / MySampleLayout.java）

    package chapters.layouts;

    import ch.qos.logback.classic.spi.ILoggingEvent;
    import ch.qos.logback.core.LayoutBase;

    public class MySampleLayout extends LayoutBase<ILoggingEvent> {

        public String doLayout(ILoggingEvent event) {
            StringBuffer sbuf = new StringBuffer(128);
            sbuf.append(event.getTimeStamp() - event.getLoggingContextVO.getBirthTime());
            sbuf.append(" ");
            sbuf.append(event.getLevel());
            sbuf.append(" [");
            sbuf.append(event.getThreadName());
            sbuf.append("] ");
            sbuf.append(event.getLoggerName();
            sbuf.append(" - ");
            sbuf.append(event.getFormattedMessage());
            sbuf.append(CoreConstants.LINE_SEP);
            return sbuf.toString();
        }
    }
    
注意`MySampleLayout`延伸。此类管理所有layout实例的共同状态，例如layout是启动还是停止，页眉，页脚和内容类型数据。它允许开发人员专注于他/她期望的格式 。请注意，该类是通用的。在其类的声明中， 扩展。

该`doLayout(ILoggingEvent event)`方法，即唯一的方法MySampleLayout，通过实例化a开始StringBuffer。它通过添加事件参数的各个字段来进行。如果一个或多个参数与日志记录请求一起传递，这一点很重要。

将这些各种字符添加到字符串缓冲区后，该 `doLayout()`方法将缓冲区转换为a String并返回结果值。

在上面的例子中，该`doLayout`方法忽略了事件中包含的任何最终的异常。在真实世界的布局实现中，你最想打印异常的内容。

### 配置您的自定义布局

自定义layout被配置为任何其他组件。如前所述，`FileAppender`其子类期望编码器。为了满足这个要求，我们传递给`FileAppender`一个`LayoutWrappingEncoder`包装我们 的实例 `MySampleLayout`。这是配置文件：

示例：MySampleLayout的配置（logback-examples / src / main / resources / chapters / layouts / sampleLayoutConfig.xml）

    <configuration>

        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
            <encoder class="ch.qos.logback.core.encoder.LayoutWrappingEncoder">
            <layout class="chapters.layouts.MySampleLayout" />
            </encoder>
        </appender>

        <root level="DEBUG">
            <appender-ref ref="STDOUT" />
        </root>
    </configuration>

示例应用程序使用作为其第一个参数传递的配置脚本配置回溯，然后记录调试消息，后跟一条错误消息。

要运行此示例，请在logback-examples目录中发出以下命令 。

    java chapters.layouts.SampleLogging src / main / java / chapters / layouts / sampleLayoutConfig.xml

这将产生：

    0 DEBUG [main] chapters.layouts.SampleLogging  - 一切进展顺利
    0 ERROR [main] chapters.layouts.SampleLogging  - 也许不完全...

//////貌似并不需要自定义.... 