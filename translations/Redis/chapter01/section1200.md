#   key事件通知

>   `重要` Keyspace通知是自2.8.0以来的一项功能

##  功能概述

Keyspace通知允许客户订阅Pub / Sub频道，以便以某种方式接收影响Redis数据集的事件

可能收到的事件的例子如下：
-   所有影响给定键的命令
-   所有接收LPUSH操作的 key
-   所有key在数据库中过期

事件使用Redis的常规Pub / Sub层传递，因此实现Pub / Sub的客户端无需修改即可使用此功能

如果你的发布/订阅客户端断开连接并在稍后重新连接，那么连接在客户端断开这段时间丢失

##  事件类型

对于影响Redis数据空间的每项操作，实施Keyspace通知都会发送两种不同类型的事件。例如，DEL 针对mykey数据库中指定的key的操作0将触发两条消息的传递，完全等同于以下两条 PUBLISH命令：
```
PUBLISH __keyspace@0__:mykey del
PUBLISH __keyevent@0__:del mykey
```

很容易看出一个通道如何允许听取针对该键的所有事件mykey，而另一个通道允许获取有关del操作目标的所有键的信息

第一种事件keyspace在通道中带有前缀，称为`key空间通知`，而第二种带有keyevent前缀的事件称为`key事件通知`

在上面的例子中del，为key生成了一个事件mykey。会发生什么是：
-   key空间频道接收消息作为消息的名称
-   key事件通道接收密钥的名称作为消息

##  组态

默认情况下，key空间事件通知被禁用，因为虽然不太明智，但该功能使用某些CPU能力。通知使用notify-keyspace-eventsredis.conf或通过CONFIG SET启用

将参数设置为空字符串会禁用通知。为了启用该功能，将使用由多个字符组成的非空字符串，其中每个字符具有特殊含义，如下表所示：

```
K     Keyspace events, published with __keyspace@<db>__ prefix.
E     Keyevent events, published with __keyevent@<db>__ prefix.
g     Generic commands (non-type specific) like DEL, EXPIRE, RENAME, ...
$     String commands
l     List commands
s     Set commands
h     Hash commands
z     Sorted set commands
x     Expired events (events generated every time a key expires)
e     Evicted events (events generated when a key is evicted for maxmemory)
A     Alias for g$lshzxe, so that the "AKE" string means all the events.
```

至少K或E应该出现在字符串中，否则不管字符串的其余部分如何，都不会传递事件

例如，要仅为列表启用key空间事件，必须将配置参数设置为Kl，等等。

该字符串`KEA`可用于启用每个可能的事件

##  由不同命令生成的事件

