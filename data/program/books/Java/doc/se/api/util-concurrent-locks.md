#   [包java.util.concurrent.locks](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/locks/package-summary.html)

接口和类，提供用于锁定和等待与内置同步和监视器不同的条件的框架

##  描述

接口和类，提供用于锁定和等待与内置同步和监视器不同的条件的框架。该框架在锁和条件的使用方面允许更大的灵活性，代价是更笨拙的语法。

该Lock接口支持语义不同（可重入，公平等）的锁定规则，并且可用于非块结构的上下文，包括手动和锁定重新排序算法。主要实施是ReentrantLock。

该ReadWriteLock接口同样定义了可以阅读器之间共享，但专用于作家锁。ReentrantReadWriteLock由于它涵盖了大多数标准使用上下文，因此仅提供单个实现。但是程序员可以创建自己的实现来覆盖非标准需求。

该Condition接口描述了可能与锁相关联的条件变量。它们与使用的隐式监视器的使用类似 Object.wait，但提供扩展功能。特别地，多个Condition对象可以与单个对象相关联Lock。为避免兼容性问题，Condition方法的名称与相应的Object版本不同。

本AbstractQueuedSynchronizer 类用作定义锁以及依赖于排队阻塞线程的其他同步器有用的超类。的AbstractQueuedLongSynchronizer类提供相同的功能，而是延伸到同步状态的64位的支持。两者都是扩展类AbstractOwnableSynchronizer，一个简单的类，有助于记录当前持有独占同步的线程。本LockSupport 类提供了更低级别的阻塞和解除阻塞支持，是为那些实现自己的定制锁类的开发人员非常有用。


----