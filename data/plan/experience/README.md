#   第四阶段：下山历练-v.0.2.2

云应用、微服务是解决复杂大型应用的方案

一些特别的场景需要对应的服务，这些服务可以提供项目之外的支持或者项目之间关联

考虑应用场景

##  理论

理论关注比较虚的东西，更多的是人思考的一种方式，可以把不同或无关的东西联系起来，建立一种认识，从而在具体技术之上的高度统一

理论指导实践，让具体过程可控，就想图纸，在开始之前就确定结果。

### REST

一种应用架构风格，让前后端分离，仅建议交换数据的方式，对于前后端具体技术没有做任何说明，换句话说，只要能够使用HTTP+xml/json等都可以

### 微服务



### 持续集成


----

##  Java扩展

看看Java里还有那些更多的框架，形式各异，让你酸爽到底

### Netty

#### 定义

编写可用网络程序是件很有难度的事情，高性能就难上加难，每当遇到这种问题，必有大牛出现解决

在Java核心技术9/10下卷`网络`章节，编写简单示例单个请求响应很简单，但是当请求成百上千，上万，几十万呢?该怎么解决..这就是技术的难度

一款NIO客户端服务器框架，可以快速轻松地开发协议服务器和客户端等网络应用程序。

它极大地简化并简化了TCP和UDP套接字服务器等网络编程，包括FTP，SMTP，HTTP以及各种基于二进制和基于文本的传统协议等。

#### 内容
-   概念及体系结构
-   编解码器
-   网络协议
-   案例研究

