#   [包java.lang.instrument](https://docs.oracle.com/javase/8/docs/api/java/lang/instrument/package-summary.html)

提供允许Java编程语言代理程序检测在JVM上运行的程序的服务

##  描述

提供允许Java编程语言代理程序检测在JVM上运行的程序的服务。检测机制是修改方法的字节码。

-   包装规格

代理程序部署为JAR文件。JAR文件清单中的属性指定将加载以启动代理的代理类。对于支持命令行界面的实现，通过在命令行上指定选项来启动代理。实现还可以支持在VM启动后的某个时间启动代理的机制。例如，实现可以提供允许工具 附加到正在运行的应用程序的机制，并且启动将工具的代理加载到正在运行的应用程序中。有关如何启动负载的详细信息取决于实现。

-   命令行界面

不需要实现来提供从命令行界面启动代理的方法。在提供从命令行界面启动代理的方法的实现上，通过将此选项添加到命令行来启动代理：

```
-javaagent:jarpath [ =选项]
```

jarpath是代理JAR文件的路径。 options是代理选项。此交换机可以在同一命令行上多次使用，从而创建多个代理。多个代理可能使用相同的jarpath。代理JAR文件必须符合JAR文件规范。

代理JAR文件的清单必须包含该属性Premain-Class。此属性的值是代理类的名称。代理类必须实现premain与main应用程序入口点原则上类似的公共静态方法。Java虚拟机（JVM）初始化后，premain将按指定代理的顺序调用每个方法，然后main调用实际的应用程序 方法。premain必须返回每个方法才能继续启动序列。

该premain方法具有两种可能的签名之一。JVM首先尝试在代理类上调用以下方法：

public static void premain(String agentArgs, Instrumentation inst);
如果代理类未实现此方法，则JVM将尝试调用：

public static void premain(String agentArgs);
代理类还可以具有agentmain在VM启动之后启动代理时使用的方法。使用命令行选项启动代理程序时，agentmain 不会调用该方法。

代理类将由系统类加载器加载（请参阅参考资料ClassLoader.getSystemClassLoader）。这是类加载器，它通常加载包含应用程序main方法的类。这些premain方法将在与应用程序main方法相同的安全性和类加载器规则下运行。代理premain方法可能没有建模限制。应用程序main可以做的任何事情，包括创建线程，都是合法的premain。

每个代理都通过agentArgs参数传递其代理选项。代理选项作为单个字符串传递，任何其他解析应由代理本身执行。

如果无法解析代理（例如，因为无法加载代理类，或者因为代理类没有适当的premain方法），JVM将中止。如果premain方法抛出未捕获的异常，则JVM将中止。

-   VM启动后启动代理

实现可以提供在VM启动之后的某个时间启动代理的机制。有关如何启动它的详细信息是特定于实现的，但通常应用程序已经启动并且其 main方法已被调用。如果实施支持在VM启动后启动代理，则以下情况适用：

1.  代理JAR的清单必须包含该属性Agent-Class。此属性的值是代理类的名称。

2.  代理类必须实现公共静态agentmain方法。

3.  系统类loader（ ClassLoader.getSystemClassLoader）必须支持将代理JAR文件添加到系统类路径的机制。

代理JAR附加到系统类路径。这是通常加载包含应用程序main方法的类的类加载器。加载代理程序类，JVM尝试调用该agentmain方法。JVM首先尝试在代理类上调用以下方法：

```
public static void agentmain(String agentArgs, Instrumentation inst);
```

如果代理类未实现此方法，则JVM将尝试调用：

```
public static void agentmain(String agentArgs);
```

代理类还可以具有premain在使用命令行选项启动代理程序时使用的方法。在VM启动后启动代理程序时，premain 不会调用该方法。

代理程序通过agentArgs参数传递其代理程序选项。代理选项作为单个字符串传递，任何其他解析应由代理本身执行。

该agentmain方法应该执行启动代理所需的任何必要的初始化。启动完成后，该方法应返回。如果无法启动代理（例如，因为无法加载代理类，或者因为代理类没有符合agentmain方法），JVM将不会中止。如果该agentmain方法抛出未捕获的异常，则将被忽略。

-   清单属性

为代理JAR文件定义了以下清单属性：

`Premain-Class`
在JVM启动时指定代理程序时，此属性指定代理程序类。也就是说，包含该premain方法的类。在JVM启动时指定代理程序时，此属性是必需的。如果该属性不存在，则JVM将中止。注意：这是类名，而不是文件名或路径。

`Agent-Class`
如果实现支持在VM启动后的某个时间启动代理的机制，则此属性指定代理类。也就是说，包含该agentmain方法的类。此属性是必需的，如果不存在，则不会启动代理。注意：这是类名，而不是文件名或路径。

`Boot-Class-Path`
引导类加载器要搜索的路径列表。路径表示目录或库（在许多平台上通常称为JAR或zip库）。在定位类的平台特定机制失败后，引导类加载器将搜索这些路径。按列出的顺序搜索路径。列表中的路径由一个或多个空格分隔。路径采用分层URI的路径组件的语法。如果以斜杠字符（'/'）开头，则路径是绝对的，否则它是相对的。根据代理JAR文件的绝对路径解析相对路径。格式错误且不存在的路径将被忽略。在VM启动后的某个时间启动代理程序时，将忽略不代表JAR文件的路径。此属性是可选的。在VM启动后的某个时间启动代理程序时，将忽略不代表JAR文件的路径。此属性是可选的。在VM启动后的某个时间启动代理程序时，将忽略不代表JAR文件的路径。此属性是可选的。

`Can-Redefine-Classes`
布尔（true或false不相关的情况）。是否能够重新定义此代理所需的类。true考虑以外的其他值false。此属性是可选的，默认为false。

`Can-Retransform-Classes`
布尔（true或false不相关的情况）。是否能够重新转换此代理所需的类。true考虑以外的其他值false。此属性是可选的，默认为false。

`Can-Set-Native-Method-Prefix`
布尔（true或false不相关的情况）。是否能够设置此代理所需的本机方法前缀。true考虑以外的其他值false。此属性是可选的，默认为false。

代理JAR文件可能同时具有 清单中的Premain-Class和Agent-Class属性。使用该-javaagent选项在命令行上启动代理程序时，该Premain-Class属性指定代理程序类的名称，并Agent-Class忽略该属性。同样，如果代理在VM启动后的某个时间启动，则该Agent-Class属性指定代理类的名称（Premain-Class忽略属性的值）。

----
