#   Web后端

##  定义

客户端和服务器端基于HTTP网络协议进行数据交换，客户端主动发起请求，服务端被动响应，请求通过URI映射到服务端

-   [依赖](dependency.md)

----

##  技术方案

-   基础设施
    -   操作系统
        -   Linux
    -   网络协议
        -   HTTP
    -   统一环境
        -   Docker
    -   持续交付
        -   代码管理
-   服务支持
    -   数据库：数据存储
        -   MySQL
        -   Redis
        -   MongoDB
    -   消息队列：内部通信 or 并行逻辑处理
        -   RabbitMQ
        -   Redis
        -   ZeroMQ
        -   ActiveMQ
    -   搜索服务：查看关心的数据
        -   Lucene
        -   Solr
        -   ElasticSearch
        -   Sphinx
        -   CoreSeek
    -   缓存系统
        -   Redis
    -   定时任务：周期性的运行
        -   Linux-Crontab
        -   Java-Quartz
        -   Python-APScheduler
    -   短信服务
-   多节点
    -   分布式服务：服务共用
        -   REST
        -   RPC
        -   Hprose
        -   Dubbo
        -   Netty
    -   HTTP代理
        -   Nginx
    -   文件系统：文件存储
        -   FastDFS
-   逻辑处理（编程语言）
    -   请求和响应对象
        -   URL的组成部分
        -   HTTP请求方法
        -   请求报头
        -   响应报头
        -   互联网媒体类型
        -   请求体
        -   参数
        -   请求对象
        -   响应对象
    -   请求数据
        -   表单
        -   文件上传
        -   路由/路径
    -   响应数据
        -   页面视图
        -   文本数据
        -   二进制
    -   会话
        -   Cookie
        -   内存存储
        -   请求头
        -   地址栏
    -   中间件/组件
        -   异常
        -   转换请求数据
        -   请求数据验证
        -   包装响应数据
        -   日志
        -   上下文
        -   过滤器/拦截器
        -   执行前后
        -   请求前后
        -   响应前后
    -   环境的问题
        -   执行环境
        -   环境特定配置
        -   网站监控
    -   持久化
        -   文件
        -   事务
        -   数据库
    -   第三方服务
        -   数据/文件
        -   天气
        -   支付
-   日志分析平台
    -   Logstash+ElasticSearch+Kibana

----

##  业务场景

-   用户验证
    -   token
-   通信安全
    -   HTTPS
    -   URL签名
    -   AES对称加密
-   版本升级
-   处理表情
-   同步更新
    -   作用
        -   获取最新的数据
    -   推拉结合
        -   有数据更新时推送通知
        -   app再更新数据
    -   数据增量更新
-   图片处理
    -   七牛
    -   又拍
-   视频处理
    -   FFmpeg

----

##  百万数据

----

