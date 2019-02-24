#   logback

Logback 为取代 log4j 而生

Logback 提供独特而实用的特性，比如 Marker、参数化记录语句、条件化堆栈跟踪和强大的事件过滤功能

对于自身的错误报告，logback 依赖状态（Status）对象，状态对象极大地简化了故障查找。

----

##  版本
-   [官网](https://logback.qos.ch/)
-   [文档](https://logback.qos.ch/documentation.html)
-   [logback](https://github.com/qos-ch/logback)

----

##  指南
-   项目结构
    -   logback-core
        -   其它两个模块的基础
    -   logback-classic
        -   对应于log4j的显着改进版本
        -   本身实现了SLF4J API，因此您可以在Logback和其他日志记录系统（如JDK 1.4中引入的log4j或java.util.logging（JUL））之间来回切换
    -   logback-access
        -   与Servlet容器集成，以提供HTTP访问日志功能
-   自动配置
    -   添加maven依赖
    -   没有`logback.xml`或`logback-test.xml`时
    -   引入`org.slf4j`包的类
    -   在类前面定义：`Logger logger = LoggerFactory.getLogger("chapters.introduction.HelloWorld1");`
-   组件
    -   Logger
        -   命名实体，定义输出范围
        -   一个 logger 可以被关联多个 appender
    -   Appenders
        -   输出目的地：控制台、文件、远程套接字服务器、MySQL、PostreSQL、Oracle和其他数据库、JMS和远程UNIX Syslog守护进程
        -   负责写记录事件
    -   Layouts
        -   把事件转换成字符串
    -   Encoder
        -   负责两件事，一是把事件转换为字节数组，二是把字节数组写入输出流
        -   完全控制在什么时候、把什么样的字节写入到由其拥有者 appender 维护的输出流
    -   Filter
        -   用任意条件对事件行过滤
-   配置元素
    -   配置 `logger` ，或`<logger>` 元素
        -   `Logger` 是用`<logger>`元素配置的。`<logger>`元素有且仅有一个 `name` 属性、一个可选的`level` 属性和一个可选的 `additivity` 属性
        -   `<logger>`元素可以包含零个或多个`<appender-ref>`元素，表示这个 `appender` 会被添加到该 `logger`
    -   配置根 `logger` ，或`<root>` 元素
        -   `<root>`元素配置根 `logger`。该元素有一个 `level` 属性。没有 `name` 属性，因为已经被命名为`“ROOT”`
    -   配置 `Appender`
        -   `Appender` 用`<appender>`元素配置，该元素必要属性 `name` 和 `class`
        -   `name` 属性指定 `appender` 的名称，`class` 属性指定 `appender` 类的全限定名
        -   `<appender>`元素可以包含零个或多个`<layout>`元素、零个或多个`<encoder>`元素和零个或多个`<filter>`元素
        -   `<layout>`元素的 `class` 属性是必要的，表示将被实例化的 `layout` 类的全限定名。因为太常用了，所以当 `layout` 是 `PatternLayout` 时，可以省略 `class` 属性
        -   `<encoder>`元素 `class` 属性是必要的，表示将被实例化的 `encoder` 类的全限定名。因为太常用了，所以当 `encoder` 是 `PatternLayoutEncoder` 时，可以省略 `class` 属性
    -   记录输出到多个 appender 很简单，先定义各种 appender，然后在 logger 里进行引用，就行了
    -   设置上下文名称
        -   借助配置指令`<contextName>`设置成其他名字
    -   变量替换
        -   变量替换的语法与 `Unix shell` 中的变量替换相似。位于`“${”`与`“}”`之间的字符串是键（`key`），取代键的值可以在同一配置文件里指定，也可以在外部文件或通过系统属性进行指定。
        -   通过`<property>`元素定义的值实际上会被插入 `logger` 上下文。换句话说，这些值变成了 `logger` 上下文的属性。
        -   需要很多变量时，更方便的做法是在一个单独的文件里声明所有变量：引用 `class path` 上的资源，`<property resource="resource1.properties" />`
    -   配置文件里的条件化处理
        -   针对不同的环境在不同的配置文件里换来换去：开发、测试、和生产
        -   `<if condition='property("HOSTNAME").contains("torino")'>`
----

