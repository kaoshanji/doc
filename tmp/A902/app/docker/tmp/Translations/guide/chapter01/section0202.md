#   获取适用于 CentOS 的 Docker CE

##  Docker EE 客户

### 操作系统要求
如需安装 Docker CE，您需要 64 位版本的 CentOS 7

### 卸载旧版本
Docker 的早期版本称为 `docker` 或 `docker-engine`。如果安装了这些版本，请卸载它们及关联的依赖资源
```
$ sudo yum remove docker \
                  docker-common \
                  docker-selinux \
                  docker-engine
```
如果 `yum` 报告未安装任何这些软件包，这表示情况正常

将保留 `/var/lib/docker/` 的内容，包括镜像、容器、存储卷和网络。Docker CE 软件包现在称为 `docker-ce`

##  安装 Docker CE
您可以通过不同方式安装 Docker CE，具体取决于您的需求：
-   大多数用户设置 Docker 的镜像仓库并从中进行安装，从而可以轻松完成安装和升级任务。这是推荐方法
-   一些用户下载 RPM 软件包并手动进行安装，然后完全由手动管理升级。在某些情况（例如，在不能访问互联网的隔离系统中安装 Docker）下，这很有用

##  使用镜像仓库进行安装
首次在新的主机上安装 Docker CE 之前，您需要设置 Docker 镜像仓库。然后，您可以从此镜像仓库安装和更新 Docker

### 设置镜像仓库
1.  安装所需的软件包。`yum-utils` 提供了 `yum-config-manager` 实用程序，并且 `devicemapper` 存储驱动需要 `device-mapper-persistent-data` 和 `lvm2`
```
 $ sudo yum install -y yum-utils device-mapper-persistent-data lvm2
```
2.  使用下列命令设置 stable 镜像仓库。您始终需要使用 stable 镜像仓库，即使您还需要通过 edge 或 testing 镜像仓库安装构建也是如此
```
$ sudo yum-config-manager \
     --add-repo \
     https://download.docker.com/linux/centos/docker-ce.repo
```
3.  `可选`：启用 `edge` 和 `testing` 镜像仓库。这些镜像仓库包含在上述 `docker.repo` 文件中，但默认情况下处于禁用状态。您可以将它们与 stable 镜像仓库一起启用
```
$ sudo yum-config-manager --enable docker-ce-edge
```
```
$ sudo yum-config-manager --enable docker-ce-testing
```
您可以通过运行带有 `--disable` 标志的 `yum-config-manager` 命令来禁用 `edge` 或 `testing` 镜像仓库。如需将其重新启用，请使用 `--enable `标志。以下命令用于禁用 `edge` 镜像仓库
```
$ sudo yum-config-manager --disable docker-ce-edge
```

### 安装 DOCKER CE
1.  更新 yum 软件包索引
```
$ sudo yum makecache fast
```
如果这是自添加 Docker 镜像仓库以来您首次刷新软件包索引，系统将提示您接受 GPG 密钥，并且将显示此密钥的指纹。验证指纹是否正确，并且在正确的情况下接受此密钥。指纹应匹配 `060A 61C5 1B55 8A7F 742B 77AA C52F EB6B 621E 9F35`

2.  安装最新版本的 Docker CE，或者转至下一步以安装特定版本
```
$ sudo yum install docker-ce
```
`警告`：如果您启用了多个 Docker 镜像仓库，进行安装 或者更新而不在 `yum install` 或 `yum update` 命令中指定版本将始终安装可用的最高版本， 这可能无法满足您的稳定性需求

3.  在生产系统中，您应该安装特定版本的 Docker CE，而不是始终使用最新版本。列出可用版本。此示例使用 `sort -r` 命令按版本号（从最高到最低）对结果进行排序，并且已被截断
>   注：此 `yum list` 命令仅显示二进制软件包。如果还需要显示 源软件包，请从软件包名称中省略 `.x86_64`
```
$ yum list docker-ce.x86_64  --showduplicates | sort -r

 docker-ce.x86_64  17.06.0.el7                               docker-ce-stable  
```
此列表的内容取决于启用了哪些镜像仓库，并且将特定于您的 CentOS 版本（在本示例中，由版本中的 .el7 后缀表示）。选择一个特定版本进行安装。第二列为版本字符串。第三列为镜像仓库名称，它表示软件包来自哪个镜像仓库并按扩展其稳定性级别列出。如需安装特定版本，请将版本字符串附加到软件包名称，并使用连字符 (-) 分隔它们
```
$ sudo yum install docker-ce-<VERSION>
```

4.  启动 Docker
```
$ sudo systemctl start docker
```

5.  验证是否正确安装了` docker`，方法是运行 `hello-world` 镜像
```
$ sudo docker run hello-world
```
此命令将下载一个测试镜像并在容器中运行它。容器运行时，它将输出一条参考消息并退出

Docker CE 已安装并且正在运行。您需要使用 `sudo` 运行 Docker 命令

### 升级 DOCKER CE
如需升级 Docker CE，首先运行 `sudo yum makecache fast`，然后按照安装说明执行操作，并选择您要安装的新版本

##  从软件包进行安装
如果您无法使用 Docker 镜像仓库安装 Docker，可以下载适用于您的版本的 .rpm 文件，并手动进行安装。每次要升级 Docker 时，您都需要下载一个新文件

1.  转至 `https://download.docker.com/linux/centos/7/x86_64/stable/Packages/` 并下载适用于您要安装的 Docker 版本的 `.rpm` 文件
>   注：如需安装 `edge` 软件包，请将 URL 中的词 `stable` 更改为 `edge`

2.  安装 Docker CE，并将下面的路径更改为您下载 Docker 软件包的路径
```
$ sudo yum install /path/to/package.rpm
```

3.  启动 Docker
```
$ sudo systemctl start docker
```

4.  验证是否正确安装了 `docker`，方法是运行 `hello-world` 镜像
```
$ sudo docker run hello-world
```
此命令将下载一个测试镜像并在容器中运行它。容器运行时，它将输出一条参考消息并退出

Docker CE 已安装并且正在运行。您需要使用 `sudo` 运行 Docker 命令

### 升级 DOCKER CE
如需升级 Docker CE，请下载较新的软件包文件并重复安装过程，使用 `yum -y upgrade` 而不是 `yum -y install` 并指向新文件

##  卸载 Docker CE
1.  卸载 Docker 软件包
```
$ sudo yum remove docker-ce
```
2.  主机上的镜像、容器、存储卷、或定制配置文件不会自动删除。如需删除所有镜像、容器和存储卷，请运行下列命令
```
 $ sudo rm -rf /var/lib/docker
```
您必须手动删除任何已编辑的配置文件

