#   [Java虚拟机工具接口（JVM TI）](https://docs.oracle.com/javase/8/docs/technotes/guides/jvmti/index.html)

JVM工具接口（JVM TI）是工具使用的本机编程接口。它提供了一种检查状态和控制Java虚拟机（JVM）中运行的应用程序执行的方法。JVM TI支持需要访问JVM状态的全部工具，包括但不限于：分析，调试，监视，线程分析和覆盖率分析工具。

注意： JVM TI是在JDK 5.0中引入的。JVM TI取代了Java虚拟机概要分析程序接口（JVMPI）和Java虚拟机调试接口（JVMDI），从JDK 6开始，不再提供这些接口。

----

##  JVM TI参考

-   有关概述，API参考和用法信息，请参阅[JVM TI参考](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html)。

----

##  更多
-   [Java虚拟机](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/index.html) - 功能，命令行选项和其他信息。
-   [Java Native Interface](https://docs.oracle.com/javase/8/docs/technotes/guides/jni/index.html) - JVM TI扩展的接口。
-   [java.lang.instrument package](https://docs.oracle.com/javase/8/docs/technotes/guides/instrumentation/index.html) - 如果仅使用JVM TI的检测功能，则替代JVM TI的Java编程语言。

----
