#   Zookeeper 入门实践

##   目录
-   [官网](https://zookeeper.apache.org/)
-   从Paxos到Zookeeper  分布式一致性原理与实践(来源)
-   ZooKeeper-分布式过程协同技术详解

----


##  [理论背景](theory.md)


----

##  [基本功能](start.md)
-   部署运行
    -   Java环境配置
    -   启动 zk
-   Java客户端库：curator
    -   会话
    -   节点
    -   事件监听
    -   Master选举
    -   分布式锁
    -   分布式计数器
    -   分布式Barrier
    -   工具

----

##  典型应用
-   [应用场景](scenes01.md)
    -   数据发布/订阅
    -   负载均衡
    -   命名服务
    -   分布式协调/通知
    -   集群管理
    -   Master选举
    -   分布式锁
    -   分布式队列
-   [在大型分布式系统里](scenes02.md)
    -   Hadoop
    -   HBase
    -   Kafka
-   [在阿里巴巴实践](scenes03.md)
    -   消息中间件：Metamorphosis
    -   RPC服务框架：Dubbo
    -   基于 Mysql Binlog 的增量订阅和消费组件：Canal
    -   分布式数据库同步系统：Otter
    -   轻量级分布式通用搜索平台
    -   实时计算引擎：JStorm


----