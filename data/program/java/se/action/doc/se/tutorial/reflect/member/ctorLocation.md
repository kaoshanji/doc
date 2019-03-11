#   [寻找构造函数](https://docs.oracle.com/javase/tutorial/reflect/member/ctorLocation.html)

构造函数声明包括名称，修饰符，参数和可抛出异常列表。本 java.lang.reflect.Constructor类提供了一种方法来获取此信息。

该 ConstructorSift示例说明了如何在类的声明构造函数中搜索具有给定类型参数的构造函数。

``` Java
import java.lang.reflect.Constructor;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class ConstructorSift {
    public static void main(String... args) {
	try {
	    Class<?> cArg = Class.forName(args[1]);

	    Class<?> c = Class.forName(args[0]);
	    Constructor[] allConstructors = c.getDeclaredConstructors();
	    for (Constructor ctor : allConstructors) {
		Class<?>[] pType  = ctor.getParameterTypes();
		for (int i = 0; i < pType.length; i++) {
		    if (pType[i].equals(cArg)) {
			out.format("%s%n", ctor.toGenericString());

			Type[] gpType = ctor.getGenericParameterTypes();
			for (int j = 0; j < gpType.length; j++) {
			    char ch = (pType[j].equals(cArg) ? '*' : ' ');
			    out.format("%7c%s[%d]: %s%n", ch,
				       "GenericParameterType", j, gpType[j]);
			}
			break;
		    }
		}
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}
```


Method.getGenericParameterTypes()将查询 类文件中的签名属性（如果存在）。如果该属性不可用，则它会回退到 Method.getParameterType()引用泛型不会改变的情况。反射中具有某些Foo值的名称的其他方法也是类似地实现的。返回值的语法在中描述 。getGenericFoo()Method.get*Types()Class.getName()

以下是java.util.Formatter具有 Locale参数的所有构造函数的输出 。
```Java

$ java ConstructorSift java.util.Formatter java.util.Locale
public
java.util.Formatter(java.io.OutputStream,java.lang.String,java.util.Locale)
throws java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.io.OutputStream
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale
public java.util.Formatter(java.lang.String,java.lang.String,java.util.Locale)
throws java.io.FileNotFoundException,java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.lang.String
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale
public java.util.Formatter(java.lang.Appendable,java.util.Locale)
       GenericParameterType[0]: interface java.lang.Appendable
      *GenericParameterType[1]: class java.util.Locale
public java.util.Formatter(java.util.Locale)
      *GenericParameterType[0]: class java.util.Locale
public java.util.Formatter(java.io.File,java.lang.String,java.util.Locale)
throws java.io.FileNotFoundException,java.io.UnsupportedEncodingException
       GenericParameterType[0]: class java.io.File
       GenericParameterType[1]: class java.lang.String
      *GenericParameterType[2]: class java.util.Locale
```

在下一个例子中示出了输出如何搜索的类型的参数char[]在 String。

```Java
$ java ConstructorSift java.lang.String "[C"
java.lang.String(int,int,char[])
       GenericParameterType[0]: int
       GenericParameterType[1]: int
      *GenericParameterType[2]: class [C
public java.lang.String(char[],int,int)
      *GenericParameterType[0]: class [C
       GenericParameterType[1]: int
       GenericParameterType[2]: int
public java.lang.String(char[])
      *GenericParameterType[0]: class [C
```

表达可接受的引用和基本类型数组的语法 Class.forName()如下所述 Class.getName()。请注意，第一个列出的构造函数package-private不是public。返回它是因为示例代码使用 Class.getDeclaredConstructors()而不是 Class.getConstructors()，它只返回public构造函数。

此示例显示搜索变量arity（具有可变数量的参数）的参数需要使用数组语法：
```Java
$ java ConstructorSift java.lang.ProcessBuilder "[Ljava.lang.String;"
public java.lang.ProcessBuilder(java.lang.String[])
      *GenericParameterType[0]: class [Ljava.lang.String;
```

这是ProcessBuilder源代码中构造函数的实际声明 ：
```Java
public ProcessBuilder(String... command)
```

该参数表示为类型的单维数组java.lang.String。这可以java.lang.String通过调用 显式地显示一个数组来区分Constructor.isVarArgs()。

最后一个示例报告了使用泛型参数类型声明的构造函数的输出：
```Java
$ java ConstructorSift java.util.HashMap java.util.Map
public java.util.HashMap(java.util.Map<? extends K, ? extends V>)
      *GenericParameterType[0]: java.util.Map<? extends K, ? extends V>
```

可以以与方法类似的方式为构造函数检索异常类型。有关更多详细信息，请参阅“ 获取方法类型信息”部分中MethodSpy描述的 示例。
