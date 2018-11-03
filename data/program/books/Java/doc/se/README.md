#   [Java SE](https://docs.oracle.com/javase/8/docs/technotes/guides/index.html)

-   版本：v8u101

通用的高级Java编程语言是一个功能强大的软件平台。Java平台的每个完整实现都会为您提供以下功能：
-   开发工具：开发工具提供编译，运行，监视，调试和记录应用程序所需的一切。作为一名新开发人员，您将使用的主要工具是javac编译器，java启动器和javadoc文档工具。
-   应用程序编程接口（API）：该API提供了Java编程语言的核心功能。它提供了大量有用的类，可以在您自己的应用程序中使用。它涵盖了从基本对象到网络和安全，到XML生成和数据库访问等等的所有内容。核心API非常大
-   部署技术：JDK软件提供标准机制，例如用于将应用程序部署到最终用户的Java Web Start软件和Java Plug-In软件。
-   用户界面工具包：JavaFX，Swing和Java 2D工具包使创建复杂的图形用户界面（GUI）成为可能。
-   集成库：Java IDL API，JDBC API，Java命名和目录接口（JNDI）API，Java RMI和基于因特网ORB间协议技术的Java远程方法调用（Java RMI-IIOP技术）等集成库支持数据库访问和远程对象的操纵。


----
##  概念图

![2167990.jpg](images/2167990.jpg)

----

##  概念图简介

-   Java Development Kit（JDK） 

JDK是JRE的超集，包含JRE中的所有内容，以及用于开发小应用程序和应用程序所需的编译器和调试器等工具。上面的 概念图说明了Java SE平台中的所有组件技术以及它们如何组合在一起。

-   Java SE API 

Java SE应用程序编程接口（API）定义了applet或应用程序可以向编译的Java SE类库提供请求并使用其可用功能的方式。（Java SE类库也是Java SE平台的一部分。）

Java SE API由核心技术，桌面（或客户端）技术和其他技术组成。

核心组件为在数据库访问，安全性，远程方法调用（RMI）和通信等关键领域编写功能强大的企业级程序提供了基本功能。

桌面组件添加了全面的功能来帮助构建提供丰富用户体验的应用程序？部署产品（如Java Plug-in），组件建模API（如JavaBeans）和图形用户界面。
其他组件完善了功能。

-   Java虚拟机 

Java虚拟机负责Java SE平台的硬件和操作系统的独立性，编译代码的小尺寸（字节码），和平台安全性。

-   Java平台工具 

Java SE平台与一系列工具协同工作，包括集成开发环境（IDE），性能和测试工具以及性能监控工具。

----

##  JRE和JDK

Oracle在Java™平台标准版（Java™SE）系列中提供两种主要软件产品：

1.  Java SE运行时环境（JRE）

JRE提供了运行用Java编程语言编写的applet和应用程序所需的库，Java虚拟机和其他组件。此运行时环境可以与应用程序一起重新分发，使其可以独立运行。

2.  Java SE开发工具包（JDK）

JDK包含JRE plus命令行开发工具，如编译器和调试器，这些工具对开发 applet和应用程序是必需的或有用的

-----

##  Java SE API

Java编程语言是一种通用的，并发的，强类型的，基于类的面向对象语言。它通常编译为Java虚拟机规范中定义的字节码指令集和二进制格式

### 基础库

为Java平台提供基本功能和基本功能的类和接口

-   [Lang和Util包](guides/lang/README.md)

提供基本的Object和Class 类，基本类型的包装类，基本的数学类等等。

-   [数学](guides/math/README.md)

数学功能包括浮点库和任意精度数学。

-   [监测和管理](guides/management/README.md)

Java平台的全面监控和管理支持，包括用于Java虚拟机的Monitoring and Management API，用于日志工具的监控和管理API，jconsole和其他监控实用程序，开箱即用的监控和管理，Java Management Extensions（JMX）和Oracle的平台扩展。

-   [包版本识别](guides/versioning/README.md)

