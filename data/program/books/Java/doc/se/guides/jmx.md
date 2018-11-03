#   [Java管理扩展（JMX)](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/index.html)

Java Management Extensions（JMX）API是用于管理和监视资源（如应用程序，设备，服务和Java虚拟机）的标准API。JMX技术最初是通过Java Community Process（JCP）开发的Java规范请求（JSR）3，Java Management Extensions和JSR 160，JMX Remote API。

JMX技术的典型用途包括：
-   咨询和更改应用程序配置
-   累积有关应用程序行为的统计信息并使其可用
-   通知州的变化和错误的条件。

JMX API包括远程访问，因此远程管理程序可以与正在运行的应用程序进行交互以实现这些目的。

----

##  概观
-   [概述](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/overview/JMXoverviewTOC.html) - 本概述介绍了JMX技术。

----
##  API规范
-   [API参考](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/spec.html) - 由Javadoc工具生成的所有JMX包，类和代理和检测RI成员的联机文档。

----
##  指南
-   [JMX教程](https://docs.oracle.com/javase/tutorial/jmx/index.html) - 本教程介绍了JMX技术的一些功能示例。
-   [示例](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/examples.html) - JMX参考实现包含JMX操作的不同区域的代码示例。

除上述示例外，您还可以下载 Java SE演示和示例包。解压缩捆绑包后，可以在以下目录中找到演示JMX API实际实现的示例应用程序：

`JDK_HOME/sample/jmx/jmx-scandir`

该jmx-scandir示例是一个高级示例，它在实际场景中提供了JMX API的高级概念。

----
##  更多
-   [JMX主页](https://www.oracle.com/technetwork/java/javase/tech/javamanagement-140525.html) - 有关JMX规范的新闻，下载，博客和其他信息的页面。
-   [JMX 1.4规范](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/JMX_1_4_specification.pdf) （PDF）
-   [JMX跟踪](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/logging.html) - JMX实现中的跟踪基于Java SE日志记录功能。
-   [JSR 3](https://jcp.org/en/jsr/detail?id=003) - JMX API的JCP页面。
-   [JSR 160](https://jcp.org/en/jsr/detail?id=160) - JMX Remote API的JCP页面。
-   [Java SE监视和管理文档](https://docs.oracle.com/javase/8/docs/technotes/guides/management/index.html)

----