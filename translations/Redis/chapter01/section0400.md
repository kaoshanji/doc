#   内存优化

##  小的聚合类型数据的特殊编码处理

Redis2.2版本及以后，存储集合数据的时候会采用内存压缩技术，以使用更少的内存存储更多的数据。如Hashes,Lists,Sets和Sorted Sets，当这些集合中的所有数都小于一个给定的元素，并且集合中元素数量小于某个值时，存储的数据会被以一种非常节省内存的方式进行编码，使用这种编码理论上至少会节省10倍以上内存（平均节省5倍以上内存）。并且这种编码技术对用户和redis api透明。因为使用这种编码是用CPU换内存，所以我们提供了更改阈值的方法，只需在redis.conf里面进行修改即可
```
hash-max-zipmap-entries 64 (2.6以上使用hash-max-ziplist-entries)
hash-max-zipmap-value 512  (2.6以上使用hash-max-ziplist-value)
list-max-ziplist-entries 512
list-max-ziplist-value 64
zset-max-ziplist-entries 128
zset-max-ziplist-value 64
set-max-intset-entries 512
```

（集合中）如果某个值超过了配置文件中设置的最大值，redis将自动把把它（集合）转换为正常的散列表。这种操作对于比较小的数值是非常快的，但是，如果你为了使用这种编码技术而把配置进行了更改，你最好做一下基准测试（和正常的不采用编码做一下对比）

##  使用32位的redis

使用32位的redis，对于每一个key,将使用更少的内存，因为32位程序，指针占用的字节数更少。但是32的redis整个实例使用的内存将被限制在4G以下。使用make 32bit命令编译生成32位的redis。RDB和AOF文件是不区分32位和64位的（包括字节顺序）,所以你可以使用64位的reidis恢复32位的RDB备份文件，相反亦然

##  位级别和字级别的操作

Redis 2.2引入了位级别和字级别的操作: `GETRANGE`, `SETRANGE`, `GETBIT` 和 `SETBIT`.使用这些命令，你可以把redis的字符串当做一个随机读取的（字节）数组。例如你有一个应用，用来标志用户的ID是连续的整数，你可以使用一个位图标记用户的性别，使用1表示男性，0表示女性，或者其他的方式。这样的话，1亿个用户将仅使用12 M的内存。你可以使用同样的方法，使用 `GETRANGE` 和 `SETRANGE` 命令为每个用户存储一个字节的信息。这仅是一个例子，实际上你可以使用这些原始数据类型解决更多问题

##  尽可能使用散列表（hashes）

小散列表（是说散列表里面存储的数少）使用的内存非常小，所以你应该尽可能的将你的数据模型抽象到一个散列表里面。比如你的web系统中有一个用户对象，不要为这个用户的名称，姓氏，邮箱，密码设置单独的key,而是应该把这个用户的所有信息存储到一张散列表里面

##  使用散列结构高效存储抽象的键值对

我知道这部分的标题很吓人，但是我将详细解释这部分内容.

一般而言，把一个模型（model）表示为key-value的形式存储在redis中非常容易，当然value必须为字符串，这样存储不仅比一般的key value存储高效，并且比memcached存储还高效

让我们做个对比：一些key存储了一个对象的多个字段要比一个散列表存储对象的多个字段占用更多的内存。这怎么可能？从原理上讲，为了保证查找一个数据总是在一个常量时间内（O(1)）,需要一个常量时间复杂度的数据结构，比如说散列表

但是，通常情况下，散列表只包括极少的几个字段。当散列表非常小的时候，我们采用将数据encode为一个O(N)的数据结构，你可以认为这是一个带有长度属性的线性数组。只有当N是比较小的时候，才会采用这种encode，这样使用HGET和HSET命令的复杂度仍然是O(1)：当散列表包含的元素增长太多的时候，散列表将被转换为正常的散列表（极限值可以在redis.conf进行配置）

无论是从时间复杂度还是从常量时间的角度来看，采用这种encode理论上都不会有多大性能提升，但是，一个线性数组通常会被CPU的缓存更好的命中（线性数组有更好的局部性）,从而提升了访问的速度.

既然散列表的字段及其对应的值并不是用redis objects表示，所以散列表的字段不能像普通的key一样设置过期时间。但是这毫不影响对散列表的使用，因为散列表本来就是这样设计的（我们相信简洁比多功能更重要，所以嵌入对象是不允许的，散列表字段设置单独的过期时间是不允许的）

所以散列表能高效利用内存。这非常有用,当你使用一个散列表存储一个对象或者抽象其他一类相关的字段为一个模型时。但是，如果我们有一个普通的key value业务需求怎么办

假如我们想使用redis存储许多小对象，这些对象可以使用json字符串表示，也可能是HTML片段和简单的key->boolean键值对。概况的说，一切皆字符串，都可以使用string:string的形式表示.

我们假设要缓存的对象使用数字后缀进行编码，如:
-   object:102393
-   object:1234
-   object:5

