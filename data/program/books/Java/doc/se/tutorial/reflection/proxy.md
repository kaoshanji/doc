#   [动态代理类](https://docs.oracle.com/javase/8/docs/technotes/guides/reflection/proxy.html)

##  内容

-   简介
-   动态代理API 
-   序列化
-   示例

----

##  介绍

动态代理类是实现在运行时指定的接口列表的类，使得通过对类的一个实例的一个接口方法调用将被编码，并通过一个统一的接口分派给另一个对象。因此，动态代理类可用于为接口列表创建类型安全的代理对象，而无需预生成代理类，例如使用编译时工具。动态代理类的实例上的方法调用被分派到实例的调用处理程序中的单个方法，并且它们使用java.lang.reflect.Method标识被调用方法的对象和Object 包含参数的类型数组进行编码 。

动态代理类对于需要在呈现接口API的对象上提供类型安全反射调度调用的应用程序或库非常有用。例如，应用程序可以使用动态代理类来创建实现多个任意事件侦听器接口的对象java.util.EventListener- 扩展的接口- 以统一的方式处理不同类型的各种事件，例如通过记录所有此类事件到一个文件。

----

##  动态代理类API

动态代理类（简称为一个代理类下文）是创建类时，它实现在运行时指定的接口列表的类。

代理接口使得由代理类实现的接口。

一个代理实例是一个实例代理类。

### 创建代理类

使用类java.lang.reflect.Proxy的静态方法创建代理类及其实例。

给定类加载器和接口数组，该Proxy.getProxyClass方法返回java.lang.Class代理类的 对象。代理类将在指定的类加载器中定义，并将实现所有提供的接口。如果已经在类加载器中定义了相同的接口排列的代理类，则将返回现有的代理类; 否则，将动态生成这些接口的代理类，并在类加载器中定义。

可以传递给参数的参数有几个限制Proxy.getProxyClass：

-   数组Class中的所有对象都 interfaces必须表示接口，而不是类或基本类型。
-   interfaces数组中没有两个元素可以引用相同的Class对象。
-   所有接口类型必须通过指定的类加载器按名称可见。换句话说，对于类加载器 cl和每个接口i，以下表达式必须为true：
        `Class.forName（i.getName（），false，cl）== i`
-   所有非公共接口必须位于同一个包中; 否则，代理类无法实现所有接口，无论它定义在哪个包中。
-   对于具有相同签名的指定接口的任何成员方法集：
    -   如果任何方法的返回类型是基本类型或void，则所有方法必须具有相同的返回类型。
    -   否则，其中一个方法必须具有可分配给其余方法的所有返回类型的返回类型。
-   生成的代理类不得超过虚拟机对类强加的任何限制。例如，VM可以将类可以实现的接口数量限制为65535; 在这种情况下，interfaces数组的大小不得超过65535。

如果违反任何这些限制， Proxy.getProxyClass将抛出一个 IllegalArgumentException。如果 interfaces数组参数或其任何元素是 null，NullPointerException则将抛出a。

请注意，指定代理接口的顺序很重要：对具有相同接口组合但顺序不同的代理类的两个请求将导致两个不同的代理类。代理类通过其代理接口的顺序来区分，以便在两个或更多个代理接口共享具有相同名称和参数签名的方法的情况下提供确定性方法调用编码; 在以下标题为多个代理接口中的重复方法的部分中更详细地描述了这种推理。

因此，每次Proxy.getProxyClass使用相同的类加载器和接口列表调用时都不需要生成新的代理类，动态代理类API的实现应该保留生成的代理类的缓存，由相应的加载器和接口键入名单。实现时应注意不要引用类加载器，接口和代理类，以防止类加载器及其所有类在适当时被垃圾收集。

### 代理类属性

代理类具有以下属性：

-   代理类是公共的，最终的，而不是抽象的。
-   未指定代理类的非限定名称。"$Proxy"但是，以字符串开头的类名空间是为代理类保留的。
-   代理类扩展java.lang.reflect.Proxy。
-   代理类以相同的顺序实现其创建时指定的接口。
-   如果代理类实现非公共接口，则它将在与该接口相同的包中定义。否则，代理类的包也未指定。请注意，程序包密封不会阻止在运行时在特定程序包中成功定义代理类，也不会在同一个类加载器中定义类，也不会在特定程序集中定义相同的程序包。
-   由于代理类实现了在其创建时指定的所有接口，因此getInterfaces对其 Class对象进行调用将返回包含相同接口列表的数组（按其创建时指定的顺序），getMethods对其Class对象进行调用将返回包含的Method对象数组这些接口中的所有方法，并且调用 getMethod将在代理接口中找到预期的方法。
-   Proxy.isProxyClass如果传递一个代理类 - 返回Proxy.getProxyClass的类或返回的对象的类，则该方法将返回true Proxy.newProxyInstance，否则返回false。这种方法的可靠性对于使用它来做出安全决策的能力很重要，因此它的实现不应仅仅测试相关类是否扩展 java.lang.reflect.Proxy。
-   java.security.ProtectionDomain代理类的是相同由引导类装载程序装载系统类，如java.lang.Object，因为是由受信任的系统代码生成代理类的代码。通常会授予此保护域 java.security.AllPermission。