软件包版本控制功能支持软件包级版本控制，以便应用程序和applet可以在运行时识别特定Java运行时环境，VM和类软件包的版本。

-   [反射对象](api/lang-ref/README.md)

引用对象支持与垃圾收集器进行有限程度的交互。程序可以使用引用对象来维护对某个其他对象的引用，使得后者的对象仍然可以被收集器收回。程序还可以安排在收集器确定给定对象的可达性已经改变之后一段时间被通知。因此，引用对象可用于构建简单缓存以及内存不足时刷新的缓存，用于实现不妨碍其键（或值）被回收的映射，以及更灵活地安排事前清理操作比Java最终化机制可能的方式。

-   [反射](guides/reflection/README.md)

反射使Java代码可以发现有关已加载类的字段，方法和构造函数的信息，并且可以在安全限制内使用反射字段，方法和构造函数在对象上对其基础对象进行操作。该API适用于需要访问目标对象的公共成员（基于其运行时类）或由给定类声明的成员的应用程序。程序可以禁止默认的反射访问控制。

-   [集合框架](guides/collections/README.md)

集合是表示一组对象中的对象。集合框架是用于表示集合的统一体系结构，允许独立于其表示的细节来操纵集合。它减少了编程工作，同时提高了性能 它允许不相关API之间的互操作性，减少设计和学习新API的工作量，并促进软件重用。有

-   [并发工具](guides/concurrency/README.md)

Concurrency Utilities包提供了一个强大的可扩展的高性能线程实用程序框架，如线程池和阻塞队列。这个包使程序员免去了手动创建这些实用程序的需要，这与集合框架为数据结构所做的几乎相同。另外，这些软件包为高级并发编程提供了低级原语。

-   [Java归档（JAR）文件](guides/jar/README.md)

JAR（Java归档）是一种独立于平台的文件格式，可将多个文件合并为一个文件。多个Java小应用程序及其必需的组件（.class文件，图像和声音）可以捆绑到一个JAR文件中，然后在单个HTTP事务中下载到浏览器中，从而大大提高了下载速度。JAR格式还支持压缩，这可以减小文件大小，进一步缩短下载时间。此外，小程序作者可以对JAR文件中的单个条目进行数字签名，以验证其来源。它是完全可扩展的。

-   [Logging](guides/logging/README.md)

Logging API通过生成适合最终用户，系统管理员，现场服务工程师和软件开发团队分析的日志报告，为客户现场的软件维护和维护提供便利。Logging API捕获应用程序或平台中的安全失败，配置错误，性能瓶颈和/或错误等信息。有关更多信息，请参阅日志记录文档。

-   [Preferences](guides/preferences/README.md)

Preferences API为应用程序提供了一种存储和检索用户和系统首选项和配置数据的方法。数据永久存储在依赖于实现的后台存储中。有两个独立的偏好节点树，一个用于用户偏好，一个用于系统偏好

### 其他基本包

-   [I/O](guides/io/README.md)

在java.io和java.nio包管理应用程序的I / O提供了丰富的API集。该功能包括文件和设备I / O，对象序列化，缓冲区管理和字符集支持。此外，这些API支持可扩展服务器的功能，包括多路复用，非阻塞I / O，内存映射和文件锁定。

-   [对象序列化](guides/serialization/README.md)

对象序列化扩展了核心Java输入/输出类，并支持对象。对象序列化支持对象的编码和从它们到达的对象编码成字节流; 它支持从流中补充重构对象图。序列化用于轻量级持久性和通过套接字或远程方法调用（RMI）进行通信。

-   [Networking](guides/net/README.md)

提供网络功能类，包括寻址，使用URL和URI的类，连接服务器的套接字类，网络安全功能等

-   [安全](guides/security/README.md)

用于安全相关功能的API，如可配置的访问控制，数字签名，身份验证和授权，加密，安全的Internet通信等。

-   [国际化](guides/intl/README.md)

支持开发国际化应用程序的API。国际化是设计一个应用程序的过程，以便它可以适应各种语言和地区而无需改变工程。

