## 第3章：配置

我们首先介绍配置 `logback` 的方法，并配置许多示例配置代码.Joran,后备依赖的配置框架将在后面的[章节](chapter11.md)中介绍。

### logback配置

将日志请求插入到应用程序代码中需要大量的规划和努力.观察显示，约4％的代码专用于日志记录.因此，即使中等大小的应用程序将包含嵌入其代码中的数千个日志记录语句.鉴于他们的数量，我们需要工具来管理这些日志语句.

Logback可以通过编程方式配置,也可以使用以XML或Groovy格式表示的配置脚本进行配置.顺便说一下，现有的log4j用户可以使用我们的 [PropertiesTranslator Web应用程序](https://logback.qos.ch/translator/)将其log4j.properties文件转换为logback.xml。

让我们从讨论初始化步骤开始，尝试配置：
1. Logback尝试在 [classpath](https://logback.qos.ch/faq.html#configFileLocation) 里找一个名为 `logback-test.xml` 的文件.
2. 如果没有找到，就找`logback.groovy`.
3. 如果没有找到，就检查 `logback.xml`.
4. 如果没有找到这样的文件，则通过查找文件 `META-INF\services\ch` 来使用 [service-provider](http://docs.oracle.com/javase/6/docs/api/java/util/ServiceLoader.html) 加载工具（在JDK 1.6中引入）来解析 [com.qos.logback.classic.spi.Configurator](https://logback.qos.ch/xref/ch/qos/logback/classic/spi/Configurator.html) 接口的实现类路径中的`qos.logback.classic.spi.Configurator`。其内容应指定所需`Configurator`实现的完全限定类名。
5. 如果以上都没有成功，logback会自动使用`BasicConfigurator`自动配置，这将导致日志输出被导向控制台。

最后一步是在没有配置文件的情况下提供默认（但非常基本的）日志功能的最后一步。

如果您使用 Maven，并且如果将 `logback-test.xml` 放在 `src/test/resources` 文件夹下，Maven 将确保它不会包含在生成的工件中.因此，您可以使用不同的配置文件，即测试期间的`logback-test.xml`，以及生产中的另一个文件，即 `logback.xml` 。

``快速启动`` Joran 需要大约100毫秒才能解析给定的对数配置文件,要在启动时清除这些毫秒数，您可以使用服务提供程序加载工具（以上第4项）将自己的自定义`Configurator类` 与`BasicConfigrator` 一起作为一个好的起点。

### logbakc自动配置

自动配置的最简单的方法是让logback恢复到默认配置，让我们来了解一下如何在一个名为 `MyApp1` 的虚构应用程序中完成这项工作。

例：`BasicConfigurator`使用的简单[示例](https://logback.qos.ch/xref/chapters/configuration/MyApp1.html)

        package chapters.configuration;

        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;

        public class MyApp1 {
            final static Logger logger = LoggerFactory.getLogger(MyApp1.class);

            public static void main(String[] args) {
                logger.info("Entering application.");

                Foo foo = new Foo();
                foo.doIt();
                logger.info("Exiting application.");
            }
        }

这个类定义了静态logger 变量。 然后它实例化一个Foo对象。 Foo代码如下：

例：简单的[日志类](https://logback.qos.ch/xref/chapters/configuration/Foo.html)

        package chapters.configuration;
  
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        
        public class Foo {
            static final Logger logger = LoggerFactory.getLogger(Foo.class);
            
            public void doIt() {
                logger.debug("Did it again!");
            }
        }

为了运行本章中的示例，您需要确保类路径中存在某些`jar文件`.有关详细信息，请参阅[设置页面](https://logback.qos.ch/setup.html)。

假设配置文件 `logback-test.xml` 或 `logback.xml` 不存在，logback将默认调用`BasicConfigurator`，它将设置一个最小配置.此最小配置由连接到根记录器的`ConsoleAppender`组成。输出格式使用`PatternLayoutEncoder`设置为模式`%d {HH：mm：ss.SSS} [%thread]%-5level%logger {36} - %msg%n`。此外，默认情况下，根记录器被分配DEBUG级别。

因此，`java chapters.configuration.MyApp1`命令的输出应该类似于：

    16:06:09.031 [main] INFO  chapters.configuration.MyApp1 - Entering application.
    16:06:09.046 [main] DEBUG chapters.configuration.Foo - Did it again!
    16:06:09.046 [main] INFO  chapters.configuration.MyApp1 - Exiting application.

`MyApp1` 应用程序通过调用 `org.slf4j.LoggerFactory` 和 `org.slf4j.Logger类` 链接到logback，检索其希望使用的记录器，并在其上打开。请注意，`Foo类`在 logback 的唯一依赖关系是通过 `org.slf4j.LoggerFactory` 和 `org.slf4j.Logger` 导入。除了配置logback的代码（如果这样的代码存在），客户端代码不需要依赖于logback。由于`SLF4J`允许在其抽象层下使用任何日志框架，因此很容易将大型代码从一个日志框架迁移到另一个日志框架。

### logback-test.xml or logback.xml 的自动配置

如前所述，logback将尝试使用文件`logback-test.xml`或`logback.xml`来配置自己，如果在类路径中找到的。这是一个等同于我们刚才看到的`BasicConfigurator`建立的配置文件。

例：基本的配置(logback-examples/src/main/resources/chapters/configuration/sample0.xml)

    <configuration>

    <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
        <!-- encoders are assigned the type
            ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
        <encoder>
        <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <root level="debug">
        <appender-ref ref="STDOUT" />
    </root>
    </configuration>

将`sample0.xml`重命名为`logback.xml`（或`logback-test.xml`）后，将其放入可从类路径访问的目录中。 运行`MyApp1`应用程序应该提供与之前的运行相同的结果。

### 警告或错误时自动打印状态信息

如果在配置文件解析期间发生警告或错误，logback 将自动在控制台上打印其内部状态数据。请注意，为避免重复，如果用户明确地注册状态侦听器（如下定义），则禁用自动状态打印。

在没有警告或错误的情况下，如果仍然希望检查logback的内部状态，则可以通过调用`StatusPrinter#print()` 来指示logback打印状态数据。下面显示的`MyApp2`应用程序与`MyApp1`相同，除了添加两行代码以打印内部状态数据。

例：[输出logback状态信息](https://logback.qos.ch/xref/chapters/configuration/MyApp2.html)

    public static void main(String[] args) {
        // assume SLF4J is bound to logback in the current environment
        LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
        // print logback's internal status
        StatusPrinter.print(lc);
        ...
    }

如果一切顺利，您应该在控制台上看到以下输出：

    17:44:58,578 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Found resource [logback-test.xml]
    17:44:58,671 |-INFO in ch.qos.logback.classic.joran.action.ConfigurationAction - debug attribute not set
    17:44:58,671 |-INFO in ch.qos.logback.core.joran.action.AppenderAction - About to instantiate appender of type [ch.qos.logback.core.ConsoleAppender]
    17:44:58,687 |-INFO in ch.qos.logback.core.joran.action.AppenderAction - Naming appender as [STDOUT]
    17:44:58,812 |-INFO in ch.qos.logback.core.joran.action.AppenderAction - Popping appender named [STDOUT] from the object stack
    17:44:58,812 |-INFO in ch.qos.logback.classic.joran.action.LevelAction - root level set to DEBUG
    17:44:58,812 |-INFO in ch.qos.logback.core.joran.action.AppenderRefAction - Attaching appender named [STDOUT] to Logger[root]

    17:44:58.828 [main] INFO  chapters.configuration.MyApp2 - Entering application.
    17:44:58.828 [main] DEBUG chapters.configuration.Foo - Did it again!
    17:44:58.828 [main] INFO  chapters.configuration.MyApp2 - Exiting application.

### 状态数据

不以代码方式调用StatusPrinter，您可以指示配置文件转储状态数据，即使没有错误。要实现此目的，您需要设置配置元素的 `debug` 属性，即配置文件中最顶层的元素，如下所示。请注意，此 `debug` 属性仅与状态数据有关。它不影响logback的配置，否则特别是对于记录器级别。 （如果你问，不，根记录器不会被设置为DEBUG。）

例：debug模式下的基本配置(logback-examples/src/main/resources/chapters/configuration/sample1.xml)

    <configuration debug="true"> 

        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender"> 
            <!-- encoders are  by default assigned the type
                ch.qos.logback.classic.encoder.PatternLayoutEncoder -->
            <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            </encoder>
        </appender>

        <root level="debug">
            <appender-ref ref="STDOUT" />
        </root>
    </configuration>

在`<configuration>`元素中设置debug =“true”将输出状态信息，假设：
1. 此配置文件可以被找到
2. 这个配置文件是XML格式

如果这两个条件中的任何一个不满足，Joran无法解释调试属性，因为配置文件无法读取。如果发现配置文件格式错误，则logback将检测错误状况，并在控制台上自动打印其内部状态。但是，如果找不到配置文件，logback将不会自动打印其状态数据，因为这不一定是错误条件。以上面的`MyApp2`应用程序以编程方式调用`StatusPrinter.print()`可以确保在每种情况下打印状态信息。

``强制状态输出``在没有状态消息的情况下，跟踪本地logback.xml配置文件可能很困难，特别是在生产中，应用程序源无法轻易修改。为了帮助识别本地配置文件的位置，您可以通过`logback.statusListenerClass`系统属性（下面定义）设置`StatusListener`来强制输出状态消息。`logback.statusListenerClass`系统属性也可用于在发生错误时自动生成信息输出。

顺便说一句，设置`debug ='true'`与安装`OnConsoleStatusListener`相当。状态侦听器将在下面进一步讨论。 接下来显示`OnConsoleStatusListener`的安装.

例：注册一个状态监听器(logback-examples/src/main/resources/chapters/configuration/onConsoleStatusListener.xml)

    <configuration>
        <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />  

        ... the rest of the configuration file  
    </configuration>

通过调试属性或通过安装`OnConsoleStatusListener`等效地启用状态数据的输出，将大大有助于您诊断日志问题。因此，非常强烈地建议启用 logback 状态数据，并应将其视为第一解决方案.

### 将默认配置文件的位置指定为系统属性

您可以使用名为`logback.configurationFile`的系统属性指定默认配置文件的位置.此属性的值可以是URL，类路径上的资源或应用程序外部文件的路径。

    java -Dlogback.configurationFile=/path/to/config.xml chapters.configuration.MyApp1

请注意，文件扩展名必须为`.xml`或`.groovy`,其他扩展名将被忽略.[明确注册状态侦听器](https://logback.qos.ch/manual/configuration.html#logback.statusLC)可能有助于调试查找配置文件的问题。

### 修改后自动重新配置配置文件

如果指示这样做，`logback-classic` 将扫描其配置文件中的更改，并在配置文件更改时自动重新配置。为了指示logback-classic 扫描其配置文件中的更改并自动重新配置自身，将`<configuration>`元素的`scan`属性设置为`true`，如下所示。

例：扫描配置文件和自动重新配置的更改(logback-examples/src/main/resources/chapters/configuration/scan1.xml)

    <configuration scan="true"> 
        ... 
    </configuration>

默认情况下，配置文件将每分钟扫描一次.您可以通过设置`<configuration>`元素的`scanPeriod`属性来指定不同的扫描周期。可以以毫秒，秒，分钟或小时为单位指定值。 这是一个例子：

例：指定不同的扫描周期(logback-examples/src/main/resources/chapters/configuration/scan2.xml)

    <configuration scan="true" scanPeriod="30 seconds" > 
        ...
    </configuration> 

``注意`` 如果没有指定时间单位，则假定时间单位为毫秒，这通常是不合适的。 如果更改默认扫描周期，请勿忘记指定时间单位。

幕后，当将`scan`属性设置为`true`时，将安装名为[ReconfigureOnChangeFilter](https://logback.qos.ch/xref/ch/qos/logback/classic/turbo/ReconfigureOnChangeFilter.html)的`TurboFilter`。`TurboFilters`在后面的[章节](chapter07.md)中有描述。因此，扫描是“线程内”完成的，也就是随时调用记录器的打印方法。例如，对于名为`myLogger`的记录器，当您编写`myLogger.debug（"hello"）;`时，如果将`scan`属性设置为`true`，则`ReconfigureOnChangeFilter`将被调用。此外，即使`myLogger`被禁用为DEBUG级别，也将调用所述过滤器。

由于每次调用任何记录器时都会调用`ReconfigureOnChangeFilter`，无论记录器级别如何，`ReconfigureOnChangeFilter`对于性能至关重要。实际上，检查扫描周期是否已经过去，本身就太贵了。为了提高性能，`ReconfigureOnChangeFilter`在每次N个日志记录操作中都是"活着"的一次。根据应用程序记录的频率，N的值可以通过logback进行备份。默认情况下，N为16，尽管对于CPU密集型应用程序，它可以高达2 ^ 16（= 65536）.

简而言之，当配置文件更改时，它将自动重新加载，但只能在几个记录器调用后和扫描周期确定的延迟之后。

### 启用堆栈跟踪中的打包数据

``注意``  从版本1.1.4起，默认情况下禁用打包数据。

如果指示这样做，logback可以包括其输出的堆栈跟踪线的每一行的打包数据。打包数据由jar文件的名称和版本组成，即起始堆栈跟踪行的类。包装数据在识别软件版本控制问题方面非常有用。然而，代价相当昂贵，特别是在频繁抛出异常的应用程序中。 这是一个示例输出：

    14:28:48.835 [btpool0-7] INFO  c.q.l.demo.prime.PrimeAction - 99 is not a valid value
    java.lang.Exception: 99 is invalid
    at ch.qos.logback.demo.prime.PrimeAction.execute(PrimeAction.java:28) [classes/:na]
    at org.apache.struts.action.RequestProcessor.processActionPerform(RequestProcessor.java:431) [struts-1.2.9.jar:1.2.9]
    at org.apache.struts.action.RequestProcessor.process(RequestProcessor.java:236) [struts-1.2.9.jar:1.2.9]
    at org.apache.struts.action.ActionServlet.doPost(ActionServlet.java:432) [struts-1.2.9.jar:1.2.9]
    at javax.servlet.http.HttpServlet.service(HttpServlet.java:820) [servlet-api-2.5-6.1.12.jar:6.1.12]
    at org.mortbay.jetty.servlet.ServletHolder.handle(ServletHolder.java:502) [jetty-6.1.12.jar:6.1.12]
    at ch.qos.logback.demo.UserServletFilter.doFilter(UserServletFilter.java:44) [classes/:na]
    at org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1115) [jetty-6.1.12.jar:6.1.12]
    at org.mortbay.jetty.servlet.ServletHandler.handle(ServletHandler.java:361) [jetty-6.1.12.jar:6.1.12]
    at org.mortbay.jetty.webapp.WebAppContext.handle(WebAppContext.java:417) [jetty-6.1.12.jar:6.1.12]
    at org.mortbay.jetty.handler.ContextHandlerCollection.handle(ContextHandlerCollection.java:230) [jetty-6.1.12.jar:6.1.12]

默认情况下禁用打包数据，但可以通过配置启用打包数据：

    <configuration packagingData="true">
        ...
    </configuration>

或者，可以通过在 `LoggerContext#setPackagingDataEnabled(boolean)`方法来编程地启用/禁用打包数据，如下所示：

    LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
    lc.setPackagingDataEnabled(true);

### 直接调用JoranConfigurator

Logback依赖于一个名为Joran的配置库，它是`logback-core`的一部分.Logback的默认配置机制在类路径上找到的默认配置文件中调用 `JoranConfigurator` 。如果您希望覆盖 logback 的默认配置机制，可以通过直接调用 `JoranConfigurator` 来实现。下一个应用程序 `MyApp3` 在作为参数传递的配置文件上调用`JoranConfigurator`。

例：直接调用 `JoranConfigurator`

    package chapters.configuration;

    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

    import ch.qos.logback.classic.LoggerContext;
    import ch.qos.logback.classic.joran.JoranConfigurator;
    import ch.qos.logback.core.joran.spi.JoranException;
    import ch.qos.logback.core.util.StatusPrinter;

    public class MyApp3 {
        final static Logger logger = LoggerFactory.getLogger(MyApp3.class);

        public static void main(String[] args) {
            // assume SLF4J is bound to logback in the current environment
            LoggerContext context = (LoggerContext) LoggerFactory.getILoggerFactory();
            
            try {
            JoranConfigurator configurator = new JoranConfigurator();
            configurator.setContext(context);
            // Call context.reset() to clear any previous configuration, e.g. default 
            // configuration. For multi-step configuration, omit calling context.reset().
            context.reset(); 
            configurator.doConfigure(args[0]);
            } catch (JoranException je) {
            // StatusPrinter will handle this
            }
            StatusPrinter.printInCaseOfErrorsOrWarnings(context);

            logger.info("Entering application.");

            Foo foo = new Foo();
            foo.doIt();
            logger.info("Exiting application.");
        }
    }

该应用程序将获取当前有效的`LoggerContext`，创建一个新的`JoranConfigurator`，设置它将在其上运行的上下文，重置日志记录器上下文，然后最终要求配置器使用作为参数传递给应用程序的配置文件配置上下文。 打印内部状态数据，以防警告或错误。请注意，对于多步骤配置，应该省略 `context.reset()` 调用。

### 查看状态消息

Logback 在 `StatusManager` 对象中收集其内部状态数据，可通过 `LoggerContext` 进行访问。

给定一个 `StatusManager` ，您可以访问与 logback 上下文相关联的所有状态数据。为了将内存使用保持在合理的级别，默认的`StatusManager`实现将状态消息存储在两个独立的部分中：头部和尾部。 头部部分存储第一 `H` 状态消息，而尾部存储最后的 `T` 消息。目前，H = T = 150，虽然这些值可能会在将来的版本中发生变化。

`Logback-classic` 带有名为 `ViewStatusMessagesServlet` 的 `servlet`。此`servlet`将与当前`LoggerContext` 关联的 `StatusManager`的内容打印为HTML表,这里是示例输出。

![图](images/lbClassicStatus.jpg)

在web应用的 `WEB-INF/web.xml` 文件里添加：

      <servlet>
        <servlet-name>ViewStatusMessages</servlet-name>
        <servlet-class>ch.qos.logback.classic.ViewStatusMessagesServlet</servlet-class>
    </servlet>

    <servlet-mapping>
        <servlet-name>ViewStatusMessages</servlet-name>
        <url-pattern>/lbClassicStatus</url-pattern>
    </servlet-mapping>

### 侦听状态消息

您还可以将`StatusListener`附加到`StatusManager`，以便您可以立即采取行动响应状态消息，特别是对于在 logback 配置后发生的消息。注册状态侦听器是一种方便的方法来监督对手的内部状态，而无需人为干预。

Logback 附带一个名为 `OnConsoleStatusListener` 的 `StatusListener` 实现，如其名称所示，在控制台上打印所有新的传入状态消息。

以下是使用`StatusManager`注册`OnConsoleStatusListener`实例的示例代码。

    LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory(); 
    StatusManager statusManager = lc.getStatusManager();
    OnConsoleStatusListener onConsoleListener = new OnConsoleStatusListener();
    statusManager.add(onConsoleListener);

请注意，注册状态侦听器只会在其注册后收到状态事件。它不会收到以前的消息，因此，将状态监听器注册指令置于其他指令之前的配置文件的顶部通常是一个好主意。

还可以在配置文件中注册一个或多个状态监听器，这是一个例子。

例：注册一个状态监听器(logback-examples/src/main/resources/chapters/configuration/onConsoleStatusListener.xml)

    <configuration>
        <statusListener class="ch.qos.logback.core.status.OnConsoleStatusListener" />  

        ... the rest of the configuration file  
    </configuration>


### "logback.statusListenerClass"系统属性

还可以通过将"logback.statusListenerClass" Java系统属性设置为要注册的侦听器类的名称来注册状态侦听器。 例如，

    java -Dlogback.statusListenerClass=ch.qos.logback.core.status.OnConsoleStatusListener ...

Logback附带了几个状态侦听器实现.`OnConsoleStatusListener`在控制台上打印输入状态消息，即在`System.out`上。 `OnErrorConsoleStatusListener`在`System.err`上打印输入状态消息, `NopStatusListener`丢弃传入状态消息。

请注意，如果在配置期间注册了任何状态侦听器，并且特别是如果用户通过"logback.statusListenerClass"系统指定状态侦听器，则禁用自动状态打印（如果出现错误）.因此，通过将`NopStatusListener`设置为状态监听器，您可以完全静音内部状态打印。

    java -Dlogback.statusListenerClass=ch.qos.logback.core.status.NopStatusListener ...

### 停止 logback-classic

为了释放由logback-classic使用的资源，始终是停止 logback 上下文的好主意。 停止上下文将关闭由上下文定义的日志记录器附加的所有追加器，并停止任何活动的线程.

    import org.sflf4j.LoggerFactory;
    import ch.qos.logback.classic.LoggerContext;
    ...

    // assume SLF4J is bound to logback-classic in the current environment
    LoggerContext loggerContext = (LoggerContext) LoggerFactory.getILoggerFactory();
    loggerContext.stop();

在Web应用程序中，可以从`ServletContextListener#contextDestroyed`方法中调用上述代码，以便停止logback-classic和释放资源。从版本1.1.10开始，相应的`ServletContextListener`会自动安装（见下文）。

#### 使用回调停止 logback-classic

安装JVM关机挂钩是关闭回退和释放相关资源的便捷方式。

    <configuration debug="true">
        <!-- in the absence of the class attribute, assume 
        ch.qos.logback.core.hook.DelayingShutdownHook -->
        <shutdownHook/>
        .... 
    </configuration>

默认关机挂钩，即`DelayingShutdownHook`，可以延迟用户指定持续时间的关机.请注意，您可以通过将类属性设置为对应于您的关闭挂钩的类名来安装自己的关闭挂钩。

#### 在web应用里停止 logback-classic

`自1.1.10起` Logback-classic 将自动请求Web服务器安装实现`ServletContainerInitializer`接口的`LogbackServletContainerInitializer`（在servlet-api 3.x及更高版本中可用）。这个初始化器依次安装和`LogbackServletContextListener`的实例。 当停止或重新加载web应用程序时，此侦听器将停止当前的logback-classic上下文。

您可以通过在Web应用程序的`web.xml`文件中设置名为`logbackDisableServletContainerInitializer`的`<context-param>`来禁用自动安装`LogbackServletContextListener`。 以下是相关的代码段:

    <web-app>
        <context-param>
            <param-name>logbackDisableServletContainerInitializer</param-name>
            <param-value>true</param-value>
        </context-param>
        .... 
    </web-app>

请注意，`logbackDisableServletContainerInitializer`变量也可以设置为Java系统属性的OS环境变量.最本地的设置优先，即web应用第一，系统属性第二，操作系统环境最后。

### 配置文件语法

正如您在手册中已经看到的许多示例仍然遵循的那样，Logback允许您重新定义日志记录行为，而无需重新编译代码。实际上，您可以轻松配置Logback，以便禁用应用程序的某些部分的日志记录，或直接输出到UNIX Syslog守护程序，数据库，日志可视化程序或将日志记录事件转发到远程日志记录服务器，这将记录 根据本地服务器策略，例如通过将日志事件转发到第二个Logback服务器。

本节的其余部分介绍配置文件的语法。

如将一再强调，logback配置文件的语法非常灵活。因此，不可能使用DTD文件或XML模式指定允许的语法。然而，配置文件的基本结构可以描述为`<configuration>`元素，包含零个或多个`<appender>`元素，后跟零个或多个`<logger`>元素，后跟最多一个`<root>`元素。下图说明了这个基本结构:

![图](images/basicSyntax.png)

### 标签名称的区分大小写

由于logback版本0.9.17，与显式规则相关的标签名称不区分大小写。例如，`<logger>`，`<Logger>`和`<LOGGER>`是有效的配置元素，将以相同的方式进行解释。请注意，XML格式规则仍然适用，如果您打开标签为`<xyz>`，则必须将其关闭为`</ xyz>`，`</ XyZ>`将无法正常工作。 对于隐式规则，标签名称区分大小写，除了第一个字母。因此，`<xyz>`和`<Xyz>`是等效的，但不是`<xYz>`。隐式规则通常遵循在Java世界中常见的`camelCase`约定。由于标签与显式操作相关联并且与隐式动作相关联并不容易，因此说明XML标记对于第一个字母是否区分大小写或不敏感，这是不重要的。如果您不确定哪个案例用于给定的标签名称，只需遵循几乎总是正确惯例的`camelCase`约定。

### 配置loggers或<logger>元素

在这一点上，您应该至少对层级继承和基本选择规则有一些了解。否则，除非你是一个埃及古物学家，否则对于你而言，回溯配置对于象形文字来说没有什么意义。

使用`<logger>`元素配置记录器。 一个`<logger>`元素只需一个必需的名称属性，一个可选的等级属性和一个可选的加性属性，允许值为`true`或`false`。`level`属性的值允许不区分大小写的字符串值`TRACE`，`DEBUG`，`INFO`，`WARN`，`ERROR`，`ALL`或`OFF`。特殊不区分大小写的值`INHERITED`或其同义词`NULL`将强制记录器的级别从层次结构中的较高层继承。如果您设置了记录器的级别，然后决定它应该继承其级别，这将派上用场。

`<logger>`元素可能包含零个或多个`<appender-ref>`元素; 这样引用的每个追加器都被添加到命名记录器中。 请注意，与log4j不同，在配置给定的记录器时，logback-classic 不会关闭或删除任何以前引用的追加器。

#### 配置 root 层次，即 <root>节点

`<root>`元素配置根记录器。 它支持单个属性，即level属性。它不允许任何其他属性，因为加性标志不适用于根记录器。 此外，由于根记录器已经被命名为“ROOT”，它也不允许使用name属性。level属性的值可以是不区分大小写的字符串TRACE，DEBUG，INFO，WARN，ERROR，ALL或OFF之一。 请注意，根记录器的级别不能设置为INHERITED或NULL。

与`<logger>`元素类似，`<root>`元素可能包含零个或多个`<appender-ref>`元素; 这样引用的每个`appender`被添加到根记录器中。请注意，与`log4j`不同，在配置根记录器时，logback-classic不会关闭或删除任何先前引用的追加器。

示例：

设置记录器或根记录器的级别与声明它并设置其级别一样简单，如下例所示。假设我们不再需要从属于`chapters.configuration`包的任何组件查看任何DEBUG消息,以下配置文件显示如何实现。

例：设置 logger级别(logback-examples/src/main/resources/chapters/configuration/sample2.xml)

    <configuration>

        <appender name="STDOUT" class="ch.qos.logback.core.ConsoleAppender">
            <!-- encoders are assigned the type
                ch.qos.logback.classic.encoder.PatternLayoutEncoder by default -->
            <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
            </encoder>
        </appender>

        <logger name="chapters.configuration" level="INFO"/>

        <!-- Strictly speaking, the level attribute is not necessary since -->
        <!-- the level of the root level is set to DEBUG by default.       -->
        <root level="DEBUG">          
            <appender-ref ref="STDOUT" />
        </root>  
    
    </configuration>

当上述配置文件作为`MyApp3`应用程序的参数给出时，它将产生以下输出：

    17:34:07.578 [main] INFO  chapters.configuration.MyApp3 - Entering application.
    17:34:07.578 [main] INFO  chapters.configuration.MyApp3 - Exiting application.

请注意，由`chapters.configuration.Foo`记录器生成的级别`DEBUG`的消息已被抑制。 另请参阅Foo类。

您可以根据需要配置尽可能多的记录器的级别。在下一个配置文件中，我们将`chapter.configuration logger`的级别设置为`INFO`，同时将`chapters.configuration.Foo`记录器的级别设置为`DEBUG`。

例：设置logger级别(logback-examples/src/main/resources/chapters/configuration/sample3.xml)

    <configuration>

        <appender name="STDOUT"
            class="ch.qos.logback.core.ConsoleAppender">
            <encoder>
            <pattern>
                %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
            </pattern>
            </encoder>
        </appender>

        <logger name="chapters.configuration" level="INFO" />
        <logger name="chapters.configuration.Foo" level="DEBUG" />

        <root level="DEBUG">
            <appender-ref ref="STDOUT" />
        </root>

    </configuration>

使用此配置文件运行`MyApp3`将导致控制台上的以下输出：

    17:39:27.593 [main] INFO  chapters.configuration.MyApp3 - Entering application.
    17:39:27.593 [main] DEBUG chapters.configuration.Foo - Did it again!
    17:39:27.593 [main] INFO  chapters.configuration.MyApp3 - Exiting application.

下表列出了日志记录器及其级别，`JoranConfigurator`已经使用`sample3.xml`配置文件进行了配置。

<table>
     <tbody>
        <tr>
            <th>Logger name</th>
            <th>Assigned Level</th>
            <th>Effective Level</th>
        </tr>
        <tr>
            <td>root</td>
            <td><code>DEBUG</code></td>
            <td><code>DEBUG</code></td>
        </tr>
        <tr>
            <td>chapters.configuration</td>
            <td><code>INFO</code></td>
            <td><code>INFO</code></td>
        </tr>
        <tr>
            <td>chapters.configuration.MyApp3</td>
            <td><code>null</code></td>
            <td><code>INFO</code></td>
        </tr>
        <tr>
            <td>chapters.configuration.Foo</td>
            <td><code>DEBUG</code></td>
            <td><code>DEBUG</code></td>
        </tr>
    </tbody>
</table>

因此，`MyApp3`类中的级别`INFO`和`Foo.doIt（）`中的`DEBUG`消息的两个日志记录语句都被启用。请注意，根记录器的级别始终设置为非空值，默认为`DEBUG`。

让我们注意，基本选择规则取决于被调用的记录器的有效级别，而不是追加者附加的记录器的级别。Logback将首先确定是否启用日志记录语句，如果启用，它将调用记录器层次结构中找到的`appender`，而不管其级别如何。配置文件`sample4.xml`就是一个例子：

例：logger最小级别(logback-examples/src/main/resources/chapters/configuration/sample4.xml)

    <configuration>

        <appender name="STDOUT"
        class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>
                %d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
            </pattern>
            </encoder>
        </appender>

        <logger name="chapters.configuration" level="INFO" />

        <!-- turn OFF all logging (children can override) -->
        <root level="OFF">
            <appender-ref ref="STDOUT" />
        </root>

    </configuration>

下表列出了应用`sample4.xml`配置文件后的记录器及其级别。

<table>
    <tbody>
        <tr>
            <th>Logger name</th>
            <th>Assigned Level</th>
            <th>Effective Level</th>
        </tr>
        <tr>
            <td>root</td>
            <td><code>OFF</code></td>
            <td><code>OFF</code></td>
        </tr>
        <tr>
            <td>chapters.configuration</td>
            <td><code>INFO</code></td>
            <td><code>INFO</code></td>
        </tr>
        <tr>
            <td>chapters.configuration.MyApp3</td>
            <td><code>null</code></td>
            <td><code>INFO</code></td>
        </tr>
        <tr>
            <td>chapters.configuration.Foo</td>
            <td><code>null</code></td>
            <td><code>INFO</code></td>
        </tr>
  </tbody>
</table>

名为`STDOU`T的`ConsoleAppender`是`sample4.xml`中唯一配置的`appender`，附加到其级别设置为`OFF`的根记录器。但是，使用配置脚本`sample4.xml`运行`MyApp3`将会产生：

    17:52:23.609 [main] INFO chapters.configuration.MyApp3 - Entering application.
    17:52:23.609 [main] INFO chapters.configuration.MyApp3 - Exiting application.

因此，根记录器的级别没有明显的影响，因为对于`INFO`级别都会启用`chapters.configuration.MyApp3`和`chapters.configuration.Foo`类中的记录器。作为附注，章节配置记录器凭借其在配置文件中的声明而存在 - 即使Java源代码不直接引用它。

#### Appenders配置