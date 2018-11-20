#   [检查枚举](https://docs.oracle.com/javase/tutorial/reflect/special/enumMembers.html)


Reflection提供了三个枚举特定的API：

-   Class.isEnum()：指示此类是否表示枚举类型
-   Class.getEnumConstants()：按照它们声明的顺序检索枚举定义的枚举常量列表
-   java.lang.reflect.Field.isEnumConstant()：指示此字段是否表示枚举类型的元素

有时需要动态检索枚举常量列表; 在非反射代码中，这是通过values()在枚举上调用隐式声明的静态方法 来实现的。如果枚举类型的实例不可用，则获取可能值列表的唯一方法是调用， Class.getEnumConstants()因为无法实例化枚举类型。

给定一个完全限定的名称，该 EnumConstants示例显示了如何使用枚举检索有序的常量列表 Class.getEnumConstants()。

```Java
import java.util.Arrays;
import static java.lang.System.out;

enum Eon { HADEAN, ARCHAEAN, PROTEROZOIC, PHANEROZOIC }

public class EnumConstants {
    public static void main(String... args) {
	try {
	    Class<?> c = (args.length == 0 ? Eon.class : Class.forName(args[0]));
	    out.format("Enum name:  %s%nEnum constants:  %s%n",
		       c.getName(), Arrays.asList(c.getEnumConstants()));
	    if (c == Eon.class)
		out.format("  Eon.values():  %s%n",
			   Arrays.asList(Eon.values()));

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}
```

输出样本如下。用户输入以斜体显示。

```Java

$ java EnumConstants java.lang.annotation.RetentionPolicy
Enum name:  java.lang.annotation.RetentionPolicy
Enum constants:  [SOURCE, CLASS, RUNTIME]
$ java EnumConstants java.util.concurrent.TimeUnit
Enum name:  java.util.concurrent.TimeUnit
Enum constants:  [NANOSECONDS, MICROSECONDS, 
                  MILLISECONDS, SECONDS, 
                  MINUTES, HOURS, DAYS]
```

此示例还显示返回 Class.getEnumConstants()的值与通过调用values()枚举类型返回的值相同。

```Java

$ java EnumConstants
Enum name:  Eon
Enum constants:  [HADEAN, ARCHAEAN, 
                  PROTEROZOIC, PHANEROZOIC]
Eon.values():  [HADEAN, ARCHAEAN, 
                PROTEROZOIC, PHANEROZOIC]
```

由于枚举是类，因此可以使用此跟踪的“ 字段”，“ 方法 ”和“ 构造函数”部分中描述的相同Reflection API获取其他信息。该 EnumSpy代码说明了如何使用这些API获取有关枚举声明的其他信息。该示例用于 Class.isEnum()限制检查的类集。它还 Field.isEnumConstant()用于区分枚举常量与枚举声明中的其他字段（并非所有字段都是枚举常量）。

```Java
import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Member;
import java.util.List;
import java.util.ArrayList;
import static java.lang.System.out;

public class EnumSpy {
    private static final String fmt = "  %11s:  %s %s%n";

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    if (!c.isEnum()) {
		out.format("%s is not an enum type%n", c);
		return;
	    }
	    out.format("Class:  %s%n", c);

	    Field[] flds = c.getDeclaredFields();
	    List<Field> cst = new ArrayList<Field>();  // enum constants
	    List<Field> mbr = new ArrayList<Field>();  // member fields
	    for (Field f : flds) {
		if (f.isEnumConstant())
		    cst.add(f);
		else
		    mbr.add(f);
	    }
	    if (!cst.isEmpty())
		print(cst, "Constant");
	    if (!mbr.isEmpty())
		print(mbr, "Field");

	    Constructor[] ctors = c.getDeclaredConstructors();
	    for (Constructor ctor : ctors) {
		out.format(fmt, "Constructor", ctor.toGenericString(),
			   synthetic(ctor));
	    }

	    Method[] mths = c.getDeclaredMethods();
	    for (Method m : mths) {
		out.format(fmt, "Method", m.toGenericString(),
			   synthetic(m));
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static void print(List<Field> lst, String s) {
	for (Field f : lst) {
 	    out.format(fmt, s, f.toGenericString(), synthetic(f));
	}
    }

    private static String synthetic(Member m) {
	return (m.isSynthetic() ? "[ synthetic ]" : "");
    }
}
$ java EnumSpy java.lang.annotation.RetentionPolicy
Class:  class java.lang.annotation.RetentionPolicy
     Constant:  public static final java.lang.annotation.RetentionPolicy
                  java.lang.annotation.RetentionPolicy.SOURCE 
     Constant:  public static final java.lang.annotation.RetentionPolicy
                  java.lang.annotation.RetentionPolicy.CLASS 
     Constant:  public static final java.lang.annotation.RetentionPolicy 
                  java.lang.annotation.RetentionPolicy.RUNTIME 
        Field:  private static final java.lang.annotation.RetentionPolicy[] 
                  java.lang.annotation.RetentionPolicy. [ synthetic ]
  Constructor:  private java.lang.annotation.RetentionPolicy() 
       Method:  public static java.lang.annotation.RetentionPolicy[]
                  java.lang.annotation.RetentionPolicy.values() 
       Method:  public static java.lang.annotation.RetentionPolicy
                  java.lang.annotation.RetentionPolicy.valueOf(java.lang.String) 
```

