## 第4章：目的地

### 什么是 目的地

Logback 将日志记录事件写入到名为`appender`的组件的任务。`Appender`必须实现该`ch.qos.logback.core.Appender` 接口。这个接口的突出方法总结如下：

    package ch.qos.logback.core;
  
    import ch.qos.logback.core.spi.ContextAware;
    import ch.qos.logback.core.spi.FilterAttachable;
    import ch.qos.logback.core.spi.LifeCycle;
    

    public interface Appender<E> extends LifeCycle, ContextAware, FilterAttachable {

        public String getName();
        public void setName(String name);
        void doAppend(E event);
    
    }

Appender 接口中的大多数方法都是`setter`和`getter`。一个值得注意的例外是使用 `doAppend()`类型为`E`的对象实例 作为其唯一参数。`E`的实际类型 将取决于logback模块。在logback-classic模块中，E将是类型为`ILoggingEvent`， 并且在logback访问模块内，它将是`AccessEvent`类型。该`doAppend()`方法可能是logback框架中最重要的。它负责将合适格式的日志记录事件输出到适当的输出设备。

Appender 是命名实体。这样可以确保它们可以通过名称进行引用，质量被确认为在配置脚本中起作用。该Appender接口扩展`FilterAttachable`接口。因此，一个或多个过滤器可以附加到追加器实例。过滤器将在后续章节中详细讨论。

Appenders 最终负责输出日志记录事件。但是，他们可以将事件的实际格式委托给一个`Layout`或一个`Encoder`对象。每个`Layout`/`Encoder`与唯一的一个追加器相关联，称为所有的追加器。一些`appender`具有内置或固定的事件格式。因此，它们不需要`Layout`/`Encoder`。例如，在`SocketAppender`通过网络传输之前，简单地将记录事件序列化。

### AppenderBase

`ch.qos.logback.core.AppenderBase`类是`Appender`接口的抽象实现类。它提供了所有`appender`共享的基本功能，例如获取或设置其名称，激活状态，`Layout`和过滤器的方法。logback 所有`appender`的超级类别都带有。虽然一个抽象类， 实际上在接口中实现了这个 `doAppend()` 方法。讨论课程的最简单方法也许是通过介绍实际源代码的摘录。

    public synchronized void doAppend(E eventObject) {

        // prevent re-entry.
        if (guard) {
            return;
        }

        try {
            guard = true;

            if (!this.started) {
                if (statusRepeatCount++ < ALLOWED_REPEATS) {
                    addStatus(new WarnStatus(
                        "Attempted to append to non started appender [" + name + "].",this));
                }
            return;
            }

            if (getFilterChainDecision(eventObject) == FilterReply.DENY) {
                return;
            }
            
            // ok, we now invoke the derived class's implementation of append
            this.append(eventObject);

        } finally {
            guard = false;
        }
    }

该`doAppend()`方法的这种实现是同步的。因此，从不同的线程进入到同一个`appender`是安全的。虽然线程（如T）正在执行该doAppend()方法，但其他线程的后续调用将排队等待，直到T离开该`doAppend()`方法，确保T独占访问该追加程序。

因为这样的同步并不总是适当的，所以与其`ch.qos.logback.core.UnsynchronizedAppenderBase`类似的logback 是非常相似的`AppenderBase` 。为了简洁起见，我们将`UnsynchronizedAppenderBase`在本文件的其余部分进行讨论 。

该`doAppend()`方法的第一件事是检查`guard`是否设置为true。如果是，它立即退出。如果未设置`guard`，则在下一条语句中设置为true。以确保该`doAppend()`方法不会递归调用自身。想象一下，一个名为某个地方的组件`append()`，想要记录某些东西。它的调用可以被引导到刚刚调用它的相同的`appender`，导致无限循环和堆栈溢出.

在下面的语句中，我们检查该`started`字段是否 为`true`。如果没有， `doAppend()`将发送一条警告消息并返回。换句话说，一旦追加者关闭，就不可能传递给它。 Appender对象实现了 `LifeCycle`接口，这意味着他们实现 `start()`，`stop()`和 `isStarted()`方法。在设置了`appender`的所有属性之后，Joran，logback的配置框架，调用该 `start()`方法来通知`appender`激活其属性。取决于它的种类，如果某些属性丢失或者由于各种属性之间的干扰，附件可能无法启动。例如，鉴于文件创建取决于截断模式，在“Append”选项的值也可以确定的情况下，`FileAppender`不能对其`File`选项的值进行操作。显式的激活步骤确保一个`appender`在其值被知​​道后对其属性起作用。

