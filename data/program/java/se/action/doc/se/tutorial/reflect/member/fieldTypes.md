-   [获取字段类型](https://docs.oracle.com/javase/tutorial/reflect/member/fieldTypes.html)

字段可以是原始字段或引用类型。有八种基本类型：boolean，byte，short，int，long，char，float，和double。引用类型是java.lang.Object包含接口，数组和枚举类型的直接或间接子类的任何内容 。

该FieldSpy示例在给定完全限定的二进制类名称和字段名称的 情况下打印字段的类型和泛型类型。

``` Java
import java.lang.reflect.Field;
import java.util.List;

public class FieldSpy<T> {
    public boolean[][] b = {{ false, false }, { true, true } };
    public String name  = "Alice";
    public List<Integer> list;
    public T val;

    public static void main(String... args) {
	try {
	    Class<?> c = Class.forName(args[0]);
	    Field f = c.getField(args[1]);
	    System.out.format("Type: %s%n", f.getType());
	    System.out.format("GenericType: %s%n", f.getGenericType());

        // production code should handle these exceptions more gracefully
	} catch (ClassNotFoundException x) {
	    x.printStackTrace();
	} catch (NoSuchFieldException x) {
	    x.printStackTrace();
	}
    }
}
```

示例输出检索三个公共字段的类型在这个类（b，name，和参数化类型list），如下。用户输入以斜体显示。

``` Java
$ java FieldSpy FieldSpy b
Type: class [[Z
GenericType: class [[Z
$ java FieldSpy FieldSpy name
Type: class java.lang.String
GenericType: class java.lang.String
$ java FieldSpy FieldSpy list
Type: interface java.util.List
GenericType: java.util.List<java.lang.Integer>
$ java FieldSpy FieldSpy val
Type: class java.lang.Object
GenericType: T
```

该字段的类型b是布尔值的二维数组。类型名称的语法在中描述 Class.getName()。

val报告字段的类型是java.lang.Object因为泛型是通过类型擦除实现的，它在编译期间删除有关泛型类型的所有信息。因此T，在这种情况下，由类型变量的上限代替java.lang.Object。

Field.getGenericType()将查询 类文件中的签名属性（如果存在）。如果该属性不可用，则它会回退到 Field.getType()引用泛型不会改变的情况。使用名称反映Foo的某些值的其他方法也是类似地实现的。getGenericFoo