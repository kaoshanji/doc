#   官方讲解

##  安装

``` xml
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis</artifactId>
  <version>x.x.x</version>
</dependency>
```

代码示例...

----

##  XML配置

MyBatis 的配置文件包含了会深深影响 MyBatis 行为的设置（settings）和属性（properties）信息。

-   properties 属性：这些属性都是可外部配置且可动态替换的
-   settings 设置：MyBatis 中极为重要的调整设置，它们会改变 MyBatis 的运行时行为
-   typeAliases 类型别名：为 Java 类型设置一个短的名字。它只和 XML 配置有关，存在的意义仅在于用来减少类完全限定名的冗余
-   typeHandlers 类型处理器：在预处理语句（PreparedStatement）中设置一个参数时，还是从结果集中取出一个值时， 都会用类型处理器将获取的值以合适的方式转换成 Java 类型
    -   处理枚举类型
-   objectFactory 对象工厂：每次创建结果对象的新实例时，它都会使用一个对象工厂（ObjectFactory）实例来完成
-   plugins 插件：在已映射语句执行过程中的某一点进行拦截调用。默认情况下，MyBatis 允许使用插件来拦截的方法调用包括
    -   只需实现 Interceptor 接口，并指定想要拦截的方法签名即可
-   environments 环境：开发、测试和生产环境需要有不同的配置，每个数据库对应一个 SqlSessionFactory 实例
    -   environment 环境变量
        -   transactionManager 事务管理器
        -   dataSource 数据源
-   databaseIdProvider 数据库厂商标识
-   mappers 映射器：告诉 MyBatis 到哪里去找到定义 SQL 映射语句
    ``` XML
    <!-- 使用相对于类路径的资源引用 -->
    <mappers>
        <mapper resource="org/mybatis/builder/AuthorMapper.xml"/>
        <mapper resource="org/mybatis/builder/BlogMapper.xml"/>
        <mapper resource="org/mybatis/builder/PostMapper.xml"/>
    </mappers>
    <!-- 使用映射器接口实现类的完全限定类名 -->
    <mappers>
        <mapper class="org.mybatis.builder.AuthorMapper"/>
        <mapper class="org.mybatis.builder.BlogMapper"/>
        <mapper class="org.mybatis.builder.PostMapper"/>
    </mappers>
    <!-- 将包内的映射器接口实现全部注册为映射器 -->
    <mappers>
        <package name="org.mybatis.builder"/>
    </mappers>
    ```

----

##  Mapper XML 文件
-   查询(select)
-   更新(insert,update,delete)
-   sql
-   参数（Parameters）
-   结果集(ResultMap)：在sql语句结果与Java对象之间转换
    -   高级结果映射
    -   自动映射
-   缓存

----

##  动态 SQL

----

##  Java API
-   SqlSessions
    -   使用 MyBatis 的主要 Java 接口就是 SqlSession
    -   通过这个接口来执行命令，获取映射器和管理事务
    -   SqlSessions 是由 SqlSessionFactory 实例创建的，而 SqlSessionFactory 本身是由 SqlSessionFactoryBuilder 创建的
-   SqlSessionFactoryBuilder
    -   有五个 build() 方法，每一种都允许你从不同的资源中创建一个 SqlSessionFactory 实例
-   SqlSessionFactory
    -   SqlSessionFactory 有六个方法创建 SqlSession 实例
    -   事务处理：我需要在 session 使用事务或者使用自动提交功能（auto-commit）吗？
    -   连接：我需要依赖 MyBatis 获得来自数据源的配置吗？还是使用自己提供的配置？
    -   执行语句：我需要 MyBatis 复用预处理语句和/或批量更新语句（包括插入和删除）吗？
-   SqlSession
    -   执行语句方法
        ``` Java
        <T> T selectOne(String statement, Object parameter)
        <E> List<E> selectList(String statement, Object parameter)
        <K,V> Map<K,V> selectMap(String statement, Object parameter, String mapKey)
        int insert(String statement, Object parameter)
        int update(String statement, Object parameter)
        int delete(String statement, Object parameter)

        <E> List<E> selectList (String statement, Object parameter, RowBounds rowBounds)
        <K,V> Map<K,V> selectMap(String statement, Object parameter, String mapKey, RowBounds rowbounds)
        void select (String statement, Object parameter, ResultHandler<T> handler)
        void select (String statement, Object parameter, RowBounds rowBounds, ResultHandler<T> handler)

        ```
    -   批量立即更新方法
        ``` Java
        List<BatchResult> flushStatements()
        ```
    -   事务控制方法
        ``` Java
        void commit()
        void commit(boolean force)
        void rollback()
        void rollback(boolean force)
        ```
    -   本地缓存
        ``` Java
        void clearCache()
        ```
    -   确保 SqlSession 被关闭
        ``` Java
        void close()
        ```
    -   使用映射器
        ``` Java
        <T> T getMapper(Class<T> type)
        ```
    -   映射器注解

----

##  日志

-   指定日志

存在任意一种流行日志都行，优先选择第一个找到的，因此应用服务器（如 Tomcat 和 WebShpere）的类路径中已经包含 Commons Logging，所以在这种配置环境下的 MyBatis 会把它作为日志工具。

在MyBatis 配置文件 mybatis-config.xml 里面添加一项 setting 来选择别的日志工具：
``` XML
<configuration>
  <settings>
    ...
    <setting name="logImpl" value="LOG4J"/>
    ...
  </settings>
</configuration>
```

-   日志配置
    -   添加jar包
    -   配置指定范围

----