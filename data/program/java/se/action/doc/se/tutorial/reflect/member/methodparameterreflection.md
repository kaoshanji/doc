#   [获取方法参数的名称](https://docs.oracle.com/javase/tutorial/reflect/member/methodparameterreflection.html)


您可以使用该方法获取任何方法或构造函数的形式参数的名称 java.lang.reflect.Executable.getParameters。（类 Method和 Constructor扩展类 Executable，因此继承该方法Executable.getParameters。）但是，.class默认情况下，文件不存储形式参数名称。这是因为许多生成和使用类文件的工具可能不会期望.class包含参数名称的文件具有更大的静态和动态占用空间。特别是，这些工具必须处理更大的.class文件，而Java虚拟机（JVM）将使用更多的内存。此外，某些参数名称（如secretor password）可能会公开有关安全敏感方法的信息。

要将正式参数名称存储在特定.class文件中，从而使Reflection API能够检索形式参数名称，请使用编译器-parameters选项编译源文件javac。

该 MethodParameterSpy示例说明了如何检索给定类的所有构造函数和方法的形式参数的名称。该示例还打印有关每个参数的其他信息。

以下命令打印类的构造函数和方法的形式参数名称 ExampleMethods。注：请记住，编译示例ExampleMethods与-parameters编译器选项：

`java MethodParameterSpy ExampleMethods`

此命令打印以下内容：
```Java 

Number of constructors: 1

Constructor #1
public ExampleMethods()

Number of declared constructors: 1

Declared constructor #1
public ExampleMethods()

Number of methods: 4

Method #1
public boolean ExampleMethods.simpleMethod(java.lang.String,int)
             Return type: boolean
     Generic return type: boolean
         Parameter class: class java.lang.String
          Parameter name: stringParam
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false
         Parameter class: int
          Parameter name: intParam
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false

Method #2
public int ExampleMethods.varArgsMethod(java.lang.String...)
             Return type: int
     Generic return type: int
         Parameter class: class [Ljava.lang.String;
          Parameter name: manyStrings
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false

Method #3
public boolean ExampleMethods.methodWithList(java.util.List<java.lang.String>)
             Return type: boolean
     Generic return type: boolean
         Parameter class: interface java.util.List
          Parameter name: listParam
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false

Method #4
public <T> void ExampleMethods.genericMethod(T[],java.util.Collection<T>)
             Return type: void
     Generic return type: void
         Parameter class: class [Ljava.lang.Object;
          Parameter name: a
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false
         Parameter class: interface java.util.Collection
          Parameter name: c
               Modifiers: 0
            Is implicit?: false
        Is name present?: true
           Is synthetic?: false
```

该MethodParameterSpy示例使用以下Parameter类中的方法 ：
-   getType: 返回Class标识参数的声明类型的 对象.
-   getName: 返回参数的名称。如果参数的名称存在，则此方法返回.class文件提供的名称。否则，此方法合成表单的名称，其中是声明参数的方法的描述符中的参数的索引。argNN

例如，假设您编译了该类ExampleMethods而未指定-parameters编译器选项。该示例MethodParameterSpy将为该方法打印以下内容ExampleMethods.simpleMethod：

```Java

public boolean ExampleMethods.simpleMethod(java.lang.String,int)
             Return type: boolean
     Generic return type: boolean
         Parameter class: class java.lang.String
          Parameter name: arg0
               Modifiers: 0
            Is implicit?: false
        Is name present?: false
           Is synthetic?: false
         Parameter class: int
          Parameter name: arg1
               Modifiers: 0
            Is implicit?: false
        Is name present?: false
           Is synthetic?: false
```

-   getModifiers : 返回一个整数，表示形式参数拥有的各种特征。如果适用于形式参数，则此值是以下值的总和：

|值（十进制）	|值（十六进制	|描述|
|------|-----|------|
|16	0×0010	|声明了形式参数 |final|
|4096	|为0x1000	|形式参数是合成的。或者，您可以调用该方法isSynthetic。|
|32768	|为0x8000	|该参数在源代码中隐式声明。或者，您可以调用该方法isImplicit|

-   isImplicit: true如果在源代码中隐式声明此参数，则返回。有关详细信息，请参阅隐式和合成参数部分。
-   isNamePresent: true如果参数根据.class文件具有名称，则返回。
-   isSynthetic: true如果在源代码中既未隐式声明也未显式声明此参数，则返回。有关详细信息，请参阅隐式和合成参数部分。

----

##  隐式和合成参数

如果未明确写入某些构造，则会在源代码中隐式声明这些构造。例如，该 ExampleMethods示例不包含构造函数。默认构造函数是为它隐式声明的。该MethodParameterSpy示例打印有关隐式声明的构造函数的信息ExampleMethods：

