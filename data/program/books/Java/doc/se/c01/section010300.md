#   仔细观察“Hello World！” 应用

现在你已经看到了“Hello World！” 应用程序（甚至可能编译并运行它），你可能想知道它是如何工作的。这里又是它的代码：
``` java
class HelloWorldApp {
    public static void main（String [] args）{
        System.out.println（“Hello World！”）; //显示字符串。
    }
}
```

“Hello World！” 应用程序由三个主要部分组成：`源代码注释`，`所述HelloWorldApp类的定义`，以及`该main方法`。以下说明将为您提供对代码的基本理解，但深层含义只有在完成本教程的其余部分的阅读后才会显现出来。

##  源代码评论

以下粗体文本定义了“Hello World！” 的注释 应用：
``` java
/ **
 HelloWorldApp类实现了一个应用程序
 *只需打印“Hello World！” 到标准输出。
 * /
class HelloWorldApp {
    public static void main（String [] args）{
        System.out.println（“Hello World！”）; //显示字符串。
    }
}
```

注释被编译器忽略，但对其他程序员很有用。Java编程语言支持三种注释：

/* text */
编译器会忽略 /* 之间 */。
/** documentation */
这表示文档评论（简称文档评论）。编译器会忽略这种评论，就像忽略使用/*和的评论一样*/。javadoc准备自动生成的文档时，该工具使用文档注释。有关更多信息javadoc，请参阅 Javadoc™工具文档。
// text
编译器会忽略//到该行末尾的所有内容。

##  在HelloWorldApp类定义

以下粗体文本开始“Hello World！”的类定义块。应用：

``` java
/ ** 
 * HelloWorldApp类实现了一个应用程序，它只是显示“Hello World！” 到标准输出。
 * / class HelloWorldApp { 
    public static void main（String [] args）{ 
        System.out.println（“Hello World！”）; //显示字符串。
    } }
```

如上所示，类定义的最基本形式是：

```java
class { 
    。。。
}
```

关键字class开始名为的类的类定义name，并且每个类的代码出现在上面以粗体标记的开头和结束花括号之间。

##  该main方法

以下粗体文本开始了main方法的定义：
``` java
/ ** 
 * HelloWorldApp类实现了一个应用程序，它
 只是显示“Hello World！” 到标准输出。
 * / 
class HelloWorldApp { public static void main（String [] args）{ 
        System.out.println（“Hello World！”）; //显示字符串。} 
}
```
    
在Java编程语言中，每个应用程序都必须包含一个main方法，其签名是：
```java
public static void main（String [] args）
```

所述改性剂public和static可以写在任何顺序（public static或static public），但惯例是使用public static如上所示。你可以根据需要命名参数，但大多数程序员选择“args”或“argv”。

该main方法与mainC和C ++中的函数类似; 它是您的应用程序的入口点，随后将调用您的程序所需的所有其他方法。

该main方法接受一个参数：一个类型元素的数组String。
```java
public static void main（String [] args）
```

该数组是运行时系统将信息传递给应用程序的机制。例如：
```java
java MyApp  arg1  arg2
```

数组中的每个字符串都称为命令行参数。命令行参数允许用户在不重新编译的情况下影响应用程序的操作。例如，排序程序可能允许用户使用此命令行参数指定数据按降序排序：
```java
-descending
```

“Hello World！” 应用程序会忽略它的命令行参数，但您应该意识到这样的参数确实存在的事实。

最后，该行：
```java
System.out.println（“Hello World！”）;
```

使用System核心库中的类来打印“Hello World！” 消息发送到标准输出。

