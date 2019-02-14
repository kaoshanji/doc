#   [附加API](https://docs.oracle.com/javase/8/docs/technotes/guides/attach/index.html)

Attach API是一个扩展，它提供了一种附加到Java虚拟机的机制。使用Java语言编写的工具使用此API附加到目标虚拟机并将其工具代理加载到该虚拟机中。例如，管理控制台可能具有管理代理程序，该管理代理程序用于从虚拟机中的已检测对象获取管理信息。如果管理控制台需要管理在不包含管理代理程序的虚拟机中运行的应用程序，则可以使用此API附加到目标虚拟机并加载代理程序。

----
##  API规范
-   [附加API](https://docs.oracle.com/javase/8/docs/jdk/api/attach/spec/index.html)

----

