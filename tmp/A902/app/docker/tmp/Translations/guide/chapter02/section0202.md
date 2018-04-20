#   管理容器中的数据

在本节中，您将学习如何管理Docker容器内部和之间的数据

您将看到可以使用Docker Engine管理数据的两种主要方式
-   数据量
-   数据量容器

##  数据量

一个数据量是绕过一个或多个容器内的特别指定的目录`union文件系统`。数据卷为永久或共享数据提供了几个有用的功能：
-   当容器被创建时，卷被初始化。如果容器的父映像包含指定装入点处的数据，则在卷初始化时，现有数据将被复制到新卷中。（请注意，在安装主机目录时这不适用。）
-   数据卷可以在容器中共享和重用。
-   数据量的变化是直接进行的。
-   更新镜像时，不会包含对数据量的更改
-   即使容器本身被删除，数据卷仍然存在

数据卷旨在持久化数据，与容器的生命周期无关。因此，Docker 在删除容器时不会自动删除卷，也不会“垃圾收集”不再由容器引用的卷

##  添加数据量

您可以使用`-v`带有`docker createand docker run`命令的标志 将数据卷添加到容器。您可以`-v`多次使用来装载多个数据卷。现在，在您的Web应用程序容器中安装一个卷

```
$ docker run -d -P --name web -v /webapp training/webapp python app.py
```

这将在一个容器内创建一个新卷`/webapp`

>   `注意`：您也可以使用a中的`VOLUME`说明`Dockerfile`将一个或多个新卷添加到从该映像创建的任何容器中

##  找到一个卷

您可以使用该`docker inspect`命令在主机上找到卷

```
$ docker inspect web
```

输出将提供容器配置的详细信息，包括容量。输出应该看起来类似于以下内容：

```
...
"Mounts": [
    {
        "Name": "fac362...80535",
        "Source": "/var/lib/docker/volumes/fac362...80535/_data",
        "Destination": "/webapp",
        "Driver": "local",
        "Mode": "",
        "RW": true,
        "Propagation": ""
    }
]
...
```

您会注意到上面`Source`指定了主机上的位置并 `Destination`指定了容器内的音量位置。RW显示该卷是否可读/写。

##  将主机目录挂载为数据卷

除了使用`-v`标志创建卷之外，还可以将Docker引擎主机的目录挂载到容器中

```
$ docker run -d -P --name web -v /src/webapp:/webapp training/webapp python app.py
```

该命令将主机目录，安装`/src/webapp`到容器中 `/webapp`。如果该路径`/webapp`已经存在于容器的映像中，则`/src/webapp`挂载覆盖但不会删除预先存在的内容。一旦挂载被删除，内容可以再次访问。这与该`mount`命令的预期行为一致。

在`container-dir`必须始终是绝对路径，例如`/src/docs`。该`host-dir`可以是绝对路径，例如`/dst/docs`在Linux或`C:\dst\docsWindows`上，或`name`价值。如果你提供了一个绝对路径`host-dir`，Docker绑定到你指定的路径。如果你提供一个`name`，Docker通过它创建一个命名的卷`name`

`name`值必须以`字母数字字符`，接着启动a-z0-9，_（下划线）， .（周期）或-（连字符）。绝对路径以/（正斜杠）开头

例如，您可以指定一个值`/foo`或`foo`一个`host-dir`值。如果您提供该`/foo`值，Docker引擎将创建一个绑定挂载。如果提供`foo`规范，Docker引擎会创建一个命名卷

如果您在Mac或Windows上使用Docker Machine，则Docker引擎守护程序只能访问您的macOS或Windows文件系统。Docker机器尝试自动共享您的`/Users（macOS）`或`C:\Users`（Windows）目录。所以，你可以使用macOS挂载文件或目录

```
docker run -v /Users/<path>:/<container path> ...
```

在Windows上，使用以下命令装载目录

```
docker run -v c:\<path>:c:\<container path>
```

所有其他路径来自您的虚拟机的文件系统，所以如果您想让其他主机文件夹可用于共享，则需要做额外的工作。在VirtualBox的情况下，您需要使主机文件夹可用作VirtualBox中的共享文件夹。然后，您可以使用Docker `-v`标志挂载它

挂载主机目录对于测试非常有用。例如，您可以在容器中安装源代码。然后，更改源代码并实时查看其对应用程序的影响。主机上的目录必须指定为绝对路径，如果该目录不存在，Docker Engine守护进程会自动为您创建它

