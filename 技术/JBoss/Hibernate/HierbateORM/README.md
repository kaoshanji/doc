Hierbate ORM doc

### 简介
- Hibernate以Java面向对象的方式操作数据库
- 把数据库与POJO映射，屏蔽数据库细节，ORM框架产品
- [官网](http://hibernate.org/orm/)
- [文档](http://hibernate.org/orm/documentation/getting-started/)
- [用户指南](https://docs.jboss.org/hibernate/orm/current/userguide/html_single/Hibernate_User_Guide.html)
- [github-hibernate](https://github.com/hibernate/hibernate-orm)
### 适用场景
- 持久层解决方案，数据库与POJO对应起来
### 组件
- 术语
    - ORM
        - 对象关系映射，是一个概念，数据库与Java对象之间映射起来，操作数据库就像使用Java对象一样
    - 实体
        - Java里Java Bean对象，数据库表在Java里的体现
    - 映射
        - 不同领域存在逻辑关系的事物关联起来，可以从这边找到那边，反过来也行
        - 比如：数据库里的表，Java里Java Bean，都是表示数据，只是处于的上下文不同
    - 值类型
        - 不同的数据库，表字段有不同的类型，不一定与Java对应
        - Java Bean里的属性是必须有类型
        - 数据库表字段、Java Bean属性，需要能够相互转换

-------

- 映射策略
    - Java组织数据与数据库表示数据存在差异，但是，数据可以在两边相互转换，数据还是数据，只是呈现的方式不同
    - 映射实体
        - Java Bean 与 表 关联
    - 映射值类型
        - Java Bean属性 与 表字段 对应
    - 映射继承关系
        - Java语法是面向对象语言，类之间可以继承、组合，但是数据库表没有这个说话，需要屏蔽这个差异
    - 映射集合
        - 数据库表一行数据可以表示为一个Java Bean对象
        - Java属性可以是集合类型，表示很多的某个对象，对应到数据库表里就是某个表多条数据
    - 实体关联关系
        - 实体之间存在逻辑关系，表之间也存在数据关系
- 事务控制
    - 管理数据
    - 事务与并发
    - 加载策略
    - 数据过滤

------------    

- 模型对象
    - 映射类型
    - 命名策略
    - 基本类型
    - 可嵌入类型
    - 实体类型
    - 主键
    - 关联关系
    - 集合
    - 动态模型
- 启动
- 生成模式
- 持久上下文
- 刷新
- 访问数据
- 事务和并发控制
- Locking
- Fetching
- 批量
- 缓存
- 拦截器和事件
- HQL and JPQL
- Criteria
- Native SQL Queries
- Spatial
- Multitenancy
- Envers
- 数据库移植注意事项
- 配置
- 映射注解
- 性能调优和最佳实践
### 实践