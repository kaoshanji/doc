#   [独立于位置的资源访问](https://docs.oracle.com/javase/8/docs/technotes/guides/lang/resources.html)

##  目录
-   概观
-   资源，名称和上下文
-   系统资源
-   非系统资源
-   资源名称
-   使用java.lang.Class的方法
-   使用java.lang.ClassLoader的方法
-   安全
-   例子
-   参考

----

##  概观

资源是程序需要以独立于程序代码位置的方式访问的数据（图像，音频，文本等）。Java程序可以使用两种机制来访问资源：Applet用于`Applet.getCodeBase()` 获取applet代码的基本URL，然后使用相对路径扩展基本URL以加载所需资源，例如`Applet.getAudioClip(url)`。应用程序使用“众所周知的位置”，例如 `System.getProperty("user.home")`或 `System.getProperty("java.home")`，然后添加`“/ lib / resource ”`，并打开该文件。

类中的方法`Class`并 `ClassLoader`提供与位置无关的方法来定位资源。例如，它们可以为以下内容定位资源：

-   使用多个HTTP连接从Internet加载的applet。
-   使用JAR文件加载的applet。
-   在CLASSPATH中加载或安装的Java Bean。
-   CLASSPATH中安装的“库”。

这些方法不提供查找本地化资源的特定支持。[国际化设施](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/index.html)支持本地化资源 。

----

##  资源，名称和上下文

资源由一个字符串标识，该字符串由一系列子字符串组成，由斜杠（/）分隔，后跟资源名称。每个子字符串必须是有效的Java标识符。资源名称的形式为`shortName`或 `shortName.extension`。双方 `shortName`并`extension` 必须是Java标识符。

资源的名称独立于Java实现; 特别是，路径分隔符始终是斜杠（/）。但是，Java实现控制资源内容如何映射到包含实际资源的文件，数据库或其他对象的详细信息。

资源名称的解释与类加载器实例有关。`ClassLoader`该类实现的方法 做了这种解释。

----

##  系统资源

系统资源是内置于系统的资源，或由主机实现保存在例如本地文件系统中的资源。计划通过访问系统资源 `ClassLoader`的方法`getSystemResource`和 `getSystemResourceAsStream`。

例如，在特定实现中，定位系统资源可能涉及搜索CLASSPATH中的条目。这些 `ClassLoader`方法在CLASSPATH中搜索资源文件中的每个目录，ZIP文件或JAR文件条目，如果找到，则返回an `InputStream`或资源名称。如果未找到，则方法返回null。可以在CLASSPATH中的不同条目中找到资源，而不是加载类文件的位置。

----

##  非系统资源

执行`getResource`一类加载器依赖于细节`ClassLoader`类。例如，`AppletClassLoader`：

-   首先尝试将资源定位为系统资源; 然后，如果没有找到，
-   搜索已加载到此CODEBASE中的档案资源（JAR文件）; 然后，如果没有找到，
-   使用CODEBASE并尝试查找资源（可能涉及联系远程站点）。

所有类加载器将首先搜索资源作为系统资源，其方式类似于对类文件进行搜索。此搜索规则允许在本地覆盖任何资源。客户端应选择一个唯一的资源名称（例如，使用公司或包名称作为前缀）。

----

##  资源名称

类使用的资源名称的常见约定是使用类的包的完全限定名称，但将所有句点（。）转换为斜杠（/），并添加表单的资源名称`name.extension`。为了支持这一点，并简化处理系统类的细节（为其 `getClassLoader`返回null），该类 `Class`提供了两个方便的方法来调用适当的方法`ClassLoader`。

给予Class方法的资源名称可以具有初始开始“/”，其将其标识为“绝对”名称。不以“/”开头的资源名称是“相对的”。

绝对名称将被剥离其起始“/”，并且无需进一步修改即可通过适当的 `ClassLoader`方法来定位资源。根据先前描述的约定修改相对名称，然后将其传递给`ClassLoader`方法。

