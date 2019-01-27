#   基本功-Java

##  目录
-   [对象管理](object/001.md)



##  软件版本
-   Java SE：8
-   Spring Framework：3.2.19.BUILD-SNAPSHOT
    -   Java SE 7 
    -   Servlet 3 
-   IDE：IDEA 2017.02
-   STS：较新版本

##  代码示例
-   [example-java](https://github.com/kaoshanji/example/tree/master/example-java)
-   Spring Framework 源码环境搭建
    -   [文档](http://plq6gjb8l.bkt.clouddn.com/spring-framework-3.2.18.RELEASE-docs.zip)+[编译后源码](http://plq6gjb8l.bkt.clouddn.com/spring-projects-3.2.19-sourcecode-build.zip)
    -   Notepad++ 批量修改 `.classpath` 包和项目依赖路径
    -   使用 STS 导入

##  Spring Framework 简介

Spring Framework 是面向`应用开发`人员在实际中`开发Java项目`的综合式框架。

模块及模块关系

![spring-overview](images/spring-overview.png)

-   核心容器：管理对象，解耦对象，解决对象之间的依赖，自动化了对象的过程
-   Aop...：把嵌套在各处具有相识的功能集中在一起
-   数据访问/集成：抽象事务和持久层，简化固定操作流程
-   Web：一套MVC框架，屏蔽了原生语法
-   Test：各种测试支持



##  参考资料
-   《Spring源码深度解析》- 郝佳
-   《Spring技术内幕：深入解析Spring架构与设计原理(第2版)》-  计文柯