#   数据访问

数据访问/集成层由JDBC，ORM，OXM，JMS和交易模块。

该`spring-jdbc`模块提供了一个JDBC -abstraction层消除了需要冗长的JDBC编码和数据库厂商特有的错误代码解析。

该`spring-tx`模块支持 对实现特殊接口和所有POJO（普通Java对象）的类进行编程式和声明式事务管理。

该`spring-orm`模块为流行的对象关系映射 API 提供了集成层 ，包括JPA， JDO和Hibernate。使用`spring-orm`模块，您可以将所有这些O / R映射框架与Spring提供的所有其他功能结合使用，例如前面提到的简单的声明式事务管理功能。

该`spring-oxm`模块提供了支持对象/ XML映射实现的抽象层，如JAXB，Castor，XMLBeans，JiBX和XStream。

该`spring-jms`模块（Java消息服务）包含用于生成和使用消息的功能。自Spring Framework 4.1以来，它提供了与`spring-messaging`模块的集成 。


##  [事务管理](section010000.md)

全面的事务支持是使用Spring框架最有说服力的理由之一。Spring框架为事务管理提供了一致的抽象，具有以下优点：
-   跨越不同事务API（如Java事务API（JTA），JDBC，Hibernate，Java持久性API（JPA）和Java数据对象（JDO））的一致编程模型。
-   支持声明式事务管理。
-   用于编程式事务管理的简单API 比诸如JTA之类的复杂事务API更为简单。
-   与Spring的数据访问抽象极佳整合。

以下部分描述了Spring框架的事务增值和技术。（本章还包括讨论最佳实践，应用程序服务器集成以及常见问题的解决方案。）
-   Spring框架事务支持模型的优点描述了为什么要使用Spring框架的事务抽象而不是EJB容器管理的事务（CMT）或选择通过Hibernate等专有API驱动本地事务。
-   了解Spring Framework事务抽象 概述了核心类，并描述了如何`DataSource` 从各种来源配置和获取实例。
-   使资源与事务同步描述应用程序代码如何确保正确创建，重用和清理资源。
-   声明式事务管理描述了对声明式事务管理的支持。
-   程序化事务管理涵盖对程序化（即明确编码）事务管理的支持。
-   事务绑定事件描述了如何在事务中使用应用程序事件。

##  [DAO支持](section020000.md)

Spring中的数据访问对象（DAO）支持旨在使它能够以一致的方式轻松处理JDBC，Hibernate，JPA或JDO等数据访问技术。这使得人们可以相当容易地在上述持久性技术之间进行切换，并且还允许人们进行编码，而不用担心捕捉每种技术特有的异常


##  [使用JDBC访问数据](section030000.md)

Spring Framework JDBC抽象提供的增值功能可能最适合通过下表中列出的操作序列显示。该表显示了Spring将处理的操作以及应用程序开发人员应负责的操作。

Spring JDBC - 谁做什么？

|Action|Spring|You|
|------|------|------|
|连接参数||×|
|打开连接|×||
|指定SQL语句||×|
|声明参数并提供参数值||×|
|准备并执行该语句|×||
|循环遍历结果|×||
|为每个元素||×|
|处理任何异常|×||
|处理事务|×||
|关闭连接、结果集|×||

Spring框架负责处理所有可能导致JDBC开发冗长的API的低级细节。


##  [对象关系映射（ORM）数据访问](section040000.md)

Spring框架支持与Hibernate，Java持久性API（JPA）和Java数据对象（JDO）的集成，用于资源管理，数据访问对象（DAO）实现和事务策略。例如，对于Hibernate来说，有一些便利的IoC功能支持一流的支持，可解决许多典型的Hibernate集成问题。您可以通过依赖注入为O / R（对象关系）映射工具配置所有支持的功能。他们可以参与Spring的资源和事务管理，并遵守Spring的通用事务和DAO异常层次结构。推荐的集成风格是针对简单的Hibernate，JPA和JDO API对DAO进行编码。不再推荐使用Spring的DAO模板。

当您创建数据访问应用程序时，Spring会为您选择的ORM层添加显着的增强功能。您可以根据需要尽可能多地利用集成支持，并且应该将此集成工作与构建类似基础架构的成本和风险相比较。无论技术如何，您都可以像使用库一样使用大部分ORM支持，因为所有内容都被设计为一组可重用的JavaBean。Spring IoC容器中的ORM便于配置和部署。因此本节中的大多数示例都显示了Spring容器内的配置。

使用Spring框架创建ORM DAO的好处包括：
-   更简单的测试。Spring的IoC方法可以轻松地交换Hibernate`SessionFactory`实例，JDBC`DataSource` 实例，事务管理器和映射对象实现（如果需要）的实现和配置位置。这反过来使得单独测试每个与持久性相关的代码变得更加容易。
-   常见的数据访问异常。Spring可以封装ORM工具中的异常，将它们从专有（可能检查的）异常转换为公共运行时DataAccessException层次结构。此功能允许您仅在适当的层中处理大多数不可恢复的持久性异常，而无需烦人的样板捕获，引发和异常声明。您仍然可以根据需要捕获和处理异常。请记住，JDBC异常（包括特定于DB的方言）也会转换为相同的层次结构，这意味着您可以在一致的编程模型中使用JDBC执行一些操作。
-   一般资源管理。Spring应用程序上下文可以处理Hibernate`SessionFactory`实例，JPA`EntityManagerFactory` 实例，JDBC`DataSource`实例和其他相关资源的位置和配置。这使得这些值易于管理和更改。Spring为持久性资源提供高效，简单和安全的处理。例如，使用Hibernate的相关代码通常需要使用相同的Hibernate`Session`来确保效率和正确的事务处理。通过Spring通过Hibernate`Session`暴露一个线程，Spring可以很容易地透明地创建和绑定到当前线程。因此，Spring解决了许多典型Hibernate使用的慢性问题，适用于任何本地或JTA事务环境。 `Session``SessionFactory`
-   综合事务管理。您可以通过`@Transactional`注释或通过在XML配置文件中显式配置事务AOP建议来使用声明式的面向方面编程（AOP）样式方法拦截器来打包ORM代码 。在这两种情况下，都会为您处理事务语义和异常处理（回滚等）。如下所述，在 资源和事务管理中，您也可以交换各种事务管理器，而不会影响与ORM相关的代码。例如，您可以在本地事务和JTA之间进行切换，在两种情况下都可以使用相同的完整服务（如声明式事务）。此外，与JDBC相关的代码可以与您用于执行ORM的代码完全集成。这对于不适合ORM的数据访问非常有用，例如批处理和BLOB流式传输，它们仍然需要与ORM操作共享公共事务。


