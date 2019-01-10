#   JAX-RS: Java™ API for RESTful Web Services

##  内容
-   应用：Applications
-   资源：Resources
-   提供者：Providers
-   客户端API：Client API
-   过滤器和拦截器：Filters and Interceptors
-   验证：Validation
-   异步协议：Asynchronous Processing
-   服务器发送的事件：Server-Sent Events
-   上下文：Context
-   环境：Environment
-   运行时委托：Runtime Delegate
-   附录

----

此规范定义了一组Java API，用于开发根据(REST)体系结构样式构建的Web服务。

##  应用：Applications

-   配置

构成JAX-RS应用程序的资源和提供程序是通过应用程序提供的Application子类配置的。

-   验证

-   发布

应用程序以不同方式发布，具体取决于应用程序是在Java SE环境中运行还是在容器内运行。

1.  Java SE

在Java SE环境中，可以使用RuntimeDelegate的create-Endpoint方法获取端点类的已配置实例。

2.  Servlet

##  资源：Resources

使用JAX-RS，Web资源实现为资源类，请求由资源方法处理。

-   资源类

资源类是一个Java类，它使用JAX-RS注释来实现相应的Web资源。 资源类是POJO，至少有一个使用@Path注释的方法或请求方法指示符。

-   字段和Bean属性

实例化资源类时，根据注释的语义设置使用以下注释之一注释的字段和bean属性的值。

-   资源方法

资源方法是使用请求方法指示符注释的资源类的方法，它们用于处理请求。

-   URI模板

使用@Path批注将根资源类锚定在URI空间中。 注释的值是相对URI路径模板，其基URI由部署上下文和应用程序路径的组合提供。

-   声明媒体类型功能

应用程序类可以分别使用@Consumes和@Produces注解声明支持的请求和响应媒体类型。

-   注解继承

JAX-RS注释可以用于超类或实现的接口的方法和方法参数。

-   匹配资源方法的请求

实现不需要使用编写的算法，但必须产生与算法产生的结果等效的结果。

-   确定响应的MediaType

在许多情况下，不可能静态地确定响应的媒体类型。

##  提供者：Providers

JAX-RS中的提供者负责各种横切关注点，例如过滤请求，将表示转换为Java对象，将异常映射到响应。

-   声明周期和环境

默认情况下，为每个JAX-RS应用程序实例化每个提供程序类的单个实例。

-   实体提供者

实体提供程序在表示及其关联的Java类型之间提供映射服务。

-   上下文提供者

上下文提供者为资源类和其他提供者提供上下文。 上下文提供程序类实现ContextResolver <T>接口，可以使用@Provider进行注释以进行自动发现。

-   异常映射提供程序

异常映射提供程序将已检查或运行时异常映射到Response实例。 异常映射提供程序实现ExceptionMapper <T>接口，可以使用@Provider进行批注以进行自动发现。

-   异常

1.  服务端运行时

2.  客户端运行时


##  客户端API：Client API

客户端API用于访问Web资源。 它提供了比HttpURLConnection更高级的API以及与JAX-RS提供程序的集成。 除非另有说明，否则本章中介绍的类型位于javax.ws.rs.client包中。

-   引导客户端实例

-   资源访问

-   客户端目标

-   实体类型

-   调用

-   可配置类型

-   反应式客户端

-   执行服务

##  过滤器和拦截器：Filters and Interceptors

可以在JAX-RS实现中的明确定义的扩展点处注册过滤器和实体拦截器以执行。 它们用于扩展实现，以提供日志记录，机密性，身份验证，实体压缩等功能。

-   拦截器

实体拦截器环绕特定扩展点的方法调用。 过滤器在扩展点执行代码但不包装方法调用。

-   过滤器

过滤器分为过滤器链。 上一节中介绍的每个扩展点都有一个单独的过滤器链，即：ClientRequest，ClientResponse，ContainerRequest，ContainerResponse和PreMatch-ContainerRequest。

-   实体拦截器

实体拦截器实现接口ReaderInterceptor或WriterInterceptor，或两者。 每种实体拦截器都有一个拦截器链。 链中的实体拦截器根据其优先级进行排序并按顺序执行。

-   生命周期

-   绑定

绑定是过滤器或拦截器与资源类或方法（服务器API）或调用（客户端API）相关联的过程。

-   优先级

过滤器和拦截器作为相应链的一部分执行的顺序由[15]中定义的@Priority注释控制。

-   异常

##  验证：Validation

验证是验证某些数据是否遵循一个或多个预定义约束的过程。 Bean Validation规范定义了一个用于验证Java Bean的API。

-   约束注解

Server API支持提取请求值并使用注释（如@HeaderParam，@ QueryParam等）将它们映射到Java字段，属性和参数。

-   注解和验证

注释约束和验证器是根据Bean Validation规范定义的

-   实体验证

请求实体主体可以映射到资源方法参数。

-   默认验证模式

-   注解继承

-   验证和错误报告

##  异步协议：Asynchronous Processing

介绍JAX-RS中的异步处理功能。 客户端API和Server API都支持异步处理。

-   Server API

1.  AsyncResponse

异步处理使资源方法能够通知JAX-RS实现在返回时响应不易获得但将在未来生成。

2.  CompletionStage

注入AsyncResponse的另一种方法是使资源方法返回CompletionStage <T>的实例，作为对底层JAX-RS实现的指示，即启用异步处理。

-   EJB Resource Classes

-   Client API

流程API支持异步调用，作为调用构建过程的一部分。


##  服务器发送的事件：Server-Sent Events

服务器发送事件（SSE）是最初由W3C作为HTML5的一部分引入的规范，但目前由WHATWG维护。它提供了一种建立从服务器到客户端的单向通道的方法。

-   Client API

用于SSE的JAX-RS客户端API受到HTML5中相应JavaScript API的启发，但其变化源自使用不同语言。

-   Server API

JAX-RS SSE服务器API用于接受连接并将事件发送到一个或多个客户端。

-   广播

应用程序可能需要同时向多个客户端发送事件。 此操作在JAX-RS中称为广播。 可以在单个SseBroadcaster上注册多个SseEventSink。

-   处理管道

来自SSE客户端的连接由SseEventSink的可注入实例表示。 SSE和异步处理之间有一些相似之处。

-   Environment

SseEventSource类使用基于RuntimeDelegate的现有JAX-RS机制来查找使用服务名称javax.ws.rs.sse.SseEventSource.Builder的实现。

##  上下文：Context

JAX-RS提供了用于获取和处理有关应用程序部署上下文和各个请求的上下文的信息的工具。

-   并发

上下文特定于特定请求，但某些JAX-RS组件（具有除每个请求之外的生命周期的提供程序和资源类）的实例可能需要支持多个并发请求。

-   上下文类型

1.  Application

2.  URIs and URI Templates

3.  Headers

4.  内容谈判和先决条件

5.  安全

6.  服务者

7.  资源

8.  配置

##  环境：Environment

JAX-RS根资源类或提供程序可用的容器管理资源取决于部署它的环境。

-   Servlet 容器

@Context注释可用于指示对Servlet定义的资源的依赖性。

-   与Java EE技术集成

##  运行时委托：Runtime Delegate

RuntimeDelegate是一个抽象工厂类，它为创建实现JAX-RS API的对象提供了各种方法。这些方法旨在供其他JAX-RS API类使用，不应由应用程序直接调用。

-   Configuration

如果未通过注入提供，则提供的RuntimeDelegate API类使用以下算法获取具体实现类。


##  附录

-   注解
-   HTTP头
-   处理管道 流程图

----