如果`appender`无法启动，或者停止运行，将通过logback的内部状态管理系统发出警告消息。经过几次尝试，为了避免内部状态系统溢出同一警告消息的副本，该`doAppend()`方法将停止发出这些警告。

下一个`if语句`检查所附过滤器的结果。根据过滤器链所产生的决定，可以拒绝或明确接受事件。在没有过滤器链的决定的情况下，默认情况下接受事件。

该`doAppend()`方法然后调用派生类的`append()`方法的实现。该方法将事件附加到适当的设备。

最后，`guard`被释放，以允许随后调用该`doAppend()`方法。

对于本手册的其余部分，我们为通过`setter`和`getter`方法使用JavaBeans内省动态推断的任何属性保留术语“选项”或“属性”。

### Logback-core 

Logback-core构建了其他Logback模块的基础。一般来说，logback-core中的组件需要一些虽然很小的定制。然而，在接下来的几个部分中，我们将介绍几个可以开箱即用的`appender`。

### OutputStreamAppender

`OutputStreamAppender` 将事件追加到`java.io.OutputStream`。这个类提供其他`appender`建立的基本服务。用户通常不`OutputStreamAppender`直接实例化对象，因为通常`java.io.OutputStream` 类型不能方便地映射到字符串，因为无法`OutputStream`在配置脚本中指定目标对象。简单来说，您不能 `OutputStreamAppender`从配置文件配置。但是，这并不意味着`OutputStreamAppender` 缺少可配置的属性。接下来描述这些属性。

<table>
    <tbody>
        <tr>
            <th>Property Name</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
        <tr>
            <td>
                <b>encoder</b>
            </td>
            <td>
                <a href="../xref/ch/qos/logback/core/encoder/Encoder.html"><code>Encoder</code></a>
            </td>
            <td>
                确定事件写入底层的方式OutputStreamAppender。编码器在专门的<a href="https://logback.qos.ch/manual/encoders.html">章节中进行了说明</a>。
			</td>
         </tr>
        <tr>
            <td>
                <a>
                    <span class="anchor"></span></a><b><span class="prop" name="immediateFlush">immediateFlush</span></b>
            </td>
            <td>
                <code>boolean</code>
            </td>
            <td>
               `immediateFlush`的默认值为“true”。立即刷新输出流确保记录事件立即写出，如果您的应用程序退出而不正确关闭追加程序，则不会丢失该事件。另一方面，将此属性设置为“false”可能会增加四倍（您的里程可能会有所不同）记录吞吐量。再次，如果 immediateFlush设置为“false”，并且如果在应用程序退出时app app未正确关闭，则记录事件尚未写入磁盘可能会丢失。
            </td>
        </tr>
	</tbody>
</table>

该`OutputStreamAppender`是超一流的其他三个附加目的地，即`ConsoleAppender`， `FileAppender`这又是超一流的 `RollingFileAppender`。下图说明了`OutputStreamAppender`其类别及其子类的类图。

![图](./images/appenderClassDiagram.jpg)

### ConsoleAppender

顾名思义，附加在控制台上，或者更准确地说上的System.out或 System.err的，前者是默认的目标。在用户指定的编码器的帮助下格式化事件。编码器将在后面的章节中讨论。双方的System.out和System.err的 是类型。因此，它们被包裹在缓冲器I / O操作中。

