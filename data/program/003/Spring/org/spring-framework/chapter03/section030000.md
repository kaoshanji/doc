#   使用JDBC访问数据

Spring框架负责处理所有可能导致JDBC开发冗长的API的低级细节。


`为JDBC数据库访问选择一种方法`


您可以选择几种方法来形成JDBC数据库访问的基础。除了三种JdbcTemplate之外，新的SimpleJdbcInsert和SimplejdbcCall方法优化了数据库元数据，而RDBMS Object style采用了更类似于JDO Query设计的面向对象的方法。一旦你开始使用这些方法之一，你仍然可以混合和匹配，以包含来自不同方法的功能。所有的方法都需要JDBC 2.0兼容的驱动程序，并且一些高级功能需要JDBC 3.0驱动程序。

-   JdbcTemplate是最经典的Spring JDBC方法。这种“最低级别”的方法和所有其他人在封面下使用JdbcTemplate。
-   NamedParameterJdbcTemplate包装a`JdbcTemplate`以提供命名参数，而不是传统的JDBC“？” 占位符。当你有一个SQL语句的多个参数时，这种方法提供了更好的文档和易用性。
-   SimpleJdbcInsert和SimpleJdbcCall优化数据库元数据以限制必要配置的数量。这种方法简化了编码，因此您只需提供表格或过程的名称并提供匹配列名称的参数映射。这只适用于数据库提供了足够的元数据。如果数据库不提供此元数据，则必须提供参数的明确配置。
-   包括MappingSqlQuery，SqlUpdate和StoredProcedure在内的RDBMS对象要求您在数据访问层初始化期间创建可重用且线程安全的对象。这种方法是在JDO Query之后建模的，其中您定义了查询字符串，声明参数并编译查询。一旦你这样做了，可以用传入的各种参数值多次调用执行方法。


`包层次结构`

Spring框架的JDBC抽象框架由四个不同的包，即`core`，`datasource`，`object`，和`support`。

该`org.springframework.jdbc.core`包包含`JdbcTemplate`类及其各种回调接口，以及各种相关的类。一个名为subpackage `org.springframework.jdbc.core.simple`包含`SimpleJdbcInsert`和 `SimpleJdbcCall`类。另一个命名`org.springframework.jdbc.core.namedparam`的子包 包含`NamedParameterJdbcTemplate` 类和相关的支持类。

该`org.springframework.jdbc.datasource`软件包包含一个易于`DataSource`访问的实用程序类 以及`DataSource`可用于在Java EE容器之外测试和运行未经修改的JDBC代码的各种简单实现。名为的子包`org.springfamework.jdbc.datasource.embedded`提供了使用Java数据库引擎（如HSQL，H2和Derby）创建嵌入式数据库的支持。

该`org.springframework.jdbc.object`软件包包含表示RDBMS查询，更新和存储过程的类，作为线程安全的可重用对象。虽然由查询返回的对象自然与数据库断开连接，但这种方法由JDO建模。这种较高级别的JDBC抽象取决于`org.springframework.jdbc.core`程序包中的较低级抽象。

该`org.springframework.jdbc.support`软件包提供`SQLException`翻译功能和一些实用程序类。JDBC处理过程中引发的异常会转换为`org.springframework.dao`程序包中定义的异常。这意味着使用Spring JDBC抽象层的代码不需要实现JDBC或RDBMS特定的错误处理。所有经过翻译的异常均未经过检查，您可以选择捕获可从中恢复的异常，同时允许将其他异常传播给调用者。


##  使用JDBC核心类来控制基本的JDBC处理和错误处理

`JdbcTemplate`类是在JDBC核心包的核心类。它处理资源的创建和释放，这可以帮助您避免常见错误，例如忘记关闭连接。它执行核心JDBC工作流的基本任务，例如语句创建和执行，使应用程序代码提供SQL并提取结果。在JdbcTemplate完成SQL查询，更新语句和存储过程调用，执行了迭代ResultSetS和返回的参数值的提取。它还捕获JDBC异常并将其转换为org.springframework.dao程序包中定义的通用，更丰富的异常层次结构

`NamedParameterJdbcTemplate`类增加了支持使用命名参数如何在SQL语句，如只使用常规的占位符（而不是如何在SQL语句`'?'`）的参数。这个`NamedParameterJdbcTemplate`类包装一个 `JdbcTemplate`，并委托给包装`JdbcTemplate`来完成它的大部分工作


##  控制数据库连接

Spring通过一个`DataSource`获得与数据库的连接。 `DataSource`是JDBC规范的一部分，是一个通用连接工厂。它允许容器或框架隐藏应用程序代码中的连接池和事务管理问题。作为开发人员，您不需要知道如何连接到数据库的详细信息; 这是设置数据源的管理员的职责。在开发和测试代码时，您很可能会兼顾这两种角色，但您不一定非得知道生产数据源的配置方式。


##  JDBC批处理操作

如果将多个调用批量处理到相同的预处理语句，大多数JDBC驱动程序都会提高性能 通过将更新分组成批次，可以限制往返数据库的次数



##  使用SimpleJdbc类简化JDBC操作

这些`SimpleJdbcInsert`和`SimpleJdbcCall`类通过利用可以通过JDBC驱动程序检索的数据库元数据来提供简化的配置。这意味着前面配置的数量较少，但如果您希望提供代码中的所有详细信息，则可以覆盖或关闭元数据处理。



##  将JDBC操作建模为Java对象

该`org.springframework.jdbc.object`包中包含的类允许您以更加面向对象的方式访问数据库



##  参数和数据值处理的常见问题

参数和数据值的常见问题存在于Spring Framework JDBC提供的不同方法中。


##  嵌入式数据库支持

该`org.springframework.jdbc.datasource.embedded`软件包为嵌入式Java数据库引擎提供支持。本地提供对[HSQL](http://www.hsqldb.org/)， [H2](http://www.h2database.com/html/main.html)和[Derby](http://db.apache.org/derby/)的支持。您还可以使用可扩展的API来插入新的嵌入式数据库类型和 DataSource实现。



##  初始化数据源

该`org.springframework.jdbc.datasource.init`软件包为初始化现有软件提供支持`DataSource`。嵌入式数据库支持为创建和初始化`DataSource`应用程序提供了一个选项，但有时您需要初始化在某个服务器上运行的实例。