根据以下列表，不同的命令会生成不同类型的事件。
-   DELdel为每个已删除的key生成一个事件
-   RENAME生成两个事件，一个rename_from是源键的rename_to事件，另一个是目标键的事件
-   EXPIRE每当将过期结果设置为要删除的key时expire，在过期设置为密钥或事件时生成事件。expiredEXPIRE
-   SORT用于设置新key sortstore时生成一个事件STORE。如果结果列表为空，并且使用了该STORE选项，并且已有一个具有该名称的现有key，则结果是key被删除，因此del在此情况下会生成一个事件
-   SET和它的所有变体（SETEX，SETNX，GETSET）生成set的事件。不过SETEX也会产生一个expire事件
-   MSETset为每个键生成一个分离的事件
-   SETRANGE生成一个setrange事件
-   INCR，DECR，INCRBY，DECRBY命令所有生成incrby的事件
-   INCRBYFLOAT生成一个incrbyfloat事件
-   APPEND生成一个append事件。
-   LPUSH并LPUSHX生成单个lpush事件，即使在可变情况下也是如此。
-   RPUSH并RPUSHX生成单个rpush事件，即使在可变情况下也是如此。
-   RPOP生成一个rpop事件。此外，del如果由于弹出列表中的最后一个元素而将键移除，则会生成一个事件。
-   LPOP生成一个lpop事件。此外，del如果由于弹出列表中的最后一个元素而将键移除，则会生成一个事件。
-   LINSERT生成一个linsert事件。
-   LSET生成一个lset事件。
-   LTRIM生成一个ltrim事件，del如果生成的列表为空并且键被删除，则还会生成一个事件。
-   RPOPLPUSH并BRPOPLPUSH生成一个rpop事件和一个lpush事件。在这两种情况下，订单都会得到保证（lpush活动将始终在rpop活动结束后交付）。此外，del如果生成的列表长度为零并且键被删除，则会生成一个事件。
-   HSET，HSETNX并且HMSET全部生成单个hset事件。
-   HINCRBY生成一个hincrby事件。
-   HINCRBYFLOAT生成一个hincrbyfloat事件。
-   HDEL生成一个单独的hdel事件，del如果生成的哈希值为空并且键被删除，则生成一个附加事件。
-   SADDsadd即使在可变情况下也会生成单个事件。
-   SREM生成单个srem事件，del如果生成的集合为空且键被删除，则生成附加事件。
-   SMOVEsrem为源密钥生成一个事件，并sadd为目标密钥生成一个事件。
-   SPOP生成一个spop事件和一个附加del事件，如果结果集为空并且键被删除。
-   SINTERSTORE，SUNIONSTORE，SDIFFSTORE生成sinterstore，sunionostore，sdiffstore分别事件。在特殊情况下，结果集为空，并且存储结果的键已经存在，del因为键被删除，所以会生成一个事件。
-   ZINCR生成一个zincr事件。
-   ZADDzadd即使添加了多个元素也会生成单个事件。
-   ZREMzrem即使多个元素被删除，也会生成单个事件。当生成的排序集合为空并且生成密钥时，会生成附加del事件。
-   ZREMBYSCORE生成单个zrembyscore事件。当生成的排序集合为空并且生成密钥时，会生成附加del事件。
-   ZREMBYRANK生成单个zrembyrank事件。当生成的排序集合为空并且生成密钥时，会生成附加del事件。
-   ZINTERSTORE并ZUNIONSTORE分别产生zinterstore和zunionstore事件。在特殊情况下，生成的排序集合为空，并且存储结果的键已经存在，del因为键被删除，所以会生成一个事件。
-   每次将与生存时间关联的密钥从数据集中删除，因为它已过期，expired则会生成一个事件。
-   每次从数据集中清除密钥以释放内存作为maxmemory策略的结果时，evicted都会生成事件

`重要`只有在目标密钥真正被修改的情况下，所有命令才会生成事件。例如，SREM从一个Set中删除一个不存在的元素实际上并不会改变该键的值，所以不会生成任何事件

如果不确定某个命令是如何产生事件的，最简单的做法是观察自己：
```
$ redis-cli config set notify-keyspace-events KEA
$ redis-cli --csv psubscribe '__key*__:*'
Reading messages... (press Ctrl-C to quit)
"psubscribe","__key*__:*",1
```

此时，redis-cli在另一个终端中使用命令将命令发送到Redis服务器并观察生成的事件：
```
"pmessage","__key*__:*","__keyspace@0__:foo","set"
"pmessage","__key*__:*","__keyevent@0__:set","foo"
...
```

##  过期事件的时间

有时间关联的key由Redis以两种方式过期：
-   当通过命令访问key并被发现已过期时
-   通过一个在后台查找过期密钥的后台系统，以便能够收集永远不会被访问的key

expired当一个key被访问并且被上述系统中的一个发现过期时，这些事件就会生成，因此无法保证Redis服务器能够expired在关键时间到达时生成事件零值

如果没有命令持续关注key，并且有许多与TTL关联的密钥，则key生存时间下降到零的时间与expired生成事件的时间之间可能存在显着的延迟

基本上，expired事件是在Redis服务器删除key时生成的，而不是理论上达到零值的时间