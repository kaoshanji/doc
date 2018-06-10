#   JavaScript：一门跨平台、面向对象的轻量级脚本语言

在宿主环境（例如 web 浏览器）中， JavaScript 能够通过其所连接的环境提供的编程接口进行控制

JavaScript 的核心部分可以通过添加对象来扩展语言以适应不同用途；例如：
-   客户端的 JavaScript 通过提供控制浏览器及其文档对象模型（DOM）的对象来扩展语言核心。例如：客户端版本直接支持应用将元素放在HTML表单中并且支持响应用户事件比如鼠标点击、表单提交和页面导航。
-   服务端的 JavaScript 则通过提供有关在服务器上运行 JavaScript 的对象来可扩展语言核心。例如：服务端版本直接支持应用和数据库通信，提供应用不同调用间的信息连续性，或者在服务器上执行文件操作。

令人兴奋的是建立在 JavaScript 语言的核心之上的功能。在你的 JavaScript 代码里，被称为应用程序编程接口。APIs 是已经建立好的一套代码组件，目的是让开发者可以实现除此之外很难甚至不可能实现的程序。它们 (APIs) 通常分成两个分类
-   浏览器 APIs (Browser APIs) 已经安装在你的网页浏览器中，而且能够从周围的计算机环境中揭露数据，或者做有用的复杂事情
    -   文档对象模型 API允许你操作 HTML 和 CSS，创建，移除和修改 HTML，动态地应用新的样式到你的页面，等等。比如说每次你在一个页面里看到一个弹出窗口，或者显示一些新的内容（像我们在上面的简单演示中看到那样），这就是 DOM 在运作
    -   地理定位 API获取地理信息。这就是为什么谷歌地图可以找到你的位置，而且标示在地图上。
    -   画布 和 WebGL APIs 允许你创建生动的 2D 和 3D 图像。人们正运用这些网页技术进行一些令人惊叹的事情
    -   音像和影像 APIs ，像 HTMLMediaElement 和 WebRTC 允许你运用多媒体去做一些非常有趣的事情，比如在网页中播放音像和影像，或者从你的网页摄像头中获取获取录像，然后在其他人的电脑上展示
-   第三方 APIs (Third party APIs) 默认是没有安装到浏览器中的，而你通常需要从网络上的某些地方取得它们的代码和信息
    -   推特 API 允许你做一些像是在你的网站上展示你的最新推送之类的事情
    -   谷歌地图 API 允许你去嵌入定制的地图到你的网站，和其他的功能


##  指南
-   语法与数据类型
    -   基本语法与注释
    -   声明
    -   变量作用域
    -   变量提升
    -   数据结构与类型
    -   字面量
-   控制流与错误处理
    -   if...else
    -   switch
    -   try/catch/throw
    -   Error 对象
    -   Promises
-   循环与迭代
    -   for
    -   while
    -   do...while
    -   break/continue
    -   for..in
    -   for..of
-   函数
    -   定义函数
    -   调用函数
    -   函数作用域
    -   闭包
    -   arguments 对象 和 参数
    -   箭头函数
-   表达式和运算符
    -   赋值 & 比较
    -   算术运算符
    -   位运算 & 逻辑运算符
    -   条件（三元）运算符
-   数字和日期
    -   Number 字面值
    -   Number 对象
    -   Math 对象
    -   Date 对象
-   文本格式化
    -   字符串字面量
    -   字符串对象
    -   模版字面量
    -   国际化
    -   正则表达式
-   索引集合
   -   数组
   -   类型数组
-   键值集合
   -   Map
   -   WeakMap
   -   Set
   -   WeakSet
-   处理对象
   -   对象和属性
   -   创建对象
   -   定义方法
   -   getter 和 setter
-   对象模型的细节
   -   基于原型的面向对象编程
   -   创建对象层次结构
   -   继承
-   迭代器与生成器
   -   迭代器
   -   生成器
   -   可迭代对象
   -   高级生成器
-   元编程
   -   Proxy
   -   Handlers 和 traps
   -   撤销 Proxy
   -   Reflect

##  参考：可复制到其他语言中去
-   [标准对象](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects)
-   [表达式和运算符](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Operators)
-   [语句和声明](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Statements)
-   [函数](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Functions)


##  工具
-   Firefox 开发工具
