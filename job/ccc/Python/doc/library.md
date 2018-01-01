#   官方标准库 记录
> http://python.usyiyi.cn/documents/python_278/library/index.html

##  引言
-   首先介绍了内置的数据类型
-   然后内置的函数和表达式
-   最后是按照相关性组织把模块组织成一些章节
-   按照章节中的模块大致从常用到不那么重要来排列的
-   模块 => 类 => 方法
##  内建异常
-   异常定义在 exceptions 模块中,该模块从不需要被显式地导入：这些异常在内建的命名空间中有提供
-   BaseException - 所有内建的异常的基类。它并不意味用户定义的类应该直接继承它
-   Exception  - 所有内建的、非系统退出的异常，都是从该类派生的。此外，应该从该类派生所有用户定义的异常
    -   StopIteration - 当一个 iterator 的 next() 方法发出信号，表示没有更多的值时引发
    -   StandardError - 应用异常
    -   Warning - 警告类别
-   SystemExit - 由 sys.exit() 函数引发此异常
-   KeyboardInterrupt - 当用户按下中断键（通常是 Ctrl-C 或 Delete）时引发
-   GeneratorExit - 当调用一个 generator 对象的 close() 方法时引发
##  字符串服务
-   string — 常见字符串操作
-   re — 正则表达式操作
-   difflib — 计算文档差异
-   StringIO — Read and write strings as files
-   cStringIO — Faster version of StringIO
-   textwrap — Text wrapping and filling
-   codecs — 编码解码器的注册和基本的类
##  数据类型
-   datetime — 基本的日期和时间类型
-   calendar — 通用日历相关函数
-   collections — 高性能容器数据类型
-   heapq — 堆队列算法
-   bisect — 数组二分算法
-   array — 定义了一个对象类型，可以紧凑地表示一个基本值的数组：字符，整数，浮点数
-   sched — 事件调度器
-   Queue — 同步队列类
    -   实现了多生产者、多消费者队列
    -   实现了所有必须的锁语义
-   types — Names for built-in types
-   copy - 浅层和深层复制操作
-   pprint — 打印整洁的数据
##  数值和数学模块
-   numbers — 数字的抽象基类
-   math — 数学函数
-   decimal — 十进制定点和浮点算术
##  文件和目录访问
-   os.path — 常用的路径操作
-   fileinput — 行遍历多个输入流
-   filecmp — 文件和目录的比较
-   tempfile — 生成临时文件和目录
-   glob — 根据 Unix shell 使用的规则查找所有与指定模式匹配的路径名
-   fnmatch — Unix shell样式通配符
-   linecache — Random access to text lines
-   shutil — 高级的文件操作(支持文件复制和删除的函数)
##  数据持久性
-   pickle — Python 对象序列化
-   cPickle — 一个更快的 pickle
-   sqlite3 — SQLite数据库DB-API 2.0接口
-   marshal — 能够读取和写入二进制格式的Python值的函数
-   anydbm - 对DBM样式数据库的通用访问
##  数据压缩和归档
-   gzip — Support for gzip files
-   zipfile — 和 ZIP 压缩文档打交道
##  文件格式
-   csv — CSV 文件的读写
    -   CSV格式是电子表格和数据库导入和导出最常见的格式
-   ConfigParser — 配置文件解析器
##  加密服务
-   hashlib — 安全哈希和消息摘要
-   hmac — 用于消息认证的加密哈希算法
-   md5 — MD5 信息摘要算法
##  通用操作系统服务
-   os — 操作系统的各种接口
-   time —时间获取和转换
-   select — 提供了访问select()和poll()函数（大部分OS支持），epoll()（仅Linux 2.5+支持）和kqueue()（仅大部分BSD系列支持）
-   threading — 高级线程接口
-   thread — 多线程控制
-   multiprocessing — 基于进程的“线程式”接口
##  进程间通信及网络访问
-   subprocess — 管理子进程
-   socket — 底层网络接口
-   signal — 提供了python中的信号处理机制
-   asyncore — 异步套接字处理器
-   asynchat — 异步套接字命令/响应处理器
    -   建立在 asyncore 基础结构上，简化了异步客户端和服务器，使得处理带有以任意字符串终止或者可变长度的元素的协议更加容易
##  网络数据处理
-   email — 电子邮件和MIME处理包
-   json — JSON 格式的编码器和解码器
-   base64 — Base16, Base32, Base64 数据编码
##  结构化标记处理工具
-   HTMLParser - 简单的HTML和XHTML解析器
-   XML — XML 处理模块
##  互联网协议和支持
-   webbrowser - 方便的Web浏览器控制器
-   cgi — 通用网关接口支持
-   wsgiref - WSGI实用程序和参考实现
-   urllib — Open arbitrary resources by URL通过URL打开任意资源
-   urllib2 — 扩展库for opening URLS
-   ftplib — FTP类实现 FTP 协议的客户端
-   poplib — POP3 协议客户端
-   smtplib — 定义了可用于将邮件发送到 SMTP 或 ESMTP 侦听器守护进程任何互联网机 SMTP 客户端会话对象
-   smtpd — SMTP 服务器
-   urlparse - 将URL解析成组件
-   BaseHTTPServer — 简单的HTTP 服务器
##  Python运行时服务
-   sys — 系统相关的参数和函数