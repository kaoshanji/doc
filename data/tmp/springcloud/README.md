#   Spring Cloud

解决微服务架构实施的综合性解决框架，整合了诸多被广泛实践和证明过的框架作为实施的基础部件。

##  简介

基于 Spring Boot 实现的微服务架构开发工具，为微服务架构中涉及的配置管理、服务治理、断路器、智能路由、微代理、控制总线、全局锁、决策竞选、分布式会话和集群管理等操作提供了一种简单的开发方式。

-   Spring Cloud Config：配置管理工具，支持使用 Git 存储配置内容，实现应用配置的外部化存储，并支持客户端配置信息刷新、加密/解密配置内容
-   Spring Cloud Netflix：核心组件
    -   Eureka(独立运行)：服务治理组件，包含服务注册中心、服务注册与发现机制
    -   Hystrix：容错管理组件，实现断路器模式，帮助服务依赖中出现的延迟和为故障提供强大的容错能力
    -   Ribbon：客户端负载均衡的服务调用
    -   Feign：基于 Ribbon 和 Hystrix 的声明式服务调用
    -   Zuul：网关组件，提供智能路由、访问过滤等
    -   Archaius：外部化配置组件
-   Spring Cloud Bus：事件、消息总线，用于传播集群中的状态变化或事件，以触发后续处理，比如用来动态刷新配置
-   Spring Cloud Cluster：针对 ZooKeeper、Reids、Hazalcase、Consul的选举算法和通用状态模式的实现
-   Spring Cloud Cloudfoundry：与 Pivotal Cloudfoundry等整合
-   Spring Cloud Consul：服务发现与配置管理工具
-   Spring Cloud Stream：通过 Redis、Rabbit 或 Kafka实现的消息微服务，可以通过简单的声明式模型来发送和接收消息
-   Spring Cloud AWS：简化整合 Amazon Web Service的组件
-   Spring Cloud Security：安全工具包，提供在Zuul代理中对OAuth2客户端请求的中继器
-   Spring Cloud Sleuth：Spring Cloud 应用的分布式跟踪实现，整合Zipkin











