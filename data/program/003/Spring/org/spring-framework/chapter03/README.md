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



