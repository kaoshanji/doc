#   Spring Cloud Netflix

核心组件

##  Spring Cloud  Eureka

用来实现各个微服务实例的自动化注册和发现，解决微服务架构中的`服务实例`维护问题，包含服务注册中心、服务注册与服务发现

Eureka 服务端，即服务注册中心，支持高可用配置，依托强一致性提供良好的服务实例可用性，应对多种不同的故障场景。Netflix 推荐每个可用的区域运行一个 Eureka服务器，通过他形成集群，不同可用区域的服务注册中心通过异步模式相互复制各自的状态，意味着在任意给定的时间点每个实例关于所有服务的状态是有细微差别的。

Eureka 客户端，即服务的注册与发现，客户端通过注解和参数配置的方式，嵌入在客户端应用程序的代码中，在应用运行时，Eureka 客户端向注册中心注册自身提供的服务并周期性的发送心跳来更新他的服务租约。

-   [项目示例](eureka-project.md)
-   [详情](eureka-detail.md)


----

##   Spring Cloud  Hystrix

容错管理组件，实现断路器模式，帮助服务依赖中出现的延迟和为故障提供强大的容错能力


----

##   Spring Cloud  Ribbon

客户端负载均衡的服务调用

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

