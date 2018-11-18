#   [发现类成员](https://docs.oracle.com/javase/tutorial/reflect/class/classMembers.html)

Class为访问字段，方法和构造函数提供了两类方法 ：枚举这些成员的方法和搜索特定成员的方法。还有一些不同的方法可以访问直接在类上声明的成员，而不是用于搜索继承成员的超接口和超类的方法。下表提供了所有成员定位方法及其特征的摘要。

-   定位字段的类方法

|Class API	|会员名单？	|继承成员？	|私人会员？|
|-------|-----|-----|------|
|getDeclaredField()	|没有	|没有	|是|
|getField()	|没有	|是	|没有|
|getDeclaredFields()	|是	|没有	|是|
|getFields()	|是	|是	|没有|
|||||

-   定位方法的类方法

|Class API	|会员名单？	|继承成员？	|私人会员？|
|-------|-----|-----|------|
|getDeclaredMethod()	|没有	|没有	|是|
|getMethod()	|没有	|是	|没有|
|getDeclaredMethods()	|是	|没有	|是|
|getMethods()	|是	|是	|没有|
|||||

-   定位构造函数的类方法

|Class API	|会员名单？	|继承成员？	|私人会员？|
|-------|-----|-----|------|
|getDeclaredConstructor()	|没有	|不适用1	|是|
|getConstructor()	|没有	|不适用1	|没有|
|getDeclaredConstructors()	|是	|不适用1	|是|
|getConstructors()	|是	|不适用1	|没有|
|||||

构造函数不是继承的。

给定类名称以及对哪些成员感兴趣的指示，该 ClassSpy示例使用这些get*s()方法来确定所有公共元素的列表，包括任何继承的元素。

``` Java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Member;
import static java.lang.System.out;

enum ClassMember { CONSTRUCTOR, FIELD, METHOD, CLASS, ALL }

public class ClassSpy {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    out.format("Class:%n  %s%n%n", c.getCanonicalName());

	    Package p = c.getPackage();
	    out.format("Package:%n  %s%n%n",
		       (p != null ? p.getName() : "-- No Package --"));

	    for (int i = 1; i < args.length; i++) {
		switch (ClassMember.valueOf(args[i])) {
		case CONSTRUCTOR:
		    printMembers(c.getConstructors(), "Constructor");
		    break;
		case FIELD:
		    printMembers(c.getFields(), "Fields");
		    break;
		case METHOD:
		    printMembers(c.getMethods(), "Methods");
		    break;
		case CLASS:
		    printClasses(c);
		    break;
		case ALL:
		    printMembers(c.getConstructors(), "Constuctors");
		    printMembers(c.getFields(), "Fields");
		    printMembers(c.getMethods(), "Methods");
		    printClasses(c);
		    break;
		default:
		    assert false;
		}
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static void printMembers(Member[] mbrs, String s) {
	out.format("%s:%n", s);
	for (Member mbr : mbrs) {
	    if (mbr instanceof Field)
		out.format("  %s%n", ((Field)mbr).toGenericString());
	    else if (mbr instanceof Constructor)
		out.format("  %s%n", ((Constructor)mbr).toGenericString());
	    else if (mbr instanceof Method)
		out.format("  %s%n", ((Method)mbr).toGenericString());
	}
	if (mbrs.length == 0)
	    out.format("  -- No %s --%n", s);
	out.format("%n");
    }

    private static void printClasses(Class<?> c) {
	out.format("Classes:%n");
	Class<?>[] clss = c.getClasses();
	for (Class<?> cls : clss)
	    out.format("  %s%n", cls.getCanonicalName());
	if (clss.length == 0)
	    out.format("  -- No member interfaces, classes, or enums --%n");
	out.format("%n");
    }
}
```

这个例子比较紧凑; 然而，printMembers()由于java.lang.reflect.Member界面自最早的反射实现以来一直存在，并且无法修改以包含getGenericString()引入泛型时更有用的方法，因此该方法稍微有些尴尬 。唯一的选择是测试和投如图所示，以取代这种方法printConstructors()，printFields()和printMethods()，或满足于相对空闲的结果 Member.getName()。

输出样本及其解释如下。用户输入以斜体显示。

```
$ java ClassSpy java.lang.ClassCastException CONSTRUCTOR
Class:
  java.lang.ClassCastException

Package:
  java.lang

Constructor:
  public java.lang.ClassCastException()
  public java.lang.ClassCastException(java.lang.String)
```

由于构造函数不是继承的，因此找不到Throwable在直接超类RuntimeException和其他超类中定义的异常链接机制构造函数（具有参数的构造 函数） 

```
$ java ClassSpy java.nio.channels.ReadableByteChannel METHOD
Class:
  java.nio.channels.ReadableByteChannel

Package:
  java.nio.channels

Methods:
  public abstract int java.nio.channels.ReadableByteChannel.read
    (java.nio.ByteBuffer) throws java.io.IOException
  public abstract void java.nio.channels.Channel.close() throws
    java.io.IOException
  public abstract boolean java.nio.channels.Channel.isOpen()
```

接口 java.nio.channels.ReadableByteChannel定义 read()。其余方法继承自超级接口。此代码可以很容易地修改，只列出那些通过替换类实际上声明的方法get*s()与getDeclared*s()。

```
$ java ClassSpy ClassMember FIELD METHOD
Class:
  ClassMember

Package:
  -- No Package --

Fields:
  public static final ClassMember ClassMember.CONSTRUCTOR
  public static final ClassMember ClassMember.FIELD
  public static final ClassMember ClassMember.METHOD
  public static final ClassMember ClassMember.CLASS
  public static final ClassMember ClassMember.ALL

Methods:
  public static ClassMember ClassMember.valueOf(java.lang.String)
  public static ClassMember[] ClassMember.values()
  public final int java.lang.Enum.hashCode()
  public final int java.lang.Enum.compareTo(E)
  public int java.lang.Enum.compareTo(java.lang.Object)
  public final java.lang.String java.lang.Enum.name()
  public final boolean java.lang.Enum.equals(java.lang.Object)
  public java.lang.String java.lang.Enum.toString()
  public static <T> T java.lang.Enum.valueOf
    (java.lang.Class<T>,java.lang.String)
  public final java.lang.Class<E> java.lang.Enum.getDeclaringClass()
  public final int java.lang.Enum.ordinal()
  public final native java.lang.Class<?> java.lang.Object.getClass()
  public final native void java.lang.Object.wait(long) throws
    java.lang.InterruptedException
  public final void java.lang.Object.wait(long,int) throws
    java.lang.InterruptedException
  public final void java.lang.Object.wait() hrows java.lang.InterruptedException
  public final native void java.lang.Object.notify()
  public final native void java.lang.Object.notifyAll()
```

在这些结果的字段部分中，列出了枚举常量。虽然这些是技术领域，但将它们与其他领域区分开来可能是有用的。可以修改此示例以 [java.lang.reflect.Field.isEnumConstant()](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Field.html#isEnumConstant--)用于此目的。EnumSpy此跟踪的后续部分中的 示例“ 检查枚举 ”包含可能的实现。

在输出的方法部分中，观察方法名称包含声明类的名称。因此，该toString()方法是通过Enum而不是继承 而实现的 Object。可以通过使用修改代码以使其更加明显 [Field.getDeclaringClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/Field.html#getDeclaringClass--)。以下片段说明了潜在解决方案的一部分。

```
if (mbr instanceof Field) {
    Field f = (Field)mbr;
    out.format("  %s%n", f.toGenericString());
    out.format("  -- declared in: %s%n", f.getDeclaringClass());
}
```