<table>
	<tbody>
        <tr>
			<th>Property Name</th>
			<th>Type</th>
			<th>Description</th>
		</tr>
		<tr>
			<td><a name="conAppEncoder" href="#conAppEncoder"><span class="anchor"></span></a><b><span class="prop" container="conApp">encoder</span></b></td>
            <td>
                <a  href="https://logback.qos.ch/xref/ch/qos/logback/core/encoder/Encoder.html"><code>Encoder</code></a>
            </td>
			<td>查看OutputStreamAppender属性。</td>
		</tr>
		<tr>
			<td><a name="conAppTarget" href="#conAppTarget"><span class="anchor"></span></a><b><span class="prop" container="conApp">target</span></b></td>
			<td><code>String</code></td>
			<td>
				其中一个String值System.out或 System.err。默认目标是System.out。
			</td>
		</tr>
		<tr>
			<td><a name="conAppWithJansi" href="#conAppWithJansi"><span class="anchor"></span></a><b><span class="prop" container="conApp">withJansi</span></b></td>
			<td><code>boolean</code></td>
			<td>默认情况下，Jansi属性设置为false。设置withJansi以true激活 Jansi库，它提供了在Windows机器ANSI颜色代码的支持。在Windows主机上，如果此属性设置为true，则应在类路径上放置“org.fusesource.jansi：jansi：1.9”。请注意，基于Unix的操作系统（如Linux和Mac OS X）默认支持ANSI颜色代码。
			</td>
		</tr>
	</tbody>
</table>

这是一个使用的示例配置 ConsoleAppender。

示例：ConsoleAppender配置(logback-examples/src/main/resources/chapters/appenders/conf/logback-Console.xml)

    <configuration>

        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
            <!-- encoders are assigned the type
                ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
            <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg %n</pattern>
            </encoder>
        </appender>

        <root level="DEBUG">
            <appender-ref ref="STDOUT" />
        </root>
    </configuration>

将当前路径设置为 logback-examples目录并设置您的类路径后，可以通过发出以下命令给上述配置文件：

    java chapters.appenders.ConfigurationTester src/main/java/chapters/appenders/conf/logback-Console.xml

### FileAppender

该`FileAppender`子类`OutputStreamAppender`将日志事件追加到文件中。目标文件由`File`选项指定。如果文件已经存在，则根据append属性的值将其附加到或截短 。

`立即刷新`默认情况下，每个日志事件立即刷新到底层输出流。这种默认方法更安全，因为如果您的应用程序退出而不正确关闭追加程序，则记录事件不会丢失。但是，为了显着增加日志记录吞吐量，您可能需要将`immediateFlush`属性设置为`false`。

以下是一个配置文件的示例 FileAppender：

示例：FileAppender配置(logback-examples / src / main / resources / chapters / appenders / conf / logback-fileAppender.xml)

    <configuration>
        <appender name="FILE" class="ch.qos.logback.core.FileAppender">
            <file>testFile.log</file>
            <append>true</append>
            <!-- set immediateFlush to false for much higher logging throughput -->
            <immediateFlush>true</immediateFlush>
            <!-- encoders are assigned the type
                ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
            <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
            </encoder>
        </appender>
                
        <root level="DEBUG">
            <appender-ref ref="FILE" />
        </root>
    </configuration>

将当前目录更改为 logback-examples后，通过启动以下命令运行此示例：

    java chapters.appenders.ConfigurationTester
   src/main/java/chapters/appenders/conf/logback-fileAppender.xml

### 唯一命名的文件（按时间戳）

在应用程序开发阶段或短期应用程序（例如批处理应用程序）的情况下，最好在每次新的应用程序启动时创建一个新的日志文件。这在`<timestamp>`元素的帮助下很容易。这是一个例子。

示例：按时间戳(logback-examples/src/main/resources/chapters/appenders/conf/logback-timestamp.xml)

    <configuration>

        <!-- Insert the current time formatted as "yyyyMMdd'T'HHmmss" under
            the key "bySecond" into the logger context. This value will be
            available to all subsequent configuration elements. -->
        <timestamp key="bySecond" datePattern="yyyyMMdd'T'HHmmss"/>

        <appender name="FILE" class="ch.qos.logback.core.FileAppender">
            <!-- use the previously created timestamp to create a uniquely
                named log file -->
            <file>log-${bySecond}.txt</file>
            <encoder>
            <pattern>%logger{35} - %msg%n</pattern>
            </encoder>
        </appender>

        <root level="DEBUG">
            <appender-ref ref="FILE" />
        </root>
    </configuration>

`timestamp`元素需要两个必需属性`key`和`datePattern` 以及一个可选的`timeReference` 属性。所述关键属性是时间戳将提供给后续配置元件在其下键的名称作为变量。所述`datePattern`属性表示用于将当前时间（在该配置文件被解析）转换成一个字符串的时间图案。日期模式应遵循`SimpleDateForma`t中定义的约定。所述 `timeReference`属性表示用于时间戳的时间参考。默认是配置文件的解释/解析时间，即 当前时间。然而，在某些情况下，将上下文生成时间用作时间参考可能是有用的。这可以通过将`timeReference`属性设置为``contextBirth``。

