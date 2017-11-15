## 第1章：介绍

### logback是什么??
Logback旨在作为流行的log4j项目的继承者.它是由log4j的创始人CekiGülcü设计的,他建立在具有十年行业经验之上，由此产生的产品，即logback，它更快，系统占用资源更小，同样重要的是，Logback提供了具有独特而其他框架没有的特性.

### 第一步
#### 要求
使用 `Logback-classic` 需要在 classpath 添加 `slf4j-api.jar`、`logback-core.jar` 和 `logback-classic.jar`.

`logback-*.jar` 是独立的，而 `slf4j-api-1.7.25.jar` 附带 `SLF4J`.

想在让我们开始使用logback。
[添加jar](https://logback.qos.ch/setup.html)

例 1.1 [logging 基本模板](https://logback.qos.ch/xref/chapters/introduction/HelloWorld1.html)

    package chapters.introduction;

    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;

    public class HelloWorld1 {

    public static void main(String[] args) {

        Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld1");
        logger.debug("Hello world.");

        }
    }

HelloWorld1类默认放在 `chapters.introduction`包里。导入的 `Logger` 和 `LoggerFactory` 都是 `SLF4J API`，需要注意是 `org.slf4j`包.

第一行 `main()`方法里，变量`logger`是 `Logger`接口实例，通过`LoggerFactory`静态方法`getLogger`返回.logger 的名字是 "chapters.introduction.HelloWorld1".`main`方法调用这个记录器的调试方法，`Hello World`作为参数，使用是 DEBUG 级别的日志记录，并显示消息`Hello world`.

请注意，上述示例不引用任何logback类.在大多数情况下，就日志而言，您的类只需要导入SLF4J类,因此，大多数(不是全部)的示例都是SLF4J API,并忽视这点说明..

您可以使用以下命令启动第一个示例应用程序 chapterters.introduction.HelloWorld1：

    
    java chapters.introduction.HelloWorld1

启动HelloWorld1应用程序将在控制台上输出一行,凭借logback的默认配置策略，当没有找到默认配置文件时，logback会将一个ConsoleAppender添加到根记录器

    20:49:07.962 [main] DEBUG chapters.introduction.HelloWorld1 - Hello world.

Logback可以使用内置状态系统来报告有关其内部状态的信息。在Logback的生命周期中发生的重要事件可以通过称为`StatusManager`的组件访问.暂时让我们通过调用StatusPrinter类的static print（）方法来指示logback来打印它的内部状态.

例：[输出Logger状态](https://logback.qos.ch/xref/chapters/introduction/HelloWorld2.html)

    package chapters.introduction;

    import org.slf4j.Logger;
    import org.slf4j.LoggerFactory;
    import ch.qos.logback.classic.LoggerContext;
    import ch.qos.logback.core.util.StatusPrinter;

    public class HelloWorld2 {

    public static void main(String[] args) {
        Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld2");
        logger.debug("Hello world.");

        // print internal state
        LoggerContext lc = (LoggerContext) LoggerFactory.getILoggerFactory();
        StatusPrinter.print(lc);
        }
    }

运行 `HelloWorld2`应用，输出：

    12:49:22.203 [main] DEBUG chapters.introduction.HelloWorld2 - Hello world.
    12:49:22,076 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback.groovy]
    12:49:22,078 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback-test.xml]
    12:49:22,093 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Could NOT find resource [logback.xml]
    12:49:22,093 |-INFO in ch.qos.logback.classic.LoggerContext[default] - Setting up default configuration.

Logback解释说，没有找到logback-test.xml和logback.xml配置文件（稍后讨论），它使用默认策略配置自己，这是一个基本的`ConsoleAppender`.一个`Appender`是一个可以看作输出目标的类.Appender存在许多不同的目的地，包括控制台，文件，Syslog，TCP套接字，JMS等等,用户还可以根据具体情况轻松创建自己的Appender.

请注意，如果发生错误，logback将自动在控制台上打印其内部状态.

以前的例子很简单,更大应用程序中的实际日志记录将不会那么大. 记录语句的一般模式不会改变,只有配置过程会有所不同. 但是，您可能希望根据需要自定义或配置, 后续配置将在后续章节中介绍.

请注意，在上述示例中，我们已经通过调用`StatusPrinter.print()`方法来指示logback打印其内部状态。 Logback的内部状态信息对于诊断与logback有关的问题非常有用。

以下是要在应用程序中启用日志记录的三个必需步骤的列表:
- 配置 Logback 环境。 你可以用几种或多种复杂的方法来做到这一点, 稍后再说.
- 在您希望执行日志记录的每个类中，通过调用 `org.slf4j.LoggerFactory` 类 `getLogger()`方法，将当前类名称或类本身作为参数来检索Logger实例。
- 通过调用它的打印方法即debug（），info（），warn（）和error（）方法来使用此日志实例。 这将在配置上产生日志输出。

#### 构建 logback
logback 是用 Maven构建