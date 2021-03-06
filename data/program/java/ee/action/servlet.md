#   Java™ Servlet 大纲

##  内容
-   Servlet接口：Servlet Interface
-   请求对象：Request
-   Servlet上下文：Servlet Context
-   响应对象：Response
-   过滤器：Filtering
-   会话：Sessions
-   注解和插件：Annotations and pluggability
-   分发请求：Dispatching Requests
-   web应用：Web Applications
-   应用生命周期事件：Application Lifecycle Events
-   映射请求到Servlets：Mapping Requests to Servlets
-   安全：Security

----

##  Servlet 接口

Servlet接口是一个普通的Java技术组件。

Servlet接口是Java Servlet API的中心抽象。 所有servlet都可以通过扩展实现接口的类来直接或更常见地实现此接口。 Java Servlet API中实现Servlet接口的两个类是GenericServlet和HttpServlet。 在大多数情况下，开发人员将扩展HttpServlet以实现其servlet。

-   请求处理方法

基本的Servlet接口定义了一个用于处理客户端请求的 service 方法。servlet容器处理每个请求时路由到一个servlet实例来调用此方法。

业务逻辑方法与HTTP请求方法保持一致

-   Servlet 生命周期
    -   加载和实例化
    -   初始化
    -   异常处理
-   处理请求
    -   多线程问题
    -   请求处理异常
    -   `异步处理`
    -   线程安全
    -   协议升级
-   结束 Servlet

##  请求对象

request 对象封装来自客户端请求的所有信息。 在HTTP协议中，从客户端传输到服务器此信息在HTTP标头和请求的消息体中。

-   HTTP协议参数

servlet 的请求参数是客户端作为其请求的一部分发送到servlet容器的字符串。

当请求是HttpServletRequest对象，容器将填充URI查询字符串和POST-ed数据中的参数。

参数存储为一组名称 - 值对。 对于任何给定的参数名称，可以存在多个参数值。ServletRequest接口的以下方法可用于访问参数：getParameterxxx

-   文件上传

发送数据类型：multipart/formdata 就是上传文件，获取数据：getPart方法

-   属性

属性是与请求关联的对象。 属性可以由容器设置以表示否则不能通过API表达的信息，或者可以由servlet设置以将信息传递给另一个servlet（通过RequestDispatcher）。

-   Headers

servlet 可以访问 HTTP 请求头信息

-   请求路径节点

为servlet请求提供服务的请求路径由许多重要部分组成：上下文路径、servlet路径、PathInfo

-   文件路径方法

-   `非阻塞I/O`

Web容器中的非阻塞请求处理有助于提高对改进的Web容器可伸缩性的不断增长的需求，增加Web容器可以同时处理的连接数。

-   `HTTP / 2服务器推送`

服务器推送是出现在servlet API中的HTTP / 2中最明显的改进。HTTP / 2中的所有新功能（包括服务器推送）旨在提高Web浏览体验的感知性能。

-   Cookies

HttpServletRequest接口提供getCookies方法以获取请求中存在的cookie数组。 这些cookie是客户端发出的每个请求从客户端发送到服务器的数据。

-   SSL 属性

如果请求已通过安全协议（如HTTPS）传输，则必须通过ServletRequest接口的isSecure方法公开此信息。

-   国际化

客户端可以选择向Web服务器指示他们更喜欢响应的语言。可以使用Accept-Language头以及HTTP / 1.1规范中描述的其他机制从客户端传达此信息。

-   请求编码

目前，许多浏览器不会使用Content-Type标头发送char编码限定符，而是打开用于读取HTTP请求的字符编码的确定。如果没有char编码限定符，如果Content-Type是application / x-www-form-urlencoded，则容器用于创建请求阅读器的默认编码和解析POST数据必须是US-ASCII。

-   请求对象的生命周期

每个请求对象仅在servlet的服务方法范围内有效，或者在过滤器的doFilter方法范围内有效，除非为组件启用了异步处理并且在请求对象上调用了startAsync方法。

