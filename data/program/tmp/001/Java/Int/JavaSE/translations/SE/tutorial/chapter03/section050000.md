#   国际化

这条线索的教训将教你如何国际化Java应用程序。国际化的应用程序很容易根据世界各地最终用户的习俗和语言进行调整。

>   注意：  本教程跟踪核心国际化功能，这是桌面，企业和移动应用程序提供的附加功能所需的基础。有关更多信息，请参阅 Java Internationalization主页。

-   [简介](section050100.md)定义术语国际化，提供快速示例程序，并提供可用于国际化现有程序的清单。
-   [设置区域设置](section050200.md)说明如何创建和如何使用Locale对象。
-   [隔离特定于区域的数据](section050300.md)显示如何动态访问随对象而变化的对象Locale。
-   [格式化](section050400.md)说明如何根据数字，日期和文本消息进行格式设置Locale，以及如何使用模式创建自定义格式。
-   [使用文本](section050500.md)提供了以独立于区域的方式处理文本的技术。
-   [网络资源国际化](section050600.md)解释了如何为IDN提供国际化。
-   [国际化服务提供商](section050700.md)解释了如何启用与区域相关的数据和服务的插件。

##  目录

-   [介绍](section050100.md)
    -   [一个快速的例子](section050101.md)
        -   [国际化之前](section050101/0100.md)
        -   [国际化之后](section050101/0200.md)
        -   [运行示例程序](section050101/0300.md)
        -   [示例程序的国际化](section050101/0400.md)
    -   [清单](section050102.md)
-   [设置区域设置](section050200.md)
    -   [创建一个语言环境](section050201.md)
    -   [BCP 47扩展](section050202.md)
    -   [识别可用的语言环境](section050203.md)
    -   [语言标记过滤和查找](section050204.md)
    -   [Locale的范围](section050205.md)
    -   [区域敏感服务SPI](section050206.md)
-   [隔离特定于区域的数据](section050300.md)
    -   [关于ResourceBundle类](section050301.md)
    -   [准备使用ResourceBundle](section050302.md)
    -   [使用属性文件备份ResourceBundle](section050303.md)
    -   [使用ListResourceBundle](section050304.md)
    -   [定制资源包加载](section050305.md)
-   [格式化](section050400.md)
    -   [数字和货币](section050401.md)
        -   [使用预定义的格式](section050401/0100.md)
        -   [自定义格式](section050401/0200.md)
    -   [日期和时间](section050402.md)
        -   [使用预定义的格式](section050402/0100.md)
        -   [自定义格式](section050402/0200.md)
        -   [更改日期格式符号](section050402/0300.md)
    -   [消息](section050403.md)
        -   [处理复合消息](section050403/0100.md)
        -   [处理复数](section050403/0200.md)
-   [使用文本](section050500.md)
    -   [检查字符属性](section050501.md)
    -   [比较字符串](section050502.md)
        -   [执行区域独立比较](section050502/0100.md)
        -   [自定义整理规则](section050502/0200.md)
        -   [提高整理性能](section050502/0300.md)
    -   [统一](section050503.md)
        -   [术语](section050503/0100.md)
        -   [作为替代者的补充字符](section050503/0200.md)
        -   [字符和字符串API](section050503/0300.md)
        -   [样例用法](section050503/0400.md)
        -   [设计注意事项](section050503/0500.md)
        -   [更多信息](section050503/0600.md)
    -   [检测文本边界](section050504.md)
        -   [关于BreakIterator类](section050504/0100.md)
        -   [人物边界](section050504/0200.md)
        -   [单词边界](section050504/0300.md)
        -   [句子边界](section050504/0400.md)
        -   [线边界](section050504/0500.md)
    -   [将拉丁数字转换为其他Unicode数字](section050505.md)
    -   [转换非Unicode文本](section050506.md)
        -   [字节编码和字符串](section050506/0100.md)
        -   [字符和字节流](section050506/0200.md)
    -   [规范化文本](section050507.md)
    -   [使用JTextComponent类处理双向文本](section050508.md)
-   [网络资源的国际化](section050600.md)
    -   [国际化域名](section050601.md)
-   [国际化服务提供商](section050700.md)
    -   [安装自定义资源包作为扩展](section050701.md)


