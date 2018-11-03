#   [注解](https://docs.oracle.com/javase/8/docs/technotes/guides/language/annotations.html)

许多API需要相当数量的样板代码。例如，为了编写JAX-RPC Web服务，您必须提供配对的接口和实现。如果程序使用注释“装饰”指示哪些方法可远程访问，则可以由工具自动生成此样板。
其他API要求“副文件”与程序并行维护。例如，JavaBeans要求一个BeanInfo 类与bean并行维护，而Enterprise JavaBeans（EJB）需要一个部署描述符。如果这些辅助文件中的信息在程序本身中作为注释进行维护，那么它将更方便，更不容易出错。

Java平台一直有各种ad hoc注释机制。例如，transient修饰符是一个ad hoc注释，指示序列化子系统应忽略一个字段，而@deprecatedjavadoc标记是一个ad hoc注释，指示不再使用该方法。该平台具有通用注释（也称为元数据）工具，允许您定义和使用自己的注释类型。该工具包括用于声明注释类型的语法，用于注释声明的语法，用于读取注释的API，用于注释的类文件表示以及由javac工具提供的注释处理支持。

注释不直接影响程序语义，但它们确实会影响程序被工具和库处理的方式，这反过来又会影响正在运行的程序的语义。可以从源文件，类文件或运行时反射性地读取注释。

注释补充了javadoc标签。通常，如果标记旨在影响或生成文档，它应该是一个javadoc标记; 否则，它应该是一个注释。

典型的应用程序员永远不必定义注释类型，但这并不难。注释类型声明类似于普通接口声明。 关键字@前面有一个at符号（）interface。每个方法声明都定义了注释类型的元素。方法声明不得包含任何参数或throws子句。返回类型被限制为图元，String， Class， 枚举，注解和前述类型的数组。方法可以具有默认值。这是一个示例注释类型声明：
```
/ **
 *描述了领导的增强请求（RFE）
 *存在带注释的API元素。
 * /
public @interface RequestForEnhancement {
    int    id();
    String synopsis();
    String engineer() default "[unassigned]"; 
    String date()    default "[unimplemented]"; 
}
```

一旦定义了注释类型，就可以使用它来注释声明。注释是一种特殊的改性剂，并且可以在任何地方使用的其它改性剂（如public， static或final）都可以使用。按照惯例，注释在其他修饰符之前。注释由at符号（@）后跟注释类型和带括号的元素 - 值对列表组成。值必须是编译时常量。这是一个方法声明，其注释对应于上面声明的注释类型：
```
@RequestForEnhancement(
    id       = 2868724,
    synopsis = "Enable time-travel",
    engineer = "Mr. Peabody",
    date     = "4/1/3007"
)
public static void travelThroughTime(Date destination) { ... }
```
没有元素的注释类型称为标记 注释类型，例如：
```
/ **
 *表示带注释的API元素的规范
 *是初步的，可能会有变化。
 * /
public @interface Preliminary {}
```
允许在标记注释中省略括号，如下所示：
```
@Preliminary public class TimeTravel { ... }
```
在具有单个元素的注释中，应该命名该元素value，如下所示：
```
/ **
 *将版权声明与带注释的API元素相关联。
 * /
public @interface Copyright {
    String value();
}
```
允许在元素名称=为的单元素注释中省略元素名称和等号（）value，如下所示：
```
@Copyright("2002 Yoyodyne Propulsion Systems")
public class OscillationOverthruster { ... }
```
为了将它们结合在一起，我们将构建一个简单的基于注释的测试框架。首先，我们需要一个标记注释类型来指示方法是一种测试方法，并且应该由测试工具运行：
```
import java.lang.annotation。*;

/ **
 *表示带注释的方法是一种测试方法。
 *此注释仅应用于无参数静态方法。
 * /
@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.METHOD)
public @interface Test { }
```
请注意，注释类型声明本身已注释。这种注释称为元注释。第一个（@Retention(RetentionPolicy.RUNTIME)）表示VM将保留此类型的注释，以便在运行时可以反射性地读取它们。第二个（@Target(ElementType.METHOD)）表示此注释类型可用于仅注释方法声明。

这是一个示例程序，其中一些方法使用上面的接口进行注释：
```
public class Foo {
    @Test public static void m1() { }
    public static void m2() { }
    @Test public static void m3() {
        throw new RuntimeException("Boom");
    }
    public static void m4() { }
    @Test public static void m5() { }
    public static void m6() { }
    @Test public static void m7() {
        throw new RuntimeException("Crash");
    }
    public static void m8() { }
}
```
这是测试工具：
```
import java.lang.reflect.*;

public class RunTests {
   public static void main(String[] args) throws Exception {
      int passed = 0, failed = 0;
      for (Method m : Class.forName(args[0]).getMethods()) {
         if (m.isAnnotationPresent(Test.class)) {
            try {
               m.invoke(null);
               passed++;
            } catch (Throwable ex) {
               System.out.printf("Test %s failed: %s %n", m, ex.getCause());
               failed++;
            }
         }
      }
      System.out.printf("Passed: %d, Failed %d%n", passed, failed);
   }
}
```
该工具将类名作为命令行参数，并迭代命名类的所有方法，尝试调用使用Test 注释类型（上面定义）注释的每个方法。用于查明方法是否具有Test注释的反射查询以绿色突出显示。如果测试方法调用抛出异常，则认为测试失败，并打印失败报告。最后，打印一个摘要，显示通过和失败的测试数。以下是在Foo程序上运行测试工具时的外观 （上图）：
```
$ java RunTests Foo
Test public static void Foo.m3() failed: java.lang.RuntimeException: Boom 
Test public static void Foo.m7() failed: java.lang.RuntimeException: Crash 
Passed: 2, Failed 2
```
虽然这个测试工具显然是一个玩具，但它展示了注释的力量，并且可以很容易地扩展以克服其局限性。
