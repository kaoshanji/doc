#   入门，第 4 部分：Swarm

##  先决条件
-   安装 Docker 版本 1.13 或更高版本。
-   按照第 3 部分：先决条件中所述，获取 Docker Compose。
-   获取 Docker Machine，它使用适用于 Mac 的 Docker 和 适用于 Windows 的 Docker 预先安装，但在 Linux 系统上，您需要直接安装它
-   阅读第 1 部分中的新用户导引
-   在第 2 部分中了解如何创建容器
-   确保您已发布通过将其推送到镜像库创建的 `friendlyhello` 镜像。我们将在此处使用该共享镜像
-   确保您的镜像充当已部署的容器。运行以下命令，并填写 `username`、`repo` 和 `tag` 信息：`docker run -p 80:80 username/repo:tag`，然后访问 `http://localhost/`
-   就近从第 3 部分获取 `docker-compose.yml` 的副本

##  简介
在第 3 部分中，您使用了在第 2 部分中编写的应用，并通过将其转换为服务以及在进程中将其最多扩展 5 倍来定义了它应如何在生产中运行。

在第 4 部分中，您可以在此处将此应用部署到集群，并在多台机器上运行它。可以通过将多台机器加入“Dockerized”集群 swarm 来实现多容器、多机器应用

##  了解 swarm 集群
swarm 是一组运行 Docker 并且已加入集群中的机器。执行此操作后，您可以继续运行已使用的 Docker 命令，但现在它们在集群上由 `swarm 管理节点`执行。 swarm 中的机器可以为物理或虚拟机。加入 swarm 后，可以将它们称为`节点`。

swarm 管理节点可以使用多项策略来运行容器，例如“最空的节点”– 这将使用容器填充使用最少的机器。或“全局”，这将确保每台机器恰好获得指定容器的一个实例。您可以指示 swarm 管理节点使用 Compose 文件中的这些策略，就像您已使用的策略一样

swarm 管理节点是 swarm 中可以执行命令或授权其他机器加入 swarm 作为`工作节点`的唯一机器。工作节点仅用于提供功能，并且无权告知任何其他机器它可以做什么和不能做什么

到目前为止，您已在本地机器上以单主机模式使用 Docker。但是，也可以将 Docker 切换到 `swarm mode`，并且这可以实现 swarm 的使用。即时启用 swarm mode 可以使当前机器成为 swarm 管理节点。从那时起，Docker 将在您要管理的 swarm 上运行您执行的命令，而不是仅在当前机器上执行命令

##  Set up your swarm
swarm 由多个节点组成，这些节点可以是物理或虚拟机。基本概念非常简单：运行 `docker swarm init` 以启用 `swarm mode` 并使当前机器成为 `swarm` 管理节点，然后在其他机器上运行 `docker swarm join`，使它们以工作节点形式加入 swarm。选择下面的选项卡以查看如何在各种上下文中执行此操作。我们将使用 VM 来快速创建包含两台机器的集群并将其转换为 swarm

### 创建集群:本地机器上的 VM（MAC、LINUX、WINDOWS 7 和 WINDOWS 8）
现在，使用 `docker-machine` 和 VirtualBox 驱动来创建一对 VM：
```
$ docker-machine create --driver virtualbox myvm1
$ docker-machine create --driver virtualbox myvm2
```

现在，您已创建两个 VM，分别名为 `myvm1` 和 `myvm2`（如 `docker-machine ls` 所示）。第一个 VM 将用作管理节点，用于执行 `docker` 命令并对加入 `swarm` 的工作节点进行身份验证，而第二个 VM 将为工作节点

您可以使用 `docker-machine ssh` 向 VM 发送命令。使用 `docker swarm init` 指示 `myvm1` 成为 `swarm` 管理节点，并且您将看到类似于以下内容的输出
```
$ docker-machine ssh myvm1 "docker swarm init"
Swarm initialized: current node <node ID> is now a manager.

To add a worker to this swarm, run the following command:

  docker swarm join \
  --token <token> \
  <ip>:<port>
```

### 收到关于需要使用 `--advertise-addr` 的错误？
通过运行 `docker-machine ls` 来复制 `myvm1` 的 IP 地址，然后使用 该 IP 地址并通过 `--advertise-addr` 指定端口 2377（用于 swarm join 的端口）， 以便再次运行 `docker swarm init` 命令。例如：
```
docker-machine ssh myvm1 "docker swarm init --advertise-addr 192.168.99.100:2377"
```

如您所见，对 `docker swarm init` 的响应包含预先配置的 `docker swarm join` 命令，以便您在任何要添加的节点上运行。复制此命令，然后通过 `docker-machine ssh` 将其发送给 `myvm2`，从而让 `myvm2` 加入您的新 `swarm` 作为工作节点
```
$ docker-machine ssh myvm2 "docker swarm join \
--token <token> \
<ip>:<port>"

This node joined a swarm as a worker.
```

祝贺您，已成功创建您的第一个 swarm

>   `注`：您还可以在没有附加任何命令的情况运行 `docker-machine ssh myvm2`，以便在该 VM 上打开终端会话。在您已准备好返回到主机 shell 提示符时，请输入 `exit`。可能更容易通过这种方式粘贴 join 命令

使用 `ssh` 连接到 (`docker-machine ssh myvm1`)，并运行 `docker node ls` 以查看此 swarm 中的节点：
```
docker@myvm1:~$ docker node ls
ID                            HOSTNAME            STATUS              AVAILABILITY        MANAGER STATUS
brtu9urxwfd5j0zrmkubhpkbd     myvm2               Ready               Active              
rihwohkh3ph38fhillhhb84sk *   myvm1               Ready               Active              Leader
```

输入 `exit` 以退出该机器

