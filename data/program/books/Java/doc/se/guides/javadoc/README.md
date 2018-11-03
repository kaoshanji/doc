#   [Javadoc技术](https://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/index.html)

Javadoc是一个工具，它解析一组源文件中的声明和文档注释，并生成一组描述类，接口，构造函数，方法和字段的HTML页面。

您可以使用Javadoc doclet自定义Javadoc输出。doclet是使用Doclet API编写的程序，它指定了工具生成的输出的内容和格式。您可以编写doclet来生成任何类型的文本文件输出，例如HTML，SGML，XML，RTF和MIF。Oracle提供了用于生成HTML格式API文档的标准doclet。Doclet还可用于执行与生成API文档无关的特殊任务。

标记是一个程序，允许您创建和使用比使用该-tag 选项创建的自定义标记更灵活的自定义标记。doclet使用自定义标记来格式化和显示Javadoc标记中的文本。标记必须实现标记接口。

----

##  API规范

以下是与Javadocs相关的API：

-   [Doclet API](https://docs.oracle.com/javase/8/docs/jdk/api/javadoc/doclet/index.html) - com.sun.javadoc包中包含Doclet API。
-   [Taglet API](https://docs.oracle.com/javase/8/docs/jdk/api/javadoc/taglet/com/sun/tools/doclets/Taglet.html) - com.sun.tools.doclets.Taglet类包含Taglet API。
-   [Doctree API](https://docs.oracle.com/javase/8/docs/jdk/api/javac/tree/com/sun/source/doctree/package-summary.html) - 包 com.sun.source.doctree包含Doctree API。此API使您可以将Javadoc注释作为抽象语法树进行遍历。
-   [Javadoc Access API](https://docs.oracle.com/javase/8/docs/api/javax/tools/package-summary.html) - 包 javax.tools包含Javadoc Access API。此API使您可以直接从Java应用程序调用Javadoc工具，而无需执行新进程。

----

##  工具

以下页面列出了运行Javadoc工具的所有Javadoc标记和命令行选项，以及Solaris和Microsoft Windows操作系统的示例：

-   [Javadoc工具参考页面（Solaris，Linux或Mac OS X）](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/javadoc.html)
-   [Javadoc工具参考页面（Microsoft Windows）](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/javadoc.html)

----

##  指南
本节包含Javadoc API的教程和指南：

-   [Doclet概述](https://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/doclet/overview.html) - 对标准 doclet的介绍包括说明Doclet API的简单示例。
-   [运行标准Doclet](https://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/standard-doclet.html) - 此doclet生成默认的HTML格式的API文档。如果没有使用Javadoc -doclet选项指定其他doclet，则Javadoc使用标准doclet。
-   [过渡到5.0 Doclet API](https://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/doclet/transition-1.5docletapi.html) - 本文档提供了扩展旧doclet以支持5.0新语言功能的提示。
-   [Taglet概述](https://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/taglet/overview.html) - 对taglet的介绍包括说明Taglet API的简单示例。

----

##  更多

有关更多信息，请访问以下

-   [Javadoc常见问题解答](https://www.oracle.com/technetwork/java/javase/documentation/index-137483.html) - 查看错误的重要提示和解决方法。
-   [Javadoc论坛](https://community.oracle.com/community/groundbreakers/java/java_apis/javadoc_tool) - 与其他开发人员进行讨论。该论坛仅由Javadoc团队偶尔监控。

----
