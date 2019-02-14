#   [包javax.sql](https://docs.oracle.com/javase/8/docs/api/javax/sql/package-summary.html)

提供用于从Java TM编程语言访问和处理服务器端数据源的API

##  描述

提供用于从Java TM编程语言访问和处理服务器端数据源的API 。该软件包是对软件包的补充java.sql ，从版本1.4发行版开始，它包含在Java平台标准版（Java SE TM）中。它仍然是Java平台企业版（Java EE TM）的重要组成部分。

该javax.sql软件包提供以下内容：
-   在DataSource作为替代的接口 DriverManager，用于建立与数据源的连接
-   连接池和语句池
-   分布式事务
-   行集

应用 程序直接使用DataSource和RowSetAPI，但连接池和分布式事务API由中间层基础结构在内部使用。

### 使用DataSource对象建立连接

该javax.sql包提供了与数据源建立连接的首选方法。在DriverManager 课堂上，原来的机制，仍然是有效的，并且使用它会继续运行代码。然而，较新的DataSource机制是优选的，因为它提供了超过该DriverManager机制的许多优点 。

这些是使用DataSource对象建立连接的主要优点：
-   可以对数据源的属性进行更改，这意味着当有关数据源或驱动程序的更改时，不必更改应用程序代码。
-   连接和语句池和分布式事务可通过DataSource实现与中间层基础结构一起使用的对象获得。通过DriverManager 没有连接和语句池或分布式事务功能建立的连接。

驱动程序厂商提供DataSource实现 特定DataSource对象表示特定物理数据源，DataSource对象创建的每个连接都是与该物理数据源的连接。

数据源的逻辑名称是使用命名服务注册的，该命名服务使用Java命名和目录接口TM （JNDI）API，通常由系统管理员或执行系统管理员职责的人员使用。应用程序可以DataSource通过查找已为其注册的逻辑名称来检索所需的 对象。然后，应用程序可以使用该 DataSource对象创建与其表示的物理数据源的连接。

一个DataSource对象可以实现与中间层基础工作，所以它产生的连接将被汇集起来进行再利用。使用此类DataSource 实现的应用程序将自动获得参与连接池的连接。一个DataSource对象也可以实现与中间层基础工作，所以它产生的连接，可用于分布式事务，没有任何特殊的编码。

### 连接池和语句池

通过DataSource 实现与中间层连接池管理器一起使用的对象建立的连接将参与连接池。这可以显着提高性能，因为创建新连接非常昂贵。连接池允许使用和重用连接，从而大大减少了需要创建的新连接的数量。

连接池完全透明。它在Java EE配置的中间层自动完成，因此从应用程序的角度来看，不需要更改代码。应用程序只是使用该DataSource.getConnection方法来获取池化连接，并以与使用任何Connection 对象相同的方式使用它。

用于连接池的类和接口是：
-   ConnectionPoolDataSource
-   PooledConnection
-   ConnectionEvent
-   ConnectionEventListener
-   StatementEvent
-   StatementEventListener

连接池管理器是三层体系结构中间层的工具，它在后台使用这些类和接口。当ConnectionPoolDataSource调用对象来创建PooledConnection对象时，连接池管理器将注册为ConnectionEventListener 具有新PooledConnection对象的对象。当连接关闭或出现错误时，连接池管理器（作为侦听器）将获取包含ConnectionEvent对象的通知。

如果连接池管理器支持Statement池， PreparedStatements可以通过调用该方法来确定 DatabaseMetaData.supportsStatementPooling，则连接池管理器将注册为StatementEventListener 具有新PooledConnection对象的对象。当 PreparedStatement关闭或出现错误时，连接池管理器（作为侦听器）将获取包含StatementEvent对象的通知。

### 分布式事务

与池化连接一样，通过DataSource 实现与中间层基础结构一起工作的对象建立的连接可以参与分布式事务。这使应用程序能够在单个事务中涉及多个服务器上的数据源。
用于分布式事务的类和接口是：
-   XADataSource
-   XAConnection

