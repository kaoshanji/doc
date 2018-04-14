#   用于XML处理的Java API（JAXP）

`用于XML处理的Java API（JAXP）`跟踪通过JAXP应用程序的示例介绍Java API for XML Processing（JAXP）1.4技术。

在阅读本教程之前

要充分利用Java API for XML处理（JAXP）教程中的信息，您应该了解以下技术：
-   Java编程语言及其开发环境。
-   可扩展标记语言（XML）
-   由万维网联盟（W3C）DOM工作组定义的文档对象模型（DOM）。
-   简单的XML API（SAX），由XML-DEV邮件列表成员合作开发。
-   假定一些DOM和SAX的先前知识。本教程中仅详细研究了特定于JAXP API的代码。

-   [JAXP简介](section090100.md)简要介绍了JAXP技术，包括其目的和主要特性。
-   [简单的XML API](section090200.md)介绍了JAXP技术中使用的一种概念，简单API用于XML（SAX）：何时使用SAX，如何解析XML文件，如何实现SAX验证，如何运行SAX解析器以及如何处理词汇事件。提供了更多信息的链接。
-   [文档对象模型](section090300.md)引入了文档对象模型（DOM）所使用的树结构，并向您展示了如何使用DOM函数来创建节点，删除节点，更改节点内容以及遍历节点层次结构。
-   [可扩展样式表语言转换](section090400.md)包含有关如何将文档对象模型编写为XML文件以及如何从任意数据文件生成DOM以将其转换为XML的信息。
-   [XML流API](section090500.md)着重于基于流技术的Java技术，事件驱动，拉解析API来读写XML文档。StAX使您能够创建快速，相对易于编程且占用内存少的双向XML解析器。
-   [JAXP 1.5和新属性](section090600.md)引入了已添加到7u40和JDK8中的属性。
-   [处理限制](section090700.md)讨论JAXP实施限制，包括在7u45中添加的三个限制。

##  目录

-   [JAXP简介](section090100.md)
    -   [软件包概述](section090101.md)
    -   [简单的API用于XML API](section090102.md)
    -   [文档对象模型API](section090103.md)
    -   [可扩展样式表语言转换API](section090104.md)
    -   [流API用于XML API](section090105.md)
    -   [查找JAXP示例程序](section090106.md)
    -   [你从这里去哪里？](section090107.md)
-   [用于XML的简单API](section090200.md)
    -   [何时使用SAX](section090201.md)
    -   [使用SAX解析XML文件](section090202.md)
    -   [实施SAX验证](section090203.md)
    -   [处理词汇事件](section090204.md)
    -   [使用DTDHandler和EntityResolver](section090205.md)
    -   [更多信息](section090206.md)
-   [文档对象模型](section090300.md)
    -   [何时使用DOM](section090301.md)
    -   [将XML数据读入DOM](section090302.md)
    -   [使用XML模式进行验证](section090303.md)
    -   [更多信息](section090304.md)
-   [可扩展样式表语言转换](section090400.md)
    -   [介绍XSL，XSLT和XPath](section090401.md)
    -   [XPath如何工作](section090402.md)
    -   [写出一个DOM作为一个XML文件](section090403.md)
    -   [从任意数据结构生成XML](section090404.md)
    -   [使用XSLT转换XML数据](section090405.md)
-   [流媒体API的XML](section090500.md)
    -   [为什么选择StAX？](section090501.md)
    -   [StAX API](section090502.md)
    -   [使用StAX](section090503.md)
    -   [Oracle的流式XML解析器实现](section090504.md)
    -   [示例代码](section090505.md)
    -   [更多信息](section090506.md)
-   [JAXP 1.5和新的属性](section090600.md)
    -   [背景](section090601.md)
    -   [外部资源](section090602.md)
    -   [新的属性](section090603.md)
    -   [范围和顺序](section090604.md)
    -   [与SecurityManager的关系](section090605.md)
    -   [JDK中的属性设置](section090606.md)
    -   [使用属性](section090607.md)
    -   [错误处理](section090608.md)
    -   [StAX](section090609.md)
    -   [结论](section090610.md)
    -   [参考](section090611.md)
-   [处理限制](section090700.md)
    -   [处理限制定义](section090701.md)
    -   [范围和顺序](section090702.md)
    -   [使用限制](section090703.md)
    -   [错误处理](section090704.md)
    -   [StAX的](section090705.md)
    -   [样品](section090706.md)