### 创建代理实例

每个代理类都有一个公共构造函数，它接受一个参数，即接口的实现InvocationHandler。

每个代理实例都有一个关联的调用处理程序对象，该对象是传递给其构造函数的对象。不必使用反射API来访问公共构造函数，也可以通过调用Proxy.newProxyInstance方法来创建代理实例，该 方法将调用Proxy.getProxyClass和调用构造函数的操作与调用处理程序相结合。 Proxy.newProxyInstance抛出 IllegalArgumentException的原因与此相同 Proxy.getProxyClass。

### 代理实例属性

代理实例具有以下属性：

-   给定代理实例proxy和其代理类实现的接口之一Foo，以下表达式将返回true：
        `proxy instanceof Foo`
-   并且以下强制转换操作将成功（而不是抛出ClassCastException）：
        `(Foo) proxy`
-   静态Proxy.getInvocationHandler方法将返回与作为其参数传递的代理实例关联的调用处理程序。如果传递给的对象 Proxy.getInvocationHandler不是代理实例，则IllegalArgumentException抛出一个。
-   代理实例上的接口方法调用将被编码并调度到调用处理程序的 invoke方法，如下所述。

代理实例本身将作为第一个参数传递invoke，它的类型的Object。

传递给的第二个参数invoke将是 java.lang.reflect.Method与代理实例上调用的接口方法对应的实例。Method对象的声明类将是声明方法的接口，它可以是代理接口继承方法的代理接口的超接口。

传递给的第三个参数invoke将是一个对象数组，其中包含代理实例上方法调用中传递的参数值。原始类型的参数包装在适当的原始包装类的实例中，例如java.lang.Integer或 java.lang.Boolean。该invoke方法的实现 可以自由修改该数组的内容。

在返回值invoke的方法将成为代理实例的方法调用的返回值。如果接口方法的声明返回值是基本类型，则返回的值invoke必须是相应原始包装类的实例; 否则，它必须是可分配给声明的返回类型的类型。如果invokeis 返回的值null并且接口方法的返回类型是原始的，则NullPointerException代理实例上的方法调用将抛出a 。如果返回的值 invoke与上面描述的方法声明的返回类型不兼容，ClassCastException则代理实例将抛出a 。

如果invoke方法抛出异常，则代理实例上的方法调用也会抛出异常。异常的类型必须可以分配给在接口方法的签名中声明的任何异常类型，或者分配给未经检查的异常类型 java.lang.RuntimeException或 java.lang.Error。如果抛出的checked异常 invoke不能分配给throws接口方法子句中声明的任何异常类型，则UndeclaredThrowableException 代理实例上的方法调用将抛出异常。该 UndeclaredThrowableException会与被抛出的异常构造invoke 方法。

-   调用hashCode， equals或toString声明的方法 java.lang.Object上的代理实例将被编码并分派到调用处理程序的invoke 相同的方式的方法接口方法调用进行编码和调度，如上所述。Method传递给对象的声明类invoke将是java.lang.Object。继承自代理实例的其他公共方法java.lang.Object不会被代理类覆盖，因此这些方法的调用行为与它们的实例相同java.lang.Object。

### 方法在多个代理接口中重复

当代理类的两个或多个接口包含具有相同名称和参数签名的方法时，代理类的接口的顺序变得很重要。在代理实例上调用此类重复方法时，Method 传递给调用处理程序的对象不一定是其声明类可从调用代理方法的接口的引用类型分配的对象。存在此限制是因为生成的代理类中的相应方法实现无法确定通过哪个接口调用它。因此，当在代理实例上调用重复方法时，Method在包含该方法的最前面接口中的方法的对象（直接或通过超接口继承）在代理类的接口列表中传递给调用处理程序的 invoke方法，而不管方法调用发生的引用类型如何。

如果代理接口包含具有相同的名称和参数签名的方法hashCode， equals或toString方法 java.lang.Object，当这种方法在代理实例调用时，Method传递到调用处理程序对象将java.lang.Object作为其声明类。换句话说，公共的非final方法 java.lang.Object逻辑上位于所有代理接口之前，用于确定Method 传递给调用处理程序的对象。

