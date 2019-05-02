#   Spring Cloud 入门实践

##   目录
-   [官网](https://spring.io/projects/spring-cloud)
-   [文档列表](https://spring.io/projects/spring-cloud#learn)
-   [官方文档](http://projects.spring.io/spring-cloud/spring-cloud.html)
-   [官方示例](https://github.com/spring-cloud-samples)
-   (纸)Spring Cloud微服务实战.pdf
-   (纸)Spring Cloud与Docker微服务架构实战.pdf
-   (纸)云原生Java：Spring Boot、Spring Cloud与Cloud Foundry弹性系统设计
-   Java微服务.pdf

----

##  主要项目

1.  核心基础

### [*Spring Cloud Netflix](spring-cloud-netflix/README.md)

与各种Netflix OSS组件集成

-   Netflix Eureka

`服务中心`，云端服务发现，一个基于 REST 的服务，用于定位服务，以实现云端中间层服务发现和故障转移。

管理着整个系统所有运行的服务信息

-   Netflix Hystrix

`熔断器`，容错管理工具，旨在通过熔断机制控制服务和第三方库的节点,从而对延迟和故障提供更强大的容错能力

当Hystrix发现某个服务实例不在状态不稳定立马马上让它下线，让其它服务实例来顶上来

具备服务降级、服务熔断、线程和信号隔离、请求缓存、请求合并以及服务监控

-   Netflix Zuul

`网关`，Zuul 是在云平台上提供`动态路由`,监控,弹性,安全等边缘服务的框架

对外统一，对内聚合，相当于门户。

-   Netflix Ribbon

`客户端负载均衡器`，屏蔽掉提供者服务实例

-   Netflix Feign

基于 Ribbon 和 Hystrix，提供 声明式的REST接口

-   Netflix Archaius

配置管理API，包含一系列配置管理API，提供动态类型化属性、线程安全配置操作、轮询框架、回调机制等功能。


### [*Spring Cloud Sleuth](spring-cloud-sleuth/README.md)

`日志收集`工具包，Spring Cloud应用程序的分布式跟踪，封装了Dapper和log-based追踪以及Zipkin和HTrace操作，为SpringCloud应用实现了一种分布式追踪解决方案。

### [*Spring Cloud Config](spring-cloud-config/README.md)

`配置中心`，配置管理工具包，让你可以把配置放到远程服务器，集中化管理集群配置，目前支持本地存储、Git以及Subversion

### [*Spring Cloud Stream](spring-cloud-stream/README.md)

通过 Redis、Rabbit 或 Kafka实现的消息微服务，可以通过简单的声明式模型来发送和接收消息

轻量级事件驱动的微服务框架，可快速构建可连接到外部系统的应用程序。数据流操作开发包，在Spring Boot应用程序之间使用Apache Kafka或RabbitMQ发送和接收消息的简单声明模型。

一个业务会牵扯到多个任务，任务之间是通过事件触发的，这就是Spring Cloud stream要干的事了


----

2.  扩展或补充

### [Spring Cloud Gateway](spring-cloud-gateway/README.md)

Spring Cloud Gateway是一款基于Project Reactor的智能可编程`路由器`。

### [*Spring Cloud Bus](spring-cloud-bus/README.md)

用于将服务和服务实例与分布式消息传递链接在一起的事件总线 用于在群集中传播状态更改（例如，配置更改事件）。

事件、消息总线，用于在集群（例如，配置变化事件）中传播状态变化，可与Spring Cloud Config联合实现热部署。

### [Spring Cloud Cluster](spring-cloud-cluster/README.md)

提供在分布式系统中的集群所需要的`基础功能`支持，如：选举、集群的状态一致性、全局锁、tokens等常见状态模式的抽象和实现。

领导者选举和共同的有状态模式与Zookeeper，Redis，Hazelcast，Consul的抽象和实现。

### [Spring Cloud Security](spring-cloud-security/README.md)

为Zuul代理中的负载平衡OAuth2 rest客户端和身份验证头中继提供支持。

基于spring security的安全工具包，为你的应用程序添加安全控制。

### [Spring Cloud Consul](spring-cloud-consul/README.md)

Consul 是一个支持多数据中心分布式高可用的`服务发现和配置共享`的服务软件。Consul 支持健康检查,并允许 HTTP 和 DNS 协议调用 API 存储键值对。与`Docker`容器可以无缝集成。

### [Spring Cloud Task](spring-cloud-task/README.md)

一种短命的微服务框架，用于快速构建执行有限数据处理的应用程序。用于向Spring Boot应用程序添加功能和非功能功能的简单声明。

比如说某些定时任务晚上就跑一次，或者某项数据分析临时就跑几次。

### [Spring Cloud Zookeeper](spring-cloud-zookeeper/README.md)

使用Apache Zookeeper进行服务发现和配置管理。

ZooKeeper是一个分布式的，开放源码的分布式应用程序协调服务，是Google的Chubby一个开源的实现，是Hadoop和Hbase的重要组件。它是一个为分布式应用提供一致性服务的软件，提供的功能包括：配置维护、域名服务、分布式同步、组服务等。

### [Spring Cloud Pipelines](spring-cloud-pipelines-to-cloud-pipelines-migration/README.md)

Spring Cloud Pipelines提供了一个固定意见的部署管道，其中包含确保您的应用程序可以零停机方式部署并轻松回滚出错的步骤。

### [Spring Cloud Contract](spring-cloud-contract/README.md)

Spring Cloud Contract是一个总体项目，其中包含帮助用户成功实施消费者驱动合同方法的解决方案。


----

3.  数据管道


### [Spring Cloud Dataflow](spring-cloud-dataflow/README.md)

适用于现代运行时的可组合微服务应用程序的云本机编排服务。易于使用的DSL，拖放式GUI和REST-API共同简化了基于微服务的数据管道的整体编排。


### [Spring Cloud Task App Starters](spring-cloud-task-app-starters/README.md)

Spring Cloud Task App Starters是Spring Boot应用程序，可能是任何进程，包括不能永久运行的Spring Batch作业，它们在有限的数据处理期后结束/停止。



4.  云平台

### [Spring Cloud Stream App Starters](spring-cloud-stream-app-starters/README.md)

Spring Cloud Stream App Starters是基于Spring Boot的Spring Integration应用程序，可提供与外部系统的集成。


### [Spring Cloud Open Service Broker](spring-cloud-cloudfoundry-service-broker/README.md)

提供构建实现Open Service Broker API的服务代理的起点。


### [Spring Cloud Cloudfoundry](spring-cloud-cloudfoundry/README.md)

将您的应用程序与Pivotal Cloud Foundry集成。提供服务发现实现，还可以轻松实现受SSO和OAuth2保护的资源。

### [Spring Cloud AWS](spring-cloud-aws/README.md)

简化整合 Amazon Web Service的组件

与托管的Amazon Web Services轻松集成。它提供了一种使用众所周知的Spring习语和API（如消息传递或缓存API）与AWS提供的服务进行交互的便捷方式。开发人员可以围绕托管服务构建应用程序，而无需关心基础结构或维护。

### [Spring Cloud Connectors](spring-cloud-connectors/README.md)

使各种平台中的PaaS应用程序可以轻松连接到数据库和消息代理（该项目以前称为“Spring Cloud”）等后端服务。

### [Spring Cloud Function](spring-cloud-function/README.md)

Spring Cloud Function通过函数促进业务逻辑的实现。它支持无服务器提供商之间的统一编程模型，以及独立运行（本地或PaaS）的能力。


----

##  发布说明

Spring Cloud是一个由独立项目组成的总体项目，原则上具有不同的发布节奏。为了管理投资组合，发布了BOM（物料清单），其中包含一组针对单个项目的依赖关系（见下文）。发布列车有名称而不是版本，以避免与子项目混淆。这些名称是一个字母序列（所以你可以按时间顺序排序）伦敦地铁站的名称（“天使”是第一个版本，“布里克斯顿”是第二个版本）。当各个项目的点数累积到临界质量时，或者其中一个项目中存在一个需要每个人都可用的关键错误时，发布列车将推出名称结尾为“.SRX”的“服务发布”，其中“X”是一个数字。

----
