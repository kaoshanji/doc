logback.qos.ch 文档 - 2017-07
>  [官网](https://logback.qos.ch/index.html)


### 简介
Logback 是很受欢迎的 log4j 项目继承者。

Logback的架构是非常通用的，以便在不同的情况下应用，目前，logback分为三个模块：logback-core，logback-classic和logback-access。

logback-core 模块是其他两个模块的基础，logback-classic可以看作是改进的log4j版本，另外，他还实现了 SLF4J API，可以切换到其他日志框架。

logback-access 模块与Tomcat和Jetty等Servlet容器集成，提供HTTP访问日志功能。可以在 logback-core 之上构建自己的模块。

#### 相关项目
[logback-audit](http://audit.qos.ch/) 旨在处理具有长期业务意义的记录事件，基于logback-core。

- [手册](manual/Index.md)
- [使用logback-access访问HTTP日志](access.md)