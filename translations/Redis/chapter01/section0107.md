#   Lists

-   [BLPOP](http://www.redis.cn/commands/blpop.html):BLPOP 是阻塞式列表的弹出原语
-   [BRPOP](http://www.redis.cn/commands/brpop.html):BRPOP 是一个阻塞的列表弹出原语
-   [BRPOPLPUSH](http://www.redis.cn/commands/brpoplpush.html):BRPOPLPUSH 是 RPOPLPUSH 的阻塞版本
-   [LINDEX](http://www.redis.cn/commands/lindex.html):返回列表里的元素的索引 index 存储在 key 里面
-   [LINSERT](http://www.redis.cn/commands/linsert.html):把 value 插入存于 key 的列表中在基准值 pivot 的前面或后面
-   [LLEN](http://www.redis.cn/commands/llen.html):返回存储在 key 里的list的长度
-   [LPOP](http://www.redis.cn/commands/lpop.html):移除并且返回 key 对应的 list 的第一个元素
-   [LPUSH](http://www.redis.cn/commands/lpush.html):将所有指定的值插入到存于 key 的列表的头部
-   [LPUSHX](http://www.redis.cn/commands/lpushx.html):只有当 key 已经存在并且存着一个 list 的时候，在这个 key 下面的 list 的头部插入 value
-   [LRANGE](http://www.redis.cn/commands/lrange.html):返回存储在 key 的列表里指定范围内的元素
-   [LREM](http://www.redis.cn/commands/lrem.html):从存于 key 的列表里移除前 count 次出现的值为 value 的元素
-   [LSET](http://www.redis.cn/commands/lset.html):设置 index 位置的list元素的值为 value
-   [LTRIM](http://www.redis.cn/commands/ltrim.html):修剪(trim)一个已存在的 list，这样 list 就会只包含指定范围的指定元素
-   [RPOP](http://www.redis.cn/commands/rpop.html):移除并返回存于 key 的 list 的最后一个元素
-   [RPOPLPUSH](http://www.redis.cn/commands/rpoplpush.html):原子性地返回并移除存储在 source 的列表的最后一个元素,并把该元素放入存储在 destination 的列表的第一个元素位置
-   [RPUSH](http://www.redis.cn/commands/rpush.html):向存于 key 的列表的尾部插入所有指定的值
-   [RPUSHX](http://www.redis.cn/commands/rpushx.html):将值 value 插入到列表 key 的表尾, 当且仅当 key 存在并且是一个列表