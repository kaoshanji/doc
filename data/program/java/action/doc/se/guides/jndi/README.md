#   [Java命名和目录接口（JNDI）](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/index.html)


Java命名和目录接口（JNDI）为使用Java编程语言编写的应用程序提供命名和目录功能。它旨在独立于任何特定的命名或目录服务实现。因此，可以以通用方式访问各种服务 - 新的，新兴的和已经部署的服务。

JNDI体系结构由API（应用程序编程接口）和SPI（服务提供者接口）组成。Java应用程序使用此API来访问各种命名和目录服务。SPI允许透明地插入各种命名和目录服务，允许使用JNDI技术API的Java应用程序访问其服务。

----

##  API和SPI规范
-   [JNDI API和SPI规范](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/reference.html) - JNDI技术中包含的软件包列表。

----

##  教程
-   [Java命名和目录接口](https://docs.oracle.com/javase/tutorial/jndi/index.html)跟踪。
-   [JNDI教程](https://docs.oracle.com/javase/jndi/tutorial/index.html) - 带有编程示例的JNDI技术教程介绍。

----

##  更多
-   JNDI架构文件：
    -   [JNDI API](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/spec/jndi/index.html)
    -   [JNDI SPI](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/spec/spi/spicover.frame.html)
-   JNDI服务提供者：

要将JNDI与特定的命名或目录服务一起使用，您需要一个JNDI 服务提供者，该提供者是一个插入JNDI API下方以访问命名或目录服务的模块。 

Java SE版本包括以下服务提供者：
-   [LDAP服务提供商](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/jndi-ldap.html)
-   [COS命名服务提供商](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/jndi-cos.html)
-   [RMI注册服务提供商](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/jndi-rmi.html)
-   [DNS服务提供商](https://docs.oracle.com/javase/8/docs/technotes/guides/jndi/jndi-dns.html)

----
