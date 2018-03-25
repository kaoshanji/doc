#   Geo

-   [GEOADD](http://www.redis.cn/commands/geoadd.html):将指定的地理空间位置（纬度、经度、名称）添加到指定的key中
-   [GEOHASH](http://www.redis.cn/commands/geohash.html):返回一个或多个位置元素的 Geohash 表示
-   [GEOPOS](http://www.redis.cn/commands/geopos.html):从key里返回所有给定位置元素的位置（经度和纬度）
-   [GEODIST](http://www.redis.cn/commands/geodist.html):返回两个给定位置之间的距离
-   [GEORADIUS](http://www.redis.cn/commands/georadius.html):以给定的经纬度为中心， 返回键包含的位置元素当中， 与中心的距离不超过给定最大距离的所有位置元素
-   [GEORADIUSBYMEMBER](http://www.redis.cn/commands/georadiusbymember.html):这个命令和 GEORADIUS 命令一样， 都可以找出位于指定范围内的元素