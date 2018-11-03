#   Java Archive（JAR）文件

JAR（Java Archive）是一种独立于平台的文件格式，可将多个文件聚合为一个文件。多个Java小程序及其必需组件（.class文件，图像和声音）可以捆绑在一个JAR文件中，然后在单个HTTP事务中下载到浏览器中，从而大大提高了下载速度。JAR格式还支持压缩，这可以减小文件大小，进一步缩短下载时间。此外，applet作者可以对JAR文件中的各个条目进行数字签名，以验证其来源。它是完全可扩展的。

##  概述和规范
-   [概述 - JAR文件概述](https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jarGuide.html)
-   [规范 - JAR文件规范](https://docs.oracle.com/javase/8/docs/technotes/guides/jar/jar.html)

----

##  指南
-   [JAR文件的教程简介。](https://docs.oracle.com/javase/tutorial/deployment/jar/)

----

##  JAR工具
-   [适用于Solaris，Linux或Mac OS X的JAR工具参考页](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/jar.html)
-   [适用于Windows的JAR工具参考页面](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/jar.html)

----

##  更多
-   [扩展机制体系结构](https://docs.oracle.com/javase/8/docs/technotes/guides/extensions/spec.html) - 扩展Java平台的机制使用JAR文件格式来打包扩展类。清单属性可用于支持扩展机制和相关功能，如包密封和包版本控制

----