#### 网站
-   [官网](http://netty.io/index.html)
-   [GitHub](https://github.com/netty/netty)
-   [文档教程](http://netty.io/wiki/)

#### 书籍
-   Netty实战
-   Netty权威指南

### Lucene

#### 定义

一个全文检索引擎的架构，提供了完整的查询引擎和索引引擎，部分文本分析引擎。

全文检索引擎工具包，方便的在目标系统中实现全文检索的功能，或者是以此为基础建立起完整的全文检索引擎

#### 内容
-   扩展的高性能索引
-   强大，准确和高效的搜索算法

#### 网站
-   [官网](http://lucene.apache.org/core/)
-   [文档](http://lucene.apache.org/core/documentation.html)
-   [GitHub](https://github.com/apache/lucene-solr)

#### 书籍
-   Lucene实战

### Spring Boot

#### 定义

简化构建基于Spring的应用程序

#### 内容
-   构建Spring应用
-   定义配置文件
-   编写Bean对象
-   监控运行对象
-   部署运行

#### 网站
-   [官网](https://spring.io/projects/spring-boot)
-   [文档](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle/)
-   [GitHub](https://github.com/spring-projects/spring-boot)

#### 书籍
-   Spring Boot实战

### Spring Data

#### 定义

为数据访问提供熟悉且一致的基于Spring的编程模型，同时仍保留底层数据存储的特​​殊特性

Spring Data是一个由独立项目组成的综合项目，原则上它有不同的发布节奏

#### 内容
-   [Spring Data Commons](https://docs.spring.io/spring-data/commons/docs/current/reference/html/) - 支持每个Spring Data项目的核心Spring概念。
-   [Spring Data Gemfire](https://projects.spring.io/spring-data-gemfire/) - 从Spring应用程序中轻松配置和访问GemFire。
-   [Spring Data JPA](https://projects.spring.io/spring-data-jpa/) - 可以轻松实现基于JPA的存储库。
-   [Spring Data JDBC](https://projects.spring.io/spring-data-jdbc/) - 基于JDBC的存储库。
-   [Spring Data KeyValue](https://github.com/spring-projects/spring-data-keyvalue) - `Map`基于存储库和SPI可以轻松为键值存储构建Spring Data模块。
-   [Spring Data LDAP](https://projects.spring.io/spring-data-ldap/) - 为[Spring LDAP](https://github.com/spring-projects/spring-ldap)提供Spring Data存储库支持。
-   [Spring Data MongoDB](https://projects.spring.io/spring-data-mongodb/) - 基于Spring的对象文档支持和MongoDB存储库。
-   [Spring Data REST](https://projects.spring.io/spring-data-rest/) - 将Spring Data存储库导出为超媒体驱动的RESTful资源。
-   [Spring Data Redis](https://projects.spring.io/spring-data-redis/) - 从Spring应用程序中轻松配置和访问Redis。
-   [Apache Cassandra](https://projects.spring.io/spring-data-cassandra/) Spring数据 - Apache Cassandra的 Spring Data模块。
-   [Apache Solr](https://projects.spring.io/spring-data-solr/) Spring数据 - Apache Solr的 Spring Data模块。

#### 网站
-   [官网](https://projects.spring.io/spring-data/)
-   [文档](https://docs.spring.io/spring-data/)
-   [示例](https://github.com/spring-projects/spring-data-examples)

#### 书籍
-   Spring Data实战

### Spring Batch

#### 定义

一个轻量级，全面的批处理框架，旨在支持开发对企业系统日常运作至关重要的强大批处理应用程序

#### 内容
-   交易管理
-   基于块的处理
-   声明式I / O
-   启动/停止/重新启动
-   重试/跳过
-   基于Web的管理界面

#### 网站
-   [官网](https://spring.io/projects/spring-batch)
-   [文档](https://docs.spring.io/spring-batch/trunk/reference/htmlsingle/)
-   [GitHub](https://github.com/spring-projects/spring-batch)

#### 书籍
-   Spring-Batch批处理框架

### Spring Cloud

#### 定义

开发人员提供了快速构建分布式系统中一些常见模式的工具（例如配置管理，服务发现，断路器，智能路由，微代理，控制总线，一次性令牌，全局锁定，领导选举，分布式会话，群集状态）

#### 内容
-   分布式/版本化配置
-   服务注册和发现
-   路由
-   服务对服务呼叫
-   负载均衡
-   断路器
-   全局锁定
-   分布式消息

#### 网站
-   [官网](http://projects.spring.io/spring-cloud/)

#### 书籍
-   Spring Cloud微服务实战
-   Spring Cloud与Docker微服务架构实战

----

##  引入服务

体会一下服务器的威力，想不到的场景只能说见识太少，世界比想象的精彩太多

### Nginx

#### 定义

一个高性能的HTTP和反向代理服务器，也是一个IMAP/POP3/SMTP服务器

#### 内容
-   文件结构
-   配置文件
-   虚拟主机
-   代理服务
-   Rewrite功能
-   Gzip压缩
-   缓存机制
-   HTTPS服务器
-   WebSocket
-   邮件服务
-   优化选项

#### 网站
-   [官网](http://nginx.org/)
-   [文档](http://nginx.org/en/docs/)

#### 书籍
-   Nginx高性能Web服务器详解

### Docker

#### 定义

Docker 是一个开源的应用容器引擎，让开发者可以打包他们的应用以及依赖包到一个可移植的容器中，然后发布到任何流行的 Linux 机器上，也可以实现虚拟化。容器是完全使用沙箱机制，相互之间不会有任何接口

#### 内容
-   概念对象
-   基本配置
-   管理 swarm
-   安全引擎
-   扩展引擎

#### 网站
-   [文档](https://docs.docker-cn.com/)

#### 书籍
-   第一本Docker书

### RabbitMq

#### 定义

最广泛的开源消息代理，支持多种消息传递协议。可以部署在分布式和联合配置中，以满足高规模，高可用性需求

#### 内容
-   CLI工具
-   配置
-   认证和授权
-   网络和TLS
-   分布式RabbitMQ
-   消息存储和资源管理
-   队列，路由和消费者功能
-   STOMP，MQTT，WebSockets
-   插件

#### 网站
-   [网站](http://www.rabbitmq.com/)
-   [教程](http://www.rabbitmq.com/getstarted.html)
-   [代码示例](https://github.com/rabbitmq/rabbitmq-tutorials)
-   [文档](http://www.rabbitmq.com/documentation.html)
-   [rabbitmq-java-client](https://github.com/rabbitmq/rabbitmq-java-client)
-   [rabbitmq-server](https://github.com/rabbitmq/rabbitmq-server)

#### 书籍
-   RabbitMQ实战：高效部署分布式消息队列

### MySql

#### 定义

一个关系型数据库管理系统，关系数据库将数据保存在不同的表中，而不是将所有数据放在一个大仓库内

社区版服务器就好

#### 内容
-   安装
-   管理员
-   安全
-   备份和恢复
-   优化
-   字符集
-   数据类型
-   函数和操作符
-   SQL语句语法
-   存储引擎
-   复制
-   集群
-   分区
-   作为文档存储

#### 网站
-   [官网](https://www.mysql.com/)
-   [文档](https://dev.mysql.com/doc/)

#### 书籍
-   高性能MySQL

### Redis

#### 定义

内存中的数据结构存储系统，它可以用作数据库、缓存和消息中间件

#### 内容
-   Redis 使用
    -   `Redis命令` redis完整的命令列表，以及他们的说明文档。
    -   `管道（Pipelining）`：学习如何一次发送多个命令，节省往返时间。
    -   `Redis 发布/订阅（Pub/Sub）`：redis是一个快速、稳定的发布/订阅的信息系统。
    -   `内存优化`：了解如何使用内存和学习一些使用技巧。
    -   `过期（Expires）`：Redis允许为每一个key设置不同的过期时间，当它们到期时将自动从服务器上删除。
    -   `将Redis当做使用LRU算法的缓存来使用`：如何配置并且将Redis当做缓存来使用，通过限制内存及自动回收键。
    -   `Redis 事务`：将一组命令放在同一个事务中进行处理。
    -   `大量插入数据`：如何在短时间里向Redis写入大量数据。
    -   `从文件中批量插入数据`：将文件中的指令批量执行。
    -   `分区（Partitioning）`：如何将你的数据分布在多个Redis里面。
    -   `分布式锁（Distributed locks）`：用Redis实现分布式锁管理器。
    -   `key事件通知（Redis keyspace notifications）`：通过发布/订阅获得key事件的通知（版本2.8或更高）。
    -   `创建二级索引（Creating secondary indexes with Redis）`：使用redis的数据结构创建二级索引。
-   Redis 管理
    -   `Redis-Cli`：学习怎么通过命令行使用redis。
    -   `配置（Configuration）`：怎么配置 redis。
    -   `复制（Replication）`：你需要知道怎么设置主从复制。
    -   `持久化（Persistence）`：了解如何配置redis的持久化。
    -   `Redis 管理（Redis Administration）`：学习redis管理方面的知识。
    -   `安全性（Security）`：概述Redis的安全。
    -   `加密（encryption）`：如何加密redis的客户端与服务端通信。
    -   `信号处理（Signals Handling）`：如何处理Redis信号。
    -   `连接处理（Connections Handling）`：如何处理Redis客户端连接。
    -   `高可用性（High Availability）`：Redis Sentinel是Redis官方的高可用性解决方案。
    -   `延迟监控（Latency monitoring）`：redis集成的延迟监控和报告功能对于为低延迟应用场景优化redis很有帮助。
    -   `基准（Benchmarks）`：看看Redis在不同平台上跑得有多快。
-   Redis Cluster
    -   `Redis 集群教程`
    -   `Redis 集群规范`

#### 网站
-   [中文官网](http://www.redis.cn/)
-   [文档](http://www.redis.cn/documentation.html)

#### 书籍
-   Redis实战

### MongoDB

#### 定义

一个基于分布式文件存储的数据库。支持的数据结构非常松散，是类似json的bson格式，因此可以存储比较复杂的数据类型

支持的查询语言非常强大，其语法有点类似于面向对象的查询语言

#### 内容
-   shell
-   CRUD操作
-   聚合
-   数据模型
-   索引
-   安全
-   游标
-   复制
-   分片
-   管理
-   存储

#### 网站
-   [官网](https://www.mongodb.com/)
-   [文档](https://docs.mongodb.com)

#### 书籍
-   MongoDB权威指南

### Solr

#### 定义

构建于Apache Lucene上的流行的，超快速的开源企业搜索平台

#### 内容
-   管理用户界面
-   文档、字段和架构设计
-   分析器、标识符和过滤器
-   索引和基本数据操作
-   搜索
-   配置示例
-   监视
-   部署和操作
-   安全
-   客户端API

#### 网站
-   [官网](https://lucene.apache.org/solr/)
-   [文档教程](https://lucene.apache.org/solr/guide/)
-   [GitHub](https://github.com/apache/lucene-solr)

#### 书籍
-   Solr 实战

### Jenkins

#### 定义

开源自动化服务器，支持构建，部署和自动化任何项目

#### 内容
-   运行多个步骤
-   定义执行环境
-   记录测试结果
-   清理和通知
-   部署

#### 网站
-   [官网](https://jenkins.io/)
-   [文档](https://jenkins.io/doc/)
-   [GitHub](https://github.com/jenkinsci/jenkins)

#### 书籍
-   Jenkins权威指南

### Fastdfs

#### 定义

一款开源的高性能分布式文件系统

满足基于照片共享网站和视频共享网站等文件服务的网站的要求

#### 内容
-   文件存储
-   文件同步
-   文件访问（文件上传和文件下载）
-   高容量和负载均衡设计

#### 网站
-   [GitHub](https://github.com/happyfish100/fastdfs)
-   [fastdfs-client-java](https://github.com/happyfish100/fastdfs-client-java)
-   [fastdfs-nginx-module](https://github.com/happyfish100/fastdfs-nginx-module)

----
