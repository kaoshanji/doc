#   Spring Cloud Netflix

核心组件，基本满足微服务

##  Spring Cloud  Eureka

>   独立运行

用来实现各个微服务实例的自动化注册和发现，解决微服务架构中的`服务实例`维护问题，包含服务注册中心、服务注册与服务发现

Eureka 服务端，即服务注册中心，支持高可用配置，依托强一致性提供良好的服务实例可用性，应对多种不同的故障场景。Netflix 推荐每个可用的区域运行一个 Eureka服务器，通过他形成集群，不同可用区域的服务注册中心通过异步模式相互复制各自的状态，意味着在任意给定的时间点每个实例关于所有服务的状态是有细微差别的。

Eureka 客户端，即服务的注册与发现，客户端通过注解和参数配置的方式，嵌入在客户端应用程序的代码中，在应用运行时，Eureka 客户端向注册中心注册自身提供的服务并周期性的发送心跳来更新他的服务租约。


### 服务注册中心：Eureka

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
    -   主类注解：启用En..Server注解

类似一个现存产品，大多数情况下不需要修改他的配置信息

### 服务提供者
-   业务实现
-   依赖：web、eureka
-   主要配置
    -   指定名称：spring.application.name=he-se
    -   实例名配置：eureka-instance.instanceId=${spring.application.name}:${random.int}
    -   指定注册地址
-   入口
    -   主类注解：启用En..Client注解

### 服务消费者
-   接口调用
-   依赖：web、eureka、Feign(ribbon、hystrix)
-   主要配置
    -   指定名称：spring.application.name=he-se
    -   实例名配置：eureka-instance.instanceId=${spring.application.name}:${random.int}
    -   指定注册地址
-   入口
    -   主类注解：启用En..Client注解
    -   RestTemplate。。@LoadBa注解开启客户端负载均衡
        -   地址：服务提供者名称

----

##   Spring Cloud  Ribbon

>   被嵌入服务之中

客户端负载均衡的服务调用。

存在于每一个Spring Cloud构建的微服务和基础设施里

-   RestTemplate。。@LoadBa注解开启客户端负载均衡
    -   RestTemplate API 请求拦截实现对依赖服务的接口调用
    -   地址：服务提供者名称

重试机制参数

----

##   Spring Cloud  Hystrix

>   监控服务单独运行

服务保护和监控

容错管理组件，实现断路器模式，帮助服务依赖中出现的延迟和为故障提供强大的容错能力

具备服务降级、服务熔断、线程和信号隔离、请求缓存、请求合并以及服务监控

-   监控
    -   服务实例依赖：hystrix、actuator
    -   单个服务监控
    -   集群服务监控：Turbine，集成Rabbit
-   服务执行异常

----

##   Spring Cloud Feign 

对 Ribbon 和 Hystrix 整合，并提供 声明式的Web服务客户端定义方式

定义和实现依赖服务接口的定义，只需创建一个接口并用注解的方式来配置他，即可完成对服务提供方的接口绑定

编解码器

-   服务消费者
    -   服务实现依赖：web、eureka、feign
    -   服务接口定义：web
    -   主类注解：@En..FeifnCli..
-   定义服务业务接口
    -   类上标注服务名称 @Fei..Cli
    -   方法上标注映射名称 @Requ。。。
-   参数绑定
-   配置
    -   Ribbon配置
    -   Hystrix配置
    -   日志
    -   请求压缩

----

##  Spring Cloud  Zuul  

>   独立运行，可以加入自定义过滤器来实现对请求的拦截和过滤

统一的API网关入口被客户端访问

看起来是个智能应用服务器，定义类像门面模式，为整个微服务架构系统提供门面，所有的外部客户端访问都需要经过他来进行调度和过滤

提供请求路由、负载均衡、效验过滤等，还有与服务治理框架结合、请求转发时的熔断机制、服务的聚合等

抽离非业务性质的逻辑，如签名效验、登录效验，指定那些规则的请求需要执行效验逻辑

-   依赖：zuul、eureka
-   主类注解：@Ena..ZuulPr..
-   配置
    -   面向服务的路由转发：请求路径 <--> 服务名称，默认是对应的，可以设置不开放的地址
    -   请求路径以版本号为前缀，版本号在服务名称后面
    -   指定服务中心
-   请求过滤，路径查找以定义顺序为准
-   异常处理机制
-   动态加载，配合 cloud-config 
    -   依赖：zuul、eureka、config

----

##  Spring Cloud  Archaius  

外部化配置组件




----

