#   [用于XML处理的Java API（JAXP）](https://docs.oracle.com/javase/tutorial/jaxp/index.html)

`用于XML处理的Java API（JAXP）`跟踪通过JAXP应用程序的示例介绍Java API for XML Processing（JAXP）1.4技术。

在阅读本教程之前

要充分利用Java API for XML处理（JAXP）教程中的信息，您应该了解以下技术：
-   Java编程语言及其开发环境。
-   可扩展标记语言（XML）
-   由万维网联盟（W3C）DOM工作组定义的文档对象模型（DOM）。
-   简单的XML API（SAX），由XML-DEV邮件列表成员合作开发。
-   假定一些DOM和SAX的先前知识。本教程中仅详细研究了特定于JAXP API的代码。


----
##  [JAXP简介](intro.md)

简要介绍了JAXP技术，包括其目的和主要特性。

-   软件包概述
-   简单的API用于XML API
-   文档对象模型API
-   可扩展样式表语言转换API
-   流API用于XML API
-   查找JAXP示例程序
-   你从这里去哪里？

----
##  [用于XML的简单API](sax.md)

介绍了JAXP技术中使用的一种概念，简单API用于XML（SAX）：何时使用SAX，如何解析XML文件，如何实现SAX验证，如何运行SAX解析器以及如何处理词汇事件。提供了更多信息的链接。

-   何时使用SAX
-   使用SAX解析XML文件
-   实施SAX验证
-   处理词汇事件
-   使用DTDHandler和EntityResolver
-   更多信息

----
##  [文档对象模型](dom.md)

引入了文档对象模型（DOM）所使用的树结构，并向您展示了如何使用DOM函数来创建节点，删除节点，更改节点内容以及遍历节点层次结构。

-   何时使用DOM
-   将XML数据读入DOM
-   使用XML模式进行验证
-   更多信息

----
##  [可扩展样式表语言转换](xslt.md)

包含有关如何将文档对象模型编写为XML文件以及如何从任意数据文件生成DOM以将其转换为XML的信息。

-   介绍XSL，XSLT和XPath
-   XPath如何工作
-   写出一个DOM作为一个XML文件
-   从任意数据结构生成XML
-   使用XSLT转换XML数据

----
##  [流媒体API的XML](stax.md)

着重于基于流技术的Java技术，事件驱动，拉解析API来读写XML文档。StAX使您能够创建快速，相对易于编程且占用内存少的双向XML解析器。

-   为什么选择StAX？
-   StAX API
-   使用StAX
-   Oracle的流式XML解析器实现
-   示例代码
-   更多信息

----
##  [JAXP 1.5和新的属性](properties.md)

引入了已添加到7u40和JDK8中的属性。

-   背景
-   外部资源
-   新的属性
-   范围和顺序
-   与SecurityManager的关系
-   JDK中的属性设置
-   使用属性
-   错误处理
-   StAX
-   结论
-   参考

----
##  [处理限制](limits.md)

讨论JAXP实施限制，包括在7u45中添加的三个限制。

-   处理限制定义
-   范围和顺序
-   使用限制
-   错误处理
-   StAX的
-   样品

----
