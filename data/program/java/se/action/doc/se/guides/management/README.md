#   Java平台的监视和管理

Java Platform Standard Edition为Java平台提供全面的监视和管理支持。

##  API规范

Java SE包括以下用于监视和管理的API：
-   [java.lang.management](https://docs.oracle.com/javase/8/docs/api/java/lang/management/package-summary.html) - 支持监视和管理Java虚拟机和底层操作系统。API使应用程序能够自我监控并使JMX兼容工具能够在本地和远程监控和管理虚拟机。
-   [com.sun.management](https://docs.oracle.com/javase/8/docs/jre/api/management/extension/index.html) - Oracle对java.lang.management API 的平台扩展 以及该平台的其他一些组件的管理接口。
-   [java.util.logging.LoggingMXBean](https://docs.oracle.com/javase/8/docs/api/java/util/logging/LoggingMXBean.html) - 使您可以检索和设置日志记录信息。
-   [Java Management Extensions（JMX）API](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/spec.html) - 定义Java中的应用程序和网络管理和监视的体系结构，设计模式，接口和服务。有关更多信息，请参阅JMX文档。
-   [Attach API](https://docs.oracle.com/javase/8/docs/jdk/api/attach/spec/index.html) - Oracle的平台扩展，允许将管理代理动态加载到虚拟机中。
-   [JConsole API](https://docs.oracle.com/javase/8/docs/jdk/api/jconsole/spec/index.html) - 平台扩展，提供访问JConsole的编程接口，例如添加JConsole插件。JTop是JDK_HOME/demo/management/JTop 目录中可用的JConsole插件示例

----

##  指南

-   Java SE监视和管理指南，包含以下章节：
    -   [Java SE监视和管理概述](https://docs.oracle.com/javase/8/docs/technotes/guides/management/overview.html)
    -   [使用JMX API进行监视和管理](https://docs.oracle.com/javase/8/docs/technotes/guides/management/agent.html)
    -   [使用JConsole](https://docs.oracle.com/javase/8/docs/technotes/guides/management/jconsole.html)
    -   [使用Platform MBean Server和Platform MXBeans](https://docs.oracle.com/javase/8/docs/technotes/guides/management/mxbeans.html)
    -   [SNMP监控和管理](https://docs.oracle.com/javase/8/docs/technotes/guides/management/snmp.html)
    -   [附录：Microsoft Windows的其他安全信息](https://docs.oracle.com/javase/8/docs/technotes/guides/management/security-windows.html)
-   [JMX技术教程](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/tutorial/tutorialTOC.html)，通过演示JMX API关键功能的示例，介绍JMX技术。
-   关于Java平台的JConsole和远程管理的[常见问题解答](https://docs.oracle.com/javase/8/docs/technotes/guides/management/faq.html)。
-   JDK_HOME/demo/management安装Java SE平台后的目录中提供了用于监视和管理的示例代码


----

##  更多
-   [JMX技术文档](https://docs.oracle.com/javase/8/docs/technotes/guides/jmx/index.html)

----