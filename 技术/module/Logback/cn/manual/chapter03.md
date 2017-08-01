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

该应用程序将获取当前有效的`LoggerContext`，创建一个新的`JoranConfigurator`，设置它将在其上运行的上下文，重置日志记录器上下文，然后最终要求配置器使用作为参数传递给应用程序的配置文件配置上下文。 打印内部状态数据，以防警告或错误。