# RabbitMQ

MQ全称为Message Queue, 消息队列（MQ）是一种应用程序对应用程序的通信方法。应用程序通过读写出入队列的消息（针对应用程序的数据）来通信，而无需专用连接来链接它们。消息传递指的是程序之间通过在消息中发送数据进行通信，而不是通过直接调用彼此来通信，直接调用通常是用于诸如远程过程调用的技术。排队指的是应用程序通过 队列来通信。队列的使用除去了接收和发送应用程序同时执行的要求。

MQ是消费-生产者模型的一个典型的代表，一端往消息队列中不断写入消息，而另一端则可以读取或者订阅队列中的消息。MQ和JMS类似，但不同的是JMS是SUN JAVA消息中间件服务的一个标准和API定义，而MQ则是遵循了AMQP协议的具体实现和产品

在项目中，将一些无需即时返回且耗时的操作提取出来，进行了异步处理，而这种异步处理的方式大大的节省了服务器的请求响应时间，从而提高了系统的吞吐量。

RabbitMQ是一个在AMQP基础上完成的，可复用的企业消息系统。

----

##  版本：3.7.4
-   [官网](http://www.rabbitmq.com/)
-   [文档](http://www.rabbitmq.com/documentation.html)
-   [教程](http://www.rabbitmq.com/getstarted.html)

----

##  指南组件

### 服务器和密钥插件
-   CLI工具
    -   CLI工具概述
    -   rabbitmqctl（Windows上的rabbitmqctl.bat）
    -   rabbitmq-plugins（Windows上的rabbitmq-plugins.bat）
    -   rabbitmqadmin（需要管理插件）
-   配置
    -   配置
    -   文件和目录位置
    -   日志
    -   策略和运行时参数
    -   每个虚拟主机限制
    -   客户端连接心跳
    -   节点间连接心跳
    -   队列和消息TTL
-   认证和授权
    -   身份验证和授权后端
    -   认证机制
    -   虚拟主机
    -   凭证和密码
    -   LDAP
    -   x509基于证书的身份验证
    -   已验证的用户ID
    -   身份验证失败通知
-   网络和TLS
    -   联网
    -   网络连接故障排除
    -   使用TLS进行客户端连接
    -   使用TLS进行节点间通信
    -   解决TLS问题
-   监控，审计，应用故障排除
    -   管理用户界面和HTTP API
    -   rabbitmqadmin，一个HTTP API命令行工具
    -   监控
    -   内部事件交换
    -   每个虚拟主机限制
    -   配置基于HTTP的（Web）插件
    -   消息跟踪
    -   用Wireshark捕获流量
-   分布式RabbitMQ
    -   镜像，铲子，联邦概述
    -   聚类
    -   队列镜像
    -   可靠的消息传递
-   指南
    -   监控
    -   生产清单
    -   备份还原
    -   可靠的消息传递
-   消息存储和资源管理
    -   内存使用情况
    -   内存管理
    -   资源报警
    -   可用磁盘空间警报
    -   流量控制
    -   消息存储配置
    -   队列和消息TTL
    -   队列长度限制
    -   懒惰队列
-   队列，路由和消费者功能
    -   队列属性和功能概述
    -   队列和消息TTL
    -   队列长度限制
    -   懒惰队列
    -   交换到交换绑定
    -   死刻字
    -   发件人选择分发
    -   优先队列
    -   消费者取消通知
    -   消费预取
    -   消费者优先级
    -   备用交换
-   STOMP，MQTT，WebSockets
    -   STOMP
    -   MQTT
    -   通过WebSockets STOMP
    -   通过WebSockets的MQTT

### 客户端库和功能
-   客户文件指南
    -   Java客户端
-   客户驱动功能
    -   发布商确认和消费者确认
    -   队列和消息TTL
    -   队列长度限制
    -   懒惰队列
    -   交换到交换绑定
    -   发件人选择分发
    -   优先队列
    -   消费者取消通知
    -   消费预取
    -   消费者优先级
    -   死信交流
    -   备用交换
    -   消息跟踪
    -   用Wireshark捕获流量

### 插件
-   热门插件
    -   管理
    -   STOMP
    -   MQTT
    -   通过WebSockets STOMP
    -   通过WebSockets的MQTT
    -   Federation
    -   Shovel
    -   内部事件交换

### 协议
-   AMQP 0-9-1：扩展 | 快速参考
-   STOMP
-   MQTT
-   通过WebSockets STOMP
-   通过WebSockets的MQTT


----



##  动手实践
-   [安装]
