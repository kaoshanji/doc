#   [包java.util.concurrent.atomic](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/atomic/package-summary.html)

一个小型工具包，支持对单个变量进行无锁线程安全编程。

##  描述

一个小型工具包，支持对单个变量进行无锁线程安全编程。本质上，此包中的类将volatile值，字段和数组元素的概念扩展为也提供表单的原子条件更新操作的概念：
```
  boolean compareAndSet(expectedValue, updateValue);
```
此方法（在不同类的参数类型中有所不同）以原子方式将变量设置为updateValue当前保存的变量expectedValue，报告true成功。此包中的类还包含获取和无条件设置值的方法，以及weakCompareAndSet下面描述的较弱的条件原子更新操作。

这些方法的规范使实现能够采用当代处理器上可用的高效机器级原子指令。但是在某些平台上，支持可能需要某种形式的内部锁定。因此，不严格保证方法是非阻塞的 - 线程可能在执行操作之前暂时阻塞。

类的实例 AtomicBoolean， AtomicInteger， AtomicLong，和 AtomicReference 每个提供访问和更新相应的类型的单个变量。每个类还为该类型提供适当的实用方法。例如，类AtomicLong和 AtomicInteger提供原子增量方法。一个应用程序是生成序列号，如：
```
 class Sequencer {
   private final AtomicLong sequenceNumber
     = new AtomicLong(0);
   public long next() {
     return sequenceNumber.getAndIncrement();
   }
 }
```
定义新的实用程序函数很简单，例如 getAndIncrement，将函数原子应用于值。例如，给定一些转换
```
  long transform(long input)
```
编写实用程序方法如下：
```
long getAndTransform(AtomicLong var) {
   long prev, next;
   do {
     prev = var.get();
     next = transform(prev);
   } while (!var.compareAndSet(prev, next));
   return prev; // return next; for transformAndGet
 }
```

访问和更新原子的记忆效应通常遵循挥发性规则，如 Java语言规范（17.4内存模型）中所述：
-   get具有读取volatile变量的记忆效应 。
-   set具有写入（赋值）volatile变量的记忆效应 。
-   -   lazySet具有写入（赋值）volatile变量的记忆效应，除了它允许对后续（但不是先前的）存储器动作进行重新排序，这些行为本身不会对普通的非volatile 写入施加重新排序约束。在其他用法上下文中，lazySet可以在为了垃圾收集而归零时应用从不再次访问的引用。
-   weakCompareAndSet自动读取和写入有条件的变量，但并没有 创造任何的之前发生的排序，所以不提供任何担保相对于以前或以后的读取和比的目标以外的任何变量的写入weakCompareAndSet。
-   compareAndSet 以及所有其他读取和更新操作，例如getAndIncrement 读取和写入volatile变量的记忆效应。

除了表示单个值的类之外，此包还包含Updater类，可用于获取 任何所选类的compareAndSet任何选定volatile字段的操作。 AtomicReferenceFieldUpdater， AtomicIntegerFieldUpdater和， AtomicLongFieldUpdater是基于反射的实用程序，提供对相关字段类型的访问。这些主要用于原子数据结构，其中volatile同一节点的若干字段（例如，树节点的链接）独立地受原子更新的影响。这些类在如何以及何时使用原子更新方面提供了更大的灵活性，代价是更加笨拙的基于反射的设置，不太方便的使用和较弱的保证。

的 AtomicIntegerArray， AtomicLongArray和 AtomicReferenceArray类进一步扩展到这些类型的数组原子操作的支持。这些类在volatile为其数组元素提供访问语义方面也值得注意，普通数组不支持这些语义。

原子类也支持方法 weakCompareAndSet，其适用性有限。在某些平台上，弱版本可能比compareAndSet正常情况下更有效，但不同之处在于任何给定的weakCompareAndSet方法调用都可能false 虚假地返回（也就是说，没有明显的原因）。一个 false返回仅仅意味着如果需要的话，依靠反复调用时，变量保存保证操作可以重试expectedValue，并没有其他线程也在尝试设置变量终究会成功。（例如，这种虚假故障可能是由于与预期值和当前值相等无关的内存争用效应引起的。）weakCompareAndSet不提供同步控制通常需要的排序保证。然而，该方法对于更新计数器和统计数据可能是有用的，当这些更新与在程序的排序之前发生的其他更新无关时。当一个线程看到由a引起的原子变量的更新时weakCompareAndSet，它不一定会看到在之前发生的任何其他变量的更新weakCompareAndSet。例如，在更新性能统计信息时，这可能是可以接受的，但在其他情况下很少。

的AtomicMarkableReference 类与引用关联的单个布尔值。例如，该位可能在数据结构中使用，表示被引用的对象在逻辑上已被删除。的AtomicStampedReference 类与引用关联的整数值。例如，这可以用于表示与一系列更新相对应的版本号。

原子类主要设计为用于实现非阻塞数据结构和相关基础结构类的构建块。该compareAndSet方法不是锁定的一般替代方法。仅当对象的关键更新仅限于单个变量时，它才适用。

原子类不是通用替换 java.lang.Integer和相关类。他们没有 定义方法，如equals，hashCode和 compareTo。（因为预期原子变量会发生变异，所以它们对于散列表键的选择很差。）此外，仅为那些在预期应用程序中常用的类型提供类。例如，没有用于表示的原子类byte。在您想要这样做的不常见的情况下，您可以使用a AtomicInteger来保存 byte值，并适当地进行投射。您还可以使用浮动 Float.floatToRawIntBits(float)和 Float.intBitsToFloat(int)转换，并使用Double.doubleToRawLongBits(double)和 Double.longBitsToDouble(long)转换加倍 。


----