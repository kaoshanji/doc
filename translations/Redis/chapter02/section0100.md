#   redis-cli，Redis命令行界面

redis-cli 是Redis命令行界面，它是一个简单的程序，允许向Redis发送命令，并直接从终端读取服务器发送的回复。

它有两种主要模式：一种交互模式，其中有一个REPL（读取评估打印循环），用户输入命令并获取回复; 另一种模式是将命令作为参数发送redis-cli，执行并打印在标准输出中。

在交互模式下，redis-cli具有基本的行编辑功能，可以提供良好的打字体验。

但redis-cli不仅如此。有些选项可以用来启动程序，以便将其放入特殊模式，以便redis-cli可以执行更复杂的任务，例如模拟从站并打印从主站接收到的复制流，检查Redis服务器的延迟并显示统计数据，甚至显示延迟样本和频率的ASCII艺术谱图以及许多其他内容。

本指南将涵盖redis-cli从最简单到最高级的不同方面。

如果您要广泛使用Redis，或者如果您已经这样做，那么很可能会碰巧使用redis-cli很多。花一些时间熟悉它可能是一个非常好的主意，一旦你知道了命令行界面的所有技巧，你就会发现你将更有效地使用Redis

##  命令行用法

只需运行一个命令并在标准输出上打印它的答复就如同输入要执行的命令一样简单redis-cli：
```
$ redis-cli incr mycounter
(integer) 7
```

该命令的回复是“7”。由于Redis的回复是键入的（它们可以是字符串，数组，整数，NULL，错误等等），您可以看到括号之间的回复类型。但是，当输出redis-cli必须用作另一个命令的输入时，或者我们希望将其重定向到一个文件时，这并不是一个好主意。

实际上，redis-cli只有当它检测到标准输出是tty（基本上是一个终端）时才会显示提高人类可读性的附加信息。否则，它将自动启用原始输出模式，如下例所示：
```
$ redis-cli incr mycounter > /tmp/output.txt
$ cat /tmp/output.txt
8
```

(integer)由于CLI检测到输出不再写入终端，因此输出中省略了此时间。您可以使用以下--raw选项甚至在终端上强制原始输出：
```
$ redis-cli --raw incr mycounter
9
```

同样，通过使用，您可以在写入文件或在管道中写入其他命令时强制输出可读的输出--no-raw

##  主机，端口，密码和数据库

默认情况下redis-cli，在127.0.0.1端口6379连接到服务器。正如您所猜测的，您可以使用命令行选项轻松更改此设置。要指定不同的主机名或IP地址，请使用-h。为了设置不同的端口，请使用-p
```
$ redis-cli -h redis15.localnet.org -p 6390 ping
PONG
```

如果您的实例受密码保护，则该`-a <password>`选项将执行身份验证，以保存明确使用该AUTH命令的需要：
```
$ redis-cli -a myUnguessablePazzzzzword123 ping
PONG
```

最后，可以通过使用以下`-n <dbnum>`选项发送一个命令，该命令对除默认数字零以外的数据库号码进行操作：
```
$ redis-cli flushall
OK
$ redis-cli -n 1 incr a
(integer) 1
$ redis-cli -n 1 incr a
(integer) 2
$ redis-cli -n 2 incr a
(integer) 1
```

##  从其他程序获取输入

有两种方法可以用来redis-cli从其他命令（基本上来自标准输入）获取输入。一种是使用我们从标准输入读取的有效载荷作为最后一个参数。例如，/etc/services如果我的电脑为了设置文件内容的Redis键，我可以使用下面的-x 选项：
```
$ redis-cli -x set foo < /etc/services
OK
$ redis-cli getrange foo 0 50
"#\n# Network services, Internet style\n#\n# Note that "
```

正如您在上述会话的第一行中看到的那样，该SET命令的最后一个参数 未指定。这些参数SET foo没有我希望我的密钥被设置的实际值。

而是-x指定了该选项，并将文件重定向到CLI的标准输入。所以输入被读取，并被用作命令的最后一个参数。这对编写脚本很有用。

一种不同的方法是提供redis-cli用文本文件编写的一系列命令：
```
$ cat /tmp/commands.txt
set foo 100
incr foo
append foo xxx
get foo
$ cat /tmp/commands.txt | redis-cli
OK
(integer) 101
(integer) 6
"101xxx"
```