或者，在 `docker-machine ssh` 中包装命令，以阻止必须直接登录和注销。例如：
```
docker-machine ssh myvm1 "docker node ls"
```

##  在集群上部署应用

困难的部分已完成。现在，您只需重复在第 3 部分中使用的进程，以便在新 swarm 中进行部署。只需记住，只有 `myvm1` 之类的 swarm 管理节点执行 Docker 命令；工作节点仅适用于容量

使用 `docker-machine scp` 命令将您在第 3 部分中创建的文件 `docker-compose.yml` 复制到 swarm 管理节点 `myvm1` 的主目录（别名：`~`）：
```
docker-machine scp docker-compose.yml myvm1:~
```

现在，让 `myvm1` 使用它作为 swarm 管理节点的功能来部署应用，方法是使用 `docker-machine ssh` 将您在第 3 部分中使用的 `docker stack deploy `命令发送到 `myvm1` :
```
docker-machine ssh myvm1 "docker stack deploy -c docker-compose.yml getstartedlab"
```

好的，应用已部署在集群上

将您在第 3 部分中使用的所有命令包装在对 `docker-machine ssh` 的调用中，并且它们全部将按您的预期工作。只有这一次，您会看到容器已分布在 `myvm1` 和 `myvm2` 之间
```
$ docker-machine ssh myvm1 "docker stack ps getstartedlab"

ID            NAME        IMAGE              NODE   DESIRED STATE
jq2g3qp8nzwx  test_web.1  username/repo:tag  myvm1  Running
88wgshobzoxl  test_web.2  username/repo:tag  myvm2  Running
vbb1qbkb0o2z  test_web.3  username/repo:tag  myvm2  Running
ghii74p9budx  test_web.4  username/repo:tag  myvm1  Running
0prmarhavs87  test_web.5  username/repo:tag  myvm2  Running
```

##  访问集群
您可以从 `myvm1` 或 `myvm2` 的 IP 地址访问应用。您创建的网络将在它们之间共享并实现了负载均衡。运行 `docker-machine ls` 以获取 VM 的 IP 地址，并在浏览器上访问其中一个地址，并按“刷新”（或者仅对它们执行 curl）。您将看到五个可能的容器 ID 全部随机循环，表示负载均衡

这两个 IP 地址都适用的原因在于，swarm 中的节点将参加入口`网格路由`。这可以确保 swarm 中特定端口上部署的服务始终将该端口保留给它自己，而与实际运行容器的是什么节点无关。下面显示了在三节点 swarm 上的端口 `8080` 发布的服务 `my-web` 的网格路由的图：

![ingress-routing-mesh](image/ingress-routing-mesh.png)

### 遇到连接问题？
请记住，为了使用 swarm 中的入口网络， 您需要在 swarm 节点之间开放以下端口， 然后再启用 swarm mode：
-   端口 7946 TCP/UDP，用于容器网络发现
-   端口 4789 UDP，用于容器入口网络

##  迭代和扩展应用
您可以在此处执行在“第 3 部分”中学习的所有内容

通过更改 `docker-compose.yml` 文件扩展应用

通过编辑代码更改应用行为

无论哪种情况，只需再次运行 `docker stack deploy` 即可部署这些更改

通过使用对 `myvm2` 使用的 `docker swarm join` 命令，您可以将任何机器（物理或虚拟）加入此 swarm，并且容量将添加到集群中。然后，运行 `docker stack deploy`，应用便可以利用新资源

##  清理
您可以使用 `docker stack rm` 清除技术栈。例如：
```
docker-machine ssh myvm1 "docker stack rm getstartedlab"
```

### 保留 swarm 还是将其删除？
在稍后的某个时间，您可以在需要时使用 工作节点上的 `docker-machine ssh myvm2 "docker swarm leave"` 和管理节点上的 `docker-machine ssh myvm1 "docker swarm leave --force"` 删除此 swarm，但_由于您将需要在第 5 部分中使用此 swarm，因此请 暂时将其保留

##  概要和速查表
在第 4 部分中，您已了解 swarm 是什么、swarm 中的节点如何成为管理节点或工作节点、如何创建 swarm 以及如何在其上应用。可以看到，核心 Docker 命令与第 3 部分相同，但它们必须以在 swarm master 上运行为目标。还可以了解到 Docker 网络在运行中的功能，即使容器在不同的机器上运行，此功能也可以在容器之间保持负载均衡请求。最后，您已了解如何在集群上迭代和扩展应用

以下是与 swarm 进行交互时您可能会运行的命令：
```
docker-machine create --driver virtualbox myvm1 # 创建 VM（Mac、Win7、Linux）
docker-machine create -d hyperv --hyperv-virtual-switch "myswitch" myvm1 # Win10
docker-machine env myvm1                # 查看有关节点的基本信息
docker-machine ssh myvm1 "docker node ls"         # 列出 swarm 中的节点
docker-machine ssh myvm1 "docker node inspect <node ID>"        # 检查节点
docker-machine ssh myvm1 "docker swarm join-token -q worker"   # 查看加入令牌
docker-machine ssh myvm1   # 打开与 VM 的 SSH 会话；输入“exit”以结束会话
docker-machine ssh myvm2 "docker swarm leave"  # 使工作节点退出 swarm
docker-machine ssh myvm1 "docker swarm leave -f" # 使主节点退出，终止 swarm
docker-machine start myvm1            # 启动当前未运行的 VM
docker-machine stop $(docker-machine ls -q)               # 停止所有正在运行的 VM
docker-machine rm $(docker-machine ls -q) # 删除所有 VM 及其磁盘镜像
docker-machine scp docker-compose.yml myvm1:~     # 将文件复制到节点的主目录
docker-machine ssh myvm1 "docker stack deploy -c <file> <app>"   # 部署应用
```





