#   [包java.util.concurrent](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/package-summary.html)

实用类通常在并发编程中有用


##  描述

实用类通常在并发编程中有用。该软件包包括一些小的标准化可扩展框架，以及一些提供有用功能的类，以及其他繁琐或难以实现的类。以下是主要组件的简要说明。

### Executors

接口：Executor是一个简单的标准化接口，用于定义自定义线程类子系统，包括线程池，异步I / O和轻量级任务框架。根据正在使用的具体Executor类，任务可以在新创建的线程，现有任务执行线程或线程调用中execute执行，并且可以顺序执行或同时执行。 ExecutorService提供了更完整的异步任务执行框架。ExecutorService管理任务的排队和调度，并允许受控关闭。该ScheduledExecutorService 子接口及相关的接口添加了延迟的和定期任务执行的支持。ExecutorServices提供了安排任何函数的异步执行的方法，表示为Callable结果的模拟Runnable。A Future返回函数的结果，允许确定执行是否已完成，并提供取消执行的方法。A RunnableFuture是Future 拥有一种run方法，在执行时设置其结果。

实现：类ThreadPoolExecutor并 ScheduledThreadPoolExecutor 提供可调节的灵活线程池。本Executors类提供大多数Executor的常见类型和配置，以及使用他们一些实用方法的工厂方法。基于的其他实用程序Executors包括FutureTask 提供Futures的通用可扩展实现的具体类，并且 ExecutorCompletionService有助于协调异步任务组的处理。

Class ForkJoinPool提供了一个Executor，主要用于处理实例ForkJoinTask及其子类。这些类采用工作窃取调度程序，可以获得符合计算密集型并行处理中常常存在的限制的任务的高吞吐量。

### 队列

本ConcurrentLinkedQueue类提供一个高效的可扩展的线程安全的非阻塞FIFO队列。的ConcurrentLinkedDeque类是类似的，但附加地支持Deque 接口。

五个实现都java.util.concurrent支持扩展的BlockingQueue 接口中，定义堵放的版本，并采取： LinkedBlockingQueue， ArrayBlockingQueue， SynchronousQueue， PriorityBlockingQueue，和 DelayQueue。不同的类涵盖了生产者 - 消费者，消息传递，并行任务和相关并发设计的最常见使用上下文。

扩展接口TransferQueue和实现LinkedTransferQueue 引入了同步transfer方法（以及相关特征），其中生产者可以可选地阻止等待其消费者。

该BlockingDeque接口扩展BlockingQueue为支持FIFO和LIFO（基于堆栈）操作。类LinkedBlockingDeque 提供了一个实现。

### 定时

的TimeUnit类提供了用于指定和控制基于超时操作的多个粒度（包括毫微秒）。除了无限期等待之外，程序包中的大多数类都包含基于超时的操作。在使用超时的所有情况下，超时指定方法在指示超时之前应等待的最短时间。实施工作尽最大努力在发生超时后尽快检测到超时。然而，在检测到超时和在超时之后再次实际执行的线程之间可能经过不确定的时间量。接受超时参数的所有方法都会将值小于或等于零，以表示根本不等待。要等待“永远”，您可以使用值Long.MAX_VALUE。

### 同步器

五个类有助于共同的专用同步习语。
-   Semaphore 是一种经典的并发工具。
-   CountDownLatch 是一个非常简单但非常常见的阻塞功能，直到给定数量的信号，事件或条件成立。
-   A CyclicBarrier是可复位的多路同步点，在某些并行编程风格中很有用。
-   A Phaser提供了更灵活的屏障形式，可用于控制多个线程之间的分阶段计算。
-   An Exchanger允许两个线程在集合点交换对象，并且在多个管道设计中很有用。

### 并发集合

除了队列，这个包提供的集合实现在多线程环境中设计用于： ConcurrentHashMap， ConcurrentSkipListMap， ConcurrentSkipListSet， CopyOnWriteArrayList，和 CopyOnWriteArraySet。当期望许多线程访问给定集合时，a ConcurrentHashMap通常优于同步 HashMap，并且a ConcurrentSkipListMap通常优于同步TreeMap。当预期的读取和遍历次数大大超过列表的更新次数时，A CopyOnWriteArrayList优于同步 ArrayList。

与此包中的某些类一起使用的“Concurrent”前缀是一个简写，表示与类似“synchronized”类的几个不同之处。例如java.util.Hashtable并且 Collections.synchronizedMap(new HashMap())是同步的。但ConcurrentHashMap是“并发”。并发集合是线程安全的，但不受单个排除锁的控制。在ConcurrentHashMap的特定情况下，它可以安全地允许任意数量的并发读取以及可调数量的并发写入。当您需要通过单个锁来阻止对集合的所有访问时，“同步”类可能很有用，但代价是可扩展性较差。在期望多个线程访问公共集合的其他情况下，通常优选“并发”版本。当任何集合未被共享时，或者只有在持有其他锁时才可访问非同步集合。

大多数并发Collection实现（包括大多数队列）也与通常的java.util 约定不同，因为它们的迭代器 和Spliterator提供 弱一致而不是快速失败的遍历：

-   它们可以与其他操作同时进行
-   他们永远不会扔 ConcurrentModificationException
-   它们保证在构造时只存在一次元素，并且可能（但不保证）反映构造后的任何修改。

### 内存一致性属性

Java语言规范的第17章定义了内存操作的 发生前关系，例如共享变量的读写。只有在读取操作之前发生写入操作时，一个线程的写入结果才能保证对另一个线程的读取可见。该 synchronized和volatile结构，以及在 Thread.start()和Thread.join()方法，可以形成 之前发生关系。特别是：
-   线程中的每个动作都发生在该线程中的每个动作之前，该动作在程序的顺序中稍后出现。
-   synchronized监视器的解锁（块或方法退出）发生在synchronized 同一监视器的每个后续锁定（块或方法入口）之前。并且因为发生在之前的关系是可传递的，所以在解锁之前线程的所有动作都发生在任何线程锁定该监视器之后的所有动作之前。
-   在对该相同字段的每次后续读取之前发生对volatile字段的写入。写和读的 领域也有类似的内存一致性效果进入和退出显示器，但不意味着互斥锁。 volatile
-   在启动线程中的任何操作之前发生start对线程的调用。
-   线程中的所有操作都发生在任何其他线程从该线程上成功返回之前join。

所有类java.util.concurrent及其子包的方法将这些保证扩展到更高级别的同步。特别是：
-   在将对象放入任何并发集合之前的线程中的操作发生在从另一个线程中的集合访问或移除该元素之后的操作之前。
-   在提交的前操作在一个线程Runnable 到Executor 发生，之前它开始执行。同样Callables提交给ExecutorService。
-   异步计算所采取的动作由在另一个线程中检索结果之后的Future 发生前动作表示 Future.get()。
-   操作之前为“释放”同步器的方法，例如 Lock.unlock，Semaphore.release和 CountDownLatch.countDown 发生-前行动一个成功的“获取”方法随后如 Lock.lock，Semaphore.acquire， Condition.await，和CountDownLatch.await在另一个线程相同的同步对象。
-   对于通过a成功交换对象的每对线程， 在每个线程Exchanger之前的动作发生 -在另一个线程中的对应之后的动作之前。 exchange()exchange()
-   在调用操作CyclicBarrier.await和 Phaser.awaitAdvance（以及其变体） 发生-前由阻挡动作执行通过屏障操作执行的动作和操作发生-之前从相应的成功返回后续动作await 中的其他线程。




----