`<timestamp>`通过运行命令来实现元素：

    java chapters.appenders.ConfigurationTester src/main/resources/chapters/appenders/conf/logback-timestamp.xml

要使用记录器上下文生成日期作为时间参考，您可以将`timeReference`属性设置为``contextBirth``，如下所示。

示例：使用上下文生成日期作为时间引用的时间戳记(logback-examples/src/main/resources/chapters/appenders/conf/logback-timestamp-contextBirth.xml)

    <configuration>
        <timestamp key="bySecond" datePattern="yyyyMMdd'T'HHmmss" 
                    timeReference="contextBirth"/>
        ...
    </configuration>

### RollingFileAppender

`RollingFileAppender`扩展`FileAppender`具有翻转日志文件的功能。例如，`RollingFileAppender`可以登录到名为log.txt文件的文件，一旦满足某个条件，将其日志目标更改为另一个文件。

有两个重要的子组件进行交互`RollingFileAppender`。第一 `RollingFileAppender`个子组件，即 `RollingPolicy`（见下文）负责进行翻转所需的操作。`RollingFileAppende`r即 `TriggeringPolicy`，（见下文）的第二个子组件 将决定是否和何时发生翻转。因此，`RollingPolicy`负责 做什么和`TriggeringPolicy`负责什么时候。

要有任何用处，`RollingFileAppender`必须有一个`RollingPolicy`和一个`TriggeringPolicy`设置。但是，如果它 `RollingPolicy`也实现了 `TriggeringPolicy`接口，那么只需要明确指定前者。

以下是可用的属性RollingFileAppender：

<table class="bodyTable striped">
     <tbody><tr>
       <th>Property Name</th>
       <th>Type</th>
       <th>Description</th>
     </tr>
     <tr>
       <td><a name="rfaFile" href="#rfaFile"><span class="anchor"></span></a><b><span class="prop" container="rfa">file</span></b></td>
       <td><code>String</code></td>
       <td>See <code>FileAppender</code> properties.</td>
     </tr>	
     <tr>
       <td><a name="rfaAppend" href="#rfaAppend"><span class="anchor"></span></a><b><span class="prop" container="rfa">append</span></b></td>
       <td><code>boolean</code></td>
       <td>See <code>FileAppender</code> properties.</td>
     </tr>	
     <tr>
       <td><a name="rfaEncoder" href="#rfaEncoder"><span class="anchor"></span></a><b><span class="prop" container="rfa">encoder</span></b></td>
       <td>
         <a href="../xref/ch/qos/logback/core/encoder/Encoder.html"><code>Encoder</code></a>
       </td>
       <td>See <code>OutputStreamAppender</code> properties.</td>
     </tr>
     <tr>
       <td><a name="rfaRollingPolicy" href="#rfaRollingPolicy"><span class="anchor"></span></a><b><span class="prop" container="rfa">rollingPolicy</span></b></td>
       <td><code>RollingPolicy</code></td>
       <td>This option is the component that will dictate
       <code>RollingFileAppender</code>'s behavior when rollover
       occurs. See more information below.
       </td>
     </tr>	
     <tr>
       <td><a name="rfaTriggeringPolicy" href="#rfaTriggeringPolicy"><span class="anchor"></span></a><b><span class="prop" container="rfa">triggeringPolicy</span></b></td>
       <td><code>TriggeringPolicy</code></td>
       <td>
         This option is the component that will tell 
         <code>RollingFileAppender</code> when to activate the rollover
         procedure. See more information below.
       </td>
     </tr>	
     <tr>
       <td valign="top"><a name="prudentWithRolling" href="#prudentWithRolling"><span class="anchor"></span></a><b><span class="prop" name="prudentWithRolling">prudent</span></b></td>
       <td valign="top"><code>boolean</code></td>
       <td valign="top">
         <a href="#FixedWindowRollingPolicy"><code>FixedWindowRollingPolicy</code></a>
         is not supported in prudent mode.
         <p> <code>RollingFileAppender</code> supports the prudent
         mode in conjunction with <a href="#TimeBasedRollingPolicy"><code>TimeBasedRollingPolicy</code></a>
         albeit with two restrictions.
         </p>
         <ol>
           <li>In prudent mode, file compression is not supported nor
           allowed. (We can't have one JVM writing to a file while
           another JVM is compressing it.)  </li>
           <li>The <span class="prop">file</span> property of
           <code>FileAppender</code> cannot be set and must be left
           blank. Indeed, most operating systems do not allow renaming
           of a file while another process has it opened.
           </li>
         </ol>
         See also properties for <code>FileAppender</code>.
       </td>
     </tr>
   </tbody>
