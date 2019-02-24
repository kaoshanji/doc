#   备用存储引擎

存储引擎是处理不同表类型的SQL操作的MySQL组件。InnoDB是默认和最通用的存储引擎，Oracle建议将其用于除专用用例之外的表。（默认情况下CREATE TABLE，MySQL 8.0中的语句创建InnoDB表。）

MySQL服务器使用可插拔的存储引擎架构，使存储引擎能够从正在运行的MySQL服务器中加载和卸载。

要确定服务器支持哪些存储引擎，请使用该 SHOW ENGINES语句。Support列中的值指示是否可以使用引擎。的值YES， NO或DEFAULT表示发动机可用，不可用，或可用与当前被设置为默认的存储引擎。

##  目录
-   设置存储引擎
-   MyISAM存储引擎
-   MEMORY存储引擎
-   CSV存储引擎
-   ARCHIVE存储引擎
-   BLACKHOLE存储引擎
-   MERGE存储引擎
-   FEDERATED存储引擎
-   示例存储引擎
-   其他存储引擎
-   MySQL存储引擎架构概述