##  Servlet 上下文

-   ServletContext 接口

ServletContext接口定义servlet运行的Web应用程序视图。

使用ServletContext对象，servlet可以记录事件，获取对资源的URL引用，以及设置和存储上下文中其他servlet可以访问的属性。

-   ServletContext 接口范围

ServletContext接口有一个实例对象与部署到容器中的每个Web应用程序相关联。

在容器分布在许多虚拟机上的情况下，Web应用程序将为每个JVM提供ServletContext的实例。

-   初始化参数

ServletContext接口的以下方法允许servlet访问与部署描述符中的Application Developer指定的Web应用程序关联的上下文初始化参数：getInitParamexx

-   配置方法

这些方法只能在应用程序初始化期间从ServletContextListener实现的contexInitialized方法或ServletContainerInitializer实现的onStartup方法调用。

如果ServletContext传递给ServletContextListener的
contextInitialized方法，其中ServletContextListener既未在web.xml或web-fragment.xml中声明，也未使用@WebListener进行批注，则必须为ServletContext中定义的所有方法抛出UnsupportedOperationException，以便对servlet，过滤器和侦听器进行编程配置。

-   上下文属性

servlet可以通过名称将对象属性绑定到上下文中。 绑定到上下文的任何属性都可用于属于同一Web应用程序的任何其他servlet。

-   Resources

ServletContext接口仅提供对作为Web应用程序一部分的静态内容文档层次结构的直接访问。

-   多个主机和Servlet上下文

Web服务器可以支持在服务器上共享一个IP地址的多个逻辑主机。

##  响应对象

响应对象封装了从服务器返回给客户端的所有信息。 在HTTP协议中，此信息通过HTTP头或请求的消息体从服务器传输到客户端。

-   Buffering

允许（但不是必需）servlet容器来缓冲输出到客户端以提高效率。

通常，执行缓冲的服务器使其成为默认值，但允许servlet指定缓冲参数。

-   Headers

servlet可以通过HttpServletResponse接口的以下方法设置HTTP响应的标头。

-   HTTP 预备

HTTP预告片是响应主体之后的特殊HTTP标头的集合。

-   非阻塞I/O

非阻塞IO仅适用于Servlet和过滤器中的异步请求处理和升级处理。 

-   便捷方法

-   国际化

-   关闭响应对象

-   响应对象的生命周期

除非关联的请求对象为组件启用了异步处理，否则每个响应对象仅在servlet的服务方法范围内有效，或者在过滤器的doFilter方法范围内有效。

##  过滤器

过滤器是Java组件，允许将请求中的有效负载和头信息快速转换为资源和来自资源的响应.

-   什么是 filter?

过滤器是可重用的代码段，可以转换HTTP请求，响应和标头信息的内容。

过滤器通常不像servlet那样创建响应或响应请求，而是修改或调整对资源的请求，并修改或调整来自资源的响应。

过滤器可以对动态或静态内容起作用。

-   主要概念

应用程序开发人员通过实现创建过滤器 javax.servlet.Filter接口并提供不带参数的公共构造函数。

1.  Filter 生命周期

2.  包裹 Requests 和 Responses

3.  Filter 环境

4.  配置 Filter

5.  Filters 和 RequestDispatcher


##  会话

HTTP 是一个无状态协议。要构建有效的Web应用程序，一系列相关的请求必须关联。

该规范定义了一个简单的HttpSession接口，该接口允许servlet容器使用几种方法中的任何一种来跟踪用户的会话，而不会让Application 开发 处于任何一种方法的细微差别中。

-   会话跟踪机制

1.  Cookies

2.  SSL 会话

3.  URL重写

-   创建一个会话

-   会话作用域

-   绑定会话属性

-   会话超时

-   最后访问时间

-   会话语义

1.  线程问题

2.  分布式环境

3.  客户端


##  注解和插件

本章介绍如何使用注释和其他增强功能来实现框架和库的可插入性，以便在Web应用程序中使用。