这些接口由事务管理器使用; 应用程序不直接使用它们。

该XAConnection接口是从派生 PooledConnection接口，所以什么适用于连接池也适用于这是一个分布式事务一部分的连接。中间层的事务管理器透明地处理所有事务。应用程序代码中唯一的变化是应用程序无法执行任何会干扰事务管理器处理事务的操作。具体地，应用程序可以不调用的方法Connection.commit 或Connection.rollback，并且它不能设置连接到在自动提交模式（即，它不能调用 Connection.setAutoCommit(true)）。

应用程序不需要做任何特殊的事情来参与分布式事务。它只是通过DataSource.getConnection方法创建它想要使用的数据源的连接，就像通常那样。事务管理器在后台管理事务。该 XADataSource接口创建XAConnection对象，每个XAConnection对象创建一个XAResource事务管理器用于管理连接对象。

### 行集

该RowSet界面与幕后的各种其他类和接口一起使用。这些可以分为三类。

1.  事件通知

-   RowSetListener

甲RowSet对象是一个JavaBeans TM 组件，因为它具有属性并在JavaBeans事件通知机制。该RowSetListener接口由希望被通知特定RowSet对象发生的事件的组件实现。这样的组件通过该RowSet.addRowSetListener 方法将自身注册为具有行集的侦听器。
当RowSet对象更改其中一行，更改所有行或移动其光标时，它还会通知向其注册的每个侦听器。监听器通过执行其上调用的通知方法来做出反应。

-   RowSetEvent

作为其内部通知过程的一部分，RowSet对象创建一个实例RowSetEvent并将其传递给侦听器。侦听器可以使用此RowSetEvent对象来查找哪个行集具有该事件。

2.  元数据

-   RowSetMetaData

此接口派生自 ResultSetMetaData接口，提供有关RowSet对象中列的信息。应用程序可以使用 RowSetMetaData方法来查找行集包含的列数以及每列可包含的数据类型。

该RowSetMetaData接口提供了设置有关列的信息的方法，但应用程序通常不会使用这些方法。当应用程序调用该RowSet 方法时execute，该RowSet对象将包含一组新的行，并且其RowSetMetaData对象将在内部更新以包含有关新列的信息。

3.  读/写设备

一个RowSet实现该对象RowSetInternal 接口的调用上RowSetReader与之相关的对象本身的填充数据。它还可以调用RowSetWriter 与其关联的对象，将其行的任何更改写回到最初获取行的数据源。保持连接到其数据源的行集不需要使用读写器，因为它可以直接对数据源进行操作。

-   RowSetInternal

通过实现RowSetInternal接口， RowSet对象可以访问其内部状态，并能够调用其读取器和写入器。行集跟踪其当前行中的值以及紧接在当前行之前的值，称为原始值。行集还跟踪（1）为其命令设置的参数以及（2）传递给它的连接（如果有）。行集使用 RowSetInternal幕后方法来访问此信息。应用程序通常不直接调用这些方法。

-   RowSetReader

RowSet已实现RowSetInternal接口的 断开连接的对象 可以调用其读取器（RowSetReader与其关联的 对象）以使用数据填充它。当应用程序调用该RowSet.execute方法时，该方法会调用行集的阅读器来完成大部分工作。实现可以有很大的不同，但通常读者会建立与数据源的连接，从数据源读取数据并使用它填充行集，并关闭连接。读者还可以更新RowSetMetaData对象的行集。行集的内部状态也由读者或直接由方法更新RowSet.execute。

-   RowSetWriter

RowSet已实现RowSetInternal接口的 断开连接的对象 可以调用其RowSetWriter编写器（与其关联的 对象）将更改写回基础数据源。实现可能有很大差异，但通常，作者将执行以下操作：

-   建立与数据源的连接
-   检查是否存在冲突，即是否在数据源中更改了行集中已更改的值
-   如果没有冲突，请将新值写入数据源
-   关闭连接

该RowSet接口可以以任何数量的方式来实现，任何人都可以写一个实现。鼓励开发人员使用他们的想象力来提出使用行集的新方法。