</table>

### 滚动政策概述

`RollingPolicy` 负责涉及文件移动和重命名的翻转过程。

该`RollingPolicy`界面介绍如下：

    package ch.qos.logback.core.rolling;  

    import ch.qos.logback.core.FileAppender;
    import ch.qos.logback.core.spi.LifeCycle;

    public interface RollingPolicy extends LifeCycle {

        public void rollover() throws RolloverFailure;
        public String getActiveFileName();
        public CompressionMode getCompressionMode();
        public void setParent(FileAppender appender);
    }

该`rollover`方法完成归档当前日志文件所涉及的工作。`getActiveFileName()`调用该 方法来计算当前日志文件的文件名（其中写入实时日志）。如`getCompressionMode`方法所示，`RollingPolicy`还负责确定压缩模式。最后，`RollingPolicy`通过该`setParent`方法给出了对其父代的引用。

### TimeBasedRollingPolicy

`TimeBasedRollingPolicy`可能是最受欢迎的滚动政策。它基于时间来定义翻转策略，例如按日或按月。 `TimeBasedRollingPolicy`承担翻车的责任以及触发所述翻车的责任。事实上， `TimeBasedTriggeringPolicy`实现双方 `RollingPolicy`和`TriggeringPolicy`接口。

`TimeBasedRollingPolicy`的配置需要一个强制的`fileNamePattern`属性和几个可选属性。

    /// 表说明...

### 大小和时间滚动政策

有时，您可能希望按日期本质上归档文件，但同时限制每个日志文件的大小，特别是如果后处理工具对日志文件施加大小限制。为了解决这个要求，随身携带 `SizeAndTimeBasedRollingPolicy`。

请注意，`TimeBasedRollingPolicy`已经允许限制归档日志文件的组合大小。如果您只希望限制日志存档的组合大小，那么 `TimeBasedRollingPolicy`上面描述的和设置`totalSizeCap`属性应该是足够的。

这是一个示例配置文件，演示基于时间和大小的日志文件归档.

示例：SizeAndTimeBasedFNATP(logback-examples/src/main/resources/chapters/appenders/conf/logback-sizeAndTime.xml)

    <configuration>
        <appender name="ROLLING" class="ch.qos.logback.core.rolling.RollingFileAppender">
            <file>mylog.txt</file>
            <rollingPolicy class="ch.qos.logback.core.rolling.SizeAndTimeBasedRollingPolicy">
            <!-- rollover daily -->
            <fileNamePattern>mylog-%d{yyyy-MM-dd}.%i.txt</fileNamePattern>
            <!-- each file should be at most 100MB, keep 60 days worth of history, but at most 20GB -->
            <maxFileSize>100MB</maxFileSize>    
            <maxHistory>60</maxHistory>
            <totalSizeCap>20GB</totalSizeCap>
            </rollingPolicy>
            <encoder>
            <pattern>%msg%n</pattern>
            </encoder>
        </appender>


        <root level="DEBUG">
            <appender-ref ref="ROLLING" />
        </root>

    </configuration>

请注意除`%d`之外的`%i`转换令牌。`%i`和`%d`令牌都是强制性的。每当当前日志文件在当前时间段结束之前达到`maxFileSize`时，它将以0的增加索引进行归档。

基于大小和时间的归档支持删除旧的归档文件。您需要使用`maxHistory`属性指定要保留的句点数。当您的应用程序停止并重新启动时，日志记录将继续在正确的位置，即当前时段的最大索引号。

在之前的版本1.1.7，该文件提到一个叫做组件`SizeAndTimeBasedFNATP`。然而，鉴于`SizeAndTimeBasedFNATP`提供了更简单的配置结构，我们不再记录`SizeAndTimeBasedFNATP`。然而，早期的配置文件使用`SizeAndTimeBasedFNATP`将继续工作正常。实际上 `SizeAndTimeBasedRollingPolicy`是用一个`SizeAndTimeBasedFNATP`子组件实现的 。

