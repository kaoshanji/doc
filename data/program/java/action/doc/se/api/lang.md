#   [包java.lang](https://docs.oracle.com/javase/8/docs/api/java/lang/package-summary.html)

提供对Java编程语言设计至关重要的类。

##  描述

提供对Java编程语言设计至关重要的类。最重要的类是Object类层次结构的根，并且其Class实例在运行时表示类。

通常，有必要将原始类型的值表示为对象。该包装类Boolean， Character，Integer，Long，Float，和Double服务于这个目的。Double例如，类型的对象包含一个类型为double的字段，以这样的方式表示该值，即对它的引用可以存储在引用类型的变量中。这些类还提供了许多用于在原始值之间进行转换的方法，以及支持equals和hashCode等标准方法。的 Void类是保持于基准的非实例化类Class代表类型void对象。

该类Math提供常用的数学函数，如正弦，余弦和平方根。类String，StringBuffer以及StringBuilder类似地提供字符串上常用的操作。

类ClassLoader，Process，ProcessBuilder，Runtime，SecurityManager，并 System提供了管理类的动态加载，创造外部进程中，主机环境查询，如一天中的时间，以及安全策略的执行“系统操作”。

类Throwable包含throw语句可能抛出的对象。Throwable 表示错误和异常的子类。

java.nio.charset.Charset该类 的规范描述了字符编码的命名约定以及Java平台的每个实现必须支持的标准编码集

----