-   [JavaBeans™组件API](guides/beans/README.md)

包含与开发bean相关的类 - 基于JavaBeans™体系结构的组件，可以作为开发应用程序的一部分拼凑在一起。

-   [Java管理扩展（JMX）](guides/jmx/README.md)

Java管理扩展（JMX）API是用于管理和监视资源（如应用程序，设备，服务和Java虚拟机）的标准API。典型用途包括咨询和更改应用程序配置，累积有关应用程序行为的统计信息，以及通知状态更改和错误条件。JMX API包含远程访问，因此远程管理程序可以与正在运行的应用程序交互以达到这些目的。

-   [XML（JAXP）](guides/xml/README.md)

Java平台提供了一套丰富的API来处理XML文档和数据

-   [Java本地接口（JNI）](guides/jni/README.md)

Java本地接口（JNI）是用于编写Java本机方法并将Java虚拟机嵌入本机应用程序的标准编程接口。主要目标是跨给定平台上所有Java虚拟机实现的本地方法库的二进制兼容性。


### 集成库

-   [Java数据库连接（JDBC）API](guides/jdbc/README.md)

JDBC™API提供了来自Java编程语言的通用数据访问。使用JDBC 3.0 API，开发人员可编写应用程序，从而可以访问几乎任何数据源，从关系数据库到电子表格和平面文件。JDBC技术还提供了可以构建工具和备用接口的通用基础。

-   [远程方法调用（RMI）](guides/rmi/README.md)

远程方法调用（RMI）通过提供用Java编程语言编写的程序之间的远程通信来支持分布式应用程序的开发。RMI使运行在一个Java虚拟机中的对象可以调用另一个Java VM中运行的对象上的方法，该Java VM可能位于不同的主机上。

-   [Java IDL（CORBA）](guides/idl/README.md)

Java IDL技术为Java平台增加了CORBA（公共对象请求代理体系结构）功能，提供基于标准的互操作性和连接性。Java IDL使分布式启用Web的Java应用程序能够使用对象管理组定义的行业标准IDL（对象管理组接口定义语言）和IIOP（Internet Inter-ORB协议）透明地调用远程网络服务上的操作。运行时组件包括使用IIOP通信的分布式计算的Java ORB。

-   [RMI-IIOP](guides/rmi-iiop/README.md)

互联网间ORB协议技术的Java远程方法调用RMI编程模型支持通过RMI API编程CORBA服务器和应用程序。您可以选择使用Java远程方法协议（JRMP）作为传输工具在Java编程语言中完全工作，或使用Internet InterORB协议（IIOP）与其他符合CORBA的编程语言一起工作。您可以使用rmic编译器生成将应用程序通过Internet InterORB协议（IIOP）连接到使用任何CORBA兼容语言编写的应用程序所需的代码。要使用其他语言的CORBA应用程序，可以使用rmic编译器和-idl选项从Java编程语言接口生成IDL。要生成IIOP存根和绑定类，请使用带-i选项的rmic编译器。

-   [Java命名和目录接口（JNDI）API](guides/jndi/README.md)

Java命名和目录接口（JNDI）为用Java编程语言编写的应用程序提供命名和目录功能。它旨在独立于任何特定的命名或目录服务实现。因此，各种各样的服务 - 新兴，新兴和已经部署的服务 - 可以通过一种共同的方式访问。JNDI体系结构由一个API和一个SPI（服务提供者接口）组成。Java应用程序使用此API来访问各种命名和目录服务。SPI支持透明地插入各种命名和目录服务，从而允许使用JNDI API的Java应用程序访问其服务

### 工具规格

-   [调试器架构](guides/jpda/README.md)

调试器在开发环境中使用的体系结构和规范。

-   [VM工具接口](guides/jvmti/README.md)

Java虚拟机工具接口（JVM TI）是一种用于检查状态和控制JVM中运行的应用程序执行的规范。Java虚拟机概要分析程序接口（JVMPI）已被弃用。

