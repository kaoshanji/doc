#   [包java.sql](https://docs.oracle.com/javase/8/docs/api/java/sql/package-summary.html)

提供用于使用Java TM编程语言访问和处理存储在数据源（通常是关系数据库）中的数据的API。

##  描述

提供用于使用Java TM编程语言访问和处理存储在数据源（通常是关系数据库）中的数据的API 。此API包含一个框架，可以动态安装不同的驱动程序以访问不同的数据源。虽然JDBC TM API主要用于将SQL语句传递给数据库，但它提供了使用表格格式从任何数据源读取和写入数据。javax.sql.RowSet可以定制通过接口组提供的读取器/写入器设施， 以使用和更新电子表格，平面文件或任何其他表格数据源中的数据。

### 内容

该java.sql软件包包含以下API：

-   通过DriverManager设施 与数据库建立连接
    -   DriverManager class - 与驱动程序建立连接
    -   SQLPermission class - 在安全管理器（例如applet）中运行的代码尝试通过安装程序设置日志记录流时提供权限 DriverManager
    -   Driverinterface - 提供基于JDBC技术注册和连接驱动程序的API（“JDBC驱动程序”）; 通常只由DriverManager班级使用
    -   DriverPropertyInfoclass - 提供JDBC驱动程序的属性; 一般用户不使用
-   将SQL语句发送到数据库
    -   Statement - 用于发送基本的SQL语句
    -   PreparedStatement- 用于发送预准备语句或基本SQL语句（派生自Statement）
    -   CallableStatement- 用于调用数据库存储过程（派生自PreparedStatement）
    -   Connection interface - 提供创建语句和管理连接及其属性的方法
    -   Savepoint - 在事务中提供保存点
-   检索和更新查询结果
    -   ResultSet 接口
-   SQL类型到Java编程语言中的类和接口的标准映射
    -   Array 接口 - SQL的映射 ARRAY
    -   Blob 接口 - SQL的映射 BLOB
    -   Clob 接口 - SQL的映射 CLOB
    -   Date class - SQL的映射 DATE
    -   NClob 接口 - SQL的映射 NCLOB
    -   Ref 接口 - SQL的映射 REF
    -   RowId 接口 - SQL的映射 ROWID
    -   Struct 接口 - SQL的映射 STRUCT
    -   SQLXML 接口 - SQL的映射 XML
    -   Time class - SQL的映射 TIME
    -   Timestamp class - SQL的映射 TIMESTAMP
    -   Types class - 为SQL类型提供常量
-   自定义SQL用户定义类型（UDT）到Java编程语言中的类
    -   SQLData interface - 指定UDT到此类实例的映射
    -   SQLInput interface - 提供从流中读取UDT属性的方法
    -   SQLOutput interface - 提供将UDT属性写回流的方法
-   元数据
    -   DatabaseMetaData interface - 提供有关数据库的信息
    -   ResultSetMetaDatainterface - 提供有关ResultSet对象 列的信息
    -   ParameterMetaDatainterface - 提供有关PreparedStatement命令 参数的信息
-   例外
    -   SQLException - 当访问数据时出于问题而被大多数方法抛出，而出于其他原因则由某些方法抛出
    -   SQLWarning - 抛出以表示警告
    -   DataTruncation - 抛出表示数据可能已被截断
    -   BatchUpdateException - 抛出表示批量更新中的所有命令都未成功执行





