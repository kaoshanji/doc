#   Java SE

Java™编程语言是一种通用的，并发的，强类型的，基于类的面向对象语言。它通常编译为Java虚拟机规范中定义的字节码指令集和二进制格式。

通用的高级Java编程语言是一个功能强大的软件平台。Java平台的每个完整实现都会为您提供以下功能：
-   开发工具：开发工具提供编译，运行，监视，调试和记录应用程序所需的一切。作为一名新开发人员，您将使用的主要工具是javac编译器，java启动器和javadoc文档工具。
-   应用程序编程接口（API）：该API提供了Java编程语言的核心功能。它提供了大量有用的类，可以在您自己的应用程序中使用。它涵盖了从基本对象到网络和安全，到XML生成和数据库访问等等的所有内容。核心API非常大
-   部署技术：JDK软件提供标准机制，例如用于将应用程序部署到最终用户的Java Web Start软件和Java Plug-In软件。
-   用户界面工具包：JavaFX，Swing和Java 2D工具包使创建复杂的图形用户界面（GUI）成为可能。
-   集成库：Java IDL API，JDBC API，Java命名和目录接口（JNDI）API，Java RMI和基于因特网ORB间协议技术的Java远程方法调用（Java RMI-IIOP技术）等集成库支持数据库访问和远程对象的操纵。

-----

##  概念图

![2167990.jpg](image/2167990.jpg)

----

##  [平台概述](section010000.md)

Java SE平台系列中有两个主要产品： `Java SE运行时环境（JRE）`和 `Java开发工具包（JDK）`

### Java运行时环境（JRE） 

Java运行时环境（JRE）提供库，Java虚拟机和其他组件来运行用Java编程语言编写的小程序和应用程序。另外，两个关键的部署技术是JRE的一部分： Java Plug-in，它使小程序可以在流行的浏览器中运行; 以及 通过网络部署独立应用程序的 Java Web Start。它也是Java 2 Platform，Enterprise Edition（J2EE）中用于企业软件开发和部署的技术的基础。JRE不包含用于开发小应用程序和应用程序的工具和实用程序，例如编译器或调试器。

### Java Development Kit（JDK） 

JDK是JRE的超集，包含JRE中的所有内容，以及用于开发小应用程序和应用程序所需的编译器和调试器等工具。上面的 概念图说明了Java SE平台中的所有组件技术以及它们如何组合在一起。

### Java SE API 

Java SE应用程序编程接口（API）定义了applet或应用程序可以向编译的Java SE类库提供请求并使用其可用功能的方式。（Java SE类库也是Java SE平台的一部分。）

Java SE API由核心技术，桌面（或客户端）技术和其他技术组成。

核心组件为在数据库访问，安全性，远程方法调用（RMI）和通信等关键领域编写功能强大的企业级程序提供了基本功能。
桌面组件添加了全面的功能来帮助构建提供丰富用户体验的应用程序？部署产品（如Java Plug-in），组件建模API（如JavaBeans）和图形用户界面。
其他组件完善了功能。

### Java虚拟机 

Java虚拟机负责Java SE平台的硬件和操作系统的独立性，编译代码的小尺寸（字节码），和平台安全性。

### Java平台工具 

Java SE平台与一系列工具协同工作，包括集成开发环境（IDE），性能和测试工具以及性能监控工具。


----

##  关于Java技术

-   [白皮书](section040000.md)
-   [语言规范](section030000.md)
-   [虚拟机](section020000.md)

### Java编程语言

Java编程语言是一种高级语言，可以用以下所有流行语来表征：
-   简单
-   面向对象
-   分布式
-   多线程
-   动态
-   架构中立
-   便捷
-   高性能
-   强大的
-   安全

在[Java语言环境中](section040000.md)，James Gosling和Henry McGilton编写了一份白皮书，解释了前面的每一个流行语 。

在Java编程语言中，所有源代码首先以纯文本文件编写，并以.java扩展名结尾。这些源文件然后.class由javac编译器编译成文件。一个.class文件不包含的代码是原产于你的处理器; 它代之以字节码 - Java虚拟机1（Java VM）的机器语言。然后，java启动程序工具将使用Java虚拟机的实例运行您的应用程序。

![getStarted-compiler.gif](image/getStarted-compiler.gif)
软件开发过程的概述

由于Java VM在许多不同的操作系统上都可用，因此相同的.class文件能够在Microsoft Windows，Solaris™操作系统（Solaris OS），Linux或Mac OS上运行。一些虚拟机（例如 [Java SE HotSpot概览](http://www.oracle.com/technetwork/java/javase/tech/index-jsp-136373.html)）在运行时执行其他步骤，以提高应用程序的性能。这包括各种任务，如查找性能瓶颈和重新编译（本地代码）经常使用的代码部分。

![helloWorld.gif](image/helloWorld.gif)

###  Java平台

一个平台是在程序运行的硬件或软件环境。我们已经提到了一些最流行的平台，如Microsoft Windows，Linux，Solaris OS和Mac OS。大多数平台可以被描述为操作系统和底层硬件的组合。Java平台不同于大多数其他平台，因为它是一个运行在其他基于硬件的平台之上的纯软件平台。

Java平台有两个组件：
-   在Java虚拟机
-   在Java应用程序编程接口（API）

您已经被引入Java虚拟机; 它是Java平台的基础，并被移植到各种基于硬件的平台上。

API是大量现成的软件组件，提供许多有用的功能。它被分组到相关类和接口的库中; 这些库被称为包。

![getStarted-jvm.gif](image/getStarted-jvm.gif)
API和Java虚拟机将程序与底层硬件隔离开来

作为一个独立于平台的环境，Java平台可能比本地代码慢一点。然而，编译器和虚拟机技术的进步使性能接近本机代码的性能，而不会威胁到可移植性。

术语“Java虚拟机”和“JVM”是指用于Java平台的虚拟机。


----

##  动手实践
-   搭建环境

----

##  源码解读

----