#   Tomcat

Tomcat是Apache 软件基金会（Apache Software Foundation）的Jakarta 项目中的一个核心项目

Tomcat 服务器是一个免费的开放源代码的Web 应用服务器，属于轻量级应用服务器，在中小型系统和并发访问用户不是很多的场合下被普遍使用，是开发和调试JSP 程序的首选。

Tomcat是Apache 服务器的扩展，但运行时它是独立运行的，所以当你运行tomcat 时，它实际上作为一个与Apache 独立的进程单独运行的。Apache 为HTML页面服务，而Tomcat 实际上运行JSP 页面和Servlet。

Apache Tomcat 9.0版本实现了Servlet 4.0和JavaServer Pages 2.3 规范。

----

##  版本：9.0
-   [官网](http://tomcat.apache.org/)
-   [文档](https://tomcat.apache.org/tomcat-9.0-doc/index.html)

----

##  指南
-   `简介` - 简要介绍Apache Tomcat的高级概述。
-   `设置` - 如何在各种平台上安装和运行Apache Tomcat。
-   `第一个Web应用程序` - 介绍Servlet规范中定义的 Web应用程序的概念。涵盖Web应用程序源代码树的基本组织结构，Web应用程序归档的结构以及Web应用程序部署描述符（/WEB-INF/web.xml）的介绍。
-   `部署者` - 操作Apache Tomcat部署者来部署，预编译和验证Web应用程序。
-   `Manager` - 运行 Manager Web应用程序以在Apache Tomcat运行时部署，取消部署和重新部署应用程序。
-   `主机管理器` - 运行 Host Manager Web应用程序以在Apache Tomcat运行时添加和删除虚拟主机。
-   `领域和访问控制` - 描述如何配置领域（用户，密码及其相关角色的数据库）以用于使用 Container Managed Security的 Web应用程序。
-   `安全管理器` - 配置和使用Java安全管理器来支持对Web应用程序行为的细粒度控制。
-   `JNDI资源` - 在提供给每个Web应用程序的JNDI命名上下文中配置标准和自定义资源。
-   `JDBC DataSource` - 使用数据库连接池配置JNDI数据源。许多流行数据库的例子。
-   `类加载` - 有关Apache Tomcat中类加载的信息，包括应用程序类的放置位置，以便它们可见。
-   `JSP` - 有关Jasper配置的信息，以及JSP编译器的用法。
-   `SSL/TLS` - 安装和配置SSL / TLS支持，以便您的Apache Tomcat可以使用https协议提供请求。
-   `SSI` - 在Apache Tomcat中使用服务器端包含。
-   `CGI` - 在Apache Tomcat中使用CGI。
-   `代理支持` - 将Apache Tomcat配置为在代理服务器（或充当代理服务器的Web服务器）后面运行。
-   `MBean描述符` - 为自定义组件配置MBean描述符文件。
-   `默认Servlet `- 配置默认servlet和自定义目录列表。
-   `Apache Tomcat集群` - 在Apache Tomcat环境中启用会话复制。
-   `平衡器` - 配置，使用和扩展负载平衡器应用程序。
-   `连接器` - Apache Tomcat中提供的连接器和本地Web服务器集成。
-   `监控和管理` - 启用JMX远程支持，并使用工具来监控和管理Apache Tomcat。
-   `日志记录` - 在Apache Tomcat中配置日志记录。
-   `Apache便携式运行时` - 使用APR提供卓越的性能，可扩展性以及与本机服务器技术的更好集成。
-   `虚拟主机` - 在Apache Tomcat中配置虚拟主机。
-   `高级IO` - 通过常规阻塞IO提供的扩展。
-   `其他组件` - 获取额外的可选组件。
-   `在Maven中使用Tomcat库` - 通过Maven获取Tomcat jar。
-   `安全注意事项` - 保护Apache Tomcat安装时要考虑的选项。
-   `高并发性JDBC池` - 配置Tomcat以使用备用JDBC池。
-   `WebSocket支持` - 为Apache Tomcat开发WebSocket应用程序。
-   `URL重写` - 使用基于正则表达式的重写阀进行条件URL和主机重写

----


##  动手实践
-   [安装]



##  源码分析

