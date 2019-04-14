#   Spring Cloud Netflix

核心组件

##  Spring Cloud  Eureka

>   独立运行

用来实现各个微服务实例的自动化注册和发现，解决微服务架构中的`服务实例`维护问题，包含服务注册中心、服务注册与服务发现

Eureka 服务端，即服务注册中心，支持高可用配置，依托强一致性提供良好的服务实例可用性，应对多种不同的故障场景。Netflix 推荐每个可用的区域运行一个 Eureka服务器，通过他形成集群，不同可用区域的服务注册中心通过异步模式相互复制各自的状态，意味着在任意给定的时间点每个实例关于所有服务的状态是有细微差别的。

Eureka 客户端，即服务的注册与发现，客户端通过注解和参数配置的方式，嵌入在客户端应用程序的代码中，在应用运行时，Eureka 客户端向注册中心注册自身提供的服务并周期性的发送心跳来更新他的服务租约。


### 服务端-Eureka 服务端

-   第一个启动
-   依赖：eureka-server
-   主要配置：不同的端口、名称相互指定实现可用
    -   指定端口
    -   指定名称：eureka-instance.hostname
    -   禁用自己注册自己：eureka-client.
    -   指示客户端注册地址：eureka-client.
    -   本地开发可以考虑关闭保护机制，eureka.server.enable-self-pre..=false
-   端点配置及监控
-   入口
    -   启用En..Server注解

### 客户端-服务提供者
-   业务实现
-   依赖：web、eureka
-   主要配置
    -   指定名称：spring.application.name=he-se
    -   实例名配置：eureka-instance.instanceId=${spring.application.name}:${random.int}
    -   指定注册地址
-   入口
    -   启用En..Client注解

### 客户端-服务消费者
-   接口调用
-   依赖：web、eureka、ribbon、hystrix
-   主要配置
    -   指定名称：spring.application.name=he-se
    -   实例名配置：eureka-instance.instanceId=${spring.application.name}:${random.int}
    -   指定注册地址
-   入口
    -   启用En..Client注解
    -   RestTemplate。。@LoadBa注解开启客户端负载均衡
        -   地址：服务提供者名称


----

##   Spring Cloud  Ribbon

>   被嵌入服务之中

客户端负载均衡的服务调用。

存在于每一个Spring Cloud构建的微服务和基础设施里

-   RestTemplate。。@LoadBa注解开启客户端负载均衡
    -   RestTemplate API
    -   地址：服务提供者名称

重试机制参数

----

##   Spring Cloud  Hystrix

>   监控服务单独运行

容错管理组件，实现断路器模式，帮助服务依赖中出现的延迟和为故障提供强大的容错能力

具备服务降级、服务熔断、线程和信号隔离、请求缓存、请求合并以及服务监控

-   监控
    -   服务实例依赖：hystrix、actuator
    -   单个服务监控
    -   集群服务监控：Turbine，集成Rabbit
-   服务执行异常

----

##   Spring Cloud  Feign 

基于 Ribbon 和 Hystrix 的声明式服务调用

----

##  Spring Cloud  Zuul  

网关组件，提供智能路由、访问过滤等

----

##  Spring Cloud  Archaius  

外部化配置组件




----

