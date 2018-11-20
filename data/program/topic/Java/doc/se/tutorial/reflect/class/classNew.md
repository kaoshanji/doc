#   [检索类对象](https://docs.oracle.com/javase/tutorial/reflect/class/classNew.html)

所有反射操作的入口点是 [java.lang.Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)。除了 [java.lang.reflect.ReflectPermission](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/ReflectPermission.html)没有[java.lang.reflect](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)公共构造函数的类之外 。要获得这些类，有必要调用适当的方法 Class。Class根据代码是否可以访问对象，类的名称，类型或现有， 有几种方法可以获得 Class。

##  Object.getClass（）

如果一个对象的实例可用，那么获取它的最简单方法 Class就是调用它 [Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)。当然，这仅适用于所有继承自的引用类型 Object。一些例子如下。

`Class c = "foo".getClass();`

返回 Classfor String

`Class c = System.console().getClass();`

有一个与该static方法 返回的虚拟机关联的唯一控制台[System.console()](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#console--)。返回的值 getClass()是 Class对应的 [java.io.Console](https://docs.oracle.com/javase/8/docs/api/java/io/Console.html)。

```
enum E { A, B }
Class c = A.getClass();
```

A是枚举的一个实例E; 因此 getClass()返回 Class对应的枚举类型E。

```
byte[] bytes = new byte[1024];
Class c = bytes.getClass();
```

由于数组是 Objects，因此也可以getClass()在数组的实例上调用 。返回 Class对应于具有组件类型的数组byte。

```
import java.util.HashSet;
import java.util.Set;

Set<String> s = new HashSet<String>();
Class c = s.getClass();
```

在这种情况下， [java.util.Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)是类型对象的接口 [java.util.HashSet](https://docs.oracle.com/javase/8/docs/api/java/util/HashSet.html)。返回的值 getClass()是对应的类 java.util.HashSet。

----

##  .class语法

如果类型可用但没有实例，那么可以Class通过附加".class"类型的名称来获得a 。这也是获取Class原始类型的最简单方法 。

```
boolean b;
Class c = b.getClass();   // compile-time error

Class c = boolean.class;  // correct
```
请注意，该语句boolean.getClass()将产生编译时错误，因为a boolean是基本类型，无法解除引用。该.class语法返回 Class对应于该类型boolean。

```
Class c = java.io.PrintStream.class;
```

变量c将 Class与类型对应 [java.io.PrintStream](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html)。

```
Class c = int[][][].class;
```

.class语法可用于检索Class对应于给定类型的多维阵列的语法 。

----

##  Class.forName（）

如果类的完全限定名称可用，则可以Class使用静态方法获取相应 的名称 Class.forName()。这不能用于原始类型。数组类名称的语法描述如下 [Class.getName()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#forName-java.lang.String-)。此语法适用于引用和基元类型。

```Class c = Class.forName("com.duke.MyLocaleServiceProvider");```

此语句将根据给定的完全限定名称创建一个类。
```
Class cDoubleArray = Class.forName("[D");

Class cStringArray = Class.forName("[[Ljava.lang.String;");
```
该变量cDoubleArray将包含 Class对应于基本类型的数组double（即相同double[].class）。该cStringArray变量将包含 Class对应于二维数组 String（即相同String[][].class）。

----

##  原始类型包装的TYPE字段

该.class语法是一种更方便，以获得优选的方式 Class为一个基本类型; 然而，有另一种方式来获得 Class。每个基本类型void都有一个包装类 java.lang，用于将基元类型装箱到引用类型。每个包装类包含一个名为的字段TYPE，该字段等于 Class被包装的基本类型。

```
Class c = Double.TYPE;
```
还有一类 java.lang.Double是用来包裹基本类型double每当 Object是必需的。价值 Double.TYPE与double.class。相同。

```
Class c = Void.TYPE;
```
Void.TYPE是完全相同的void.class。

----

##  返回类的方法

有几个Reflection API可以返回类，但只有在Class已经直接或间接获得的情况下才能访问这些类 。

-   [Class.getSuperclass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#getSuperclass--)
    -   Returns the super class for the given class.
        `Class c = javax.swing.JButton.class.getSuperclass();`
    -   The super class of javax.swing.JButton is javax.swing.AbstractButton.

-   [Class.getClasses()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#getClasses--)
    -   Returns all the public classes, interfaces, and enums that are members of the class including inherited members.
        `Class<?>[] c = Character.class.getClasses();`
    -   Character contains two member classes Character.Subset and Character.UnicodeBlock.

-   [Class.getDeclaredClasses()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#getDeclaredClasses--)
    -   Returns all of the classes interfaces, and enums that are explicitly declared in this class.
        `Class<?>[] c = Character.class.getDeclaredClasses();`
    -   Character contains two public member classes Character.Subset and Character.UnicodeBlock and one private class Character.CharacterCache.

-   Class.getDeclaringClass()
-   java.lang.reflect.Field.getDeclaringClass()
-   java.lang.reflect.Method.getDeclaringClass()
-   java.lang.reflect.Constructor.getDeclaringClass()
    -   Returns the Class in which these members were declared. Anonymous Class Declarations will not have a declaring class but will have an enclosing class.
        
    ```
    import java.lang.reflect.Field;

    Field f = System.class.getField("out");
    Class c = f.getDeclaringClass();
    ```

    -   The field out is declared in System.

    ```
    public class MyClass {
        static Object o = new Object() {
            public void m() {} 
        };
        static Class<c> = o.getClass().getEnclosingClass();
    }
    ```
    
    -   The declaring class of the anonymous class defined by o is null.

[Class.getEnclosingClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#getEnclosingClass--)
    -   Returns the immediately enclosing class of the class.
        `Class c = Thread.State.class().getEnclosingClass();`
    -   The enclosing class of the enum Thread.State is Thread.
    ``` Java
    public class MyClass {
        static Object o = new Object() { 
            public void m() {} 
        };
        static Class<c> = o.getClass().getEnclosingClass();
    }
    ```
    The anonymous class defined by o is enclosed by MyClass.

----