#   Sets

-   [SADD](http://www.redis.cn/commands/sadd.html):添加一个或多个指定的member元素到集合的 key中
-   [SCARD](http://www.redis.cn/commands/scard.html):返回集合存储的key的基数 (集合元素的数量)
-   [SDIFF](http://www.redis.cn/commands/sdiff.html):返回一个集合与给定集合的差集的元素
-   [SDIFFSTORE](http://www.redis.cn/commands/sdiffstore.html):该命令类似于 SDIFF, 不同之处在于该命令不返回结果集，而是将结果存放在destination集合中
-   [SINTER](http://www.redis.cn/commands/sinter.html):返回指定所有的集合的成员的交集
-   [SINTERSTORE](http://www.redis.cn/commands/sinterstore.html):这个命令与SINTER命令类似, 但是它并不是直接返回结果集,而是将结果保存在 destination集合中
-   [SISMEMBER](http://www.redis.cn/commands/sismember.html):返回成员 member 是否是存储的集合 key的成员
-   [SMEMBERS](http://www.redis.cn/commands/smembers.html):返回key集合所有的元素
-   [SMOVE](http://www.redis.cn/commands/smove.html):将member从source集合移动到destination集合中
-   [SPOP](http://www.redis.cn/commands/spop.html):从设置值存储中移除并返回一个或多个随机元素key
-   [SRANDMEMBER](http://www.redis.cn/commands/srandmember.html):仅提供key参数,那么随机返回key集合中的一个元素
-   [SREM](http://www.redis.cn/commands/srem.html):在key集合中移除指定的元素
-   [SUNION](http://www.redis.cn/commands/sunion.html):返回给定的多个集合的并集中的所有成员
-   [SUNIONSTORE](http://www.redis.cn/commands/sunionstore.html):该命令作用类似于SUNION命令,不同的是它并不返回结果集,而是将结果存储在destination集合中