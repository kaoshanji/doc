#   [链式异常工具](https://docs.oracle.com/javase/8/docs/technotes/guides/lang/chained-exceptions.html)

Java代码通常会捕获一个异常并抛出另一个异常：
```
try {
    ...
} catch(YourException e) {
    throw new MyException();
}
```
不幸的是，“因果异常”（上例中的YourException）中包含的信息通常会丢失，这使调试变得非常复杂。认识到这个问题，开发人员有时会构建临时机制，允许某些“包装异常”包含第二个异常。通常提供访问器来提取包含的异常。这种机制有时被称为“异常链接工具”，因为当包含的异常本身是包装异常时，它们允许构造任意的异常链。

统一所有这些设施有很多好处。其中最主要的是：（1）我们保证任何想要记录一个例外导致另一个例外的事实的人都可以这样做，无论例外是什么。（2）通过提供一个通用API来记录一个异常导致另一个异常的事实，我们简化了这项任务，使程序员更有可能不厌其烦地去做。（3）通过提供访问因果异常的通用API，我们极大地增加了将这些信息提供给需要它的人的可能性。实际上，所提出的机制打印整个“因果链”作为标准堆栈回溯的一部分，确保预先存在的程序将提供这些信息而不需要作者的额外努力。

为了解决这些问题，我们向Throwable，[getCause（）](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getCause--) 和initCause（Throwable）添加了两个新方法 ，以及两个新的构造函数 [Throwable（Throwable）](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#Throwable-java.lang.Throwable-)和[Throwable（String，Throwable）](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#Throwable-java.lang.String-java.lang.Throwable-)。其他“通用”异常类（如Exception， RunTimeException 和Error）也同样配备了（Throwable）和 （String，Throwable）构造函数。但是，即使没有这样的构造函数的异常也可以通过initCause方法用作“包装异常” 。

修改了[Throwable.printStackTrace](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#printStackTrace--)的实现，以显示整个因果链的回溯。新方法getStackTrace 提供对printStackTrace提供的堆栈跟踪信息的编程访问。

所有平台的包装异常都将进行改造，以支持新设施（除了旧版API）
