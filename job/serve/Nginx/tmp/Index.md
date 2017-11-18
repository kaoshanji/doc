Nginx doc

### 简介

- [官网](http://nginx.org/)
- 一款免费开源的高性能HTTP服务器及反向代理服务器产品，还提供IMAP/POP3代理服务等功能
### 适用场景
- 可以用作HTTP服务器，也可以作为反向代理服务器或者邮件服务器
- 能够快速响应静态页面的请求
- 支持FastCGI、SSL、Virtual Host、URL Rewrite、HTTP Basic Auth、Gzip等大量功能
### 组件
- 配置
### 实践
- [安装与管理](doc/practice/install.md)
- [基础配置指令](doc/practice/configuration.md)
    - 了解主要配置功能
- [静态资源](doc/practice/static.md)
    - 服务器静态文件对外提供访问
- [Rewrite功能](doc/practice/rewrite.md)
    - 服务重定向
    - 不同URI映射到指定路径
- [Gzip压缩](doc/practice/compression.md)
    - 11
- [代理服务](doc/practice/proxy.md)
    - 把内外不通的区域连接起来
- [缓存](doc/practice/cache.md)
### 源码
- 源码结构
- 启动初始化
- 工作进程
### 实现
- Web请求处理机制
- 事件驱动模型
- 高级配置
- 时间管理
- 内存管理