输出显示声明 java.lang.annotation.RetentionPolicy只包含三个枚举常量。枚举常量作为public static final字段公开。字段，构造函数和方法是编译器生成的。该$VALUES字段与该values()方法的实现有关。

注意：  由于各种原因，包括对枚举类型的演化的支持，枚举常量的声明顺序很重要。 Class.getFields()并且 Class.getDeclaredFields()不保证返回值的顺序与声明源代码中的顺序匹配。如果应用程序要求订购，请使用 Class.getEnumConstants()。

输出 java.util.concurrent.TimeUnit显示更复杂的枚举是可能的。此类包括几个方法以及声明static final的非枚举常量的其他字段。

```Java
$ java EnumSpy java.util.concurrent.TimeUnit
Class:  class java.util.concurrent.TimeUnit
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.NANOSECONDS
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.MICROSECONDS
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.MILLISECONDS
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.SECONDS
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.MINUTES
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.HOURS
     Constant:  public static final java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.DAYS
        Field:  static final long java.util.concurrent.TimeUnit.C0
        Field:  static final long java.util.concurrent.TimeUnit.C1
        Field:  static final long java.util.concurrent.TimeUnit.C2
        Field:  static final long java.util.concurrent.TimeUnit.C3
        Field:  static final long java.util.concurrent.TimeUnit.C4
        Field:  static final long java.util.concurrent.TimeUnit.C5
        Field:  static final long java.util.concurrent.TimeUnit.C6
        Field:  static final long java.util.concurrent.TimeUnit.MAX
        Field:  private static final java.util.concurrent.TimeUnit[] 
                  java.util.concurrent.TimeUnit. [ synthetic ]
  Constructor:  private java.util.concurrent.TimeUnit()
  Constructor:  java.util.concurrent.TimeUnit
                  (java.lang.String,int,java.util.concurrent.TimeUnit)
                  [ synthetic ]
       Method:  public static java.util.concurrent.TimeUnit
                  java.util.concurrent.TimeUnit.valueOf(java.lang.String)
       Method:  public static java.util.concurrent.TimeUnit[] 
                  java.util.concurrent.TimeUnit.values()
       Method:  public void java.util.concurrent.TimeUnit.sleep(long) 
                  throws java.lang.InterruptedException
       Method:  public long java.util.concurrent.TimeUnit.toNanos(long)
       Method:  public long java.util.concurrent.TimeUnit.convert
                  (long,java.util.concurrent.TimeUnit)
       Method:  abstract int java.util.concurrent.TimeUnit.excessNanos
                  (long,long)
       Method:  public void java.util.concurrent.TimeUnit.timedJoin
                  (java.lang.Thread,long) throws java.lang.InterruptedException
       Method:  public void java.util.concurrent.TimeUnit.timedWait
                  (java.lang.Object,long) throws java.lang.InterruptedException
       Method:  public long java.util.concurrent.TimeUnit.toDays(long)
       Method:  public long java.util.concurrent.TimeUnit.toHours(long)
       Method:  public long java.util.concurrent.TimeUnit.toMicros(long)
       Method:  public long java.util.concurrent.TimeUnit.toMillis(long)
       Method:  public long java.util.concurrent.TimeUnit.toMinutes(long)
       Method:  public long java.util.concurrent.TimeUnit.toSeconds(long)
       Method:  static long java.util.concurrent.TimeUnit.x(long,long,long)
```