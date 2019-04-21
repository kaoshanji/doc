#   JDBC-v.0.0.2

##  JDBC的设计

JDBC接口(驱动管理器) ===> 供应商驱动(数据库网络协议)  ===> 数据库服务器

相关：SQL语句，独立于Java存在，属于关系型数据库标准语言

![20180728001](image/20180728001.png)
-   HTTP与Java对象之间转换
-   Java对象与数据库之间转换

----

##  JDBC操作数据库
-   安装关系数据库服务器，使用客户端连接，创建数据库，如get_over，获得数据库URL：与数据库类型相关的参数，例如主机名、端口号和数据库名(因为是Java/Mysql所以，URL应该是jdbc:mysql://localhost:3306/get_over)
-   添加驱动程序JAR文件，例如Mysql:mysql-connector-java-xxx.jar，并启动数据库服务器
-   Java代码连接数据库服务器，一次网络请求，围绕 `Connection`
``` Java
 // 1、 注册驱动器类
    String drivers = "com.mysql.jdbc.Driver";
    Class.forName(drivers);
 // 2、 获得数据库连接对象
    // url      : 对应上面的URL
    // username : 连接用户名
    // password : 连接密码
    Connection connection = DriverManager.getConnection(url,username, password);
    // 可以设置一些 连接属性

 // 3、 发起请求：执行SQL语句
    // 3.1、执行SQL语句对象
    Statement stat = connection.createStatement();
        // Sql语句有参数，优先考虑Statement子接口：PreparedStatement
        // 批量更新，考虑 stat.addBatch();
    // 3.2、查询：获取数据，属于读
        // 查询全部(包含一条)
        ResultSet result = stat.executeQuery("SELECT * FROM Greetings")
    // 3.3、更新：删除、创建、更新，属于写
        // 设置事务
            Boolean auto =  conn.getAutoCommit();
            conn.setAutoCommit(false);

            // 更新语句..
            int num = stat.executeUpdate("INSERT INTO Greetings ('Hello')");

            // 获取自动生成键
            stat.executeUpdate("insertSql", Statement.RETURN_GENERATED_KEYS);
            
            conn.commit();
            conn.setAutoCommit(auto);
 // 4、 接收响应：处理结果
    // 4.1、查询
        // 遍历 ResultSet对象，优先考虑使用ResultSet子接口：CachedRowSet(缓存结果集，断开连接正常使用)
        // 构建Java对象的过程..把ResultSet对象里的数据转换成Java对象
        if (result.next()) {
            // 一个List<Map<String,Object> 数据格式
            // 根据字段名称，位置等获取值，可以指定Java基本类型方法，就不用转换
            // 一些特殊数据，如：大字段等，也有对应的对象
            logger.info(result.getString(1));
        }
    // 4.2、更新
        // 影响数量
            int num = ...
        // 获取自动生成键
            ResultSet rs = stat.getGeneratedKeys();
            if (rs.next()) {
                int key = rs.getInt(1);
            }

 // 5、 关闭连接
    // 放在 finally 里面
    connection.close();
```

----

##  其他
-   元数据：描述数据库或其组成部分的数据
``` Java

// 数据库：
DatabaseMetaData meta = connection.getMetaData();

// 结果集：
ResultSetMetaData meta = result.getMetaData();

```
-   Sql语句类型

----
