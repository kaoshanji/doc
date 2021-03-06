-   [深入理解 Spring 事务原理](http://www.linkedkeeper.com/1195.html)
-   [Spring mvc 上下文初始化过程](https://blog.csdn.net/and1kaney/article/details/51214149)
-   [给你一份超详细Spring Boot知识清单](https://mp.weixin.qq.com/s/q8OI2Ou8-gYP-usjToBbkQ)
-   [自己手写一个 SpringMVC 框架](http://www.iteye.com/news/32924)
-   [二十一、SpringBoot整合Mybatis、通用mapper和pageHelp](https://blog.csdn.net/L_Sail/article/details/70247407)
-   [logback与Spring、SpringMVC结合使用教程](https://blog.csdn.net/evankaka/article/details/50637994)
-   [《Spring 5 官方文档》1. Spring入门指南](http://ifeve.com/overview-getting-started-with-spring/comment-page-1/)
-   [当前标签: spring](http://www.cnblogs.com/bigdataZJ/tag/spring/)

##  Spring 源码编译

1.  下载指定版本源码

``` 
git clone --branch v3.2.18.RELEASE https://github.com/spring-projects/spring-framework.git
git clone -b 3.2.x https://github.com/spring-projects/spring-framework.git
```

下载最新 gradle ，如同java一样配置环境：gradle -version

打开命令窗口切换到Spring源码路径.输入 “gradle cleanidea eclipse”  gradle cleanidea eclipse