#   排他锁

-   需求

锁是解决并发场景下有用的工具。

##  排他锁

一份数据在某一时刻只能被一个程序访问。

为了对数据进行排他性访问，程序首先要做的就是获取锁。

可以锁住整个集合，也可以锁住指定元素，让锁的粒度更细，性能更高。

锁需要一个超时时间。

##  计数信号量