-   注解和插件

以下是javax.servlet中的注解。 所有这些都具有Web xsd所涵盖的相应部署描述符元数据，从javax.servlet.annotation：

1.  HttpConstraint
2.  HttpMethodConstraint
3.  MultipartConfig：当在Servlet上指定时，此批注指示它所期望的请求是multipart / form-data类型。
4.  ServletSecurity
5.  WebFilter：用于在Web应用程序中定义Filter组件
6.  WebInitParam：用于指定必须传递给Servlet或Filter的任何init参数。
7.  WebListener：用于注释侦听器以获取特定Web应用程序上下文上的各种操作的事件。
8.  WebServlet：用于在Web应用程序中定义Servlet组件，在类上指定，并包含有关正在声明的Servlet的元数据。

web.xml和相关片段也涵盖了相关包中的以下注释，从javax.annotation：

1.  PostConstruct
2.  PreDestroy
3.  Resource
4.  Resources

来自javax.annotation.security:

1.  DeclareRoles
2.  RunAs

来自javax.annotation.sql：

1.  DataSourceDefinition
2.  DataSourceDefinitions

来自javax.persistence：

1.  PersistenceContext
2.  PersistenceContexts
3.  PersistenceUnit
4.  PersistenceUnits

-   插件

##  分发请求

构建Web应用程序时，将请求处理转发到另一个servlet或将另一个servlet的输出包含在响应中通常很有用。 RequestDispatcher接口提供了实现此目的的机制。

在请求上启用异步处理时，AsyncContext允许用户将请求分派回servlet容器。

-   获取一个 RequestDispatcher

可以通过以下方法从ServletContext获取实现RequestDispatcher接口的对象：getRequestDispatcher、getNamedDispatcher

-   请求分发

要使用请求调度程序，servlet会调用RequestDispatcher接口的include方法或forward方法。

-   Include 方法

可以随时调用RequestDispatcher接口的include方法。 include方法的目标servlet可以访问请求对象的所有方面，但它对响应对象的使用更加有限。

-   Forward 方法

只有当没有输出已提交给客户端时，调用servlet才能调用RequestDispatcher接口的forward方法。如果输出数据存在于尚未提交的响应缓冲区中，则必须在调用目标servlet的服务方法之前清除内容。

-   异常处理

如果作为请求调度程序目标的servlet抛出运行时异常或ServletException或IOException类型的已检查异常，则应将其传播到调用servlet。

-   获取 AsyncContext

可以通过startAsync方法之一从ServletRequest获取实现AsyncContext接口的对象。

-   Dispatch 方法

##  web 应用

Web应用程序是servlet，HTML页面，类和其他资源的集合，它们构成Web服务器上的完整应用程序。 Web应用程序可以捆绑在多个供应商的多个容器上运行。

-   Web服务器中的Web应用程序

Web应用程序以Web服务器中的特定路径为根。

servlet容器可以为自动生成Web应用程序建立规则。

-   关联到 ServletContext

servlet容器必须在Web应用程序和ServletContext之间强制执行一对一的对应关系。 ServletContext对象为servlet提供了应用程序的视图。

-   web应用组成

-   部署层次结构

-   目录结构

-   Web应用程序存档文件

-   Web应用程序部署描述符

-   更换 web 应用

-   错误处理

-   欢迎文件

-   Web应用程序环境

-   web 应用部署

-   包含web.xml部署描述符

##  应用生命周期事件

-   介绍

-   事件监听

-   事件类型和监听接口

-   监听类配置

-   部署示例

-   监听器实例和线程

-   监听示例

-   分布式容器

-   会话事件

##  请求和Servlet映射

-   URL路径

-   映射规范

-   映射的运行时发现

##  安全

-   简介

-   声明式安全

-   编程式安全

-   程序化安全策略配置

-   角色

-   认证

-   认证信息的服务器跟踪

-   指定安全约束

-   默认策略

-   登录与登出


----
