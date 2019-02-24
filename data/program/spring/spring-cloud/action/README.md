#   Spring Cloud 入门实践

##   目录
-   [官网](https://spring.io/projects/spring-cloud)
-   (纸)Spring Cloud微服务实战.pdf
-   (纸)Spring Cloud与Docker微服务架构实战.pdf
-   (纸)云原生Java：Spring Boot、Spring Cloud与Cloud Foundry弹性系统设计
-   Java微服务.pdf

----

##  主要项目
-   [简介](Introduction.md)
-   [Spring Cloud Config](spring-cloud-config/README.md)

由git存储库支持的集中式外部配置管理。配置资源直接映射到Spring，Environment但如果需要，可以由非Spring应用程序使用。

-   [Spring Cloud Netflix](spring-cloud-netflix/README.md)

与各种Netflix OSS组件集成（Eureka，Hystrix，Zuul，Archaius等）

-   [spring Cloud Bus](spring-cloud-bus/README.md)

用于将服务和服务实例与分布式消息传递链接在一起的事件总线 用于在群集中传播状态更改（例如，配置更改事件）。

-   [Spring Cloud Cloudfoundry](spring-cloud-cloudfoundry/README.md)

将您的应用程序与Pivotal Cloud Foundry集成。提供服务发现实现，还可以轻松实现受SSO和OAuth2保护的资源。

-   [Spring Cloud Open Service Broker](spring-cloud-cloudfoundry-service-broker/README.md)

提供构建实现Open Service Broker API的服务代理的起点。

-   [Spring Cloud Cluster](spring-cloud-cluster/README.md)

领导者选举和共同的有状态模式与Zookeeper，Redis，Hazelcast，Consul的抽象和实现。

-   [Spring Cloud Consul](spring-cloud-consul/README.md)

Hashicorp Consul的服务发现和配置管理。

-   [Spring Cloud Security](spring-cloud-security/README.md)

为Zuul代理中的负载平衡OAuth2 rest客户端和身份验证头中继提供支持。

-   [Spring Cloud Sleuth](spring-cloud-sleuth/README.md)

Spring Cloud应用程序的分布式跟踪，兼容Zipkin，HTrace和基于日志（例如ELK）的跟踪。

-   [Spring Cloud Dataflow](spring-cloud-dataflow/README.md)

适用于现代运行时的可组合微服务应用程序的云本机编排服务。易于使用的DSL，拖放式GUI和REST-API共同简化了基于微服务的数据管道的整体编排。

-   [Spring Cloud Stream](spring-cloud-stream/README.md)

轻量级事件驱动的微服务框架，可快速构建可连接到外部系统的应用程序。在Spring Boot应用程序之间使用Apache Kafka或RabbitMQ发送和接收消息的简单声明模型。

-   [Spring Cloud Stream App Starters](spring-cloud-stream-app-starters/README.md)

Spring Cloud Stream App Starters是基于Spring Boot的Spring Integration应用程序，可提供与外部系统的集成。

-   [Spring Cloud Task](spring-cloud-task/README.md)

一种短命的微服务框架，用于快速构建执行有限数据处理的应用程序。用于向Spring Boot应用程序添加功能和非功能功能的简单声明。

-   [Spring Cloud Task App Starters](spring-cloud-task-app-starters/README.md)

Spring Cloud Task App Starters是Spring Boot应用程序，可能是任何进程，包括不能永久运行的Spring Batch作业，它们在有限的数据处理期后结束/停止。

-   [Spring Cloud Zookeeper](spring-cloud-zookeeper/README.md)

使用Apache Zookeeper进行服务发现和配置管理。

-   [Spring Cloud AWS](spring-cloud-aws/README.md)

与托管的Amazon Web Services轻松集成。它提供了一种使用众所周知的Spring习语和API（如消息传递或缓存API）与AWS提供的服务进行交互的便捷方式。开发人员可以围绕托管服务构建应用程序，而无需关心基础结构或维护。

-   [Spring Cloud Connectors](spring-cloud-connectors/README.md)

使各种平台中的PaaS应用程序可以轻松连接到数据库和消息代理（该项目以前称为“Spring Cloud”）等后端服务。

-   [Spring Cloud Contract](spring-cloud-contract/README.md)

Spring Cloud Contract是一个总体项目，其中包含帮助用户成功实施消费者驱动合同方法的解决方案。

-   [Spring Cloud Gateway](spring-cloud-gateway/README.md)

Spring Cloud Gateway是一款基于Project Reactor的智能可编程路由器。

-   [Spring Cloud OpenFeign](spring-cloud-openfeign/README.md)

Spring Cloud OpenFeign通过自动配置和Spring环境以及其他Spring编程模型习惯用法提供Spring Boot应用程序的集成。

-   [Spring Cloud Pipelines](spring-cloud-pipelines-to-cloud-pipelines-migration/README.md)

Spring Cloud Pipelines提供了一个固定意见的部署管道，其中包含确保您的应用程序可以零停机方式部署并轻松回滚出错的步骤。

-   [Spring Cloud Function](spring-cloud-function/README.md)

Spring Cloud Function通过函数促进业务逻辑的实现。它支持无服务器提供商之间的统一编程模型，以及独立运行（本地或PaaS）的能力。

----

##  发布说明

Spring Cloud是一个由独立项目组成的总体项目，原则上具有不同的发布节奏。为了管理投资组合，发布了BOM（物料清单），其中包含一组针对单个项目的依赖关系（见下文）。发布列车有名称而不是版本，以避免与子项目混淆。这些名称是一个字母序列（所以你可以按时间顺序排序）伦敦地铁站的名称（“天使”是第一个版本，“布里克斯顿”是第二个版本）。当各个项目的点数累积到临界质量时，或者其中一个项目中存在一个需要每个人都可用的关键错误时，发布列车将推出名称结尾为“.SRX”的“服务发布”，其中“X”是一个数字。

----
