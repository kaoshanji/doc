## 动态SQL
> 如果有使用 JDBC 或其他类似框架的经验，你就能体会到根据不同条件拼接 SQL 语句有多么痛苦

### if
- 动态 SQL 通常要做的事情是有条件地包含 where 子句的一部分
- 例如:
    ``` xml
    <select id="findActiveBlogWithTitleLike"resultType="Blog">
        SELECT * FROM BLOG WHERE state = 'ACTIVE' 
        <if test="title != null">
            AND title like #{title}
        </if>
    </select>
    ```

### choose, when, otherwise
- 不想用到所有的条件语句，而只想从中择其一二
- 例如：
    ``` xml
    <select id="findActiveBlogLike" resultType="Blog">
        SELECT * FROM BLOG WHERE state = 'ACTIVE'
        <choose>
            <when test="title != null">
            AND title like #{title}
            </when>
            <when test="author != null and author.name != null">
            AND author_name like #{author.name}
            </when>
            <otherwise>
            AND featured = 1
            </otherwise>
        </choose>
    </select>
    ```

### trim, where, set
- where 条件字段有可能出现
- 例如：
    ``` sql

    SELECT * FROM BLOG WHERE
    SELECT * FROM BLOG WHERE AND title like 'someTitle'
    ```

- 解决：
    ``` xml
    <select id="findActiveBlogLike" resultType="Blog">
        SELECT * FROM BLOG 
        <where> 
            <if test="state != null">
                state = #{state}
            </if> 
            <if test="title != null">
                AND title like #{title}
            </if>
            <if test="author != null and author.name != null">
                AND author_name like #{author.name}
            </if>
        </where>
    </select>
    ```

### foreach
- 需要对一个集合进行遍历，通常是在构建 IN 条件语句的时候
``` xml
<select id="selectPostIn" resultType="domain.blog.Post">
    SELECT *
    FROM POST P
    WHERE ID in
    <foreach item="item" index="index" collection="list"
        open="(" separator="," close=")">
            #{item}
    </foreach>
</select>
```