还要注意，当将重复方法分派给调用处理程序时，该invoke方法可能只抛出可在其 调用的所有代理接口中分配给throws方法子句中的一个异常类型的已检查异常类型。如果该 方法抛出一个已检查的异常，该异常不能分配给该方法在其中一个可以调用的代理接口中声明的任何异常类型，则代理实例上的调用将抛出未经检查的异常。此限制意味着并非所有通过调用传递给方法的对象返回的异常类型 都必须通过该方法成功抛出。invokeUndeclaredThrowableExceptiongetExceptionTypesMethodinvokeinvoke

----

##  序列化

从java.lang.reflect.Proxyimplements开始 java.io.Serializable，代理实例可以序列化，如本节所述。但是，如果代理实例包含不可分配的调用处理程序 java.io.Serializable，则在java.io.NotSerializableException将此类实例写入a时 将抛出a java.io.ObjectOutputStream。请注意，对于代理类，实现java.io.Externalizable与序列化具有相同的实现效果 java.io.Serializable：接口的方法writeExternal 和readExternal方法 Externalizable永远不会在代理实例（或调用处理程序）上作为其序列化过程的一部分进行调用。与所有Class对象一样，Class代理类的 对象始终可序列化。

代理类没有序列化字段和 serialVersionUID的0L。换句话说，当Class代理类的对象传递给静态lookup方法时 java.io.ObjectStreamClass，返回的 ObjectStreamClass实例将具有以下属性：

-   调用其getSerialVersionUID方法将返回0L。
-   调用其getFields方法将返回一个长度为零的数组。
-   getField使用任何String参数调用其方法 将返回null。

对象序列化的流协议支持名为的类型代码TC_PROXYCLASSDESC，它是流格式的语法中的终端符号; 其类型和值由java.io.ObjectStreamConstants接口中的以下常量字段定义 ：

    `final static byte TC_PROXYCLASSDESC = (byte)0x7D;`

语法还包括以下两个规则，第一个是原始newClassDesc 规则的备用扩展：

newClassDesc：
        TC_PROXYCLASSDESC newHandle proxyClassDescInfo

proxyClassDescInfo：
        (int)<count> proxyInterfaceName [count] classAnnotation superClassDesc

proxyInterfaceName：
        (utf)

当ObjectOutputStream序列化作为代理类的类的类描述符时，通过将其Class对象传递给Proxy.isProxyClass方法来 确定，它使用 TC_PROXYCLASSDESC类型代码而不是 TC_CLASSDESC遵循上述规则。在proxyClassDescInfo的扩展中，proxyInterfaceName项的序列是 代理类实现的所有接口的名称，按照通过调用对象getInterfaces上的方法返回它们的顺序Class。该classAnnotation和 superClassDesc项目具有相同的含义，因为他们在做 classDescInfo规则。对于代理类，superClassDesc 是它的超类的类描述符， java.lang.reflect.Proxy; 包括此描述符允许Proxy代理实例的类的序列化表示的演变。

对于非代理类，ObjectOutputStream调用其受保护的annotateClass方法以允许子类将自定义数据写入特定类的流。对于代理类，使用代理类的对象调用annotateClass以下方法：java.io.ObjectOutputStreamClass

    `protected void annotateProxyClass(Class cl) throws IOException;`

annotateProxyClassin 的默认实现ObjectOutputStream什么都不做。

当ObjectInputStream遇到的类型的代码 TC_PROXYCLASSDESC，它反序列用于从所述流的代理类，如上所述格式化类描述符。调用以下方法而不是调用其resolveClass 方法来解析Class类描述符的对象 java.io.ObjectInputStream：

    `protected Class resolveProxyClass(String[] interfaces)
        throws IOException, ClassNotFoundException;`

在代理类描述符中反序列化的接口名称列表作为interfaces参数传递给resolveProxyClass。

resolveProxyClassin 的默认实现ObjectInputStream返回使用参数中指定的接口Proxy.getProxyClass的Class对象 列表 调用的结果 interfaces。Class用于每个接口名称的对象i是通过调用重新调整的值

        `Class.forName（i，false，loader）`

其中loader是执行堆栈中的第一个非null类加载器，或者堆栈中null是否没有非null类加载器。这是由方法的默认行为所做的相同的类加载器选择resolveClass。同样的值loader也是传递给的类加载器 Proxy.getProxyClass。如果 Proxy.getProxyClass抛出 IllegalArgumentException，resolveClass 将抛出一个ClassNotFoundException包含 IllegalArgumentException。

由于代理类从不具有自己的可序列化字段，因此代理实例的流表示中的 classdata []完全由其超类的实例数据组成 java.lang.reflect.Proxy。Proxy有一个可序列化的字段，h其中包含代理实例的调用处理程序。

----

##  例子

