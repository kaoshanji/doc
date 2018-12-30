#   简介



----

##  Spring Cloud Netflix

核心组件

----




-   Spring Cloud Config：配置管理工具，支持使用 Git 存储配置内容，实现应用配置的外部化存储，并支持客户端配置信息刷新、加密/解密配置内容
-   Spring Cloud Bus：事件、消息总线，用于传播集群中的状态变化或事件，以触发后续处理，比如用来动态刷新配置
-   Spring Cloud Cluster：针对 ZooKeeper、Reids、Hazalcase、Consul的选举算法和通用状态模式的实现
-   Spring Cloud Cloudfoundry：与 Pivotal Cloudfoundry等整合
-   Spring Cloud Consul：服务发现与配置管理工具
-   Spring Cloud Stream：通过 Redis、Rabbit 或 Kafka实现的消息微服务，可以通过简单的声明式模型来发送和接收消息
-   Spring Cloud AWS：简化整合 Amazon Web Service的组件
-   Spring Cloud Security：安全工具包，提供在Zuul代理中对OAuth2客户端请求的中继器
-   Spring Cloud Sleuth：Spring Cloud 应用的分布式跟踪实现，整合Zipkin