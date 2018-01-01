# 官方教程 记录
> http://python.usyiyi.cn/documents/python_278/tutorial/index.html

## 控制流
-   if 语句
```
    if x < 0:
        x = 0
        print 'Negative changed to zero'
    elif x == 0:
        print 'zero'
    elif x == 1:
        print 'Single'
    else:
        print 'More'
```
-   for 语句
```
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print w, len(w)
```
-   range()函数
```
    # 遍历一个数字序列
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
-   break和continue语句，以及循环中else子句
```
    #   break语句用于跳出最近的for或while循环
    #   continue语句表示继续下一次迭代
    for n in range(2, 10):
        for x in range(2, n):
            if n % x == 0:
                print n, 'equals', x, '*', n/x
                break
        else:
            print n, 'is a prime number'
    # 注：else子句属于for循环，不属于if语句
```
-   pass语句
```
    #   pass语句什么也不做。它用于语法上必须要有一条语句，但程序什么也不需要做的场合
    while True:
        pass
```
-   定义函数
```
    def fib(n):
        """简短说明/摘要..更多空出一行,在下面写"""

        """细说,详细的说"""
        a, b = 0, 1
        while a < n:
            print a,
            a, b = b, a+b

    fib(2000)
```
##  数据结构
-   深入list(列表)
```
    # 定义
    a = [66.25, 333, 333, 1, 1234.5]
    # 函数
    filter(function, sequence)  # 返回的序列由function(item)结果为真的元素组成
    map(function, sequence)  # 序列中的每一个元素调用 function(item) 函数并返回结果的列表
```
-  del语句
```
    # 根据索引而不是值来删除一个元素
    # 从列表中删除切片或清除整个列表
    # 删除整个变量
```
-   Tuples(元组)和sequences(序列)
```
    # 元组由逗号分割的若干值组成
    t = 12345, 54321, 'hello!'
    singleton = 'hello',
```
-   set(集合)
```
    # 集合中的元素没有顺序且不会重复。集合的基本用途有成员测试和消除重复的条目
    ss = {1,2,3}
    fruit = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
    # 若要创建一个空的集合你必须使用set()
```
-   字典
```
    # 无序的键:值 对集合，要求是键必须是唯一的
    # 一对花括号将创建一个空的字典：{}
    # 花括号中由逗号分隔的键:值对将成为字典的初始值
    tel = {'jack': 4098, 'sape': 4139}
```
-   遍历的技巧
```
    # 遍历一个序列时，使用enumerate()函数可以同时得到索引和对应的值
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print i, v

    # 同时遍历两个或更多的序列，使用zip()函数可以成对读取元素
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q, a in zip(questions, answers):
        print 'What is your {0}?  It is {1}.'.format(q, a)

    # 要按排序顺序循环一个序列，请使用sorted()函数，返回一个新的排序的列表，同时保留源不变
    basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print f

    # 遍历字典时，使用iteritems()方法可以同时得到键和对应的值
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.iteritems():
        print k, v
