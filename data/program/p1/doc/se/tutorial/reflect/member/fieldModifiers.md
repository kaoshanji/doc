#   [检索和分析字段修饰符](https://docs.oracle.com/javase/tutorial/reflect/member/fieldModifiers.html)

-   有几个修饰符可能是字段声明的一部分：

    -   访问修饰符：public，protected，和private
    -   控制运行时行为的特定于字段的修饰符：transient和volatile
    -   修饰符限制为一个实例： static
    -   修饰符禁止修改值： final
    -   注释

该方法 Field.getModifiers()可用于返回表示该字段的声明修饰符集的整数。表示此整数中修饰符的位在中定义 java.lang.reflect.Modifier。

该 FieldModifierSpy示例说明了如何使用给定修饰符搜索字段。它还通过分别调用Field.isSynthetic()和 确定所定位的字段是合成的（编译器生成的）还是枚举常量 Field.isEnumCostant()。

``` Java
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import static java.lang.System.out;

enum Spy { BLACK , WHITE }

public class FieldModifierSpy {
    volatile int share;
    int instance;
    class Inner {}

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    int searchMods = 0x0;
	    for (int i = 1; i < args.length; i++) {
		searchMods |= modifierFromString(args[i]);
	    }

	    Field[] flds = c.getDeclaredFields();
	    out.format("Fields in Class '%s' containing modifiers:  %s%n",
		       c.getName(),
		       Modifier.toString(searchMods));
	    boolean found = false;
	    for (Field f : flds) {
		int foundMods = f.getModifiers();
		// Require all of the requested modifiers to be present
		if ((foundMods & searchMods) == searchMods) {
		    out.format("%-8s [ synthetic=%-5b enum_constant=%-5b ]%n",
			       f.getName(), f.isSynthetic(),
			       f.isEnumConstant());
		    found = true;
		}
	    }

	    if (!found) {
		out.format("No matching fields%n");
	    }

        // production code should handle this exception more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	}
    }

    private static int modifierFromString(String s) {
	int m = 0x0;
	if ("public".equals(s))           m |= Modifier.PUBLIC;
	else if ("protected".equals(s))   m |= Modifier.PROTECTED;
	else if ("private".equals(s))     m |= Modifier.PRIVATE;
	else if ("static".equals(s))      m |= Modifier.STATIC;
	else if ("final".equals(s))       m |= Modifier.FINAL;
	else if ("transient".equals(s))   m |= Modifier.TRANSIENT;
	else if ("volatile".equals(s))    m |= Modifier.VOLATILE;
	return m;
    }
}
```

示例输出如下：

``` Java
$ java FieldModifierSpy FieldModifierSpy volatile
Fields in Class 'FieldModifierSpy' containing modifiers:  volatile
share    [ synthetic=false enum_constant=false ]

$ java FieldModifierSpy Spy public
Fields in Class 'Spy' containing modifiers:  public
BLACK    [ synthetic=false enum_constant=true  ]
WHITE    [ synthetic=false enum_constant=true  ]

$ java FieldModifierSpy FieldModifierSpy\$Inner final
Fields in Class 'FieldModifierSpy$Inner' containing modifiers:  final
this$0   [ synthetic=true  enum_constant=false ]

$ java FieldModifierSpy Spy private static final
Fields in Class 'Spy' containing modifiers:  private static final
$VALUES  [ synthetic=true  enum_constant=false ]
```

请注意，即使它们未在原始代码中声明，也会报告某些字段。这是因为编译器将生成运行时期间所需的一些合成字段。要测试字段是否为合成字段，示例将调用 Field.isSynthetic()。合成字段集依赖于编译器; 但是常用字段包括this$0内部类（即非静态成员类的嵌套类），用于引用最外层的封闭类，$VALUES并由枚举用于实现隐式定义的静态方法values()。未指定合成类成员的名称，并且在所有编译器实现或发行版中可能不相同。这些和其他合成字段将包含在返回Class.getDeclaredFields()但未标识 的数组中 Class.getField()因为合成成员通常不是public。

因为 Field实现了接口 java.lang.reflect.AnnotatedElement，所以可以检索任何运行时注释 java.lang.annotation.RetentionPolicy.RUNTIME。有关获取注释的示例，请参阅“ 检查类修饰符和类型 ”一节。