#   Transactions

-   [DISCARD](http://www.redis.cn/commands/discard.html):刷新一个事务中所有在排队等待的指令，并且将连接状态恢复到正常
-   [EXEC](http://www.redis.cn/commands/exec.html):执行事务中所有在排队等待的指令并将链接状态恢复到正常 当使用WATCH 时，只有当被监视的键没有被修改，且允许检查设定机制时，EXEC会被执行
-   [MULTI](http://www.redis.cn/commands/multi.html):标记一个事务块的开始。 随后的指令将在执行EXEC时作为一个原子执行
-   [UNWATCH](http://www.redis.cn/commands/unwatch.html):刷新一个事务中已被监视的所有key
-   [WATCH](http://www.redis.cn/commands/watch.html):标记所有指定的key 被监视起来，在事务中有条件的执行（乐观锁）
