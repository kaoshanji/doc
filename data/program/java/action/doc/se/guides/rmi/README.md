#   [Java远程方法调用API（Java RMI）](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/index.html)


##  概观

Java远程方法调用（Java RMI）使程序员能够基于Java技术的应用程序创建基于Java技术的分布式技术，其中远程Java对象的方法可以从其他Java虚拟机调用，可能在不同的主机上调用。RMI使用对象序列化来编组和解组参数，并且不截断类型，支持真正的面向对象的多态性。

----

##  安全建议
请参阅[RMI安全建议](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/rmi_security_recommendations.html)以提高RMI应用程序的安全性。

----

##  API规范
-   [java.rmi包](https://docs.oracle.com/javase/8/docs/api/java/rmi/package-summary.html)
-   [java.rmi.dgc包](https://docs.oracle.com/javase/8/docs/api/java/rmi/dgc/package-summary.html)
-   [java.rmi.registry包](https://docs.oracle.com/javase/8/docs/api/java/rmi/registry/package-summary.html)
-   [java.rmi.server包](https://docs.oracle.com/javase/8/docs/api/java/rmi/server/package-summary.html)
-   [java.rmi.activation包](https://docs.oracle.com/javase/8/docs/api/java/rmi/activation/package-summary.html)
-   架构和功能规范
    -   [Java RMI规范](https://docs.oracle.com/javase/8/docs/platform/rmi/spec/rmiTOC.html)

----

##  教程
-   [入门](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/hello/hello-world.html)

教程向您展示了使用Java RMI创建经典Hello World程序的分布式版本所遵循的步骤。Hello World applet对从中下载它的服务器进行远程方法调用，以检索消息“Hello World！”。

-   [在Java RMI中](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/socketfactory/index.html)

使用自定义套接字工厂“使用自定义套接字工厂和Java RMI”教程向您展示如何创建分布式Hello World程序的版本，其中Java RMI运行时使用程序员选择的类型的套接字。本教程还讨论了如何通过SSL套接字使用Java RMI。

-   [激活教程](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/activation/overview.html)

激活教程描述了如何使用Java RMI API实现，注册和使用可激活对象。每个教程都提供了一种实现可激活对象的不同方法。所有教程都使用相同的参数化安装程序，该程序使用Java RMI激活系统守护程序（rmid）注册有关可激活对象的信息。

-   [配置 inetd启动rmid Solaris操作系统（Solaris OS）支持](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/inetd/rmid-inetd.html)

的Internet服务守护程序inetd提供了在系统引导时启动服务的替代方法。此守护程序是Internet标准服务的服务器进程，可以配置为按需启动服务。

-   [设计要启动的服务inetd](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/inetd/launch-service.html)

本教程描述了如何构建服务程序（使用特殊导出的本地注册表），以便可以inetd在客户端连接到服务的本地注册表时inetd 启动服务，以及如何配置以启动服务程序。

-   [使用Java RMI动态下载代码（使用java.rmi.server.codebase 属性）](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/codebase.html)

Java平台最重要的功能之一是能够将Java软件从任何URL动态下载到在单独进程中运行的VM，通常是在不同的物理系统上。结果是远程系统可以运行程序，例如从未在其磁盘上安装的applet。本教程描述了在Java系统中使用动态代码下载，以及如何将其与Java RMI一起使用。

-   [对于Java RMI线索的 Java教程](https://docs.oracle.com/javase/tutorial/rmi/index.html)

这条古道提供的Java RMI系统的简要概述，然后走过使用Java RMI的独特功能加载和运行时执行用户定义任务的完整的客户端/服务器的例子。示例中的服务器实现了一个通用计算引擎，客户端使用它来计算pi的值。

----

##  更多
-   [Java RMI主页](https://www.oracle.com/technetwork/java/javase/tech/index-jsp-136424.html)
-   [Java RMI和对象序列化常见问题解答](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/faq.html)
-   [有用的java.rmi属性](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/javarmiproperties.html)
-   [有用的sun.rmi属性](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/sunrmiproperties.html)
-   [Java RMI实现日志记录](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/logging.html)
-   [将工厂模式应用于Java RMI](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/Factory.html)
-   [将Java RMI与SSL配合使用](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi/socketfactory/SSLInfo.html)

----
