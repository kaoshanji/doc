#   [获取方法类型信息](https://docs.oracle.com/javase/tutorial/reflect/member/methodType.html)

方法声明包括名称，修饰符，参数，返回类型和可抛出异常列表。本 java.lang.reflect.Method类提供了一种方法来获取此信息。

该 MethodSpy示例说明了如何枚举给定类中的所有声明的方法，并检索给定名称的所有方法的返回，参数和异常类型。

```Java
import java.lang.reflect.Method;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class MethodSpy {
    private static final String  fmt = "%24s: %s%n";

    // for the morbidly curious
    <E extends RuntimeException> void genericThrow() throws E {}

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Method[] allMethods = c.getDeclaredMethods();
	    for (Method m : allMethods) {
		if (!m.getName().equals(args[1])) {
		    continue;
		}
		out.format("%s%n", m.toGenericString());

		out.format(fmt, "ReturnType", m.getReturnType());
		out.format(fmt, "GenericReturnType", m.getGenericReturnType());

		Class<?>[] pType  = m.getParameterTypes();
		Type[] gpType = m.getGenericParameterTypes();
		for (int i = 0; i < pType.length; i++) {
		    out.format(fmt,"ParameterType", pType[i]);
		    out.format(fmt,"GenericParameterType", gpType[i]);
		}

		Class<?>[] xType  = m.getExceptionTypes();
		Type[] gxType = m.getGenericExceptionTypes();
		for (int i = 0; i < xType.length; i++) {
		    out.format(fmt,"ExceptionType", xType[i]);
		    out.format(fmt,"GenericExceptionType", gxType[i]);
		}
	    }

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}
```

这里的输出 Class.getConstructor()是具有参数化类型和可变数量参数的方法的示例。

```Java
$ java MethodSpy java.lang.Class getConstructor
public java.lang.reflect.Constructor<T> java.lang.Class.getConstructor
  (java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,
  java.lang.SecurityException
              ReturnType: class java.lang.reflect.Constructor
       GenericReturnType: java.lang.reflect.Constructor<T>
           ParameterType: class [Ljava.lang.Class;
    GenericParameterType: java.lang.Class<?>[]
           ExceptionType: class java.lang.NoSuchMethodException
    GenericExceptionType: class java.lang.NoSuchMethodException
           ExceptionType: class java.lang.SecurityException
    GenericExceptionType: class java.lang.SecurityException
```

这是源代码中方法的实际声明：

`public Constructor <T> getConstructor（Class <？> ... parameterTypes）`

首先请注意，返回和参数类型是通用的。 Method.getGenericReturnType()将查询 类文件中的签名属性（如果存在）。如果该属性不可用，则它会回退到 Method.getReturnType()引用泛型不会改变的情况。反射中具有某些Foo值的名称的其他方法也是类似地实现的。getGenericFoo()

接下来，请注意最后一个（也是唯一的）参数parameterType是类型的变量arity（具有可变数量的参数）java.lang.Class。它表示为类型的单维数组java.lang.Class。这可以java.lang.Class通过调用 显式地显示一个数组来区分Method.isVarArgs()。返回值的语法在Method.get*Types()中描述 Class.getName()。

以下示例说明了具有泛型返回类型的方法。

```Java
$ java MethodSpy java.lang.Class cast
public T java.lang.Class.cast(java.lang.Object)
              ReturnType: class java.lang.Object
       GenericReturnType: T
           ParameterType: class java.lang.Object
    GenericParameterType: class java.lang.Object
```

Class.cast()报告方法的泛型返回类型 是java.lang.Object因为泛型是通过类型擦除实现的，它在编译期间删除有关泛型类型的所有信息。擦除T由以下声明定义 Class：

`public final class Class<T> implements ...`

因此T，在这种情况下，由类型变量的上限代替java.lang.Object。

最后一个示例说明了具有多个重载的方法的输出。

```Java
$ java MethodSpy java.io.PrintStream format
public java.io.PrintStream java.io.PrintStream.format
  (java.util.Locale,java.lang.String,java.lang.Object[])
              ReturnType: class java.io.PrintStream
       GenericReturnType: class java.io.PrintStream
           ParameterType: class java.util.Locale
    GenericParameterType: class java.util.Locale
           ParameterType: class java.lang.String
    GenericParameterType: class java.lang.String
           ParameterType: class [Ljava.lang.Object;
    GenericParameterType: class [Ljava.lang.Object;
public java.io.PrintStream java.io.PrintStream.format
  (java.lang.String,java.lang.Object[])
              ReturnType: class java.io.PrintStream
       GenericReturnType: class java.io.PrintStream
           ParameterType: class java.lang.String
    GenericParameterType: class java.lang.String
           ParameterType: class [Ljava.lang.Object;
    GenericParameterType: class [Ljava.lang.Object;
```

如果发现了相同方法名称的多个重载，则它们都将返回 Class.getDeclaredMethods()。由于format()有两个重载（有一个 Locale和一个没有），两者都显示MethodSpy。

注意：Method.getGenericExceptionTypes()存在是因为实际上可以使用通用异常类型声明方法。但是这很少使用，因为无法捕获通用异常类型。