所有的命令commands.txt一个接一个地执行， redis-cli就好像它们是用户交互式输入的一样。如果需要，可以在文件内引用字符串，以便可以在空间或换行符或其他特殊字符中使用单个参数：
```
$ cat /tmp/commands.txt
set foo "This is a single argument"
strlen foo
$ cat /tmp/commands.txt | redis-cli
OK
(integer) 25
```

##  连续运行相同的命令

可以在执行过程中用户选择暂停的情况下执行相同的命令指定的次数。这在不同的情况下非常有用，例如，当我们想要持续监视某些关键内容或INFO字段输出，或者当我们想要模拟一些反复出现的写入事件时（例如每5秒将一个新项目推入列表）。

此功能由两个选项控制：`-r <count>`和`-i <delay>`。第一种状态表示运行命令的次数，第二种表示不同命令调用之间的延迟，以秒为单位（能够指定十进制数字，如0.1表示100毫秒）。

默认情况下，间隔（或延迟）被设置为0，所以命令只是尽快执行：
```
$ redis-cli -r 5 incr foo
(integer) 1
(integer) 2
(integer) 3
(integer) 4
(integer) 5
```

要永远运行相同的命令，请将其-1用作计数。因此，为了随时监控RSS存储器的大小，可以使用如下的命令：
```
$ redis-cli -r -1 -i 1 INFO | grep rss_human
used_memory_rss_human:1.38M
used_memory_rss_human:1.38M
used_memory_rss_human:1.38M
... a new line will be printed each second ...
```

##  使用大量插入数据 redis-cli

批量插入使用redis-cli包含在一个分离的页面中，因为它本身就是一个有价值的话题

##  CSV输出

有时您可能想要使用redis-cli以便将数据从Redis快速导出到外部程序。这可以使用CSV（逗号分隔值）输出功能来完成：
```
$ redis-cli lpush mylist a b c d
(integer) 4
$ redis-cli --csv lrange mylist 0 -1
"d","c","b","a"
```

##  交互模式

到目前为止，我们探讨了如何使用Redis CLI作为命令行程序。这对于脚本和某些类型的测试非常有用，但大多数人会花大部分时间redis-cli使用交互模式。

在交互模式下，用户在提示符下键入Redis命令。该命令被发送到服务器，进行处理，回复被解析并呈现为更简单的形式以供读取。

在交互模式下运行CLI无需特别 - 只需在没有任何争论的情况下进行午餐即可，并且您处于：
```
$ redis-cli
127.0.0.1:6379> ping
PONG
```

字符串127.0.0.1:6379>是提示符。它提醒您，您已连接到给定的Redis实例。

当连接的服务器发生更改时，或者当您在与数据库编号0不同的数据库上运行时，提示会发生变化：
```
127.0.0.1:6379> select 2
OK
127.0.0.1:6379[2]> dbsize
(integer) 1
127.0.0.1:6379[2]> select 0
OK
127.0.0.1:6379> dbsize
(integer) 503
```

##  处理连接和重新连接

connect在交互模式下使用该命令可以通过指定我们想要连接的主机名和端口来连接到不同的实例：
```
127.0.0.1:6379> connect metal 6379
metal:6379> ping
PONG
```

正如你所看到的提示相应地改变。如果用户尝试连接到无法访问的实例，则会redis-cli进入断开连接模式并尝试重新连接每个新命令：
```
127.0.0.1:6379> connect 127.0.0.1 9999
Could not connect to Redis at 127.0.0.1:9999: Connection refused
not connected> ping
Could not connect to Redis at 127.0.0.1:9999: Connection refused
not connected> ping
Could not connect to Redis at 127.0.0.1:9999: Connection refused
```

通常在检测到断开连接后，CLI始终尝试以透明方式重新连接：如果尝试失败，则会显示错误并进入断开连接状态。以下是断开和重新连接的示例：
```
127.0.0.1:6379> debug restart
Could not connect to Redis at 127.0.0.1:6379: Connection refused
not connected> ping
PONG
127.0.0.1:6379> (now we are connected again)
```

重新连接时，redis-cli自动重新选择最后选择的数据库编号。然而，关于连接的所有其他状态都会丢失，例如，如果我们处于中间状态，则处于事务状态：
```
$ redis-cli
127.0.0.1:6379> multi
OK
127.0.0.1:6379> ping
QUEUED

( here the server is manually restarted )

127.0.0.1:6379> exec
(error) ERR EXEC without MULTI
```

