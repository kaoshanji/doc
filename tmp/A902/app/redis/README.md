#   Redis

Redis 是一个开源（BSD许可）的，内存中的数据结构存储系统，它可以用作数据库、缓存和消息中间件。

----

##  版本：4.0
-   [中文官网](http://www.redis.cn/)
-   [文档](http://www.redis.cn/documentation.html)

----


##  指南

### Redis 使用
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

### Redis 管理
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

### Redis Cluster
-   `Redis 集群教程`：入门级的Redis集群使用指南。
-   `Redis 集群规范`：进阶版的Redis集群使用规范

----

##  动手实践
-   [安装]

----

