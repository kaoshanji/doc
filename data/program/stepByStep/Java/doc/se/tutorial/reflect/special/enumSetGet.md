#   [使用枚举类型获取和设置字段](https://docs.oracle.com/javase/tutorial/reflect/special/enumSetGet.html)

存储枚举的字段使用Field.set()和 设置和检索为任何其他引用类型 Field.get()。有关访问字段的更多信息，请参阅此跟踪的“ 字段”部分。

考虑需要动态修改服务器应用程序中跟踪级别的应用程序，该应用程序通常不允许在运行时进行此更改。假设服务器对象的实例可用。该 SetTrace示例显示了代码如何String将枚举的 表示转换为枚举类型，并检索和设置存储枚举的字段的值。

```Java
import java.lang.reflect.Field;
import static java.lang.System.out;

enum TraceLevel { OFF, LOW, MEDIUM, HIGH, DEBUG }

class MyServer {
    private TraceLevel level = TraceLevel.OFF;
}

public class SetTrace {
    public static void main(String... args) {
	TraceLevel newLevel = TraceLevel.valueOf(args[0]);

	try {
	    MyServer svr = new MyServer();
	    Class<?> c = svr.getClass();
	    Field f = c.getDeclaredField("level");
	    f.setAccessible(true);
	    TraceLevel oldLevel = (TraceLevel)f.get(svr);
	    out.format("Original trace level:  %s%n", oldLevel);

	    if (oldLevel != newLevel) {
 		f.set(svr, newLevel);
		out.format("    New  trace level:  %s%n", f.get(svr));
	    }

        // production code should handle these exceptions more gracefully
	} catch (IllegalArgumentException x) {
	    x.printStackTrace();
	} catch (IllegalAccessException x) {
	    x.printStackTrace();
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	}
    }
}
```

由于枚举常量是单例，因此可以使用==和!=运算符来比较相同类型的枚举常量。

```Java
$ java SetTrace OFF
Original trace level:  OFF
$ java SetTrace DEBUG
Original trace level:  OFF
    New  trace level:  DEBUG
```