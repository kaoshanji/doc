#   Web框架


web 由的`spring-web`，`spring-webmvc`，`spring-websocket`，和 `spring-webmvc-portlet`模块。

该`spring-web`模块提供基本的面向Web的集成功能，例如多部分文件上传功能和使用Servlet侦听器对IoC容器进行初始化以及面向Web的应用程序上下文。它还包含一个HTTP客户端和Spring远程处理支持的Web相关部分。

该`spring-webmvc`模块（也称为Web-Servlet模块）包含用于Web应用程序的Spring的模型 - 视图 - 控制器（MVC）和REST Web服务实现。Spring的MVC框架提供了域模型代码和Web表单之间的清晰分离，并与Spring框架的所有其他功能集成在一起。

该`spring-webmvc-portlet`模块（也称为Web-Portlet模块）提供了用于Portlet环境的MVC实现，并反映了基于Servlet的`spring-webmvc`模块的功能。


##  [Web MVC框架](section010000.md)

Spring Web模型 - 视图 - 控制器（MVC）框架是围绕一个 `DispatcherServlet`将请求分派给处理程序的设计，具有可配置的处理程序映射，视图分辨率，区域设置，时区和主题解析以及对上载文件的支持。默认处理程序基于`@Controller`和`@RequestMapping` 注释，提供了广泛的灵活的处理方法。随着Spring 3.0的推出，该`@Controller`机制还允许您通过`@PathVariable`注释和其他功能创建RESTful Web站点和应用程序。

在Spring Web MVC中，可以使用任何对象作为命令或表单支持对象; 您不需要实现特定于框架的接口或基类。Spring的数据绑定非常灵活：例如，它将类型不匹配视为可由应用程序评估的验证错误，而不是系统错误。因此，您不需要将业务对象的属性复制为表单对象中简单的非类型化字符串，只是为了处理无效提交或正确转换字符串。相反，通常最好直接绑定到您的业务对象。

Spring的视图分辨率非常灵活。A `Controller`通常负责`Map`使用数据准备模型并选择视图名称，但它也可以直接写入响应流并完成请求。通过文件扩展名或Accept头内容类型协商，通过bean名称，属性文件甚至自定义`ViewResolver`实现，视图名称解析是高度可配置的。模型（MVC中的M）是一个`Map`接口，它允许视图技术的完整抽象。您可以直接与基于模板的渲染技术（如JSP，Velocity和Freemarker）集成，也可以直接生成XML，JSON，Atom和许多其他类型的内容。该模型`Map` 简单地转换为适当的格式，例如JSP请求属性，Velocity模板模型。


##  [视图技术](section020000.md)

Spring擅长的领域之一是将视图技术与MVC框架的其余部分分开。例如，决定使用Groovy标记模板或Thymeleaf代替现有的JSP主要是配置问题。本章将介绍与Spring合作的主要视图技术，并简要介绍如何添加新技术。


##  [WebSocket支持](section030000.md)

介绍Spring Framework对Web应用程序中WebSocket风格的消息传递的支持，包括将STOMP用作应用程序级WebSocket子协议


##  [CORS支持](section040000.md)

出于安全原因，浏览器禁止对当前原点以外的资源进行AJAX调用。例如，当您在一个选项卡中检查您的银行帐户时，您可以在另一个选项卡中打开evil.com网站。来自evil.com的脚本不应该能够使用您的凭据向您的银行API发送AJAX请求（例如，从您的帐户中提取资金！）。

跨源资源共享 （CORS）是由大多数浏览器实现 的W3C规范，允许您以灵活的方式指定哪种跨域请求被授权，而不是使用一些安全性较低和功能较弱的黑客（如IFRAME或JSONP）。

从Spring Framework 4.2开始，CORS得到支持。CORS请求（包括使用`OPTIONS`方法的预检）将自动发送到各种注册`HandlerMapping`的服务器。它们处理CORS预检请求并通过CorsProcessor 实现（ 默认为DefaultCorsProcessor）拦截CORS简单和实际的请求 ，以便`Access-Control-Allow-Origin`根据您提供的CORS配置添加相关的CORS响应头（例如）