下面是一个简单的示例，它在实现任意接口列表的对象上的方法调用之前和之后打印出一条消息：

```
public interface Foo {
    Object bar(Object obj) throws BazException;
}

public class FooImpl implements Foo {
    Object bar(Object obj) throws BazException {
        // ...
    }
}

public class DebugProxy implements java.lang.reflect.InvocationHandler {

    private Object obj;

    public static Object newInstance(Object obj) {
        return java.lang.reflect.Proxy.newProxyInstance(
            obj.getClass().getClassLoader(),
            obj.getClass().getInterfaces(),
            new DebugProxy(obj));
    }

    private DebugProxy(Object obj) {
        this.obj = obj;
    }

    public Object invoke(Object proxy, Method m, Object[] args)
        throws Throwable
    {
        Object result;
        try {
            System.out.println("before method " + m.getName());
            result = m.invoke(obj, args);
        } catch (InvocationTargetException e) {
            throw e.getTargetException();
        } catch (Exception e) {
            throw new RuntimeException("unexpected invocation exception: " +
                                       e.getMessage());
        } finally {
            System.out.println("after method " + m.getName());
        }
        return result;
    }
}

```
构造接口DebugProxy的实现Foo并调用其中一个方法：

    `Foo foo =（Foo）DebugProxy.newInstance（new FooImpl（））;
    foo.bar（NULL）;`

下面是一个实用程序调用处理程序类的示例，它为从中继承的方法提供默认代理行为， java.lang.Object并根据调用方法的接口实现将某些代理方法调用委派给不同的对象：
```
import java.lang.reflect.*;

public class Delegator implements InvocationHandler {

    // preloaded Method objects for the methods in java.lang.Object
    private static Method hashCodeMethod;
    private static Method equalsMethod;
    private static Method toStringMethod;
    static {
        try {
            hashCodeMethod = Object.class.getMethod("hashCode", null);
            equalsMethod =
                Object.class.getMethod("equals", new Class[] { Object.class });
            toStringMethod = Object.class.getMethod("toString", null);
        } catch (NoSuchMethodException e) {
            throw new NoSuchMethodError(e.getMessage());
        }
    }

    private Class[] interfaces;
    private Object[] delegates;

    public Delegator(Class[] interfaces, Object[] delegates) {
        this.interfaces = (Class[]) interfaces.clone();
        this.delegates = (Object[]) delegates.clone();
    }

    public Object invoke(Object proxy, Method m, Object[] args)
        throws Throwable
    {
        Class declaringClass = m.getDeclaringClass();

        if (declaringClass == Object.class) {
            if (m.equals(hashCodeMethod)) {
                return proxyHashCode(proxy);
            } else if (m.equals(equalsMethod)) {
                return proxyEquals(proxy, args[0]);
            } else if (m.equals(toStringMethod)) {
                return proxyToString(proxy);
            } else {
                throw new InternalError(
                    "unexpected Object method dispatched: " + m);
            }
        } else {
            for (int i = 0; i < interfaces.length; i++) {
                if (declaringClass.isAssignableFrom(interfaces[i])) {
                    try {
                        return m.invoke(delegates[i], args);
                    } catch (InvocationTargetException e) {
                        throw e.getTargetException();
                    }
                }
            }

            return invokeNotDelegated(proxy, m, args);
        }
    }

    protected Object invokeNotDelegated(Object proxy, Method m,
                                        Object[] args)
        throws Throwable
    {
        throw new InternalError("unexpected method dispatched: " + m);
    }

    protected Integer proxyHashCode(Object proxy) {
        return new Integer(System.identityHashCode(proxy));
    }

    protected Boolean proxyEquals(Object proxy, Object other) {
        return (proxy == other ? Boolean.TRUE : Boolean.FALSE);
    }

    protected String proxyToString(Object proxy) {
        return proxy.getClass().getName() + '@' +
            Integer.toHexString(proxy.hashCode());
    }
}
```
的子类Delegator可以重写 invokeNotDelegated，以实现不直接委托给其他对象的代理方法调用的行为，他们可以覆盖proxyHashCode， proxyEquals以及proxyToString覆盖的代理从继承的方法的默认行为java.lang.Object。

构造Delegator用于Foo接口的实现：
```
Class[] proxyInterfaces = new Class[] { Foo.class };
Foo foo = (Foo) Proxy.newProxyInstance(Foo.class.getClassLoader(),
    proxyInterfaces,
    new Delegator(proxyInterfaces, new Object[] { new FooImpl() }));
```
请注意，Delegator上面给出的类的实现旨在说明而不是优化; 例如，而不是缓存和比较Method 的对象hashCode，equals和 toString方法，它可能只是通过它们的字符串名称匹配他们，因为没有这些方法名的过载 java.lang.Object。

----

