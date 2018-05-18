#   CORS支持

从Spring Framework 4.2开始，CORS得到支持。CORS请求（包括使用`OPTIONS`方法的预检）将自动发送到各种注册`HandlerMapping`的服务器。它们处理CORS预检请求并通过CorsProcessor 实现（ 默认为DefaultCorsProcessor）拦截CORS简单和实际的请求 ，以便`Access-Control-Allow-Origin`根据您提供的CORS配置添加相关的CORS响应头（例如）

##  控制器方法CORS配置



##  全局CORS配置



##  高级定制



##  基于过滤器的CORS支持



