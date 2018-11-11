#   [JDBC（TM）数据库访问](https://docs.oracle.com/javase/tutorial/jdbc/index.html)

JDBC™API旨在简化简单的事情。这意味着JDBC使日常数据库任务变得轻松。这个线索将引导您使用JDBC来执行通用SQL语句的示例，并执行数据库应用程序通用的其他目标。

到第一课结束时，您将知道如何使用基本JDBC API创建表，向其中插入值，查询表，检索查询结果以及更新表。在这个过程中，您将学习如何使用简单的语句和准备好的语句，您将看到一个存储过程的例子。您还将学习如何执行交易以及如何捕获异常和警告。


----
##  [JDBC简介](overview.md)

列出JDBC功能，描述JDBC体系结构并查看SQL命令和关系数据库概念。

-   JDBC架构
-   关系数据库概述

----
##  JDBC基础知识

包含JDBC API，它包含在Java™SE 6版本中。

-   [开始](gettingstarted.md)
-   [使用JDBC处理SQL语句](processingsqlstatements.md)
    -   [建立连接](connecting.md)
    -   [连接数据源对象](sqldatasources.md)
    -   处理SQLExceptions
    -   设置表格
    -   从结果集中检索和修改值
    -   使用预先准备的语句
    -   使用事务
-   使用RowSet对象
    -   使用JdbcRowSet对象
    -   使用CachedRowSetObjects
    -   使用JoinRowSet对象
    -   使用FilteredRowSet对象
    -   使用WebRowSet对象
-   使用高级数据类型
    -   使用大对象
    -   使用SQLXML对象
    -   使用数组对象
    -   使用DISTINCT数据类型
    -   使用结构化对象
    -   使用自定义类型映射
    -   使用数据链接对象
    -   使用RowId对象
-   使用存储过程
-   在GUI API中使用JDBC

----

