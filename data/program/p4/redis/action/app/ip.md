#   根据IP查找城市

-   需求

根据访客的IP地址查询访客所在城市地区

##  载入位置表格

-   [地址库：maxmind](https://dev.maxmind.com/geoip/geoip2/geolite2/)
    -   IP地址段与应城市ID
    -   城市ID与城市信息
-   两个查找表
    -   IP地址 --> 城市ID：有序集合，元素：城市ID，分值是根据IP地址计算出来的整数值
    -   城市ID --> 城市信息：散列，键-城市ID，值-Json格式的城市信息
-   唯一城市ID
    -   多个IP地址范围可能会被映射至同一个城市ID，所以程序在普通的城市ID后面，加上一个_字符以及有序集合目前已有城市ID的数量。

##  查找IP所属城市

首先将给定的IP地址转换为分值，然后在所有分值小于或等于给定IP地址的IP地址里面，找出分值最大的那个IP地址所对应的城市ID。

找到城市ID之后，就可以在存储着城市ID与城市信息映射的散列里面获取ID对应城市的信息了。


