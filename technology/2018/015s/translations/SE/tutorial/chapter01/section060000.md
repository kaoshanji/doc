#   部署

Java富Internet应用程序（RIA）是具有类似于桌面应用程序的特性的应用程序，但通过Internet部署。Java RIA可以开发和部署为Java小程序或Java Web Start应用程序。
-   Applets - Java applet在浏览器的上下文中运行。Java Plug-in软件控制Java小程序的执行和生命周期。
-   Java Web Start应用程序 - 首次通过浏览器启动Java Web Start应用程序。他们可能随后从桌面快捷方式启动。一旦下载了Java Web Start应用程序并且其安全证书已被用户接受，它的行为几乎就像是一个独立的应用程序。

##  基于组件的RIA架构

过去，决定是将Java富Internet应用程序作为applet部署在浏览器内还是作为Java Web Start应用程序部署在浏览器之外，这些决定可能会对应用程序的设计产生重大影响。使用最新的Java Plug-in，这个决定已经大大简化了。

传统上，应用程序构建他们的用户接口，包括顶层Frame，在main方法。这种编程风格阻止了在浏览器中轻松重新部署应用程序，因为它假定应用程序创建它自己的应用程序Frame。当作为applet在浏览器中运行时，applet是应该保存应用程序用户界面的顶级容器。顶层Frame是不需要的。

在设计Java富Internet应用程序时使用基于组件的体系结构。尝试将其功能组织到一个或多个可以组合在一起的组件中。在此上下文中，术语“组件”指的是GUI元素，它是AWT Component类，Swing JComponent类或另一个子类的子类。例如，您可以拥有一个顶层JPanel，其中包含其他UI组件（如更多嵌套JPanel和文本字段，组合框等）。通过这样的设计，将核心功能部署为applet或Java Web Start应用程序变得相对容易。

要作为Java applet进行部署，只需要将核心功能包装在Appletor中，JApplet并根据需要添加浏览器特定的功能。要部署为Java Web Start应用程序，请将功能包装在一个JFrame。

##  在Java Applets和Java Web Start应用程序之间进行选择

在 富互联网应用程序决策指南包含详细的信息，帮助你决定是否要部署你的代码作为Java applet或Java Web Start应用程序。

##  自包含的应用程序替代方案

自包含应用程序提供了不需要浏览器的部署选项。用户在本地安装您的应用程序并运行它类似于本地应用程序 自包含的应用程序包括运行应用程序所需的JRE，因此用户始终拥有正确的JRE。

这条线索讨论了RIA和独立应用程序的开发和部署。请参阅 各种版本的客户端Java运行时环境（JRE）软件中引入的功能的新增功能。

-  [Java小程序](section060200.md)
    -   [小程序入门](section060201.md)
        -   [定义一个Applet子类](section060201/0100.md)
        -   [里程碑的方法](section060201/0200.md)
        -   [一个Applet的生命周期](section060201/0300.md)
        -   [Applet的执行环境](section060201/0400.md)
        -   [开发一个Applet](section060201/0500.md)
        -   [部署一个Applet](section060201/0600.md)
            -   [使用Applet标签进行部署](section060201/0700.md)
    -   [用小苹果做更多](section060202.md)
        -   [查找和加载数据文件](section060202/0100.md)
        -   [定义和使用Applet参数](section060202/0200.md)
        -   [显示短状态字符串](section060202/0300.md)
        -   [在浏览器中显示文档](section060202/0400.md)
        -   [从Applet调用JavaScript代码](section060202/0500.md)
        -   [从JavaScript代码调用Applet方法](section060202/0600.md)
        -   [使用事件处理程序处理初始化状态](section060202/0700.md)
        -   [处理Applet的Web页面的DOM](section060202/0800.md)
        -   [显示自定义加载进度指示器](section060202/0900.md)
        -   [将诊断写入标准输出和错误流](section060202/1000.md)
        -   [开发可拖动小程序](section060202/1100.md)
        -   [与其他小程序通信](section060202/1200.md)
        -   [使用服务器端应用程序](section060202/1300.md)
                -   [网络客户端小程序示例](section060202/1301.md)
        -   [Applets可以做什么和不可以做什么](section060202/1400.md)
    -   [解决常见的Applet问题](section060203.md)
    -   [问题和练习：小程序](section060204.md)
