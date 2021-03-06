#   [识别数组类型](https://docs.oracle.com/javase/tutorial/reflect/special/arrayComponents.html)

可以通过调用来标识数组类型 Class.isArray()。要获得 Class使用此跟踪的“ 检索类对象”部分中描述的方法之一。

该 ArrayFind示例标识指定类中具有数组类型的字段，并报告每个字段的组件类型。

```Java
import java.lang.reflect.Field;
import java.lang.reflect.Type;
import static java.lang.System.out;

public class ArrayFind {
    public static void main(String... args) {
	boolean found = false;
 	try {
	    Class<?> cls = Class.forName(args[0]);
	    Field[] flds = cls.getDeclaredFields();
	    for (Field f : flds) {
 		Class<?> c = f.getType();
		if (c.isArray()) {
		    found = true;
		    out.format("%s%n"
                               + "           Field: %s%n"
			       + "            Type: %s%n"
			       + "  Component Type: %s%n",
			       f, f.getName(), c, c.getComponentType());
		}
	    }
	    if (!found) {
		out.format("No array fields%n");
	    }

        // production code should handle this exception more gracefully
 	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }
}
```

返回值的语法在Class.get*Type()中描述 Class.getName()。[类型名称开头的' '字符数表示数组的维数（即嵌套深度）。

输出样本如下。用户输入以斜体显示。一个原始类型的数组byte：

```Java
$java ArrayFind java.nio.ByteBuffer
final byte[] java.nio.ByteBuffer.hb
           Field: hb
            Type: class [B
  Component Type: byte
```

引用类型数组 StackTraceElement：

```Java
$ java ArrayFind java.lang.Throwable
private java.lang.StackTraceElement[] java.lang.Throwable.stackTrace
           Field: stackTrace
            Type: class [Ljava.lang.StackTraceElement;
  Component Type: class java.lang.StackTraceElement
```

predefined是引用类型的一维阵列 java.awt.Cursor和cursorProperties是引用类型的二维数组 String：

```Java
$ java ArrayFind java.awt.Cursor
protected static java.awt.Cursor[] java.awt.Cursor.predefined
           Field: predefined
            Type: class [Ljava.awt.Cursor;
  Component Type: class java.awt.Cursor
static final java.lang.String[][] java.awt.Cursor.cursorProperties
           Field: cursorProperties
            Type: class [[Ljava.lang.String;
  Component Type: class [Ljava.lang.String;
```