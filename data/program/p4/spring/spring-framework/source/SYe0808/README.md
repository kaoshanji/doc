#   Spring技术内幕：深入解析Spring架构与设计原理(第2版)

4星！理清书的逻辑思路，对于理解Spring很有帮助

从宏观和微观两个角度深入剖析Spring架构设计和实现原理

----

##  核心

分析IoC容器和AOP实现

-   IoC容器
    -   [概述](01.md)
    -   [具体：设计与实现：BeanFactory和ApplicationContext](02.md)
    -   [流程：IoC容器初始化过程](03.md)
        -   BeanDifinition的Resource定位
        -   BeanDifinition的载入和解析
        -   BeanDifinition的注册
    -   [流程：IoC容器依赖注入](04.md)
    -   相关特性的设计与实现
        -   ApplicationContext和Bean的初始化及销毁
        -   BeanPostProcessor的实现
        -   autowiring(自动依赖装配)的实现
        -   Bean依赖检查
        -   Bean对Ioc容器的感知
-   AOP的实现
    -   概述
    -   依据：设计与实现
    -   流程：建立AopProxy代理对象
    -   流程：Spring AOP拦截器调用的实现
    -   高级特性

----

##  组件

Java EE组件在Spring中的实现

-   Spring MVC
    -   概述
    -   Web环境
    -   流程：启动上下文
        -   Ioc容器启动
        -   Web容器
        -   ContextLoader
    -   流程：设计与实现
        -   应用场景
        -   设计概述
        -   DispatcherServlet的启动和初始化
        -   MVC处理HTTP分发请求
    -   流程：视图的呈现
        -   DispatcherServlet视图呈现
        -   PDF视图
-   数据库操作
    -   设计与实现
    -   模板类
    -   RDBMS操作对象
    -   驱动MyBatis的设计与实现
-   事务处理
    -   设计概述
    -   应用场景
    -   应用：声明式事务处理
    -   流程：设计与实现
    -   事务处理器

----