Docker卷默认以读写模式挂载，但您也可以将其设置为只读挂载

```
$ docker run -d -P --name web -v /src/webapp:/webapp:ro training/webapp python app.py
```

在这里你已经挂载了相同的`/src/webapp`目录，但是你添加了`ro` 选项来指定挂载应该是只读的

您还可以通过添加以下cached选项来放宽挂载目录的一致性要求以提高性能：

```
$ docker run -d -P --name web -v /src/webapp:/webapp:cached training/webapp python app.py
```

该`cached`选项通常会提高Docker for Mac上读取繁重工作负载的性能，代价是主机和容器之间存在一些暂时的不一致。在其他平台上，`cached`目前没有任何效果。Docker for Mac中的用户引导缓存文章 提供了有关cachedmacOS 行为的更多详细信息

>   `注意`：主机目录本质上取决于主机。因为这个原因，你不能从一个主机目录挂载`Dockerfile`，该`VOLUME` 指令不支持传递一个`host-dir`，因为构建的映像应该是可移植的。主机目录在所有可能的主机上都不可用

##  将共享存储卷挂载为数据卷

除了在容器中安装主机目录之外，一些Docker 卷插件允许您配置和装入共享存储，如iSCSI，NFS或FC

使用共享卷的好处是它们独立于主机。这意味着只要有权访问共享存储后端并且安装了插件，就可以在容器启动的任何主机上使用卷。

使用音量驱动程序的一种方法是通过`docker run`命令。卷驱动程序按名称创建卷，而不是像其他示例中的路径

以下命令`my-named-volume`使用`convoy`卷驱动程序（`convoy`是各种存储后端的插件）创建一个名为volume的命名卷，并使其在容器中可用`/webapp`。在运行该命令之前， 请安装并配置车队。如果你不想安装`convoy`，更换`convoy`与`local`在下面的例子中命令使用该`local`驱动程序

```
$ docker run -d -P \
  --volume-driver=convoy \
  -v my-named-volume:/webapp \
  --name web training/webapp python app.py
```

您也可以使用该`docker volume create`命令在容器中使用它之前创建一个卷

以下示例还会`my-named-volume`使用该`docker volume create`命令创建卷。选项被指定为格式中的键值对`o=<key>=<value>`

```
$ docker volume create -d convoy --opt o=size=20GB my-named-volume

$ docker run -d -P \
  -v my-named-volume:/webapp \
  --name web training/webapp python app.py
```

##  卷标

像SELinux这样的标签系统要求在安装到容器中的卷内容上放置正确的标签。如果没有标签，安全系统可能会阻止容器内运行的进程使用内容。默认情况下，Docker不会更改OS设置的标签

要更改容器上下文中的标签，可以添加两个后缀中的任意一个`:z`或添加 `:Z`到卷装载。这些后缀告诉Docker重新标记共享卷上的文件对象。该z选项告诉Docker两个容器共享卷内容。因此，Docker使用共享内容标签来标记内容。共享卷标允许所有容器读取/写入内容。该Z选项告诉Docker使用私有非共享标签标记内容。只有当前容器可以使用私人卷

##  将主机文件挂载为数据卷

该`-v`标志还可用于 从主机安装单个文件 - 而不仅仅是目录

```
$ docker run --rm -it -v ~/.bash_history:/root/.bash_history ubuntu /bin/bash
```

这会让你进入一个新的容器中的bash shell，你将从主机获得你的bash历史记录，并且当你退出容器时，主机将拥有在容器中键入的命令的历史记录

>   `注意`：许多用于编辑文件的工具，包括`vi`和`sed --in-place`可能导致inode更改。由于Docker v1.1.0，这将产生一个错误，如“ sed：无法重命名./sedKdJ9Dy：设备或资源繁忙 ”。在你想编辑挂载文件的情况下，通常最容易挂载父目录

##  创建和安装数据卷容器

如果您想要在容器之间共享某些持久性数据，或者想要使用非持久性容器，则最好创建一个名为“数据容量容器”，然后从中装入数据

让我们创建一个新的带有要共享的卷的命名容器。虽然此容器不运行应用程序，但它会重新使用该`training/postgres` 映像，以便所有容器都使用通用层，从而节省磁盘空间  

