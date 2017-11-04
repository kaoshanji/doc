## XML配置
> MyBatis 的配置文件包含了会深深影响 MyBatis 行为的设置（settings）和属性（properties）信息

### configuration 配置元素
- properties 属性
- settings 设置
- typeAliases 类型别名
- typeHandlers 类型处理器
- objectFactory 对象工厂
- plugins 插件
- environments 环境
- databaseIdProvider 数据库厂商标识
- mappers 映射器

### properties
- 可外部配置且可动态替换,既可以在典型的 Java 属性文件中配置，亦可通过 properties 元素的子元素来传递
- 例如:
    ``` xml
    <properties resource="org/mybatis/example/config.properties">
        <property name="username" value="dev_user"/>
        <property name="password" value="F2Fa3!33TYyg"/>
    </properties>

    <!- 其中的属性就可以在整个配置文件中使用来替换需要动态配置的属性值->

    <dataSource type="POOLED">
        <property name="driver" value="${driver}"/>
        <property name="url" value="${url}"/>
        <property name="username" value="${username}"/>
        <property name="password" value="${password}"/>
    </dataSource>
    ```
- 例子中的 username 和 password 将会由 properties 元素中设置的相应值来替换
-  driver 和 url 属性将会由 config.properties 文件中对应的值来替换
- settings
    - MyBatis 中极为重要的调整设置，它们会改变 MyBatis 的运行时行为
    - 例如:
        ``` xml
        <settings>
            <setting name="cacheEnabled" value="true"/>
            <setting name="lazyLoadingEnabled" value="true"/>
            <setting name="multipleResultSetsEnabled" value="true"/>
            <setting name="useColumnLabel" value="true"/>
            <setting name="useGeneratedKeys" value="false"/>
            <setting name="autoMappingBehavior" value="PARTIAL"/>
            <setting name="autoMappingUnknownColumnBehavior" value="WARNING"/>
            <setting name="defaultExecutorType" value="SIMPLE"/>
            <setting name="defaultStatementTimeout" value="25"/>
            <setting name="defaultFetchSize" value="100"/>
            <setting name="safeRowBoundsEnabled" value="false"/>
            <setting name="mapUnderscoreToCamelCase" value="false"/>
            <setting name="localCacheScope" value="SESSION"/>
            <setting name="jdbcTypeForNull" value="OTHER"/>
            <setting name="lazyLoadTriggerMethods" value="equals,clone,hashCode,toString"/>
        </settings>
        ```

### typeAliases
- 类型别名是为 Java 类型设置一个短的名字。它只和 XML 配置有关，存在的意义仅在于用来减少类完全限定名的冗余
- 例如:
    ``` xml
    <typeAliases>
        <typeAlias alias="Author" type="domain.blog.Author"/>
        <typeAlias alias="Blog" type="domain.blog.Blog"/>
        <typeAlias alias="Comment" type="domain.blog.Comment"/>
        <typeAlias alias="Post" type="domain.blog.Post"/>
        <typeAlias alias="Section" type="domain.blog.Section"/>
        <typeAlias alias="Tag" type="domain.blog.Tag"/>
    </typeAliases>
    ```
    - 当这样配置时，Blog可以用在任何使用domain.blog.Blog的地方
- 也可以指定一个包名，MyBatis 会在包名下面搜索需要的 Java Bean
- 例如:
    ``` xml
        <typeAliases>
            <package name="domain.blog"/>
        </typeAliases>
    ```
    - 每一个在包 domain.blog 中的 Java Bean，在没有注解的情况下，会使用 Bean 的首字母小写的非限定类名来作为它的别名
    - 比如 domain.blog.Author 的别名为 author；若有注解，则别名为其注解值
    ``` Java
    @Alias("author")
    public class Author {
        ...
    }
    ```

### typeHandlers
- 无论是 MyBatis 在预处理语句（PreparedStatement）中设置一个参数时，还是从结果集中取出一个值时， 都会用类型处理器将获取的值以合适的方式转换成 Java 类型
- 重写类型处理器或创建你自己的类型处理器来处理不支持的或非标准的类型
    - 实现 `org.apache.ibatis.type.TypeHandler` 接口
    - 或继承一个很便利的类 `org.apache.ibatis.type.BaseTypeHandler`
    - 然后可以选择性地将它映射到一个 JDBC 类型

### 对象工厂(objectFactory)
- MyBatis 每次创建结果对象的新实例时，它都会使用一个对象工厂（ObjectFactory）实例来完成
-  默认的对象工厂需要做的仅仅是实例化目标类，要么通过默认构造方法，要么在参数映射存在的时候通过参数构造方法来实例化
- 如果想覆盖对象工厂的默认行为，则可以通过创建自己的对象工厂来实现

### 插件(plugins)
- MyBatis 允许你在已映射语句执行过程中的某一点进行拦截调用。默认情况下，MyBatis 允许使用插件来拦截的方法调用包括
    - Executor (update, query, flushStatements, commit, rollback, getTransaction, close, isClosed)
    - ParameterHandler (getParameterObject, setParameters)
    - ResultSetHandler (handleResultSets, handleOutputParameters)
    - StatementHandler (prepare, parameterize, batch, update, query)

### 配置环境(environments)
- 开发、测试和生产环境需要有不同的配置
- 共享相同 Schema 的多个生产数据库， 想使用相同的 SQL 映射
- `每个数据库对应一个 SqlSessionFactory 实例`
- 例如:
    ``` xml
    <environments default="development">
        <environment id="development">
            <transactionManager type="JDBC">
            <property name="..." value="..."/>
            </transactionManager>
            <dataSource type="POOLED">
            <property name="driver" value="${driver}"/>
            <property name="url" value="${url}"/>
            <property name="username" value="${username}"/>
            <property name="password" value="${password}"/>
            </dataSource>
        </environment>
    </environments>
    ```
- 默认的环境 ID(比如:default=”development”)
- 每个 environment 元素定义的环境 ID(比如:id=”development”)
- 事务管理器的配置(比如:type="JDBC")
- 数据源的配置(比如:type="POOLED")

### 数据库厂商标识(databaseIdProvider)
- MyBatis 可以根据不同的数据库厂商执行不同的语句，这种多厂商的支持是基于映射语句中的 databaseId 属性

### 映射器(mappers)
- 最佳的方式是告诉 MyBatis 到哪里去找映射文件
- 例如:
    ``` xml
    <!-- Using classpath relative resources -->
    <mappers>
        <mapper resource="org/mybatis/builder/AuthorMapper.xml"/>
        <mapper resource="org/mybatis/builder/BlogMapper.xml"/>
        <mapper resource="org/mybatis/builder/PostMapper.xml"/>
    </mappers>
    <!-- Using mapper interface classes -->
    <mappers>
        <mapper class="org.mybatis.builder.AuthorMapper"/>
        <mapper class="org.mybatis.builder.BlogMapper"/>
        <mapper class="org.mybatis.builder.PostMapper"/>
    </mappers>
    <!-- Register all interfaces in a package as mappers -->
    <mappers>
        <package name="org.mybatis.builder"/>
    </mappers>
    ```