我们可以这样做。每次SET的时候，把key分为两部分，第一部分当做一个key，第二部当做散列表字段。比如“object:1234”,分成两部分:
-   a Key named object:12
-   a Field named 34

我们使用除最后2个数字的部分作为key,最后2个数字做为散列表的字段。使用命令:
```
HSET object:12 34 somevalue
```

如你所见，每个散列表将（理论上）包含100个字段，这是CPU资源和内存资源之间的一个折中.

另一个需要你关注的是在这种模式下，无论缓存多少对象，每个散列表都会分配100个字段。因为我们的对象总是以数字结尾，而不是一个随机的字符串。从某些方面来说，这是一种隐性的预分片

对于小数字怎么处理？比如object:2,我们采用object:作为key,所有剩下的数字作为一个字段。所以object:2和object:10都会被存储到key为object:的散列表中，但是一个使用2作为字段，一个使用10作为字段

这种方式将节省多少内存?

我使用了下面的Ruby程序进行了测试:
```
require 'rubygems'
require 'redis'

UseOptimization = true

def hash_get_key_field(key)
    s = key.split(":")
    if s[1].length > 2
        {:key => s[0]+":"+s[1][0..-3], :field => s[1][-2..-1]}
    else
        {:key => s[0]+":", :field => s[1]}
    end
end

def hash_set(r,key,value)
    kf = hash_get_key_field(key)
    r.hset(kf[:key],kf[:field],value)
end

def hash_get(r,key,value)
    kf = hash_get_key_field(key)
    r.hget(kf[:key],kf[:field],value)
end

r = Redis.new
(0..100000).each{|id|
    key = "object:#{id}"
    if UseOptimization
        hash_set(r,key,"val")
    else
        r.set(key,"val")
    end
}
```

在redis2.2的64位版本上测试结果:
-   当开启优化时使用内存1.7M
-   当未开启优化时使用内存11M

从结果看出，这是一个数量级的优化，我认为这种优化使redis成为最出色的键值缓存

特别提示: 要使上面的程序较好的工作，别忘记设置你的redis:
```
hash-max-zipmap-entries 256
```

相应的最大键值长度设置:
```
hash-max-zipmap-value 1024
```

每次散列表的元素数量或者值超过了阈值，散列将被扩展为一张真正的散列表进行存储，此时节约存储的优势就没有了

或许你想问，你为什么不自动将这些key进行转化以提高内存利用率？有两个原因：第一是因为我们更倾向于让这些权衡明确，而且必须在很多事情之间权衡：CPU，内存，最大元素大小限制。第二是顶级的键空间支持很多有趣的特性，比如过期，LRU算法，所以这种做法并不是一种通用的方法.

Redis的一贯风格是用户必须理解它是如何运作的，必须能够做出最好的选择和权衡，并且清楚它精确的运行方式

##  内存分配

为了存储用户数据,当设置了maxmemory后Redis会分配几乎和maxmemory一样大的内存（然而也有可能还会有其他方面的一些内存分配）

精确的值可以在配置文件中设置，或者在启动后通过 CONFIG SET 命令设置(see Using memory as an LRU cache for more info). Redis内存管理方面，你需要注意以下几点:

-   当某些缓存被删除后Redis并不是总是立即将内存归还给操作系统。这并不是redis所特有的，而是函数malloc()的特性。例如你缓存了5G的数据，然后删除了2G数据，从操作系统看，redis可能仍然占用了5G的内存（这个内存叫RSS,后面会用到这个概念），即使redis已经明确声明只使用了3G的空间。这是因为redis使用的底层内存分配器不会这么简单的就把内存归还给操作系统，可能是因为已经删除的key和没有删除的key在同一个页面（page）,这样就不能把完整的一页归还给操作系统
-   上面的一点意味着，你应该基于你可能会用到的 `最大内存` 来指定redis的最大内存。如果你的程序时不时的需要10G内存，即便在大多数情况是使用5G内存，你也需要指定最大内存为10G.
-   内存分配器是智能的，可以复用用户已经释放的内存。所以当使用的内存从5G降低到3G时，你可以重新添加更多的key，而不需要再向操作系统申请内存。分配器将复用之前已经释放的2G内存
-   因为这些，当redis的peak内存非常高于平时的内存使用时，碎片所占可用内存的比例就会波动很大。当前使用的内存除以实际使用的物理内存（RSS）就是fragmentation；因为RSS就是peak memory，所以当大部分key被释放的时候，此时内存的mem_used / RSS就比较高

如果 maxmemory 没有设置，redis就会一直向OS申请内存，直到OS的所有内存都被使用完。所以通常建议设置上redis的内存限制。或许你也想设置 maxmemory-policy 的值为 noeviction（在redis的某些老版本默认 并 不是这样）

设置了maxmemory后，当redis的内存达到内存限制后，再向redis发送写指令，会返回一个内存耗尽的错误。错误通常会触发一个应用程序错误，但是不会导致整台机器宕掉