-  [Java Web Start](section060300.md)
    -   [开发Java Web Start应用程序](section060301.md)
        -   [检索资源](section060301/0101.md)
    -   [部署Java Web Start应用程序](section060302.md)
        -   [设置Web服务器](section060302/0101.md)
    -   [显示自定义加载进度指示器](section060303.md)
    -   [运行Java Web Start应用程序](section060304.md)
    -   [Java Web Start和安全性](section060305.md)
    -   [常见的Java Web Start问题](section060306.md)
    -   [问题和练习：Java Web Start](section060307.md)
-  [使用Java Rich Internet应用程序做更多](section060400.md)
    -   [设置可信参数和安全属性](section060401.md)
        -   [系统属性](section060401/0101.md)
    -   [JNLP API](section060402.md)
        -   [使用JNLP API访问客户端](section060402/0100.md)
    -   [饼干](section060403.md)
        -   [访问Cookie](section060403/0100.md)
    -   [定制加载体验](section060404.md)
    -   [富Internet应用程序中的安全性](section060405.md)
    -   [确保富互联网应用程序的指南](section060406.md)
    -   [问题和练习：使用富互联网应用程序做更多](section060407.md)
-  [部署深入](section060500.md)
    -   [用户接受RIA](section060501.md)
    -   [部署工具包](section060502.md)
        -   [部署一个Applet](section060502/0100.md)
            -   [自定义加载屏幕](section060502/0101.md)
            -   [在Applet标签中嵌入JNLP文件](section060502/0102.md)
        -   [部署Java Web Start应用程序](section060502/0200.md)
            -   [更改启动按钮](section060502/0201.md)
            -   [无需编码库部署](section060502/0202.md)
        -   [检查客户端JRE软件版本](section060502/0300.md)
    -   [Java网络启动协议](section060503.md)
        -   [JNLP文件的结构](section060503/0100.md)
    -   [部署最佳实践](section060504.md)
        -   [减少下载时间](section060504/0100.md)
        -   [避免不必要的更新检查](section060504/0200.md)
        -   [确保JRE软件的存在](section060504/0300.md)
    -   [问题和练习：部署深入](section060505.md)

-  [部署自包含的应用程序](section060600.md)
    -   [包装自备应用程序的先决条件](section060601.md)
    -   [转换现有的应用程序](section060602.md)
    -   [使用文件关联](section060603.md)
        -   [添加一个外部库](section060603/0100.md)
        -   [提供默认参数](section060603/0201.md)
        -   [为所有平台使用通用构建文件](section060603/0300.md)
    -   [使用多个入口点](section060604.md)
    -   [问题和练习：独立应用程序](section060605.md)

-  [打包JAR文件中的程序](section060700.md)
    -   [使用JAR文件：基础](section060701.md)
        -   [创建一个JAR文件](section060701/0100.md)
        -   [查看JAR文件的内容](section060701/0200.md)
        -   [提取JAR文件的内容](section060701/0300.md)
        -   [更新JAR文件](section060701/0400.md)
        -   [运行JAR打包软件](section060701/0500.md)
    -   [使用清单文件：基础知识](section060702.md)
        -   [了解默认清单](section060702/0200.md)
        -   [修改清单文件](section060702/0300.md)
        -   [设置应用程序的入口点](section060702/0400.md)
        -   [将类添加到JAR文件的类路径](section060702/0500.md)
        -   [设置包版本信息](section060702/0600.md)
        -   [在JAR文件中密封包](section060702/0700.md)
        -   [用清单属性增强安全性](section060702/0800.md)
    -   [签名和验证JAR文件](section060703.md)
        -   [了解签名和验证](section060703/0100.md)
        -   [签署JAR文件](section060703/0200.md)
        -   [验证已签名的JAR文件](section060703/0300.md)
    -   [使用JAR相关的API](section060704.md)
        -   [JarClassLoader类](section060704/0100.md)
        -   [JarRunner类](section060704/0200.md)
    -   [问题和练习：JAR](section060705.md)
