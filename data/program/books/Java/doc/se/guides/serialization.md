#   [Java对象序列化](https://docs.oracle.com/javase/8/docs/technotes/guides/serialization/index.html)

对象序列化支持将对象和从它们可到达的对象编码为字节流。序列化还支持从流中对象图的互补重建。序列化用于轻量级持久性以及通过套接字或Java远程方法调用（Java RMI）进行通信。对象的默认编码可保护私有和瞬态数据，并支持类的演变。类可以实现自己的外部编码，然后单独负责外部格式。

序列化现在包括一个API，允许独立于类的字段指定对象的序列化数据，并允许使用现有协议将这些序列化数据字段写入流和从流中读取，以确保与默认写入的兼容性和阅读机制。

----

##  规格
-   [规范](https://docs.oracle.com/javase/8/docs/platform/serialization/spec/serialTOC.html) - 描述对象序列化系统和API的体系结构。

----

##  API参考
-   [java.io包](https://docs.oracle.com/javase/8/docs/api/java/io/package-summary.html) - 记录所有接口和类。

----

##  更多
-   [常见问题](https://www.oracle.com/technetwork/java/javase/tech/serializationfaq-jsp-136699.html) - 解答有关对象序列化的最常见问题。

----

##  例子
-   [示例](https://docs.oracle.com/javase/8/docs/technotes/guides/serialization/examples/index.html) - 演示对象序列化的不同方面和用途。

----

##  工具
-   [serialver](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/serialver.html) - 解释 serialver命令，该命令返回类的 serialVersionUID。

----