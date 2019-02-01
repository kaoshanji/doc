# bean加载

- 出发地：AbstractBeanFactory#doGetBean(String, Class<T>, Object[], boolean)

##  流程
-   转换对应 beanName
-   尝试从缓存中加载单例
-   bean的实例化
-   原型模式的依赖检查
-   检测parentBeanFactory
-   将存储XML配置文件的GernericBeanDefinition转换为RootBeanDefinition
-   寻找依赖
-   针对不同的scope进行bean的创建
-   类型转换

##  获取bean

1.   缓存中获取

`getSingleton(beanName)`

单例在spring的同一个容器内只会被创建一次，后续再获取bean直接从单例缓存中获取。

在创建单例bean的时候会存在依赖注入的情况，而在创建依赖的时候为了避免循环依赖，spring创建bean的原则是不等bean创建完成就会将创建bean的ObjectFactory提早曝光加入到缓存中，一旦下一个bean创建时需要依赖上个bean，则直接使用 ObjectFactory。

这个方法涉及`循环依赖`的检查，以及涉及很多变量的记录读取。

-   对 FactoryBean 正确性的验证
-   对非 FactoryBean 不做任何处理
-   对 bean 进行转换
-   将从 Factory 中解析 bean  的工作委托给 getObjectForBeanInstance

2.   bean的实例中获取

`getObjectForBeanInstance(sharedInstance, name, beanName, null)`

得到bean的实例后要做的第一步就是调用这个方法来检测一下正确性，就是用于检测当前 bean 是否是 FactoryBean 类型的bean，如果是，那么需要调用该bean对应的 FactoryBean 实例中的 getObject() 作为返回值。

3.   获取单例

`sharedInstance = getSingleton(beanName, new ObjectFactory<Object>(){}`

-   检查缓存是否已经加载过
-   若没有加载，则记录 beanName 的正在加载状态
-   加载单例前记录加载状态：`beforeSingletonCreation(beanName)`
-   通过调用参数传入的 ObjectFactory 的个体 Object 方法实例化 bean
-   加载单例后的处理方法调用：`afterSingletonCreation(beanName)`
-   将结果记录至缓存并删除加载 bean 过程中所记录的各种辅助状态：`addSingleton(beanName, singletonObject);`
-   返回值处理结果

##  创建bean

4.   准备创建bean

5.   创建中..

6.   初始化

7.   注册