### FixedWindowRollingPolicy

滚动后，如下所述，根据固定窗口算法重命名文件:FixedWindowRollingPolicy

该fileNamePattern选项代表了存档（滚过）日志文件的文件名模式。此选项是必需的，并且必须在模式中的某处包含整数令牌 ％i。

以下是可用的属性 FixedWindowRollingPolicy

<table>
     <tbody><tr>
       <th>Property Name</th>
       <th>Type</th>
       <th>Description</th>
     </tr>
     <tr>
       <td><a name="fwrpMinIndex" href="#fwrpMinIndex"><span class="anchor"></span></a><b><span class="prop" container="fwrp">minIndex</span></b></td>
       <td><code>int</code></td>
       <td>
         <p>This option represents the lower bound for the window's
         index.
         </p>
       </td>
     </tr>
     <tr>
       <td><a name="fwrpMaxIndex" href="#fwrpMaxIndex"><span class="anchor"></span></a><b><span class="prop" container="fwrp">maxIndex</span></b></td>
       <td><code>int</code></td>
       <td>
         <p>This option represents the upper bound for the window's
         index.
         </p>
       </td>
     </tr>
     <tr>
       <td><a name="fwrpFileNamePattern" href="#fwrpFileNamePattern"><span class="anchor"></span></a><b><span class="prop" container="fwrp">fileNamePattern</span></b></td>
       <td><code>String</code></td>
       <td>
         <p>This option represents the pattern that will be followed
         by the <code>FixedWindowRollingPolicy</code> when renaming
         the log files. It must contain the string <em>%i</em>, which
         will indicate the position where the value of the current
         window index will be inserted.
         </p>
         <p>For example, using <em>MyLogFile%i.log</em> associated
         with minimum and maximum values of <em>1</em> and <em>3</em>
         will produce archive files named <em>MyLogFile1.log</em>,
         <em>MyLogFile2.log</em> and <em>MyLogFile3.log</em>.
         </p>
         <p>Note that file compression is also specified via this
         property. For example, <span class="prop">fileNamePattern</span> set to
         <em>MyLogFile%i.log.zip</em> means that archived files must be
         compressed using the <em>zip</em> format; <em>gz</em> format
         is also supported.
         </p>
       </td>
     </tr>			
   </tbody>
</table>

鉴于固定窗口滚动策略需要与窗口大小一样多的文件重命名操作，因此强烈地不鼓励大窗口大小。当用户指定大值时，当前的实现将自动将窗口大小减小到20。

我们来看一个更具体的固定窗口翻转策略的例子。假设minIndex设置为1，maxIndex设置为 3，fileNamePattern属性设置为foo％i.log，该文件 属性设置为foo.log。

<table>
     <tbody><tr>
       <th>Number of rollovers</th>
       <th>Active output target</th>
       <th>Archived log files</th>
       <th>Description</th>
     </tr>
		<tr>
			<td>0</td>
			<td>foo.log</td>
			<td>-</td>
			<td>No rollover has happened yet, logback logs into the initial
			file.
			</td>
     </tr>		
     <tr>
       <td>1</td>
       <td>foo.log</td>
       <td>foo1.log</td>
       <td>First rollover. <em>foo.log</em> is renamed as
       <em>foo1.log</em>. A new <em>foo.log</em> file is created and
       becomes the active output target.
       </td>
     </tr>
     <tr>
       <td>2</td>
       <td>foo.log</td>
       <td>foo1.log, foo2.log</td>
       <td>Second rollover. <em>foo1.log</em> is renamed as
       <em>foo2.log</em>.  <em>foo.log</em> is renamed as
       <em>foo1.log</em>. A new <em>foo.log</em> file is created and
       becomes the active output target.
       </td>
     </tr>
     <tr>
       <td>3</td>
       <td>foo.log</td>
       <td>foo1.log, foo2.log, foo3.log</td>
       <td>Third rollover.  <em>foo2.log</em> is renamed as
       <em>foo3.log</em>. <em>foo1.log</em> is renamed as
       <em>foo2.log</em>.  <em>foo.log</em> is renamed as
       <em>foo1.log</em>. A new <em>foo.log</em> file is created and
       becomes the active output target.
       </td>
     </tr>
     <tr>
       <td>4</td>
       <td>foo.log</td>
       <td>foo1.log, foo2.log, foo3.log</td>
       <td>In this and subsequent rounds, the rollover begins by
       deleting <em>foo3.log</em>. Other files are renamed by
       incrementing their index as shown in previous steps. In this and
       subsequent rollovers, there will be three archive logs and one
       active log file.
       </td>
     </tr>
   </tbody>