----

##  使用java.lang.Class的方法

本`Class`类实现加载资源的几种方法。

该方法`getResource()`返回资源的URL。URL（及其表示）特定于实现和JVM（即，在一个运行时实例中获取的URL可能在另一个运行时实例中不起作用）。其协议通常特定于`ClassLoader`加载资源。如果资源由于安全考虑而不存在或不可见，则方法返回null。

如果客户端代码想要读取资源的内容`InputStream`，则可以`openStream()`在URL上应用该 方法。这是很常见的理由加入`getResourceAsStream()`到 `Class`和`ClassLoader`。 `getResourceAsStream()`与调用相同 `getResource().openStream()`，除了 `getResourceAsStream()`捕获IO异常返回null `InputStream`。

客户端代码还可以通过`java.net.URL.getContent()` 在URL上应用该方法来请求资源的内容作为对象。例如，当资源包含图像的数据时，这很有用。在图像的情况下，结果是`awt.image.ImageProducer`对象，而不是 `Image`对象。

该`getResource`和 `getResourceAsStream`方法找到一个给定名称的资源。如果找不到具有指定名称的资源，则返回null。搜索与给定类关联的资源的规则由类的ClassLoader实现。在应用命名约定之后，`Class`方法委托给 `ClassLoader`方法：如果资源名称以“/”开头，则按原样使用。否则，在将所有句点（。）转换为斜杠（/）之后，将预先附加包的名称。

```
public InputStream getResourceAsStream(String name) {
  name = resolveName(name);
  ClassLoader cl = getClassLoader();
  if (cl==null) {
    return ClassLoader.getSystemResourceAsStream(name); // A system class.
  }
  return cl.getResourceAsStream(name);
}

public java.net.URL getResource(String name) {
  name = resolveName(name);
  ClassLoader cl = getClassLoader();
  if (cl==null) {
    return ClassLoader.getSystemResource(name);  // A system class.
  }
  return cl.getResource(name);
}
```
`resolveName`如果名称不是绝对的，则该方法添加包名称前缀，如果名称是绝对的，则删除任何前导“/”。虽然不常见，但是在不同的包中使用共享相同资源的类是可能的。
```
 private String resolveName(String name) {
  if (name == null) {
    return name;
  }
  if (!name.startsWith("/")) {
    Class c = this;
    while (c.isArray()) {
      c = c.getComponentType();
    }
    String baseName = c.getName();
    int index = baseName.lastIndexOf('.');
    if (index != -1) {
      name = baseName.substring(0, index).replace('.', '/') + "/" + name;
    }
  } else {
    name = name.substring(1);
  }
  return name;
}
```
----

##  使用java.lang.ClassLoader的方法

该`ClassLoader`班有两套方法来访问资源。一组`InputStream`为资源返回一个。另一组返回一个URL。返回a的方法`InputStream`更易于使用并且将满足许多需求，而返回URL的方法提供对更复杂信息的访问，例如Image和AudioClip。

该`ClassLoaderManges`律师资源同样的方式，管理类。A `ClassLoader`控制如何将资源名称映射到其内容。`ClassLoader `还提供了访问系统资源的方法，类似于系统类。本`Class` 类提供了一些方便的方法是委托功能的`ClassLoader`方法。

许多Java程序将通过I18N（本地化）API间接访问这些方法。其他人将通过方法访问它`Class`。一些将直接调用 `ClassLoader`方法。

方法`ClassLoader`使用给定的String作为资源的名称，而不应用任何绝对/相对转换（请参阅Class中的方法）。名称不应该有前导“/”。

系统资源是由主机实现直接处理的资源。例如，它们可能位于CLASSPATH中。

资源的名称是“/” - 分隔的标识符序列。的Class类提供了用于访问资源便利方法; 这些方法实现了一种约定，其中包名称以资源的短名称为前缀。

资源可以作为`InputStreamURL`或URL 访问。

