#   分布式服务跟踪：Spring Cloud Sleuth

对于每个请求，全链路调用的跟踪非常关键，通过实现对请求调用的跟踪可以帮助我们快速发现错误根源以及监控分析每条请求链路上的性能瓶颈。

存在于各个微服务调用与被调用之间

-   应用服务
    -   依赖：sleuth
-   logback日志收集
    -   依赖：logback-encoder
    -   在logback的配置中增加对 Logstash 的 Appender，就能将日志转成JSON格式存储和输出了

##  Zipkin
-   服务器
    -   独立运行
    -   依赖：zipkin-server、..-ui、jdbc、mysql、zipkin-autoconfigure-storage-mysql
    -   配置
        -   指定端口：9411
-   应用
    -   依赖：sleuth-zipkin
    -   配置
        -   指定地址

引入基于日志的分析系统集中收集、存储和搜索这个跟踪信息。







