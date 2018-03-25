#   HyperLogLog

-   [PFADD](http://www.redis.cn/commands/pfadd.html):将除了第一个参数以外的参数存储到以第一个参数为变量名的HyperLogLog结构中
-   [PFCOUNT](http://www.redis.cn/commands/pfcount.html):当参数为一个键时，返回存储在HyperLogLog结构体的该变量的近似基数，如果该变量不存在，则返回0
-   [PFMERGE](http://www.redis.cn/commands/pfmerge.html):将多个 HyperLogLog 合并（merge）为一个 HyperLogLog