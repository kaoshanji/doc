#   [使用JDBC处理SQL语句](https://docs.oracle.com/javase/tutorial/jdbc/basics/processingsqlstatements.html)

通常，要使用JDBC处理任何SQL语句，请按照下列步骤操作：

1.  建立连接。
2.  创建一个声明。
3.  执行查询。
4.  处理ResultSet对象。
5.  关闭连接。

此页面使用以下方法，CoffeesTables.viewTable从教程示例中演示这些步骤。此方法输出表的内容COFFEES。本教程后面将详细讨论此方法：

``` Java
public static void viewTable(Connection con, String dbName)
    throws SQLException {

    Statement stmt = null;
    String query = "select COF_NAME, SUP_ID, PRICE, " +
                   "SALES, TOTAL " +
                   "from " + dbName + ".COFFEES";
    try {
        stmt = con.createStatement();
        ResultSet rs = stmt.executeQuery(query);
        while (rs.next()) {
            String coffeeName = rs.getString("COF_NAME");
            int supplierID = rs.getInt("SUP_ID");
            float price = rs.getFloat("PRICE");
            int sales = rs.getInt("SALES");
            int total = rs.getInt("TOTAL");
            System.out.println(coffeeName + "\t" + supplierID +
                               "\t" + price + "\t" + sales +
                               "\t" + total);
        }
    } catch (SQLException e ) {
        JDBCTutorialUtilities.printSQLException(e);
    } finally {
        if (stmt != null) { stmt.close(); }
    }
}
```

----

##  建立连接

首先，与要使用的数据源建立连接。数据源可以是DBMS，遗留文件系统或具有相应JDBC驱动程序的一些其他数据源。此连接由Connection对象表示。有关更多信息，请参阅 建立连接。

##  创建语句

A Statement是表示SQL语句的接口。您执行Statement对象，它们生成ResultSet对象，这是一个表示数据库结果集的数据表。您需要一个Connection对象来创建一个Statement对象。

例如，使用以下代码CoffeesTables.viewTable创建Statement对象：

stmt = con.createStatement（）;

有三种不同的陈述：

-   Statement：用于实现没有参数的简单SQL语句。
-   PreparedStatement:( Extends Statement。）用于预编译可能包含输入参数的SQL语句。有关更多信息，请参阅 使用准备语句。
-   CallableStatement:（Extends PreparedStatement。）用于执行可能包含输入和输出参数的存储过程。有关更多信息，请参阅 存储过程。

##  执行查询

执行查询，调用一个execute从方法Statement如以下内容：

-   execute：true如果查询返回的第一个对象是对象，则返回ResultSet。如果查询可以返回一个或多个ResultSet对象，请使用此方法。ResultSet通过重复调用来检索从查询返回的对象Statement.getResultSet。
-   executeQuery：返回一个ResultSet对象。
-   executeUpdate：返回一个整数，表示受SQL语句影响的行数。如果您正在使用，或使用SQL语句INSERT，请使用此方法。DELETEUPDATE

例如，使用以下代码CoffeesTables.viewTable执行了一个Statement对象：

ResultSet rs = stmt.executeQuery（query）;
有关详细信息，请参阅 从结果集中检索和修改值。

##  处理ResultSet对象

您可以ResultSet通过游标访问对象中的数据。请注意，此游标不是数据库游标。该游标是指向ResultSet对象中一行数据的指针。最初，光标位于第一行之前。您可以调用ResultSet对象中定义的各种方法来移动光标。

例如，CoffeesTables.viewTable重复调用该方法ResultSet.next将光标向前移动一行。每次调用时next，该方法都会在光标当前所在的行中输出数据：

``` Java
try {
    stmt = con.createStatement();
    ResultSet rs = stmt.executeQuery(query);
    while (rs.next()) {
        String coffeeName = rs.getString("COF_NAME");
        int supplierID = rs.getInt("SUP_ID");
        float price = rs.getFloat("PRICE");
        int sales = rs.getInt("SALES");
        int total = rs.getInt("TOTAL");
        System.out.println(coffeeName + "\t" + supplierID +
                           "\t" + price + "\t" + sales +
                           "\t" + total);
    }
}
// ...
```

有关详细信息，请参阅 从结果集中检索和修改值。

##  关闭连接

完成使用a后Statement，调用该方法Statement.close立即释放它正在使用的资源。调用此方法时，其ResultSet对象将关闭。

例如，通过将对象包装在块中，该方法CoffeesTables.viewTable可确保在方法Statement结束时关闭对象，而不管SQLException抛出任何对象finally：
``` Java
} finally {
    if（stmt！= null）{stmt.close（）; }
}
```
JDBC SQLException在与数据源交互期间遇到错误时会引发错误。有关更多信息，请参阅 处理SQL异常。

在JDBC 4.1，这是可以在Java SE 7版及更高版本，可以使用try-与资源语句自动关闭Connection，Statement和ResultSet对象，无论是否在SQLException已抛出。自动资源语句由try语句和一个或多个声明的资源组成。例如，您可以修改CoffeesTables.viewTable以使其Statement对象自动关闭，如下所示：

``` Java
public static void viewTable(Connection con) throws SQLException {

    String query = "select COF_NAME, SUP_ID, PRICE, " +
                   "SALES, TOTAL " +
                   "from COFFEES";

    try (Statement stmt = con.createStatement()) {

        ResultSet rs = stmt.executeQuery(query);

        while (rs.next()) {
            String coffeeName = rs.getString("COF_NAME");
            int supplierID = rs.getInt("SUP_ID");
            float price = rs.getFloat("PRICE");
            int sales = rs.getInt("SALES");
            int total = rs.getInt("TOTAL");
            System.out.println(coffeeName + ", " + supplierID +
                               ", " + price + ", " + sales +
                               ", " + total);
        }
    } catch (SQLException e) {
        JDBCTutorialUtilities.printSQLException(e);
    }
}
```
以下语句是try-with-resources语句，它声明一个资源，stmt当try块终止时将自动关闭：

``` Java
try（Statement stmt = con.createStatement（）） {
    // ...
}
```

