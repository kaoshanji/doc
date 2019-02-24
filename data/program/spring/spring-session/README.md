#   Spring Session

Spring Session提供了一个管理用户会话信息的API和实现。

`特征`

Spring Session使得支持集群会话的过程变得非常简单，而不会受限于特定于应用程序容器的解决方案。它还提供透明的整合：
-   `HttpSession` - 允许替换`HttpSession`应用程序容器（即Tomcat）中立的方式，支持在头中提供会话ID以使用RESTful API
-   `WebSocket` - 提供`HttpSession`在接收WebSocket消息时保持活动状态的能力
-   `WebSession` - 允许以`WebSession`应用程序容器中立的方式替换Spring WebFlux

`模块`

Spring Session包含以下模块：
-   `Spring Session Core` - 提供核心Spring会话功能和API
-   `Spring Session Data Redis` - 由Redis 提供`SessionRepository`和`ReactiveSessionRepository`实现的支持和配置支持
-   `Spring Session JDBC` - 提供`SessionRepository`由关系数据库和配置支持支持的实现
-   `Spring Session Hazelcast` - 提供`SessionRepository`由Hazelcast和配置支持支持的实施


##  版本：2.0.2.RELEASE
-   [文档](https://docs.spring.io/spring-session/docs/2.0.2.RELEASE/reference/html5/)
-   [API](https://docs.spring.io/spring-session/docs/2.0.2.RELEASE/api/)
-   [GitHub](https://github.com/spring-projects/spring-session)

----

##  样本和指南（从这里开始）



##  Spring Session会话模块



##  HttpSession集成



##  WebSocket集成



##  WebSession集成



##  Spring Security Integration



##  API文档