</table>

下面的配置文件给出了配置`RollingFileAppender`和 配置的一个例子 `FixedWindowRollingPolicy`。请注意，`File`选项是强制性的，即使它包含与`fileNamePattern`选项一起传递的一些相同的信息。

示例：`RollingFileAppender`使用`FixedWindowRollingPolicy`(logback-examples/src/main/resources/chapters/appenders/conf/logback-RollingFixedWindow.xml)

    <configuration>
        <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
            <file>test.log</file>

            <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <fileNamePattern>tests.%i.log.zip</fileNamePattern>
            <minIndex>1</minIndex>
            <maxIndex>3</maxIndex>
            </rollingPolicy>

            <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <maxFileSize>5MB</maxFileSize>
            </triggeringPolicy>
            <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
            </encoder>
        </appender>
                
        <root level="DEBUG">
            <appender-ref ref="FILE" />
        </root>
    </configuration>

### 触发政策概述

TriggeringPolicy 实施负责指示 RollingFileAppender何时翻转。

该TriggeringPolicy界面只包含一种方法。

    package ch.qos.logback.core.rolling;

    import java.io.File;
    import ch.qos.logback.core.spi.LifeCycle;

    public interface TriggeringPolicy<E> extends LifeCycle {

        public boolean isTriggeringEvent(final File activeFile, final <E> event);
    }


该`isTriggeringEvent()`方法将当前处理的活动文件和日志记录事件作为参数。具体实现根据这些参数确定是否发生翻转。

最广泛使用的触发政策， `TimeBasedRollingPolicy`也是滚动政策的两倍，已经与其他滚动政策一起早已讨论过了。

### SizeBasedTriggeringPolicy

`SizeBasedTriggeringPolicy`查看当前活动文件的大小。如果它增长到大于指定的大小，它将发出信号`RollingFileAppender`以触​​发现有活动文件的翻转。

`SizeBasedTriggeringPolicy`只接受一个参数，即`maxFileSize`，默认值为`10 MB`。

该`maxFileSize`为选项可以以字节为单位来指定，千字节，由后面添加一个数字值MB或GB KB，MB和分别 GB。例如，500万，5000KB， 5MB和2GB都是有效的值，其中前三个等同。

这是一个示例配置， 当日志文件的大小达到5MB时`RollingFileAppender`结合 `SizeBasedTriggeringPolicy`触发翻转。

示例：`RollingFileAppender`使用 `SizeBasedTriggeringPolicy` （logback-examples/src/main/resources/ chapters /appenders/conf/logback-RollingSizeBased.xml）的示例配置

    <configuration>
        <appender name="FILE" class="ch.qos.logback.core.rolling.RollingFileAppender">
            <file>test.log</file>
            <rollingPolicy class="ch.qos.logback.core.rolling.FixedWindowRollingPolicy">
            <fileNamePattern>test.%i.log.zip</fileNamePattern>
            <minIndex>1</minIndex>
            <maxIndex>3</maxIndex>
            </rollingPolicy>

            <triggeringPolicy class="ch.qos.logback.core.rolling.SizeBasedTriggeringPolicy">
            <maxFileSize>5MB</maxFileSize>
            </triggeringPolicy>
            <encoder>
            <pattern>%-4relative [%thread] %-5level %logger{35} - %msg%n</pattern>
            </encoder>
        </appender>
                
        <root level="DEBUG">
            <appender-ref ref="FILE" />
        </root>
    </configuration>

### Logback Classic

在logback-core中，日志记录事件是通用的，但在logback-classic中，它们总是实例`ILoggingEvent`。Logback-classic只不过是一个专门的处理流程处理实例`ILoggingEvent`。

### SocketAppender和SSLSocketAppender

    //// 日志保存到非本地... 
