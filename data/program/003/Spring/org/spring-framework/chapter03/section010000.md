#   事务管理

以下部分描述了Spring框架的事务增值和技术
-   Spring框架事务支持模型的优点描述了为什么要使用Spring框架的事务抽象而不是EJB容器管理的事务（CMT）或选择通过Hibernate等专有API驱动本地事务。
-   了解Spring Framework事务抽象 概述了核心类，并描述了如何`DataSource` 从各种来源配置和获取实例。
-   使资源与事务同步描述应用程序代码如何确保正确创建，重用和清理资源。
-   声明式事务管理描述了对声明式事务管理的支持。
-   程序化事务管理涵盖对程序化（即明确编码）事务管理的支持。
-   事务绑定事件描述了如何在事务中使用应用程序事件。


##  [Spring框架的事务支持模型的优点](section010100.md)

Spring解决了全局和本地事务的缺点。它使应用程序开发人员能够在任何环境中使用一致的编程模型。您只编写一次代码，并且可以从不同环境中的不同事务管理策略中受益。Spring Framework提供了声明式和编程式事务管理。大多数用户更喜欢声明式事务管理，这在大多数情况下是推荐的。


##  [事务抽象](section010200.md)



Spring 事务抽象的关键是事务策略的概念。事务策略由`org.springframework.transaction.PlatformTransactionManager`接口定义。

这主要是一个服务提供者接口（SPI），尽管它可以通过应用程序代码以编程方式使用 。因为它 `PlatformTransactionManager`是一个接口，所以可以根据需要轻松地进行模拟或拼接。它不受诸如JNDI之类的查找策略的束缚。 `PlatformTransactionManager`实现像Spring Framework IoC容器中的任何其他对象（或bean）一样定义。单就此优势而言，即使您使用JTA，Spring Framework交易也是一种有价值的抽象。事务代码可以比直接使用JTA更容易测试。


##  [使资源与事务同步](section010300.md)

描述应用程序代码如何直接或间接使用持久化API（如JDBC，Hibernate或JDO）确保正确创建，重用和清理这些资源。




##  [声明式事务管理](section010400.md)

Spring框架的声明式事务管理是通过Spring面向方面编程（AOP）实现的，尽管由于事务方面的代码随Spring Framework的发行版一起提供，并且可以以样板模式使用，AOP概念通常不需要被理解有效使用这段代码



##  [编程事务管理](section010500.md)

Spring Framework提供了两种程序化事务管理方式：
-   使用`TransactionTemplate`。
-   `PlatformTransactionManager`直接 使用实现。

Spring团队通常会推荐`TransactionTemplate`进行程序化事务管理。第二种方法类似于使用JTA `UserTransactionAPI`，但异常处理不太麻烦。



##  [事务监听事件](section010600.md)

从Spring 4.2开始，事件的侦听器可以绑定到事务的一个阶段。典型的例子是在事务成功完成时处理事件：这允许在当前事务的结果对聆听者实际上重要时更灵活地使用事件



##  [事务传播](section010700.md)

Spring中事务传播的一些语义。请注意，本节并不是介绍正确的事务传播。而是详细介绍了Spring中事务传播的一些语义。



