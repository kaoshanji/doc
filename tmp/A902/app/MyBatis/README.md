# mybatis

MyBatis 是一款持久层框架，它支持定制化 SQL、存储过程以及高级映射。MyBatis 避免了几乎所有的 JDBC 代码和手动设置参数以及获取结果集。MyBatis 可以使用简单的 XML 或注解来配置和映射原生信息，将接口和 Java 的 POJOs映射成数据库中的记录

## 看看JDBC
-   [JDBC代码示例](core/JDBC.md)
-   JDBC步骤
    - 注册驱动器
    - 获得数据库连接
    - 执行查询
    - 处理结果集
    - 关闭连接
-   重点
    - 逻辑在`第三步:执行查询`，结果在`第四步:处理结果集`
    - 前面两步和最后一步，都是相同，代码模式会告诉怎样写..
    - 但是，这些又必须存在，是不是可以配置呢?

##  组件
-   [概念](core/Introduction.md)
-   [XML配置](core/Configuration.md)
-   [XML映射文件](core/Mapper.md)
-   [动态SQL](core/Dynamic-SQL.md)


### 集成/插件
-   [集成Spring](mybatis-spring/README.md)
-   [Mybatis-Plus](http://mp.baomidou.com/#/)
-   [Mybatis_PageHelper](https://gitee.com/free/Mybatis_PageHelper)
-   [Mapper](https://gitee.com/free/Mapper)