```
## 模块
> 把写好的脚本放到一个文本文件保存起来，以便在执行之后可以重复使用，或者把一些常用功能提取出来，在其他地方直接引用.这种文件称为`模块`.文件名就是模块名加上`.py`后缀.模块是包含 Python 定义和声明的文件,模块中的定义可以`导入`到其它模块或`主模块`中.

-   深入模块
    -   描述
        -   每个模块都有自己的私有符号表，模块内定义的所有函数用其作为全局符号表
        -   模块的作者可以在模块里使用全局变量，而不用担心与某个用户的全局变量有冲突
        -   模块中可以导入其它模块。习惯上将所有的 import 语句放在模块（或者脚本）的开始
    ```
        # import 语句的一个变体直接从被导入的模块中导入名字到导入模块的符号表中
        from fibo import fib, fib2
    ```
    -   执行模块
    ```
        # 模块后加入如下代码
        if __name__ == "__main__":
            import sys
            fib(int(sys.argv[1]))
        # 就可以让此文件既可以作为可执行的脚本，也可以当作可以导入的模块
        # 因为解析命令行的那部分代码只有在模块作为 “main” 文件执行时才被调用
    ```
-   标准模块
    -   Python 带有一个标准模块库，并发布有单独的文档叫Python 库参考手册
    -   有些模块被直接构建在解析器里
-   dir()函数
    -   内置函数 dir() 用来找出模块中定义了哪些名字
    -   返回一个排好序的字符串列表
-   包
    - 描述
        - 包是一种管理 Python 模块命名空间的方式，采用“点分模块名称”，模块名 A.B 表示包A 中一个名为 B 的子模块
        - 点分模块的使用让包含多个模块的包（例如 Numpy 和 Python Imaging Library）的作者也不用担心相互之间的模块重名
        - 假设你想要设计一系列模块（或一个“包”）来统一处理声音文件和声音数据
        ```
        sound/                          Top-level package
        __init__.py                     Initialize the sound package
        formats/                        Subpackage for file format conversions
                __init__.py
                wavread.py
                wavwrite.py
                aiffread.py
                aiffwrite.py
                auread.py
                auwrite.py
                ...
        effects/                  Subpackage for sound effects
                __init__.py
                echo.py
                surround.py
                reverse.py
                ...
        filters/                  Subpackage for filters
                __init__.py
                equalizer.py
                vocoder.py
                karaoke.py
        # 为了让 Python 将目录当做包，目录下必须包含__init__.py文件
        # __init__.py可以只是一个空的文件，但它也可以为包执行`初始化`代码或设置__all__变量
        # 可以从包中导入单独的模块
        import sound.effects.echo
        # 导入子模块的另一方法是
        from sound.effects import echo
        ```
##  输入和输出
-   格式化输出
    -   两种方法来设置输出格式：一种方式是自己做所有的字符串处理；使用str.format()方法
    -   string模块包含一个Template类，提供另外一种向字符串代入值的方法
    -   Python使用repr()(解释器可读)或str()(人类可读)函数将任何值转换为字符串
    ```
    # 输出字符串
    >>> s = 'Hello, world.'
    'Hello, world.'
    >>> repr(s)
    "'Hello, world.'"
    # 输出平方和立方表
    >>> for x in range(1, 11):
    ...     print repr(x).rjust(2), repr(x*x).rjust(3), // 在左侧填充空格使字符串在给定宽度的列右对齐
    ...     # Note trailing comma on previous line
    ...     print repr(x*x*x).rjust(4)
    # ------------
    >>> for x in range(1,11):
    ...     print '{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x)
    ...
    #  str.format()方法的基本用法如下所示
    >>> print '{0} and {1}'.format('spam', 'eggs')
    spam and eggs
    ```
-   读写文件
    -   描述
        -  open()返回一个文件对象，最常见的用法带有两个参数：open(filename, mode)
    -   文件对象的方法
        -   读取文件内容，可以调用f.read(size) 
        -   f.readline()从文件读取一行数据
        -   把文件中的所有行读到一个列表中，可以使用list(f)或f.readlines()
        -    f.write(string)将 string 的内容写入文件中并返回None
    -   使用json存储结构化数据
    ```
    # 有一个对象x，你可以用简单的一行代码查看其 JSON 字符串表示形式
    >>> json.dumps([1, 'simple', 'list'])
    '[1, "simple", "list"]'
    # dumps()函数的另外一个变体dump()，直接将对象序列化到一个文件。所以如果f是为写入而打开的一个文件对象，我们可以这样做
    json.dump(x, f)
    # 为了重新解码对象，如果f是为读取而打开的文件对象
    x = json.load(f)
    ```
##  错误和异常
-   描述
    -   Python（至少）有两种错误很容易区分：`语法错误` 和 `异常`
-   语法错误
    -   语法错误，或者称之为解析错误
-   异常
    -   在执行期间检测到的错误被称为异常 并且程序不会无条件地崩溃
-   处理异常
    -   可以通过编程来选择处理部分异常
    ```
    # 一直要求用户输入直到输入一个合法的整数为止，但允许用户中断这个程序,引发的是 KeyboardInterrupt 异常
    >>> while True:
    ...     try:
    ...         x = int(raw_input("Please enter a number: "))
    ...         break
    ...     except ValueError:
    ...         print "Oops!  That was no valid number.  Try again..."
    ```
-   引发异常
    -   raise语句允许程序员强行引发一个指定的异常
    ```
    >>> raise NameError('HiThere')
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    NameError: HiThere
    # raise的唯一参数指示要引发的异常。它必须是一个异常实例或异常类（从Exception派生的类）
    ```
-   用户定义的异常
    -   程序可以通过创建新的异常类来命名自己的异常（Python 类的更多内容请参见类）。异常通常应该继承Exception类，直接继承或者间接继承都可以
    ```
    >>> class MyError(Exception):
    ...     def __init__(self, value):
    ...         self.value = value
    ...     def __str__(self):
    ...         return repr(self.value)
    ...
    >>> try:
    ...     raise MyError(2*2)
    ... except MyError as e:
    ...     print 'My exception occurred, value:', e.value
    ...
    My exception occurred, value: 4
    >>> raise MyError('oops!')
    Traceback (most recent call last):
    File "<stdin>", line 1, in ?
    __main__.MyError: 'oops!'
    # Exception默认的__init__()被覆盖了。新的行为简单地创建了value 属性。这将替换默认的创建args 属性的行为
    # 大多数异常的名字都以"Error"结尾，类似于标准异常的命名
    ```
-   定义清理操作
    -    Try语句有另一个可选的子句，目的在于定义必须在所有情况下执行的清理操作
    ```
    >>> try:
    ...     raise KeyboardInterrupt
    ... finally:
    ...     print 'Goodbye, world!'
    ...
    Goodbye, world!
    KeyboardInterrupt
    # 不管有没有发生异常，在离开try语句之前总是会执行finally 子句
    #  finally子句用于释放外部资源（例如文件或网络连接），不管资源的使用是否成功
    ```
-   清理操作的预定义
    -    `With`语句可以确保像文件这样的对象总能及时准确地被清理掉
    ```
    with open("myfile.txt") as f:
    for line in f:
        print line,
    # 执行该语句后，文件f 将始终被关闭，即使在处理某一行时遇到了问题
    ```
## 类
-   描述
    -   提供了面向对象编程的所有标准功能： 类继承机制允许有多个基类，继承的类可以覆盖其基类或类的任何方法，方法能够以相同的名称调用基类中的方法
    -   对象可以包含任意数量和种类的数据
    -   和模块一样，类同样具有 Python 的动态性质：它们在运行时创建，并可以在创建之后进一步修改
-   名称和对象
    -   对象是独立的，多个名字（在多个作用域中）可以绑定到同一个对象，这在其他语言中称为别名
    -   别名的行为在某些方面类似指针
    -   例如，传递一个对象的开销是很小的，因为在实现上只是传递了一个指针
    -   如果函数修改了作为参数传进来的对象，调用者也会看到变化
-   Python作用域和命名空间
    -   `命名空间`是从名称到对象的映射
    -   各个命名空间创建的时刻是不一样的，且有着不同的生命周期
    -   `作用域`是 Python 程序中可以直接访问一个命名空间的代码区域
    -   函数的全局作用域是函数的定义所在的模块的命名空间，与函数调用的位置或者别名无关
-   初识类
    -   类定义语法
    ```
    # 类定义的最简单形式如下：
    class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
    # 类定义包含的语句通常是函数定义，不过其他语句也是被允许的
    # 进入类定义部分后，会创建出一个新的命名空间，作为局部作用域
    # 类定义正常结束时，一个类对象也就创建了。基本上它是对类定义创建的命名空间进行了一个包装
    ```
    -   类对象
        -   类对象支持两种操作：属性引用和实例化
        -   属性引用
        ```
        # 使用和Python中所有的属性引用一样的标准语法： obj.name
        class MyClass:
            """A simple example class"""
            i = 12345
            def f(self):
                return 'hello world'
        # 那么 MyClass.i 和 MyClass.f 是有效的属性引用，分别返回一个整数和一个函数对象
        # __doc__ 也是一个有效的属性，返回类的文档字符串： "A simple example class"
        ```
        -   类的实例化
        ```
        # 使用函数的符号。可以假设类对象是一个不带参数的函数，该函数返回这个类的一个新的实例
        x = MyClass()
        # 创建这个类的一个新实例，并将该对象赋给局部变量x
        # 实例化操作（“调用”一个类对象）将创建一个空对象
        # 很多类希望创建的对象可以自定义一个初始状态。因此类可以定义一个名为__init__()的特殊方法
        def __init__(self):
            self.data = []
        # 当类定义了__init__()方法，类的实例化会为新创建的类实例自动调用__init__()
        ```
    -   实例对象
        -   实例对象唯一可用的操作就是属性引用。有两种有效的属性名：数据属性和方法
        -   数据属性
            -   数据属性不需要声明；和局部变量一样，它们会在第一次给它们赋值时生成
        -   方法
            -   方法是"属于"一个对象的函数
    -   方法对象
        -   方法在绑定之后被直接调用
        ```
        x.f()
        # 在MyClass的示例中，这将返回字符串'hello world'。然而，也不是一定要直接调用方法： x.f是一个方法对象，可以存储起来以后调用
        ```
        -   方法的特别之处在于实例对象被作为函数的第一个参数传给了函数
        -   调用x.f()完全等同于MyClass.f(x)
    -   类和实例变量
        -   一般来说，实例变量用于对每一个实例都是唯一的数据，类变量用于类的所有实例共享的属性和方法
        ```
        class Dog:
            kind = 'canine'         # class variable shared by all instances
            def __init__(self, name):
                self.name = name    # instance variable unique to each instance
        >>> d = Dog('Fido')
        >>> e = Dog('Buddy')
        >>> d.kind                  # shared by all dogs
        'canine'
        >>> e.kind                  # shared by all dogs
        'canine'
        >>> d.name                  # unique to d
        'Fido'
        >>> e.name                  # unique to e
        'Buddy'
        ```
-   补充说明
    -   数据属性会覆盖同名的方法属性
    -   大写方法名称的首字母，使用一个小写的独特字符串（也许只是一个下划线）作为数据属性名称的前缀
-   继承
    -   派生类定义的语法如下所示
    ```
    class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
    #  BaseClassName必须与派生类定义在一个作用域内
    ```
-   私有变量和类本地引用
    -   在 Python 中不存在只能从对象内部访问的“私有”实例变量
    -   带有下划线（例如_spam）前缀的名称应被视为非公开的 API 的一部分（无论是函数、 方法还是数据成员）
-   异常也是类
    -   用户定义的异常类也由类标识
    -   raise语句有两种新的有效的（语义上的）形式
    ```
    raise Class, instance   // instance必须是Class或者它的子类的实例
    raise instance
    ```
-   迭代器
    -   大多数容器对象都可以用for遍历
    ```
    for element in [1, 2, 3]:
        print element
    for element in (1, 2, 3):
        print element
    for key in {'one':1, 'two':2}:
        print key
    for char in "123":
        print char
    for line in open("myfile.txt"):
        print line,
    ```
## 标准库概览
-   操作系统接口
    -   os模块提供了几十个函数与操作系统交互
    -   一定要使用import os的形式而不要用from os import *
    -   对于日常的文件和目录管理任务，shutil模块提供了一个易于使用的高级接口
    ```
    >>> import shutil
    >>> shutil.copyfile('data.db', 'archive.db')
    >>> shutil.move('/build/executables', 'installdir')
    ```
-   文件通配符
    -   glob模块提供了一个函数用于在目录中以通配符搜索文件，并生成匹配的文件列表
    ```
    >>> import glob
    >>> glob.glob('*.py')
    ['primes.py', 'random.py', 'quote.py']
    ```
-   命令行参数
    -   常见的实用程序脚本通常需要处理命令行参数。这些参数以一个列表存储在sys模块的argv 属性中
    ```
    >>> import sys
    >>> print sys.argv
    ['demo.py', 'one', 'two', 'three']
    # argparse模块提供更强大、 更灵活的命令行处理功能
    ```
-   错误输出重定向和程序终止
    -   sys模块还具有stdin、stdout和stderr属性。即使在stdout被重定向时，后者也可以用于显示警告和错误信息
    ```
    >>> sys.stderr.write('Warning, log file not found starting a new one\n')
    Warning, log file not found starting a new one
    ```
    -   终止脚本最直接的方法来是使用sys.exit()
-   字符串模式匹配
    -   re模块为高级的字符串处理提供了正则表达式工具
    ```
    >>> import re
    >>> re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
    ['foot', 'fell', 'fastest']
    >>> re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
    'cat in the hat'
    ```
    -   当只需要简单的功能时，最好使用字符串方法
    ```
    >>> 'tea for too'.replace('too', 'two')
    'tea for two'
    ```
-   数学
    -   math模块为浮点运算提供了对底层 C 函数库的访问
    -   random模块提供了进行随机选择的工具
-   互联网访问
    -   最简单的两个模块是从URL获取数据的urllib2 和发送邮件的smtplib
    ```
    >>> import urllib2
    >>> for line in urllib2.urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    ...     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
    ...         print line
    <BR>Nov. 25, 09:43:32 PM EST
    >>> import smtplib
    >>> server = smtplib.SMTP('localhost')
    >>> server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
    ... """To: jcaesar@example.org
    ... From: soothsayer@example.org
    ...
    ... Beware the Ides of March.
    ... """)
    >>> server.quit()
    # 第二个示例需要在本地主机上运行邮件服务器
    ```
-   日期和时间
    -   datetime模块提供了处理日期和时间的类，实现的重点放在更有效的处理和格式化输出。该模块还支持处理时区
-   数据压缩
    -   常见的数据打包和压缩格式都直接支持，这些模块包括：zlib、gzip、bz2、zipfile和tarfile
## 标准库概览 — 第II部分
-   输出格式
    -   repr模块提供的repr()的自定义的缩写显示大型或深层嵌套容器的版本
    -   pprint模块提供更复杂的打印控制，以解释器可读的方式打印出内置对象和用户定义的对象
    -   textwrap 模块格式化文本段落以适应设定的屏宽
    -   locale模块会访问区域性特定数据格式的数据库
-   日志
    -   logging模块提供了一个具有完整功能并且非常灵活的日志系统
-   列表工具
    -   array模块提供一个array()对象可以像list一样存储数据，只能存储同类数据和更简洁
    -   collections模块提供了一个deque()对象，就像一个列表,不过它从左边添加和弹出更快，但是在内部查询更慢
    -   heapq模块提供的函数可以实现基于常规列表的堆
-   十进制浮点数运算
    -   decimal模块提供一个Decimal数据类型用于为十进制浮点运算