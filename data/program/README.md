#   编程：21世纪的主题

数据为王，应用成形


##  数据：量（难度）
-   数据来源
-   数据存储
-   数据计算
-   数据搜索
-   数据传输
-   数据展示
-   运行环境

----

##  系统框架
-   业务逻辑
-   对象元素
-   数据流程
-   技术支持

----

##  产品工具
-   特定领域的通用解决方案
-   xx框架
-   服务、中间件

----

##  理论抽象
-   一种的东西有多种实现
-   描述某个综合式、大型、分工明细的结构

----

##  需求分析
-   业务逻辑思维导图
    -   抽象出业务逻辑
    -   把相同的东西放在一起
-   功能--业务逻辑思维导图（Model）
    -   支撑业务逻辑
    -   一个model对应多个业务逻辑
    -   先做最上面一层，尽可能多的进行一对多分析
    -   按照最小独立原则，每个model都是一个可以独立运行的模块
    -   按照人、事来分，人其实就是一个大模块，事就看里面有哪些事，相同的事就是一个模块，人和事之间又会有什么关系，那些是关系模块
-   基本功能模块关系
    -   事的划分标准是以业务逻辑来划分，要把业务逻辑里面相同的功能抽象出来形成功能模块
    -   不能主动发出请求的都归属于事
-   功能模块接口UML（设计出API）
-   在设计稿标注API
-   编写API文档

----