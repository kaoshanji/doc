## 概念
> 以简略的步骤告诉你如何安装和创建 MyBatis-Spring,并构建一个简单的数据 访问事务性的应用程序

### 安装
``` xml
<dependency>
  <groupId>org.mybatis</groupId>
  <artifactId>mybatis-spring</artifactId>
  <version>x.x.x</version>
</dependency>
```

### 开始
- 要和 Spring 一起使用 MyBatis,需要在 Spring 应用上下文中定义至少两样东西:一个 SqlSessionFactory 和至少一个数据映射器类
- 在 MyBatis-Spring 中,SqlSessionFactoryBean 是用于创建 SqlSessionFactory 的。要 配置这个工厂 bean,放置下面的代码在 Spring 的 XML 配置文件中：
  ``` xml
  <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
    <property name="dataSource" ref="dataSource" />
  </bean>
  ```
- 定义接口：
  ``` Java
    public interface UserMapper {
      @Select("SELECT * FROM users WHERE id = #{userId}")
      User getUser(@Param("userId") String userId);
    }
  ```
  - 可以使用 MapperFactoryBean,像下面这样来把接口加入到 Spring 中：

  ``` xml
  <bean id="userMapper" class="org.mybatis.spring.mapper.MapperFactoryBean">
    <property name="mapperInterface" value="org.mybatis.spring.sample.mapper.UserMapper" />
    <property name="sqlSessionFactory" ref="sqlSessionFactory" />
  </bean>
  ```
  - 要注意,所指定的映射器类必须是一个接口,而不是具体的实现类
  - 在这个示例中,注 解被用来指定 SQL 语句,但是 MyBatis 的映射器 XML 文件也可以用
- 使用：
  - 一旦配置好,你可以用注入其它任意 Spring 的 bean 相同的方式直接注入映射器到你的 business/service 对象中。MapperFactoryBean 处理 SqlSession 的创建和关闭它。如果使用 了 Spring 的事务,那么当事务完成时,session 将会提交或回滚。最终,任何异常都会被翻 译成 Spring 的 DataAccessException 异常
  - 调用 MyBatis 数据方法现在只需一行代码：
  ``` Java
  public class FooServiceImpl implements FooService {

  private UserMapper userMapper;

  public void setUserMapper(UserMapper userMapper) {
    this.userMapper = userMapper;
  }

  public User doSomeBusinessStuff(String userId) {
    return this.userMapper.getUser(userId);
  }
  ```

### SqlSessionFactoryBean
- 定义
  - 在基本的 MyBatis 中,session 工厂可以使用 SqlSessionFactoryBuilder 来创建。而在 MyBatis-Spring 中,则使用 SqlSessionFactoryBean 来替代
- 开始
  - 配置如上
  - SqlSessionFactoryBean 实现了 Spring 的 FactoryBean 接口
  - 他是由 Spring 创建的 bean 不是 SqlSessionFactoryBean 本身, 而是工厂类的 getObject()返回的方法的结果
  - 这种情况下,Spring 将会在应用启动时为你 创建 SqlSessionFactory 对象,然后将它以 SqlSessionFactory 为名来存储
- 属性
  - JDBC 的 DataSource
    - 单独的必须属性
    - 可以是任意 的 DataSource,其配置应该和其它 Spring 数据库连接是一样的
  - configLocation
    - 用来指定 MyBatis 的 XML 配置文件路径，如果基本的 MyBatis 配置需要改变, 那么这就是一个需要它的地方。 通常这会是`<settings>` 或`<typeAliases>`的部分
    - 这个配置文件不需要是一个完整的 MyBatis 配置
    - 任意环境,数据源 和 MyBatis 的事务管理器都会被忽略
    - SqlSessionFactoryBean 会创建它自己的,使用这些 值定制 MyBatis 的 Environment 时是需要的
  - mapperLocations
    - 用来指定 MyBatis 的 XML 映射器文件的位置
    - 它的值可以包含 Ant 样式来加载一个目录中所有文件, 或者从基路径下 递归搜索所有路径
    - 例如：
      ``` xml
      <bean id="sqlSessionFactory" class="org.mybatis.spring.SqlSessionFactoryBean">
        <property name="dataSource" ref="dataSource" />
        <property name="mapperLocations" value="classpath*:sample/config/mappers/**/*.xml" />
      </bean>
      ```
      - 这会从类路径下加载在 sample.config.mappers 包和它的子包中所有的 MyBatis 映射器 XML 文件

### 事务
- 定义
  - 一个使用 MyBatis-Spring 的主要原因是它允许 MyBatis 参与到 Spring 的事务管理中
  - MyBatis-Spring 利用了存在于 Spring 中的 DataSourceTransactionManager
  - 一旦 Spring 的 PlatformTransactionManager 配置好了,你可以在 Spring 中以你通常的做 法来配置事务，@Transactional 注解和 AOP(Aspect-Oriented Program,面向切面编程,译 者注)样式的配置都是支持的
  - 在事务处理期间,一个单独的 SqlSession 对象将会被创建 和使用。当事务完成时,这个 session 会以合适的方式提交或回滚
  - 一旦事务创建之后,MyBatis-Spring 将会透明的管理事务。在你的 DAO 类中就不需要额 外的代码了
- 标准配置
  - 要 开 启 Spring 的 事 务 处 理 , 在 Spring 的 XML 配 置 文 件 中 简 单 创 建 一 个 DataSourceTransactionManager 对象:
  ``` xml
  <bean id="transactionManager" class="org.springframework.jdbc.datasource.DataSourceTransactionManager">
    <property name="dataSource" ref="dataSource" />
  </bean>
  ```
  - 指定的 DataSource 一般可以是你使用 Spring 的任意 JDBC DataSource
  - 为事务管理器指定的 DataSource 必须和用来创建 SqlSessionFactoryBean 的 是同一个数据源，否则事务管理器就无法工作了

### 注入映射器
- 定义
  - 为了代替手工使用 SqlSessionDaoSupport 或 SqlSessionTemplate 编写数据访问对象 (DAO)的代码,MyBatis-Spring 提供了一个动态代理的实现:MapperFactoryBean
  - 这个类 可以让你直接注入数据映射器接口到你的 service 层 bean 中
  - 当使用映射器时,你仅仅如调 用你的 DAO 一样调用它们就可以了,但是你不需要编写任何 DAO 实现的代码,因为 MyBatis-Spring 将会为你创建代理
- MapperFactoryBean
  - 配置如上
  - 如果 UserMapper 有一个对应的 MyBatis 的 XML 映射器文件, 如果 XML 文件在类路径的 位置和映射器类相同时, 它会被 MapperFactoryBean 自动解析
- MapperScannerConfigurer
  - 将会查找类路径下的映射器并自动将它们创建成MapperFactoryBean
  - 配置：在 Spring 的配置中添加如下代码
  ``` xml
  <bean class="org.mybatis.spring.mapper.MapperScannerConfigurer">
    <property name="basePackage" value="org.mybatis.spring.sample.mapper" />
  </bean>
  ```
    - basePackage 属性是让你为映射器接口文件设置基本的包路径
  - 当只有一个数据源时，没有必要去指定`SqlSessionFactory`或`SqlSessionTemplat`，会自动装配
  - 多于一个数据源时，自动配置会失效，需要使用`sqlSessionFactoryBeanName`或 `sqlSessionTemplateBeanName` 属性来设置正确的 `bean` 名称来使用