该`getSystemResourceAsStream`方法返回指定系统资源的InputStream，如果找不到资源则返回null。资源名称可以是任何系统资源。

该`getSystemResource`方法查找具有指定名称的系统资源。它返回资源的URL，如果找不到资源，则返回null。调用 `java.net.URL.getContent()`与URL会返回一个对象，例如`ImageProducer`，`AudioClip`或`InputStream`。

该`getResourceAsStream`方法返回`InputStream`指定资源的a，如果找不到资源，则返回 null。

该`getResource`方法查找具有指定名称的资源。它返回资源的URL，如果找不到资源，则返回null。调用 `java.net.URL.getContent()`与URL会返回一个对象，例如`ImageProducer`，`AudioClip`或`InputStream`。

----

##  安全

由于`getResource()`提供对信息的访问，因此它必须具有明确定义且有充分根据的安全规则。如果安全性考虑因素不允许资源在某些安全上下文中可见，则该`getResource()`方法将失败（返回null），就像资源根本不存在一样，这解决了存在攻击。

出于安全性和性能原因，类加载器可能无法提供对.class文件内容的访问。是否可以获取.class文件的URL取决于具体情况，如下所示。

对于非系统类加载器找到的资源，没有指定的安全问题或限制。 `AppletClassLoader`提供对从源位置加载的信息的访问，无论是单独加载还是通过JAR文件加载到组中; 因此在处理URL时`AppletClassLoader` 应该应用相同的`checkConnect()`规则`getResource()`。

系统`ClassLoader`提供对CLASSPATH中信息的访问。CLASSPATH可能包含目录和JAR文件。由于有意创建了一个JAR文件，因此它与一个事物可能以更随意的方式结束的目录具有不同的意义。特别是，我们更严格地从目录中获取信息而不是从JAR文件中获取信息。

如果资源位于目录中：
-   `getResource()`调用将用于 `File.exists()`确定是否使相应的文件对用户可见。回想一下， `File.exists()`使用`checkRead()`安全管理器中的方法。
-   这同样适用于`getResourceAsStream()`。

如果资源位于JAR文件中：
-   `getResource()` 无论调用是在系统内还是在非系统类中完成，调用都将对所有文件成功。
-   `getResourceAsStream()`对于非.class资源，调用将成功，对于`java.net.URL.getContent()`相应的URL 也是如此 。

----

##  例子

本节提供了两个客户端代码示例。第一个示例使用“绝对资源”名称和传统机制来获取Class对象。
```
package pkg;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;

class Test {

  private static final String absName = "/pkg/mumble.baf";

  public static void test1() {
    Class c=null;
    try {
      c = Class.forName("pkg.Test");
    } catch (Exception ex) {
      // This should not happen.
    }
    InputStream s = c.getResourceAsStream(absName);
    // do something with it.
  }

  public void test2() {
    InputStream s = this.getClass().getResourceAsStream(absName);
  // do something with it.
  }
}
```
此示例使用“相对资源”名称和编译器通过-experimental 标志提供的机制来获取Class对象。
```
package pkg;

import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;

class Test {
  private static final String relName = "mumble.baf";
  public static void test1() {
  InputStream s = Test.class.getResourceAsStream(relName);
  // do something with it.
}

  public void test2() {
    InputStream s = Test.class.getResourceAsStream(relName);
    // do something with it.
  }
```
----

##  API参考

-   [java.lang.Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)
-   [java.lang.ClassLoader](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html)
-   [java.net.URLClassLoader](https://docs.oracle.com/javase/8/docs/api/java/net/URLClassLoader.html)
-   [java.util.ResourceBundle](https://docs.oracle.com/javase/8/docs/api/java/util/ResourceBundle.html)
-   [java.lang.SecurityManager](https://docs.oracle.com/javase/8/docs/api/java/lang/SecurityManager.html)
-   [java.security](https://docs.oracle.com/javase/8/docs/api/java/security/package-summary.html)

----