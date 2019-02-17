#   [Java IDL（CORBA）](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/index.html)

Java IDL技术将Java（平台对象请求代理体系结构）功能添加到Java平台，提供基于标准的互操作性和连接性。Java IDL使分布式Web支持的Java应用程序能够使用对象管理组定义的行业标准IDL（对象管理组接口定义语言）和IIOP（Internet Inter-ORB协议）透明地调用远程网络服务上的操作。运行时组件包括用于使用IIOP通信的分布式计算的Java ORB。

----
##  概观
-   [CORBA和Java编程语言](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/corba.html)
-   [分布式应用概念](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlDistApp.html)
-   [词汇表](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlGlossary.html)
-   [POA - 便携式对象适配器](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/POA.html)
-   [便携式拦截器  高级主题](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/PI.html)
-   [INS - 可互操作的命名服务](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/INStutorial.html)

----

##  API规范
-   [package org.omg.CORBA](https://docs.oracle.com/javase/8/docs/api/org/omg/CORBA/package-summary.html) - 提供OMG CORBA API到Java [tm]编程语言的映射
-   [package org.omg.CosNaming](https://docs.oracle.com/javase/8/docs/api/org/omg/CosNaming/package-summary.html) - 提供Java IDL的命名服务
-   [package org.omg.PortableServer](https://docs.oracle.com/javase/8/docs/api/org/omg/PortableServer/package-summary.html) - 提供类和接口，使应用程序的服务器端可以跨多个供应商ORB移植
-   [package org.omg.PortableInterceptor](https://docs.oracle.com/javase/8/docs/api/org/omg/PortableInterceptor/package-summary.html) - 提供一种注册ORB挂钩的机制，ORB服务可以通过它来拦截ORB的正常执行流程
-   [package org.omg.DynamicAny](https://docs.oracle.com/javase/8/docs/api/org/omg/DynamicAny/package-summary.html) - 提供类和接口以启用任何值动态解释（遍历）并通过DynAny对象构造
-   [org.omg.CORBA.ORB](https://docs.oracle.com/javase/8/docs/api/org/omg/CORBA/ORB.html) - 为CORBA对象请求代理功能提供API

----

##  教程和程序员指南

大多数教程都是基本分布式“Hello World”应用程序的变体。

### 入门级教程

以下文档提供了有关创建使用Java IDL的应用程序的介绍级信息。全部使用POA服务器端模型。不同之处在于服务器实现。

为了更好地理解材料，请按照此处提供的顺序逐步完成示例。

-   使用Java IDL技术的[Hello World”示例](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/GShome.html)
-   带有瞬态服务器的[Hello World”示例](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample.html)（与上例相同的代码，描述性较少的材料）
-   带有持久服务器的[Hello World”示例](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample2.html)

可以使用JavaSE创建其他服务器端模型。如果您想使用其他服务器端模型，请参阅这些教程。这两个教程都使用瞬态服务器实现。

-   带有POA-Tie（委派）服务器端模型的[“Hello World”示例](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlTieServer.html)
-   带有ImplBase（继承）服务器端模型的[“Hello World”示例](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlImplBaseServer.html)

### 中级教程

本节中列出的教程适用于了解入门级教程中材料的开发人员，并且正在寻找更复杂的材料。

-   [使用互操作命名服务](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/INStutorial.html)
-   [使用Java SE进行CORBA编程：编写瞬态和永久性服务器](https://www.oracle.com/technetwork/articles/javase/corba-137639.html)

### 高级教程

这些教程适用于有经验的开发人员。简化了描述性材料，对示例代码进行了评论，以便更好地理解材料。

-   [便携式拦截器](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/PI.html)
-   [使用Servant Activators](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/servantactivator.html)
-   [使用Servant Locators](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/servantlocators.html)
-   [使用适配器激活器](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/adapteractivator.html)

### 编程指南
-   [例外](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExceptions.html)
-   [初始化](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlInitialization.html)
-   [命名服务](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlNaming.html)
-   [动态骨架接口](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlDSI.html)
-   [将IDL映射到Java编程语言](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/mapping/jidlMapping.html)

### 其他样本申请
-   [Hello World示例代码](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlSampleCode.html) 提供了[POA服务器端模型教程中使用的所有已创建和生成文件的代码](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample.html)
-   [示例：可互操作的命名服务](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/INStutorial.html)
-   [示例：回调对象](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlExample3.html)

----

##  工具
-   IDL-to-Java编译器，idlj（[Solaris，Linux或Mac OS X](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/idlj.html)或[Windows](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/idlj.html)）
-   orbd（[Solaris，Linux或Mac OS X](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/orbd.html)或[Windows） - 包含Bootstrap服务，瞬态命名服务，持久名服务和服务器管理器的守护程序进程](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/orbd.html)
-   servertool（[Solaris，Linux或Mac OS X](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/servertool.html)或[Windows](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/servertool.html)） - 应用程序员注册，取消注册，启动和关闭服务器的易用界面。
-   tnameserv（[Solaris，Linux或Mac OS X](https://docs.oracle.com/javase/8/docs/technotes/tools/unix/tnameserv.html)或[Windows](https://docs.oracle.com/javase/8/docs/technotes/tools/windows/tnameserv.html)） - Transient Java IDL命名服务（提供向后兼容性）

----

##  更多

该[OMG](https://www.omg.org/)是所有CORBA和IIOP相关信息的官方消息。有关更多信息，请[参阅CORBA 2.3.1规范](https://www.omg.org/cgi-bin/doc?formal/99-10-07)。

有关在此Java平台版本中实现哪些OMG规范的更多信息，请参阅[合规性](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/compliance.html)文档。

有关此版本的Java IDL / RMI-IIOP技术中的[产品限制的信息](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/limitations.html)，请参阅[Java IDL产品限制](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/limitations.html)。

如有问题，请查看[Java IDL FAQ](https://docs.oracle.com/javase/8/docs/technotes/guides/idl/jidlFAQ.html)。





