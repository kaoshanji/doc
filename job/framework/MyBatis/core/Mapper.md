## Mapper XML 文件
> MyBatis 的真正强大在于它的映射语句,由于它的异常强大，映射器的 XML 文件就显得相对简单.MyBatis 就是针对 SQL 构建的，并且比普通的方法做的更好

### SQL 映射文件有很少的几个顶级元素
- `cache` – 给定命名空间的缓存配置
- `cache-ref` – 其他命名空间缓存配置的引用
- `resultMap` – 是最复杂也是最强大的元素，用来描述如何从数据库结果集中来加载对象
- `sql` – 可被其他语句引用的可重用语句块
- `insert` – 映射插入语句
- `update` – 映射更新语句
- `delete` – 映射删除语句
- `select` – 映射查询语句

### select
- 查询语句是 MyBatis 中最常用的元素之一
- 多数应用也都是查询比修改要频繁
- 例如:
    ``` xml
    <select id="selectPerson" parameterType="int" resultType="hashmap">
        SELECT * FROM PERSON WHERE ID = #{id}
    </select>
    ```
    - 这个语句被称作 selectPerson，接受一个 int（或 Integer）类型的参数，并返回一个 HashMap 类型的对象，其中的键是列名，值便是结果行中的对应值
- 细节:
    ``` xml
    <select
        id="selectPerson"
        parameterType="int"
        parameterMap="deprecated"
        resultType="hashmap"
        resultMap="personResultMap"
        flushCache="false"
        useCache="true"
        timeout="10000"
        fetchSize="256"
        statementType="PREPARED"
        resultSetType="FORWARD_ONLY">
    ```

### insert, update 和 delete
``` xml
<insert
    id="insertAuthor"
    parameterType="domain.blog.Author"
    flushCache="true"
    statementType="PREPARED"
    keyProperty=""
    keyColumn=""
    useGeneratedKeys=""
    timeout="20">

<update
    id="updateAuthor"
    parameterType="domain.blog.Author"
    flushCache="true"
    statementType="PREPARED"
    timeout="20">

<delete
    id="deleteAuthor"
    parameterType="domain.blog.Author"
    flushCache="true"
    statementType="PREPARED"
    timeout="20">
```
                
### Result Maps
- resultMap 元素是 MyBatis 中最重要最强大的元素
- 远离 90%的需要从结果 集中取出数据的 JDBC 代码的那个东西
- 例如1
    ``` xml
    <select id="selectUsers" resultType="map">
        select id, username, hashedPassword
        from some_table
        where id = #{id}
    </select>
    ```
    - 这样一个语句简单作用于所有列被自动映射到 HashMap 的键上,这由 resultType 属性 指定
- 例如2
    ``` xml
    <select id="selectUsers" resultType="com.someapp.model.User">
        select id, username, hashedPassword
        from some_table
        where id = #{id}
    </select>
    ```
    - User有三个属性:id,username 和 hashedPassword

### 自动映射 
- 当自动映射查询结果时，MyBatis会获取sql返回的列名并在java类中查找相同名字的属性（忽略大小写）
- 通常数据库列使用大写单词命名，单词间用下划线分隔；而java属性一般遵循驼峰命名法。 为了在这两种命名方式之间启用自动映射，需要将 mapUnderscoreToCamelCase设置为true