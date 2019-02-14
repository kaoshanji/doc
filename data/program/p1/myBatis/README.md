#   MyBatis

MyBatis 是一款持久层框架，它支持定制化 SQL、存储过程以及高级映射。MyBatis 避免了几乎所有的 JDBC 代码和手动设置参数以及获取结果集。MyBatis 可以使用简单的 XML 或注解来配置和映射原生信息，将接口和 Java 的 POJOs映射成数据库中的记录


##  目录
-   [大纲](000.md)
-   [数据准备--创建session]()
-   [逻辑处理--执行sql语句]()
-   扩展
-   集成Spring 

##  资料

-   [GitHub](https://github.com/mybatis/mybatis-3)
-   [入门实践](action/README.md)
    -   [官网](http://www.mybatis.org/mybatis-3/zh/index.html)
-   [原理源码](source/README.md)
    -   MyBatis技术内幕


##  集成/插件
-   集成Spring

MyBatis-Spring 会帮助你将 MyBatis 代码无缝地整合到 Spring 中。 使用这个类库中的类, Spring 将会加载必要的 MyBatis 工厂类和 session 类。 这个类库也提供一个简单的方式来注入 MyBatis 数据映射器和 SqlSession 到业务层的 bean 中。 而且它也会处理事务, 翻译 MyBatis 的异常到 Spring 的 DataAccessException 异常(数据访问异常)中。最终,它并 不会依赖于 MyBatis,Spring 或 MyBatis-Spring 来构建应用程序代码

-   [Mybatis-Plus](http://mp.baomidou.com/#/)
-   [Mybatis_PageHelper](https://gitee.com/free/Mybatis_PageHelper)
-   [Mapper](https://gitee.com/free/Mapper)
-   [mybatis集成spring](http://www.mybatis.org/spring/zh/index.html)
-   [mybatis集成spring(GitHub)](https://github.com/mybatis/spring)
-   [MyBatis分页插件PageHelper](https://pagehelper.github.io/)
-   [MyBatis分页插件PageHelper(GitHub)](https://github.com/pagehelper/Mybatis-PageHelper)
-   [极其方便的使用Mybatis单表的增删改查](https://gitee.com/free/Mapper)
-   [代码生成器：generator](http://www.mybatis.org/generator/)
-   [代码生成器：generator(GitHub)](https://github.com/mybatis/generator)

##  `打援`

-   JDBC
-   异常
-   枚举
-   注解
-   I/O
-   集合
-   设计模式
-   JAXP
-   反射
-   类加载器