```
$ docker create -v /dbdata --name dbstore training/postgres /bin/true
```

然后，您可以使用`--volumes-from`标志将`/dbdata`卷装入另一个容器中

```
$ docker run -d --volumes-from dbstore --name db1 training/postgres
```

另一个：

```
$ docker run -d --volumes-from dbstore --name db2 training/postgres
```

在这种情况下，如果`postgres`映像包含一个调用目录`/dbdata` ，则从`dbstore`容器中挂载卷会隐藏映像中的 `/dbdata`文件`postgres`。结果是只有`dbstore`容器中的文件是可见的

您可以使用多个`--volumes-from`参数来合并来自多个容器的数据卷。要查找有关 在命令参考中`--volumes-from`查看来自容器的 装入卷的详细信息`run`

您还可以通过安装的是来自于体积延长链 `dbstore`容器中通过另一个容器`db1`或`db2`容器

```
$ docker run -d --name db3 --volumes-from db1 training/postgres
```

如果删除安装卷容器，包括最初的`dbstore` 容器或接下来的容器`db1`和`db2`，卷将不会被删除。要从磁盘删除卷，必须显式调用 `docker rm -v`最后一个容器，并引用该卷。这使您可以升级或在容器之间有效迁移数据卷

>   `注意`：当删除一个容器而没有 提供`-v`删除它的卷的选项时，Docker不会警告你。如果您不使用该`-v`选项来移除容器，则最终可能会出现“摇晃”的卷; 不再被容器引用的卷。您可以使用它`docker volume ls -f dangling=true`来查找悬空卷，并用它`docker volume rm <volume name>`来删除不再需要的卷

##  备份，恢复或迁移数据卷

我们可以使用卷执行的另一个有用功能是用于备份，恢复或迁移。您可以通过使用该`--volumes-from`标志创建一个装载该卷的新容器来执行此操作 ，如下所示：

```
$ docker run --rm --volumes-from dbstore -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /dbdata
```

在这里，您启动了一个新的容器并从`dbstore`容器中安装了 容器。然后，您已经将一个本地主机目录挂载为 `/backup`。最后，您已经传递了一个命令，用于`tar`将`dbdata`卷的内容备份到`backup.tar`我们`/backup`目录中的文件中 。当命令完成并且容器停止时，我们将留下备份我们的`dbdata`卷。

然后，您可以将其恢复到同一个容器，或其他您在别处制作的另一个容器。创建一个新的容器

```
$ docker run -v /dbdata --name dbstore2 ubuntu /bin/bash
```

然后在新容器的数据卷中解压备份文件

```
$ docker run --rm --volumes-from dbstore2 -v $(pwd):/backup ubuntu bash -c "cd /dbdata && tar xvf /backup/backup.tar --strip 1"
```

您可以使用上述技术使用您首选的工具自动执行备份，迁移和恢复测试

##  列出所有卷

您可以使用列出所有现有卷`docker volume ls`

```
$ docker volume ls
DRIVER              VOLUME NAME
local               ec75c47aa8b8c61fdabcf37f89dad44266841b99dc4b48261a4757e70357ec06
local               f73e499de345187639cdf3c865d97f241216c2382fe5fa67555c64f258892128
local               tmp_data
```

##  删除卷

容器被删除后，Docker数据卷仍然存在。您可以创建命名卷或匿名卷。例如，命名卷在容器外部具有特定的源表单`awesome:/bar`。匿名卷没有特定的来源。当容器被删除时，您应该指示Docker Engine守护进程清理匿名卷。为此，请使用该`--rm`选项，例如：

```
$ docker run --rm -v /foo -v awesome:/bar busybox top
```

该命令创建一个匿名`/foo`卷。当容器被移除时，Docker引擎移除`/foo`音量但不移除`awesome`音量

要删除所有未使用的卷并释放空间

```
$ docker volume prune
```

它将删除所有未与任何容器关联的未使用的卷

##  有关使用共享卷的重要提示

多个容器也可以共享一个或多个数据卷。但是，写入单个共享卷的多个容器可能会导致数据损坏。确保您的应用程序旨在写入共享数据存储

数据卷可以直接从Docker主机访问。这意味着您可以使用普通的Linux工具读取和写入它们。在大多数情况下，您不应该这样做，因为如果您的容器和应用程序不知道您的直接访问，它可能会导致数据损坏


