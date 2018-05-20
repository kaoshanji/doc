#  关于Java技术

Java技术既是一种编程语言，也是一个平台。

## Java编程语言

Java编程语言是一种高级语言，可以用以下所有流行语来表征：
-   简单
-   面向对象
-   分散式
-   多线程
-   动态
-   建筑中立
-   手提
-   高性能
-   强大的
-   安全

在[Java语言环境中](http://www.oracle.com/technetwork/java/langenv-140151.html)，James Gosling和Henry McGilton编写了一份白皮书，解释了前面的每一个流行语 。

在Java编程语言中，所有源代码首先以纯文本文件编写，并以.java扩展名结尾。这些源文件然后.class由javac编译器编译成文件。一个.class文件不包含的代码是原产于你的处理器; 它代之以字节码 - Java虚拟机1（Java VM）的机器语言。然后，java启动程序工具将使用Java虚拟机的实例运行您的应用程序。

![getStarted-compiler.gif](image/getStarted-compiler.gif)
软件开发过程的概述

由于Java VM在许多不同的操作系统上都可用，因此相同的.class文件能够在Microsoft Windows，Solaris™操作系统（Solaris OS），Linux或Mac OS上运行。一些虚拟机（例如 [Java SE HotSpot概览](http://www.oracle.com/technetwork/java/javase/tech/index-jsp-136373.html)）在运行时执行其他步骤，以提高应用程序的性能。这包括各种任务，如查找性能瓶颈和重新编译（本地代码）经常使用的代码部分。

![helloWorld.gif](image/helloWorld.gif)

##  Java平台

一个平台是在程序运行的硬件或软件环境。我们已经提到了一些最流行的平台，如Microsoft Windows，Linux，Solaris OS和Mac OS。大多数平台可以被描述为操作系统和底层硬件的组合。Java平台不同于大多数其他平台，因为它是一个运行在其他基于硬件的平台之上的纯软件平台。

Java平台有两个组件：
-   在Java虚拟机
-   在Java应用程序编程接口（API）

您已经被引入Java虚拟机; 它是Java平台的基础，并被移植到各种基于硬件的平台上。

API是大量现成的软件组件，提供许多有用的功能。它被分组到相关类和接口的库中; 这些库被称为包。下一节， [Java技术可以做什么？](section010102.md)强调了API提供的一些功能。

![getStarted-jvm.gif](image/getStarted-jvm.gif)
API和Java虚拟机将程序与底层硬件隔离开来

作为一个独立于平台的环境，Java平台可能比本地代码慢一点。然而，编译器和虚拟机技术的进步使性能接近本机代码的性能，而不会威胁到可移植性。

术语“Java虚拟机”和“JVM”是指用于Java平台的虚拟机。


