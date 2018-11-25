#   [Java I/O, NIO, and NIO.2](https://docs.oracle.com/javase/8/docs/technotes/guides/io/index.html)

Java I / O支持包含在java.io和 java.nio 包中。这些包一起包括以下功能：
-   通过数据流，序列化和文件系统输入和输出。
-   字符集，解码器和编码器，用于在字节和Unicode字符之间进行转换。
-   访问文件，文件属性和文件系统。
-   用于使用异步或多路复用，非阻塞I / O构建可伸缩服务器的API。

----

##  指南
-   The Java Tutorial的[基本I/O](https://docs.oracle.com/javase/tutorial/essential/io/index.html)部分 ，特别是[File I/O（以NIO.2为特色）](https://docs.oracle.com/javase/tutorial/essential/io/fileio.html)
-   [开发自定义文件系统提供程序](https://docs.oracle.com/javase/8/docs/technotes/guides/io/fsp/filesystemprovider.html)
-   [Zip文件系统提供程序](https://docs.oracle.com/javase/8/docs/technotes/guides/io/fsp/zipfilesystemprovider.html)
-   [故障排除提示](https://docs.oracle.com/javase/8/docs/technotes/guides/io/troubleshooting.html)

----

##  API规范
-   [java.io](https://docs.oracle.com/javase/8/docs/api/java/io/package-summary.html) （ description） - 支持系统输入和输出，以及对象序列化。到文件系统
-   [java.nio](https://docs.oracle.com/javase/8/docs/api/java/nio/package-summary.html) （ description） -为批量内存操作定义缓冲区。可以在直接存储器中分配缓冲器以获得高性能。
-   [java.nio.channels](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/package-summary.html) （ description） - 定义通道，能够执行I / O操作的设备的抽象; 为多路复用的非阻塞I / O定义选择器
-   [java.nio.channels.spi](https://docs.oracle.com/javase/8/docs/api/java/nio/channels/spi/package-summary.html) （ description） - 提供通道的实现
-   [java.nio.file](https://docs.oracle.com/javase/8/docs/api/java/nio/file/package-summary.html) - 定义用于访问文件和文件系统的接口和类。
-   [java.nio.file.attribute](https://docs.oracle.com/javase/8/docs/api/java/nio/file/attribute/package-summary.html) - 定义用于访问文件系统属性的接口和类。
-   [java.nio.file.spi](https://docs.oracle.com/javase/8/docs/api/java/nio/file/spi/package-summary.html) - 定义用于创建文件系统实现的类。
-   [java.nio.charset](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/package-summary.html) （ description） - 定义字符集，解码器和编码器，用于在字节和Unicode字符之间进行转换
-   [java.nio.charset.spi](https://docs.oracle.com/javase/8/docs/api/java/nio/charset/spi/package-summary.html) （ description） - 提供charsets的实现
-   [com.sun.nio.sctp](https://docs.oracle.com/javase/8/docs/jre/api/nio/sctp/spec/index.html) （ description） - 用于流控制传输协议的Java API

----

##  例子
-   [NIO和NIO.2示例](https://docs.oracle.com/javase/8/docs/technotes/guides/io/example/index.html)

----

##  更多
-   [支持的编码](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/encoding.doc.html)
-   [对象序列化](https://docs.oracle.com/javase/8/docs/technotes/guides/serialization/index.html)

----