-   [Javadoc工具](guides/javadoc/README.md)

Javadoc是一个解析声明和文档注释源文件的工具，用于生成一组描述程序元素的HTML页面。Doclet API为客户端提供了一种检查程序和库的源级结构的机制，包括源中嵌入的Javadoc注释。doclet可以使用此API生成文档。

-   [动态附加](guides/attach/README.md)

com.sun.tools.attach包中包含Java平台的Oracle扩展，允许应用程序连接到正在运行的Java虚拟机。完成附加后，可以在目标虚拟机中启动工具代理。

-   JConsole API

com.sun.tools.jconsole包中包含Java平台的Oracle扩展，它提供了访问JConsole的编程接口。

-   [JDK工具和实用程序](guides/tools/README.md)

JDK中包含的工具和实用程序的文档。涵盖了基本的工具（javac的，JAVA，javadoc的，贴切，appletviewer中，罐子，加多宝，JAVAH，javap的，extcheck），安全工具，国际化的工具，RMI工具，IDL和RMI-IIOP工具，部署工具，Java插件工具，和Java Web Start工具，监视和管理工具以及故障排除工具。


### 用户界面库

-   输入法框架

输入法框架支持文本编辑组件和输入法在输入文本时进行协作。输入法是软件组件，可让用户以简单的键盘输入方式输入文本。它们通常用于使用数千个不同的字符输入日文，中文或韩文 - 在键盘数量少得多的键盘上。但是，该框架还支持其他语言的输入法和使用完全不同的输入机制，如手写或语音识别。

-   无障碍

借助Java Accessibility API，开发人员可以轻松创建可供残疾人访问的Java应用程序。可访问的Java应用程序与辅助技术（如屏幕阅读器，语音识别系统和可刷新的盲文显示器）兼容。

-   打印服务

Java™打印服务API允许在所有Java平台上进行打印，包括需要小尺寸的平台，如Java ME配置文件。

-   声音

Java平台包括一个强大的API，用于捕获，处理和回放音频和MIDI（乐器数字接口）数据。该API由高效的声音引擎支持，可确保平台的高品质音频混合和MIDI合成功能

-   拖放数据传输

通过拖放可以在Java编程语言和本地应用程序之间，在Java编程语言应用程序之间以及在单个Java编程语言应用程序中进行数据传输。有关更多信息，请参阅拖放式传输。

-   图像I / O

Java Image I / O API提供可插入式架构，用于处理存储在文件中并通过网络访问的图像。该API为添加特定于格式的插件提供了一个框架。Java Image I / O包含几种常用格式的插件，但第三方可以使用此API创建自己的插件来处理特殊格式。欲了解更多信息，请参阅图像I / O。

-   Java 2D™图形和图像

Java 2D™API是用于高级2D图形和图像的一组类。它将线条艺术，文字和图像融入单一综合模型中。该API为图像合成和Alpha通道图像提供了广泛的支持，一组类提供准确的色彩空间定义和转换，以及丰富的面向显示的成像操作。有关更多信息，请参阅Java 2D文档。

-   AWT

Java™平台的抽象窗口工具包（AWT）提供了用于构建用户界面组件（如菜单，按钮，文本字段，对话框，复选框）以及用于处理通过这些组件的用户输入的API。此外，AWT允许呈现简单的形状，如椭圆和多边形，并使开发人员能够控制其应用程序使用的用户界面布局和字体。有关更多信息，请参阅 AWT文档。

-   Swing

Swing API还提供用于用户界面的图形组件（GUI）。Swing API是用Java编程语言编写的，而不依赖于特定于底层操作系统提供的GUI工具的代码。这允许Swing GUI组件具有可在应用程序运行时切换的“可插拔”外观。有关更多信息，请参阅Java SE Swing文档。

-   JavaFX

Java SE 7 Update 2及更高版本包含JavaFX SDK。JavaFX平台是Java客户端平台的发展，旨在使应用程序开发人员能够轻松创建和部署在多个平台上保持一致的富Internet应用程序（RIA）


----

