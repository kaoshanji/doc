#   [故障排除](https://docs.oracle.com/javase/tutorial/reflect/class/classTrouble.html)

以下示例显示了在反射类时可能遇到的典型错误。

`## 编译器警告：“注意：...使用未经检查或不安全的操作”`

调用方法时，将检查参数值的类型并进行转换。 ClassWarning调用 getMethod()以导致典型的未经检查的转换警告：

```
import java.lang.reflect.Method;

public class ClassWarning {
    void m() {
	try {
	    Class c = ClassWarning.class;
	    Method m = c.getMethod("m");  // warning

        // production code should handle this exception more gracefully
	} catch (NoSuchMethodException x) {
    	    x.printStackTrace();
    	}
    }
}
$ javac ClassWarning.java
Note: ClassWarning.java uses unchecked or unsafe operations.
Note: Recompile with -Xlint:unchecked for details.
$ javac -Xlint:unchecked ClassWarning.java
ClassWarning.java:6: warning: [unchecked] unchecked call to getMethod
  (String,Class<?>...) as a member of the raw type Class
Method m = c.getMethod("m");  // warning
                      ^
1 warning
```

许多图书馆方法都使用通用声明进行了改进，其中包括几个 Class。由于c声明为原始类型（没有类型参数）且相应的参数 getMethod()是参数化类型，因此会发生未经检查的转换。编译器需要生成警告。（请参阅Java语言规范，Java SE 7 Edition，未经检查的转换和方法调用转换部分。）

有两种可能的解决方案。修改声明c以包含适当的泛型类型更为可取。在这种情况下，声明应该是：

```
Class<?> c = warn.getClass();
```

或者，可以使用@SuppressWarnings有问题的语句之前的预定义注释明确地抑制警告 。

```
Class c = ClassWarning.class;
@SuppressWarnings("unchecked")
Method m = c.getMethod("m");  
// warning gone
```

##  构造函数不可访问时的InstantiationException

Class.newInstance()InstantiationException如果尝试创建类的新实例并且零参数构造函数不可见，则抛出一个 。该 ClassTrouble示例说明了生成的堆栈跟踪。

``` Java
class Cls {
    private Cls() {}
}

public class ClassTrouble {
    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName("Cls");
	    c.newInstance();  // InstantiationException

        // production code should handle these exceptions more gracefully
	} catch (InstantiationException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}
$ java ClassTrouble
java.lang.IllegalAccessException: Class ClassTrouble can not access a member of
  class Cls with modifiers "private"
        at sun.reflect.Reflection.ensureMemberAccess(Reflection.java:65)
        at java.lang.Class.newInstance0(Class.java:349)
        at java.lang.Class.newInstance(Class.java:308)
        at ClassTrouble.main(ClassTrouble.java:9)
```

[Class.newInstance()](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html#newInstance--)表现与new关键字非常相似，但由于同样的原因new会失败。反思的典型解决方案是利用[java.lang.reflect.AccessibleObject](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/AccessibleObject.html)提供抑制访问控制检查能力的 类; 但是，这种方法不起作用，因为 java.lang.Class没有扩展 AccessibleObject。唯一的解决方案是修改要使用的Constructor.newInstance()扩展 代码 AccessibleObject。