Number of declared constructors: 1
```Java
public ExampleMethods()
```
请考虑以下摘录 MethodParameterExamples:

```Java
public class MethodParameterExamples {
    public class InnerClass { }
}
```

该类InnerClass是非静态 嵌套类或内部类。内部类的构造函数也是隐式声明的。但是，此构造函数将包含一个参数。当Java编译器编译时InnerClass，它会创建一个.class代表类似于以下代码的文件：
```Java
public class MethodParameterExamples {
    public class InnerClass {
        final MethodParameterExamples parent;
        InnerClass(final MethodParameterExamples this$0) {
            parent = this$0; 
        }
    }
}
```

该InnerClass构造包含其类型为包围类的参数InnerClass，这是MethodParameterExamples。因此，该示例MethodParameterExamples打印以下内容：

```Java
public MethodParameterExamples$InnerClass(MethodParameterExamples)
         Parameter class: class MethodParameterExamples
          Parameter name: this$0
               Modifiers: 32784
            Is implicit?: true
        Is name present?: true
           Is synthetic?: false
```

因为InnerClass隐式声明了类的构造函数，所以它的参数也是隐式的。

`注意`：

-   Java编译器为内部类的构造函数创建形式参数，以使编译器能够将创建表达式中的引用（表示立即封闭的实例）传递给成员类的构造函数。
-   值32784表示InnerClass构造函数的参数既是final（16），也是隐式（32768）。
-   Java编程语言允许带有美元符号（$）的变量名称; 但按照惯例，美元符号不会用于变量名称。

如果Java编译器发出的构造与源代码中显式或隐式声明的构造不对应，则将其标记为合成构造，除非它们是类初始化方法。合成构造是由编译器生成的工件，它们在不同的实现之间变化。请考虑以下摘录 MethodParameterExamples：

``` Java
public class MethodParameterExamples {
    enum Colors {
        RED, WHITE;
    }
}
```

当Java编译器遇到enum构造时，它会创建几个与.class文件结构兼容的方法，并提供构造的预期功能enum。例如，Java编译器将为构造创建一个.class文件，该文件表示类似于以下内容的代码：enumColors

```Java
final class Colors extends java.lang.Enum<Colors> {
    public final static Colors RED = new Colors("RED", 0);
    public final static Colors BLUE = new Colors("WHITE", 1);
 
    private final static values = new Colors[]{ RED, BLUE };
 
    private Colors(String name, int ordinal) {
        super(name, ordinal);
    }
 
    public static Colors[] values(){
        return values;
    }
 
    public static Colors valueOf(String name){
        return (Colors)java.lang.Enum.valueOf(Colors.class, name);
    }
}
```

Java编译器创建这三个构造函数和方法enum的结构：Colors(String name, int ordinal)，Colors[] values()，和Colors valueOf(String name)。方法values和valueOf隐式声明。因此，它们的形式参数名也被隐式声明。

该enum构造Colors(String name, int ordinal)是一个默认的构造函数，它是隐式声明。然而，此构造（的形式参数name和ordinal）都不会隐式声明。由于这些形式参数既未明确声明也未隐式声明，因此它们是合成的。（构造的默认构造函数的形式参数enum不是隐式声明的，因为不同的编译器不需要在这个构造函数的形式上达成一致;另一个Java编译器可能为它指定不同的形式参数。当编译器编译使用enum常量的表达式时，它们仅依赖于在enum构造的公共静态字段上，它们是隐式声明的，而不是它们的构造函数或者这些常量是如何初始化的。）

因此，该示例MethodParameterExample打印有关enum构造的以下内容Colors：

enum Colors:

Number of constructors: 0

Number of declared constructors: 1

Declared constructor #1
```Java
private MethodParameterExamples$Colors()
         Parameter class: class java.lang.String
          Parameter name: $enum$name
               Modifiers: 4096
            Is implicit?: false
        Is name present?: true
           Is synthetic?: true
         Parameter class: int
          Parameter name: $enum$ordinal
               Modifiers: 4096
            Is implicit?: false
        Is name present?: true
           Is synthetic?: true

Number of methods: 2

Method #1
public static MethodParameterExamples$Colors[]
    MethodParameterExamples$Colors.values()
             Return type: class [LMethodParameterExamples$Colors;
     Generic return type: class [LMethodParameterExamples$Colors;

Method #2
public static MethodParameterExamples$Colors
    MethodParameterExamples$Colors.valueOf(java.lang.String)
             Return type: class MethodParameterExamples$Colors
     Generic return type: class MethodParameterExamples$Colors
         Parameter class: class java.lang.String
          Parameter name: name
               Modifiers: 32768
            Is implicit?: true
        Is name present?: true
           Is synthetic?: false
```

有关隐式声明的构造的更多信息，请参阅Java语言规范，包括在Reflection API中显示为隐式的参数。



