#   Spring Cloud

基于 Spring Boot 实现的微服务架构开发工具，整合了诸多被广泛实践和证明过的框架作为实施的基础部件。为微服务架构中涉及的配置管理、服务治理、断路器、智能路由、微代理、控制总线、全局锁、决策竞选、分布式会话和集群管理等操作提供了一种简单的开发方式。

##  资料
-   [入门实践](action/README.md)
    -   (纸)Spring Cloud微服务实战.pdf
    -   (纸)Spring Cloud与Docker微服务架构实战.pdf
    -   (纸)云原生Java：Spring Boot、Spring Cloud与Cloud Foundry弹性系统设计
    -   Java微服务.pdf
-   网站
    -   [Spring Cloud教程](https://github.com/dyc87112/SpringCloud-Learning)
    -   [纯洁的微笑](http://www.ityouknow.com/spring-cloud.html)
-   博客
    -   [基于SpringBoot和SpringCloud实现微服务架构](https://blog.csdn.net/HQZ820844012/article/details/80400058)
    -   [Spring Cloud教程](https://www.cnblogs.com/chry/tag/Spring%20Cloud%E6%95%99%E7%A8%8B/)
    -   [为何spring cloud 应该使用　Euraka server　而不是 Zookeeper](https://blog.csdn.net/bigtree_3721/article/details/78389433)
-   项目
    -   [项目示例，文档演示](https://github.com/kaoshanji/example-spring-cloud)
    -   [基于 Spring Boot、Spring Cloud、Spring Oauth2 和 Spring Cloud Netflix 等框架构建的微服务项目](https://github.com/zhangxd1989/spring-boot-cloud)
    -   [Spring Cloud 学习案例](https://github.com/ityouknow/spring-cloud-examples)
    -   [cloudE](https://github.com/vangao1989/cloudE)
    -   [Cloud-Admin](https://gitee.com/minull/ace-security)

##  内容
-   基本概念
    -   Cloud Native 云原生应用
    -   微服务架构
-   服务发现与注册
    -   Eureka
    -   Zookeeper
    -   Consul
-   服务负载均衡
    -   DiscoveryClient 抽象
    -   Spring Cloud Loadbalancer
    -   Feign
-   服务配置：Spring Cloud Config
    -   Git
    -   Zookeeper
    -   Consul
-   服务限流与熔断
    -   Hystrix
    -   Resilience4j
-   服务链路追踪
    -   Dapper论文
    -   Spring Cloud Sleuth
        -   Brave
        -   Zipkin
-   消息：Spring Cloud Stream
    -   RabbitMQ
    -   Kafka
-   安全：Spring Cloud Security
-   服务网关：Spring Cloud Gateway
-   云平台支撑
    -   Spring Cloud GCP
    -   Spring Cloud AWS
    -   Spring Cloud Cloudfoundry
    -   Spring Cloud Alibaba


----

##      项目结构
-       xp-spring-cloud-example
        -       common：被嵌入
        -       app：单独运行，spring-cloud是根
                -       technology：技术支持，资源环境
                        -       eureka
                -       service：业务逻辑
                        -       user：用户模块
                        -       goods：商品部分
                        -       order：订单模块
                        -       common：公共逻辑


----

##      命令

```base
java -jar xx.jar --spring.pro=..

```


----