在交互模式下使用CLI进行测试时，这通常不是问题，但您应该了解这一限制

##  编辑，历史和完成

由于redis-cli使用[linenoise行编辑库](https://github.com/antirez/linenoise)，它始终具有行编辑功能，而不依赖于libreadline其他可选库。

您可以访问已执行的命令的历史记录，以便通过按方向键（向上和向下）来避免重复键入它们。.rediscli_history在HOME环境变量指定的用户主目录内调用的文件中，CLI的重新启动之间保存历史记录 。可以通过设置REDISCLI_HISTFILE环境变量来使用不同的历史文件名，并通过将其设置为禁用它/dev/null。

CLI还能够通过按TAB键执行命令名称完成，如下例所示：
```
127.0.0.1:6379> Z<TAB>
127.0.0.1:6379> ZADD<TAB>
127.0.0.1:6379> ZCARD<TAB>
```

##  运行相同的命令N次

可以通过在命令名前添加一个数字来多次运行相同的命令：
```
127.0.0.1:6379> 5 incr mycounter
(integer) 1
(integer) 2
(integer) 3
(integer) 4
(integer) 5
```

##  显示有关Redis命令的帮助

Redis有很多命令，有时候，当你测试的时候，你可能不记得参数的确切顺序。redis-cli使用该help命令为大多数Redis命令提供联机帮助。该命令可以以两种形式使用：
-   help @<category>显示关于给定类别的所有命令。该类别有：@generic，@list，@set，@sorted_set，@hash， @pubsub，@transactions，@connection，@server，@scripting， @hyperloglog。
-   help <commandname> 显示作为参数给出的命令的特定帮助。

例如，为了显示对该PFADD命令的帮助，请使用：
`127.0.0.1:6379>帮助PFADD`

PFADD键元素[element ...]摘要：将指定的元素添加到指定的HyperLogLog。因为：2.8.9

请注意，也help支持TAB完成。

##  清除终端屏幕

clear在交互模式下使用该命令将清除终端的屏幕

##  特殊的操作模式

到目前为止，我们看到了两种主要模式redis-cli。
-   命令行执行Redis命令。
-   交互式的“REPL-like”用法。

然而，CLI执行与Redis相关的其他辅助任务，这些任务将在以下部分中进行解释：
-   监控工具显示有关Redis服务器的连续统计信息。
-   扫描Redis数据库以查找非常大的密钥。
-   与模式匹配的关键空间扫描仪。
-   作为Pub / Sub客户订阅频道。
-   监视执行到Redis实例中的命令。
-   以不同方式检查Redis服务器的延迟。
-   检查本地计算机的调度程序延迟。
-   在本地从远程Redis服务器传输RDB备份。
-   扮演Redis奴隶的角色，展现奴隶所接受的东西。
-   模拟LRU工作负载以显示有关按键命中的统计信息。
-   Lua调试器的客户端。

##  连续统计模式

这可能是其中一个鲜为人知的特性redis-cli，而且为了实时监控Redis实例，这非常有用。要启用此模式，请使用该--stat选项。在这种模式下，CLI的行为输出非常清晰：
```
$ redis-cli --stat
------- data ------ --------------------- load -------------------- - child -
keys       mem      clients blocked requests            connections
506        1015.00K 1       0       24 (+0)             7
506        1015.00K 1       0       25 (+1)             7
506        3.40M    51      0       60461 (+60436)      57
506        3.40M    51      0       146425 (+85964)     107
507        3.40M    51      0       233844 (+87419)     157
507        3.40M    51      0       321715 (+87871)     207
508        3.40M    51      0       408642 (+86927)     257
508        3.40M    51      0       497038 (+88396)     257
```

在这种模式下，每秒都会打印一条新的线条，其中包含有用信息和旧数据点之间的差异。您可以轻松了解内存使用情况，连接的客户端等情况。

`-i <interval>`在这种情况下，该选项可用作修改器，以改变发射新线的频率。默认值是一秒。

##  扫描大键

在这个特殊的模式下，redis-cli可以作为关键的空间分析仪。它扫描大键的数据集，但也提供有关数据集组成的数据类型的信息。该模式使用该--bigkeys选项启用，并产生相当详细的输出：
```
$ redis-cli --bigkeys

# Scanning the entire keyspace to find biggest keys as well as
# average sizes per key type.  You can use -i 0.1 to sleep 0.1 sec
# per 100 SCAN commands (not usually needed).

[00.00%] Biggest string found so far 'key-419' with 3 bytes
[05.14%] Biggest list   found so far 'mylist' with 100004 items
[35.77%] Biggest string found so far 'counter:__rand_int__' with 6 bytes
[73.91%] Biggest hash   found so far 'myobject' with 3 fields

-------- summary -------

Sampled 506 keys in the keyspace!
Total key length in bytes is 3452 (avg len 6.82)

Biggest string found 'counter:__rand_int__' has 6 bytes
Biggest   list found 'mylist' has 100004 items
Biggest   hash found 'myobject' has 3 fields

504 strings with 1403 bytes (99.60% of keys, avg size 2.78)
1 lists with 100004 items (00.20% of keys, avg size 100004.00)
0 sets with 0 members (00.00% of keys, avg size 0.00)
1 hashs with 3 fields (00.20% of keys, avg size 3.00)
0 zsets with 0 members (00.00% of keys, avg size 0.00)
```

在输出的第一部分中，报告每个大于前一个较大键（同一类型）的新键。摘要部分提供有关Redis实例内数据的一般统计信息。

该程序使用该SCAN命令，因此它可以在不影响操作的情况下在繁忙的服务器上执行，但是-i可以使用该选项来限制所请求的每个100个键的指定小数秒的扫描进程。例如，-i 0.1会减慢程序执行的速度，但也会将服务器的负载减少到很小的数量。

请注意，摘要还会以更清晰的形式报告每次发现的最大键。如果对一个非常大的数据集运行，最初的输出只是提供一些有趣的信息。

##  获取密钥列表

也可以扫描密钥空间，再次以不阻塞Redis服务器的方式（当您使用类似命令时会发生这种情况KEYS *），并打印所有密钥名称或筛选特定模式。与--bigkeys选项一样，此模式使用该SCAN命令，因此如果数据集正在更改，可能会多次报告密钥，但是如果自从迭代开始以来该密钥存在，则不会丢失任何密钥。由于它使用此选项的命令被调用--scan。
```
$ redis-cli --scan | head -10
key-419
key-71
key-236
key-50
key-38
key-458
key-453
key-499
key-446
key-371
```

请注意，head -10仅用于打印输出的第一行。

扫描能够使用SCAN该--pattern选项的命令的底层模式匹配功能。
```
$ redis-cli --scan --pattern '*-11*'
key-114
key-117
key-118
key-113
key-115
key-112
key-119
key-11
key-111
key-110
key-116
```

通过wc命令管道输出可用于按键名称来计算特定种类的对象：
```
$ redis-cli --scan --pattern 'user:*' | wc -l
3829433
```

##  发布/子模式

CLI可以使用该PUBLISH命令在Redis Pub / Sub通道中发布消息。这是预料之中的，因为该PUBLISH命令与任何其他命令非常相似。订阅频道以接收消息是不同的 - 在这种情况下，我们需要阻止和等待消息，因此这是作为一种特殊模式实现的redis-cli。与其他特殊模式不同，此模式不是通过使用特殊选项启用的，而是仅使用SUBSCRIBEor PSUBSCRIBE命令启用的，无论是在交互模式还是非交互模式下：
```
$ redis-cli psubscribe '*'
Reading messages... (press Ctrl-C to quit)
1) "psubscribe"
2) "*"
3) (integer) 1

```

在阅读邮件消息表明，我们进入了发布/订阅模式。当其他客户端在某个频道发布某条消息时（例如您可以使用redis-cli PUBLISH mychannel mymessage该消息），Pub / Sub模式下的CLI将显示如下内容：
```
1) "pmessage"
2) "*"
3) "mychannel"
4) "mymessage"
```

这对调试Pub / Sub问题非常有用。要退出发布/订阅模式，只需处理CTRL-C

##  监视在Redis中执行的命令

与Pub / Sub模式类似，一旦您使用该MONITOR模式，将自动输入监控模式。它将打印Redis实例收到的所有命令：
```
$ redis-cli monitor
OK
1460100081.165665 [0 127.0.0.1:51706] "set" "foo" "bar"
1460100083.053365 [0 127.0.0.1:51707] "get" "foo"
```

请注意，可以使用管道输出，因此您可以使用类似的工具监视特定模式grep

##  监视Redis实例的延迟

Redis经常用于延迟非常关键的环境中。延迟涉及应用程序中的多个移动部分，从客户端库到网络堆栈，再到Redis实例本身。

CLI有多种功能用于研究Redis实例的延迟并了解延迟的最大值，平均值和分布。

基本的延迟检查工具是--latency可选的。使用此选项，CLI运行一个循环，将PING命令发送到Redis实例，并测量获得答复的时间。这种情况每秒发生100次，统计信息在控制台中实时更新：
```
$ redis-cli --latency
min: 0, max: 1, avg: 0.19 (427 samples)
```

统计数据以毫秒提供。通常，由于系统的内核调度程序redis-cli 本身导致延迟，所以一个非常快的实例的平均延迟往往会被高估一点，所以0.19以上的平均延迟可能很容易为0.01或更小。然而，这通常不是一个大问题，因为我们对几毫秒或更长时间的事件感兴趣。

有时研究最大和平均潜伏期如何随时间发展是有用的。该--latency-history选项用于此目的：它的工作原理与此类似--latency，但每隔15秒（默认情况下），新的采样会话将从头开始：
```
$ redis-cli --latency-history
min: 0, max: 1, avg: 0.14 (1314 samples) -- 15.01 seconds range
min: 0, max: 1, avg: 0.18 (1299 samples) -- 15.00 seconds range
min: 0, max: 1, avg: 0.20 (113 samples)^C
```

您可以使用该`-i <interval>`选项更改采样会话的长度。

最先进的延迟研究工具，对于没有经验的用户来说也有点难解释，是使用彩色终端显示一系列延迟的能力。您将看到一个彩色输出，指示不同百分比的样本，以及指示不同延迟数字的不同ASCII字符。该模式使用以下--latency-dist 选项启用：
```
$ redis-cli --latency-dist
(output not displayed, requires a color terminal, try it!)
```

里面还有一个非常不寻常的延迟工具redis-cli。它不检查Redis实例的延迟，而是检查正在运行的计算机的延迟redis-cli。你可能会问什么延迟？内核调度程序固有的延迟，虚拟化实例情况下的管理程序等等。

我们称之为内部延迟，因为它对大多数程序员来说是不透明的。如果您的Redis实例的延迟时间很长，无论所有显而易见的事情可能是什么原因造成的，那么通过redis-cli在运行Redis服务器的系统中直接在此特殊模式下运行，可以确保系统能够做到最好。

通过测量内部延迟，您知道这是基准，Redis无法超越您的系统。为了在此模式下运行CLI，请使用`--intrinsic-latency <test-time>`。测试的时间以秒为单位，并指定redis-cli检查当前正在运行的系统的延迟时间。
```
$ ./redis-cli --intrinsic-latency 5
Max latency so far: 1 microseconds.
Max latency so far: 7 microseconds.
Max latency so far: 9 microseconds.
Max latency so far: 11 microseconds.
Max latency so far: 13 microseconds.
Max latency so far: 15 microseconds.
Max latency so far: 34 microseconds.
Max latency so far: 82 microseconds.
Max latency so far: 586 microseconds.
Max latency so far: 739 microseconds.

65433042 total runs (avg latency: 0.0764 microseconds / 764.14 nanoseconds per run).
Worst run took 9671x longer than the average latency.
```

重要提示：必须在要运行Redis服务器的计算机上执行此命令，而不是在不同的主机上执行此命令。它甚至不连接到Redis实例，只在本地执行测试。

在上述情况下，我的系统不能比739微妙的最差等待时间做得更好，所以我预计某些查询可能会在不到1毫秒的时间内运行。

##  远程备份RDB文件

在Redis复制的第一次同步期间，主设备和从设备以RDB文件的形式交换整个数据集。此功能被利用redis-cli以提供远程备份功能，允许将RDB文件从任何Redis实例传输到本地计算机上运行 redis-cli。要使用此模式，请使用以下--rdb <dest-filename> 选项调用CLI ：
```
$ redis-cli --rdb /tmp/dump.rdb
SYNC sent to master, writing 13256 bytes to '/tmp/dump.rdb'
Transfer finished with success.
```

这是确保您拥有Redis实例的灾难恢复RDB备份的简单而有效的方法。但是，在脚本或cron作业中使用此选项时，请务必检查命令的返回值。如果它不为零，则发生错误，如下例所示：
```
$ redis-cli --rdb /tmp/dump.rdb
SYNC with master failed: -ERR Can't SYNC while not connected with my master
$ echo $?
1
```

##  从模式

CLI的从属模式是一种高级功能，可用于Redis开发人员和调试操作。它允许检查主站发送到复制流中的从站以便将写入传播到其副本。选项名称很简单--slave。这是如何工作的：
```
$ redis-cli --slave
SYNC with master, discarding 13256 bytes of bulk transfer...
SYNC done. Logging commands from master.
"PING"
"SELECT","0"
"set","foo","bar"
"PING"
"incr","myconuter"
```

该命令首先丢弃第一个同步的RDB文件，然后记录以CSV格式接收的每个命令。

如果您认为某些命令未在您的从站中正确复制，这是检查发生的事情的好方法，也是有用的信息以改进错误报告。

##  执行LRU模拟

Redis通常用作LRU驱逐的缓存。根据密钥的数量和为缓存分配的内存量（通过maxmemory指令指定），缓存命中和未命中的数量将会改变。有时，模拟命中率对正确配置缓存非常有用。

CLI有一个特殊模式，它在请求模式中使用80-20％幂律分布来执行GET和SET操作的模拟。这意味着20％的密钥将被请求80％的时间，这是高速缓存场景中的普遍分布。

理论上，考虑到请求分布和Redis内存开销，应该可以用数学公式分析计算命中率。但是，Redis可以配置为具有不同的LRU设置（样本数量），并且LRU的实现（在Redis中近似）在不同版本之间会发生很大变化。类似地，每个密钥的内存容量在版本之间可能会有所不同 这就是为什么这个工具被构建的原因：它的主要动机是测试Redis的LRU实现的质量，但现在也可用于测试给定版本的行为与您为部署考虑的设置有何关系。

为了使用此模式，您需要指定测试中的密钥数量。您还需要配置一个maxmemory有意义的设置作为第一次尝试。

重要注意事项：maxmemory在Redis配置中配置设置至关重要：如果没有最大内存使用限制，由于所有密钥都可以存储在内存中，因此命中最终将为100％。或者，如果您指定的键太多而没有最大内存，则最终将使用所有计算机RAM。还需要配置适当的 maxmemory策略，大部分时间是您想要的allkeys-lru。

在以下示例中，我配置了100MB的内存限制，并使用1000万个密钥对LRU进行了仿真。

警告：测试使用流水线并会给服务器带来压力，请勿将其用于生产实例。
```
$ ./redis-cli --lru-test 10000000
156000 Gets/sec | Hits: 4552 (2.92%) | Misses: 151448 (97.08%)
153750 Gets/sec | Hits: 12906 (8.39%) | Misses: 140844 (91.61%)
159250 Gets/sec | Hits: 21811 (13.70%) | Misses: 137439 (86.30%)
151000 Gets/sec | Hits: 27615 (18.29%) | Misses: 123385 (81.71%)
145000 Gets/sec | Hits: 32791 (22.61%) | Misses: 112209 (77.39%)
157750 Gets/sec | Hits: 42178 (26.74%) | Misses: 115572 (73.26%)
154500 Gets/sec | Hits: 47418 (30.69%) | Misses: 107082 (69.31%)
151250 Gets/sec | Hits: 51636 (34.14%) | Misses: 99614 (65.86%)
```

该程序每秒显示统计信息。如您所见，在第一秒钟内缓存开始被填充。失败率稍后稳定在我们可以预期的实际数字中：
```
120750 Gets/sec | Hits: 48774 (40.39%) | Misses: 71976 (59.61%)
122500 Gets/sec | Hits: 49052 (40.04%) | Misses: 73448 (59.96%)
127000 Gets/sec | Hits: 50870 (40.06%) | Misses: 76130 (59.94%)
124250 Gets/sec | Hits: 50147 (40.36%) | Misses: 74103 (59.64%)
```

对我们的用例来说，59％的愤怒可能是不可接受的。所以我们知道100MB内存是不够的。让我们试试半千兆字节。几分钟后，我们会看到输出稳定到以下数字：
```
140000 Gets/sec | Hits: 135376 (96.70%) | Misses: 4624 (3.30%)
141250 Gets/sec | Hits: 136523 (96.65%) | Misses: 4727 (3.35%)
140250 Gets/sec | Hits: 135457 (96.58%) | Misses: 4793 (3.42%)
140500 Gets/sec | Hits: 135947 (96.76%) | Misses: 4553 (3.24%)
```

所以我们知道在500MB的情况下，我们的密钥数量足够多（1000万）和分配（80-20个样式）