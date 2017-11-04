## 概念

### 安装
``` xml
<dependency>
    <groupId>org.mybatis</groupId>
    <artifactId>mybatis</artifactId>
    <version>x.x.x</version>
</dependency>
```

### SqlSessionFactory
- 每个基于 MyBatis 的应用都是以一个 SqlSessionFactory 的实例为中心
- 每个数据源对应一个
- 包含获取数据库连接实例的数据源(DataSource)
- 决定事务作用域
- 控制方式的事务管理器(TransactionManager)
- mapper 映射器(包含了 SQL 代码和映射定义信息)
- 例如:
    ``` xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE configuration
    PUBLIC "-//mybatis.org//DTD Config 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-config.dtd">
    <configuration>
        <environments default="development">
            <environment id="development">
            <transactionManager type="JDBC"/>
            <dataSource type="POOLED">
                <property name="driver" value="${driver}"/>
                <property name="url" value="${url}"/>
                <property name="username" value="${username}"/>
                <property name="password" value="${password}"/>
            </dataSource>
            </environment>
        </environments>
        <mappers>
            <mapper resource="org/mybatis/example/BlogMapper.xml"/>
        </mappers>
    </configuration>
    ```

### SqlSession
- 完全包含了面向数据库执行 SQL 命令所需的所有方法
- 例如：
    ``` Java
    SqlSession session = sqlSessionFactory.openSession();
    try {
        BlogMapper mapper = session.getMapper(BlogMapper.class);
        Blog blog = mapper.selectBlog(101);
    } finally {
        session.close();
    }
    ```

### 映射的 SQL 语句
- 通过 XML 定义
- 例如：
    ``` xml
    <?xml version="1.0" encoding="UTF-8" ?>
    <!DOCTYPE mapper
    PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
    "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
    <mapper namespace="org.mybatis.example.BlogMapper">
        <select id="selectBlog" resultType="Blog" parameterType="java.lang.Integer">
            select * from Blog where id = #{id}
        </select>
    </mapper>
- Java类
    - `BlogMapper`是一个`接口类`，定义`selectBlog`方法，返回值是`Blog`,参数是`int`
- 命名空间
    - 使用更长的完全限定名来更进一步区分语句
    - 命名空间使得你所见到的接口绑定成为可能
    - 命名空间与`Java`接口类对应
    - 命名空间下元素`id`属性值对应`接口类#方法名`，也还有，返回值、输入参数

### 作用域和生命周期
- SqlSessionFactoryBuilder
    - 这个类可以被实例化、使用和丢弃，一旦创建了 SqlSessionFactory，就不再需要它了
    - SqlSessionFactoryBuilder 实例的最佳作用域是方法作用域（也就是局部方法变量）
- SqlSessionFactory
    - 一旦被创建就应该在应用的运行期间一直存在，没有任何理由对它进行清除或重建
    - SqlSessionFactory 的最佳作用域是应用作用域。有很多方法可以做到，最简单的就是使用单例模式或者静态单例模式
- SqlSession
    - 每个线程都应该有它自己的 SqlSession 实例
    - SqlSession 的实例不是线程安全的，因此是不能被共享的，所以它的最佳的作用域是请求或方法作用域
    - 正在使用一种 Web 框架，要考虑 SqlSession 放在一个和 HTTP 请求对象相似的作用域中
    - 每次收到的 HTTP 请求，就可以打开一个 SqlSession，返回一个响应，就关闭它
- 映射器实例
    - 映射器是创建用来绑定映射语句的接口
    - 映射器实例应该在调用它们的方法中被请求，用过之后即可废弃