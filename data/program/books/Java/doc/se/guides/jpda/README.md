#   [Java平台调试器架构（JPDA）](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/index.html)


Java平台调试器体系结构（JPDA）由三个接口组成，设计用于桌面系统的开发环境中的调试器。Java虚拟机工具接口（JVM TI）定义了VM必须为调试提供的服务。Java调试线协议（JDWP）定义了在被调试进程和调试器前端之间传输的信息和请求的格式，后者实现了Java调试接口（JDI）。Java调试接口在用户代​​码级别定义信息和请求。

----

##  设计
-   [JPDA概述](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/jpda.html)
    -   模块化
    -   演练
    -   移植
-   [建筑结构](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/architecture.html)
    -   结构概述
    -   组件
    -   调试器接口
        -   Java虚拟机工具接口
        -   Java调试器有线协议
        -   Java调试接口

----

##  接口参考
-   Java虚拟机工具接口（JVM TI）

注意：JVMPI，实验性Java虚拟机概要分析界面已删除。它已被JVM TI取代。

[[规格](https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/index.html)

-   Java虚拟机调试接口（JVMDI）

[JVMDI已被删除。它已被JVM TI取代。

-   Java调试线协议（JDWP）

[规格](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/jdwp-spec.html)

-   Java调试线协议接口

[规格](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/jdwpTransport.html)

-   Java调试接口（JDI）

[规格](https://docs.oracle.com/javase/8/docs/jdk/api/jpda/jdi/index.html)

----

##  履行
-   [连接和调用详细信息](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/conninv.html)

----

##  更多
-   [Java平台调试器架构 - 常见问题解答](https://www.oracle.com/technetwork/java/javase/tech/faqs-jsp-142584.html)

----

##  例子
-   [JDI应用程序示例](https://docs.oracle.com/javase/8/docs/technotes/guides/jpda/examples.html)

----
