#   对象关系映射（ORM）数据访问

使用Spring框架创建ORM DAO的好处包括：
-   更简单的测试。Spring的IoC方法可以轻松地交换Hibernate`SessionFactory`实例，JDBC`DataSource` 实例，事务管理器和映射对象实现（如果需要）的实现和配置位置。这反过来使得单独测试每个与持久性相关的代码变得更加容易。
-   常见的数据访问异常。Spring可以封装ORM工具中的异常，将它们从专有（可能检查的）异常转换为公共运行时DataAccessException层次结构。此功能允许您仅在适当的层中处理大多数不可恢复的持久性异常，而无需烦人的样板捕获，引发和异常声明。您仍然可以根据需要捕获和处理异常。请记住，JDBC异常（包括特定于DB的方言）也会转换为相同的层次结构，这意味着您可以在一致的编程模型中使用JDBC执行一些操作。
-   一般资源管理。Spring应用程序上下文可以处理Hibernate`SessionFactory`实例，JPA`EntityManagerFactory` 实例，JDBC`DataSource`实例和其他相关资源的位置和配置。这使得这些值易于管理和更改。Spring为持久性资源提供高效，简单和安全的处理。例如，使用Hibernate的相关代码通常需要使用相同的Hibernate`Session`来确保效率和正确的事务处理。通过Spring通过Hibernate`Session`暴露一个线程，Spring可以很容易地透明地创建和绑定到当前线程。因此，Spring解决了许多典型Hibernate使用的慢性问题，适用于任何本地或JTA事务环境。 `Session``SessionFactory`
-   综合事务管理。您可以通过`@Transactional`注释或通过在XML配置文件中显式配置事务AOP建议来使用声明式的面向方面编程（AOP）样式方法拦截器来打包ORM代码 。在这两种情况下，都会为您处理事务语义和异常处理（回滚等）。如下所述，在 资源和事务管理中，您也可以交换各种事务管理器，而不会影响与ORM相关的代码。例如，您可以在本地事务和JTA之间进行切换，在两种情况下都可以使用相同的完整服务（如声明式事务）。此外，与JDBC相关的代码可以与您用于执行ORM的代码完全集成。这对于不适合ORM的数据访问非常有用，例如批处理和BLOB流式传输，它们仍然需要与ORM操作共享公共事务。


##  [一般ORM集成注意事项](section040100.md)

Spring ORM集成的主要目标是明确的应用程序层，任何数据访问和事务处理技术以及应用程序对象的松散耦合。没有更多的业务服务依赖于数据访问或事务策略，没有更多的硬编码资源查找，没有更难以替代的具体方案，没有更多的定制服务注册。一种简单而一致的方法来连接应用程序对象，尽可能保持它们的可重用性和免受容器依赖性的影响。所有单独的数据访问功能都可以自己使用，但与Spring的应用程序上下文概念很好地集成在一起，提供了基于XML的配置以及不需要Spring支持的普通JavaBean实例的交叉引用。



##  [Hibernate](section040200.md)

首先介绍Spring环境中的[Hibernate 5](http://hibernate.org/)，并用它来演示Spring在集成O / R映射器方面的方法。本节将详细介绍许多问题，并展示DAO实现和事务划分的不同变体。大多数这些模式可以直接转换为所有其他支持的ORM工具。




##  [JPA](section040300.md)

可以通过该`org.springframework.orm.jpa`包下载的Spring JPA 以类似于与Hibernate或JDO集成的方式提供对[Java持久性API](http://www.oracle.com/technetwork/articles/javaee/jpa-137156.html)的全面支持 ，同时了解底层实现以提供附加功能。

