#   Netty

Netty 是一款异步的事件驱动的网络应用程序框架，支持快速地开发可维护的高性能的面向协议的服务器和客户端。

面向对象的基本概念：用较简单的抽象隐藏底层实现的复杂性

----

##  混个脸熟

这是一个`网络数据传输`的过程，与 Servlet/Tomcat 技术并无区别，只是把具体细节都呈现出来了。

业务逻辑与网络底层解耦

### 理论
-   Java阻塞和非阻塞
-   异步通信和事件驱动

### 组件
-   Channel

代表一个到实体(如一个文件、一个网络套接字)的开发连接，如读操作和写操作。

把 Channel 看作是传入(入站)或者传出(出站)数据的载体，因此可以被打开或被关闭，连接或者断开连接。

-   部分实现
    -   EmbeddedChannel
    -   LocalServerChannel
    -   NioDatagramChannel
    -   NioSctpChannel
    -   NioSocketChannel

-   通知调用
    -   回调：ChannelHandler
    -   Future：ChannelFuture
-   事件

Netty 使用不同的事件来通知我们状态的改变或者是操作的状态。

-   ChannelHandler 家族
    -   Channel ：Socket
    -   ChannelFuture ：异步通知
    -   ChannelHandler ：充当了所有处理入站和出站数据的应用程序逻辑的容器
        -   ChannelInboundHandler ：处理入站数据以及各种状态变化
        -   ChannelOutboundHandler ：处理出站数据并且允许拦截所有的操作
    -   ChannelHandlerAdapter ：ChannelHandler 适配器
    -   ResourceLeakDetector ：资源管理
    -   ChannelPipeline ：提供了 ChannelHandler 链的容器，并定义了用于在该链上传播入站和出站事件流的API。
    -   ChannelHandlerContext ：每当有ChannelHandler 添加到ChannelPipeline 中时，都会创建ChannelHandlerContext
    -   异常处理
-   EventLoop ：控制流、多线程处理、并发，用于处理连接的生命周期中所发生的事件
-   编解码器 ：通过Netty 发送或者接收一个消息的时候，就将会发生一次数据转换
-   引导类 ：为应用程序的网络层配置提供了容器
    -   Bootstrap：连接到远程主机和端口
    -   ServerBootstrap：绑定到一个本地端口
-   ByteBuf ：Netty 的数据容器
    -   堆缓冲区
    -   直接缓冲区
    -   复合缓冲区
-   测试

### 网络与线程
-   网络传输
    -   NIO：非阻塞I/O
    -   Epoll：Linux的本地非阻塞传输
    -   OIO：旧的阻塞I/O
    -   Local：JVM内部通信
-   ![支持的传输和网络协议](images/20190220162304.png)
-   线程模型
-   网络协议
    -   WebSocket
    -   UDP

### 案例

##  资料
-   [官网](https://netty.io/)
-   [GitHub](https://github.com/netty/netty)
-   Netty实战
-   Netty权威指南
-   Netty进阶之路跟着案例学Netty
