#   [创建新数组](https://docs.oracle.com/javase/tutorial/reflect/special/arrayInstance.html)

就像在非反射代码中一样，反射支持通过动态创建任意类型和维度的数组的能力 java.lang.reflect.Array.newInstance()。考虑一下 ArrayCreator，能够动态创建数组的基本解释器。将要解析的语法如下：

```Java
fully_qualified_class_name variable_name [] = 
     {val1，val2，val3，...}
```

假设fully_qualified_class_name表示具有带单个String参数的构造函数的类 。数组的大小由提供的值的数量决定。下面的示例将构造一个数组的实例，fully_qualified_class_name并使用由val1，val2等给出的实例填充其值。（此示例假定您熟悉 Class.getConstructor()和 java.lang.reflect.Constructor.newInstance()。有关反射API的讨论， Constructor请参阅此跟踪的“ 创建新类实例”部分。 ）

```Java
import java.lang.reflect.Array;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.regex.Pattern;
import java.util.regex.Matcher;
import java.util.Arrays;
import static java.lang.System.out;

public class ArrayCreator {
    private static String s = "java.math.BigInteger bi[] = { 123, 234, 345 }";
    private static Pattern p = Pattern.compile("^\\s*(\\S+)\\s*\\w+\\[\\].*\\{\\s*([^}]+)\\s*\\}");

    public static void main(String... args) {
        Matcher m = p.matcher(s);

        if (m.find()) {
            String cName = m.group(1);
            String[] cVals = m.group(2).split("[\\s,]+");
            int n = cVals.length;

            try {
                Class<?> c = Class.forName(cName);
                Object o = Array.newInstance(c, n);
                for (int i = 0; i < n; i++) {
                    String v = cVals[i];
                    Constructor ctor = c.getConstructor(String.class);
                    Object val = ctor.newInstance(v);
                    Array.set(o, i, val);
                }

                Object[] oo = (Object[])o;
                out.format("%s[] = %s%n", cName, Arrays.toString(oo));

            // production code should handle these exceptions more gracefully
            } catch (ClassNotFoundException x) {
                x.printStackTrace();
            } catch (NoSuchMethodException x) {
                x.printStackTrace();
            } catch (IllegalAccessException x) {
                x.printStackTrace();
            } catch (InstantiationException x) {
                x.printStackTrace();
            } catch (InvocationTargetException x) {
                x.printStackTrace();
            }
        }
    }
}
$ java ArrayCreator
java.math.BigInteger [] = [123, 234, 345]

```

上面的例子显示了一种可能需要通过反射创建数组的情况; 即如果直到运行时才知道组件类型。在这种情况下，代码用于 Class.forName()获取所需组件类型的类，然后在设置相应的数组值之前调用特定的构造函数来初始化数组的每个组件。
