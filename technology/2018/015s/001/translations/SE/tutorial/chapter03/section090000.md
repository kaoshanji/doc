#   Java命名和目录接口

此跟踪描述了JNDI™（Java命名和目录接口）的API以访问目录和命名服务。在这里，您将了解基本的命名和目录服务以及如何使用JNDI编写简单的应用程序来使用这些服务。最流行的目录服务LDAP用于介绍如何使用JNDI访问目录服务。

图像表示子弹 命名和目录概念从这里开始概述命名和目录概念。

图像表示子弹 JNDI概述概述了JNDI及其体系结构和打包。

图像表示子弹 软件设置介绍设置运行此跟踪中描述的示例所需的环境以及任何其他JNDI应用程序所涉及的指令和步骤。

图像表示子弹 命名和目录操作介绍各种命名和目录操作，并通过大量使用JNDI访问命名/目录服务的示例来演示它们。

图像表示子弹 LDAP用户的高级主题LDAP用户的专门课程。它讨论了将JNDI建模为LDAP API，如何执行LDAP身份验证，SSL和管理生产环境中的连接。

图像表示子弹 访问目录中的对象显示如何将应用程序与目录集成，以便您可以在目录中存储和检索Java对象。

图像表示子弹 JDK 5.0和JDK 6中的功能介绍 JDK 5.0和JDK 6中提供的JNDI和LDAP服务提供程序中的功能。


##  目录

-   [命名和目录概念](section090100.md)
    -   [目录概念](section090101.md)
-   [JNDI概述](section090100.md)
    -   [命名包](section090101.md)
    -   [目录和LDAP包](section090102.md)
    -   [事件和服务提供程序包](section090103.md)
-   [软件设置](section090200.md)
    -   [LDAP设置](section090201.md)
    -   [Java应用程序设置](section090202.md)
-   [命名和目录操作](section090300.md)
    -   [命名例外](section090301.md)
    -   [查找对象](section090302.md)
    -   [列出上下文](section090303.md)
    -   [添加，替换或删除绑定](section090304.md)
    -   [改名](section090305.md)
    -   [创建和销毁子上下文](section090306.md)
    -   [属性名称](section090307.md)
    -   [读取属性](section090308.md)
    -   [修改属性](section090309.md)
    -   [添加，替换绑定与属性](section090310.md)
    -   [搜索](section090311.md)
        -   [基本搜索](section090311/0100.md)
        -   [过滤器](section090311/0200.md)
        -   [范围](section090311/0300.md)
        -   [结果计数](section090311/0400.md)
        -   [时限](section090311/0500.md)
    -   [疑难解答提示](section090312.md)
-   [LDAP用户的高级主题](section090400.md)
    -   [LDAP v3](section090401.md)
    -   [JNDI作为LDAP API](section090402.md)
        -   [LDAP操作如何映射到JNDI API](section090402/0100.md)
        -   [LDAP错误代码如何映射到JNDI异常](section090402/0200.md)
    -   [安全](section090403.md)
        -   [对LDAP进行身份验证的模式](section090403/0100.md)
        -   [认证机制](section090403/0200.md)
        -   [匿名](section090403/0300.md)
        -   [简单](section090403/0400.md)
        -   [SASL](section090403/0500.md)
        -   [摘要-MD5](section090403/0600.md)
        -   [SSL和自定义套接字](section090403/0700.md)
    -   [更多LDAP操作](section090404.md)
        -   [LDAP比较](section090404/0100/md)
        -   [搜索结果](section090404/0200/md)
        -   [LDAP未经请求的通知](section090404/0300/md)
    -   [连接管理](section090405.md)
        -   [创建](section090405/0100.md)
        -   [闭幕](section090405/0200.md)
        -   [池](section090405/0300.md)
        -   [组态](section090405/0400.md)
    -   [经常问的问题](section090406.md)
-   [目录中的Java对象](section090500.md)
    -   [存储和读取对象](section090501.md)
    -   [可序列化的对象](section090502.md)
-   [JDK 5.0和JDK 6中的新功能](section090600.md)
    -   [检索可分辨名称](section090601.md)
    -   [标准的LDAP控制](section090602.md)
    -   [分页结果控制](section090603.md)
    -   [排序控制](section090604.md)
    -   [管理引荐控制](section090605.md)
    -   [操作LdapName（可分辨名称）](section090606.md)
    -   [操作相对不受限制的名称（RDN）](section090607.md)
    -   [设置Ldap操作超时](section090608.md)
