#   [IIOP上的Java RMI](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/index.html)

nternet上的Java远程方法调用Inter-ORB协议技术（RMI-IIOP）是Java平台标准版（Java SE）的一部分。RMI编程模型支持通过rmi API 编程CORBA服务器和应用程序。您可以选择使用Java远程方法协议（JRMP）作为传输在Java编程语言中完全工作，或者使用Internet InterORB协议（IIOP）与其他符合CORBA的编程语言一起使用。

RMI-IIOP使用Java CORBA对象请求代理（ORB）和IIOP，因此您可以使用Java编程语言编写所有代码，并使用rmic编译器生成通过Internet InterORB协议连接应用程序所需的代码（ IIOP）以任何符合CORBA的语言编写的其他人。要使用其他语言的CORBA应用程序，可以使用带有-idl选项的rmic编译器从Java编程语言接口生成IDL 。要生成IIOP存根和绑定类，请使用带有-iiop选项的rmic编译器。

----

##  概观
-   [概述](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/rmiiiopUsing.html) - 概述何时应使用RMI-IIOP和分布式应用程序开发选项。

----

##  API规范
-   [org.omg.CORBA中](https://docs.oracle.com/javase/8/docs/api/org/omg/CORBA/package-summary.html)
-   [org.omg.PortableServer中](https://docs.oracle.com/javase/8/docs/api/org/omg/PortableServer/package-summary.html)
-   [org.omg.CosNaming中](https://docs.oracle.com/javase/8/docs/api/org/omg/CosNaming/package-summary.html)
-   [javax.rmi.CORBA中](https://docs.oracle.com/javase/8/docs/api/javax/rmi/CORBA/package-summary.html)
-   [javax.rmi](https://docs.oracle.com/javase/8/docs/api/javax/rmi/package-summary.html) （带有 PortableRemoteObject类的链接）

----

##  教程和程序员指南
-   [教程](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/tutorial.html) - 入门在IIOP上使用Java RMI。
-   [示例](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/rmiiiopexample.html) - 使用POA服务器端模型的IIOP上的RMI。
-   [Java RMI-IIOP程序员指南](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/rmi_iiop_pg.html)。
-   [Enterprise JavaBeans组件和CORBA客户端](https://docs.oracle.com/javase/8/docs/technotes/guides/rmi-iiop/interop.html) - 开发人员指南。
-   [Java IDL和Java RMI-IIOP技术：使用可移植拦截器](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/PI.html) - 适用于高级CORBA开发人员。

----

##  更多
请参阅[IIOP技术主页上](https://www.oracle.com/technetwork/java/index-140703.html)的[Java RMI](https://www.oracle.com/technetwork/java/index-140703.html)。

在[的Java IDL技术的网页](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/index.html) 包含了大量的信息是使用Java RMI-IIOP技术开发人员非常有用。

该[对象管理组](https://www.omg.org/)是所有CORBA和IIOP相关信息的官方消息。在CORBA 2.3.1规范的电子版从正规/ 99-10-07。CORBA规范的URL可能会更改。如果链接不起作用，请访问http://www.omg.org 并搜索规范。

有关此发行版Java平台中实现的规范的更多信息，请参阅合规性文档。

----
