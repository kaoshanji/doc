#   常见问题（及其解决方案）

##  编译器问题

### Microsoft Windows系统上的常见错误消息

```java
'javac' is not recognized as an internal or external command, operable program or batch file
```

如果您收到此错误，Windows无法找到编译器（javac）。

这是一种告诉Windows在哪里可以找到的方法javac。假设你安装了JDK C:\jdk1.8.0。在提示符下输入以下命令并按Enter键：

```java
C：\ jdk1.8.0 \ bin \ javac HelloWorldApp.java
```

如果您选择此选项，则每次编译或运行程序时都必须在命令javac和java命令之前C:\jdk1.8.0\bin\。要避免这种额外的输入，请参阅JDK 8安装说明中的更新PATH变量部分 。

```java
Class names, 'HelloWorldApp', are only accepted if annotation processing is explicitly requested
```

如果您收到此错误，则.java在编译程序时忘记包含后缀。请记住，该命令javac HelloWorldApp.java不是javac HelloWorldApp。

### UNIX系统上的常见错误消息

```java
javac: Command not found
```

如果您收到此错误，UNIX无法找到编译器，javac。

这是一种告诉UNIX在哪里可以找到的方法javac。假设你安装了JDK /usr/local/jdk1.8.0。在提示符下输入以下命令并按回车键：

```java
/usr/local/jdk1.8.0/javac HelloWorldApp.java
```

`注意`：如果您选择此选项，则每次编译或运行程序时，都必须在您的命令javac和java命令之前加上/usr/local/jdk1.8.0/。为了避免这种额外的输入，可以将这些信息添加到PATH变量中。这样做的步骤会因您当前运行的外壳而异。

```java
Class names, 'HelloWorldApp', are only accepted if annotation processing is explicitly requested
```

如果您收到此错误，则.java在编译程序时忘记包含后缀。请记住，该命令javac HelloWorldApp.java不是javac HelloWorldApp。

### 语法错误（所有平台）

如果您错误地输入了程序的一部分，编译器可能会发出语法错误。该消息通常显示错误的类型，检测到错误的行号，该行上的代码以及错误在代码中的位置。这是由于;在语句结尾处省略分号（）造成的错误：

```java
testing.java:14：`;' 预期。
System.out.println（“Input has”+ count +“chars。”）
                                                     ^
1错误
```

有时编译器无法猜测您的意图，并且如果错误级联在多行上，则会输出令人困惑的错误消息或多个错误消息。例如，下面的代码片段忽略;粗体行中的分号（）：

```java
while（System.in.read（）！= -1）
     count ++
System.out.println（“Input has”+ count +“chars。”）; 
```

处理此代码时，编译器会发出两条错误消息：

```java
testing.java:13：无效的类型表达式。
        算上++
                 ^
testing.java:14：声明无效。
    System.out.println（“Input has”+ count +“chars。”）;
                      ^
2错误
```

编译器发出两条错误消息，因为count++编译器的状态在处理之后表示它处于表达式的中间。没有分号，编译器无法知道该语句是否完整。

如果您看到任何编译器错误，那么您的程序没有成功编译，编译器也没有创建.class文件。仔细验证程序，修复您检测到的任何错误，然后重试。

### 语义错误

除了验证您的程序在语法上是否正确之外，编译器还会检查其他基本的正确性。例如，编译器会在您每次使用尚未初始化的变量时发出警告：

```java
testing.java:13：变量计数可能尚未初始化。
        算上++
        ^
testing.java:14：变量计数可能尚未初始化。
    System.out.println（“Input has”+ count +“chars。”）;
                                       ^
2错误
```

同样，你的程序没有成功编译，编译器也没有创建一个.class文件。修复错误并重试。

##  运行时问题

### Microsoft Windows系统上的错误消息

```java
Exception in thread "main" java.lang.NoClassDefFoundError: HelloWorldApp
```

如果您收到此错误，java找不到您的字节码文件HelloWorldApp.class。

其中一个地方java试图找到您的.class文件是您当前的目录。所以如果你的.class文件在C:\java，你应该改变你的当前目录。要更改目录，请在提示符下键入以下命令并按Enter键：

```java
cd c：\ java
```

提示符应该更改为C:\java>。如果输入dir的提示，你应该看到您.java和.class文件。现在java HelloWorldApp再次输入。

如果仍有问题，则可能需要更改CLASSPATH变量。要查看是否有必要，请尝试使用以下命令来打开类路径。

```
设置CLASSPATH =
```

现在java HelloWorldApp再次输入。如果程序现在可以工作，则必须更改CLASSPATH变量。要设置此变量，请参阅JDK 8安装说明中的 更新PATH变量部分。CLASSPATH变量的设置方式相同。

```java
Could not find or load main class HelloWorldApp.class
```

初学者程序员犯的一个常见错误是尝试在由编译器创建java的.class文件上运行启动器。例如，如果您尝试运行程序java HelloWorldApp.class而不是运行程序，则会出现此错误java HelloWorldApp。请记住，参数是您要使用的类的名称，而不是文件名。

```java
Exception in thread "main" java.lang.NoSuchMethodError: main
```

Java VM要求您使用它执行的类具有main开始执行应用程序的方法。 仔细看看“Hello World！” 应用程序详细讨论了该main方法。

### UNIX系统上的错误消息

```java
Exception in thread "main" java.lang.NoClassDefFoundError: HelloWorldApp
```

如果您收到此错误，java找不到您的字节码文件HelloWorldApp.class。

其中一个地方java试图找到您的字节码文件是您当前的目录。所以，例如，如果你的字节码文件在/home/jdoe/java，你应该改变你的当前目录。要更改目录，请在提示符下键入以下命令并按回车键：

```java
cd / home / jdoe / java
```

如果你pwd按提示进入，你应该看到/home/jdoe/java。如果输入ls的提示，你应该看到您.java和.class文件。现在java HelloWorldApp再次输入。

如果仍有问题，则可能需要更改CLASSPATH环境变量。要查看是否有必要，请尝试使用以下命令来打开类路径。

```java
取消设置CLASSPATH
```

现在java HelloWorldApp再次输入。如果程序现在可以工作，则必须按照上述PATH变量相同的方式更改CLASSPATH变量。

```java
Exception in thread "main" java.lang.NoClassDefFoundError: HelloWorldApp/class
```

初学者程序员犯的一个常见错误是尝试在由编译器创建java的.class文件上运行启动器。例如，如果您尝试运行程序java HelloWorldApp.class而不是运行程序，则会出现此错误java HelloWorldApp。请记住，参数是您要使用的类的名称，而不是文件名。

```java
Exception in thread "main" java.lang.NoSuchMethodError: main
```

Java VM要求您使用它执行的类具有main开始执行应用程序的方法。 仔细看看“Hello World！” 应用程序详细讨论了该main方法。

### Applet或Java Web Start应用程序被阻止

如果您通过浏览器运行应用程序，并收到安全警告，说明应用程序被阻止，请检查以下项目：
-   验证JAR文件清单中的属性是否针对运行该应用程序的环境正确设置。权限属性是必需的。在NetBeans项目中，可以通过展开项目文件夹并双击manifest.mf，从NetBeans IDE的“文件”选项卡打开清单文件。
-   验证应用程序是否由有效证书签名，并且证书位于签名者CA密钥库中。
-   如果您正在运行本地小程序，请设置一个Web服务器用于测试。您还可以将您的应用程序添加到异常站点列表，该列表在Java控制面板的安全选项卡中进行管理。
