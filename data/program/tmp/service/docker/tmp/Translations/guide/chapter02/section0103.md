#   入门，第 3 部分：服务

##  先决条件
-   安装 Docker 版本 1.13 或更高版本
-   获取 Docker Compose。在 适用于 Mac 的 Docker 及 适用于 Windows 的 Docker 上，它已预先安装，因此您已准备就绪。在 Linux 系统上，您需要直接安装它
-   阅读第 1 部分中的新用户导引
-   在第 2 部分中了解如何创建容器
-   确保您已发布通过将其推送到镜像库创建的 friendlyhello 镜像。我们将在此处使用该共享镜像
-   确保您的镜像充当已部署的容器。运行以下命令，并填写 `username`、`repo` 和 `tag` 信息：`docker run -p 80:80 username/repo:tag`，然后访问 `http://localhost/`

##  简介
在第 3 部分中，我们将扩展应用并启用负载均衡。如需完成此操作，我们必须前往分布式应用的层次结构中的上一级别： `服务`
-   技术栈
-   `服务`（您在此处）
-   容器（请参阅第 2 部分）

##  了解服务
在分布式应用中，应用的不同部分称为“服务”。例如，假设有一个视频共享网站，它可能提供用于在数据库中存储应用程序数据的服务、用于在用户上传一些内容后在后台进行视频转码的服务、用于前端的服务等

服务实际上是“生产中的容器”。一项服务仅运行一个镜像，但它会编制镜像的运行方式 - 它应使用的端口、容器的多少个从节点应运行才能使服务的容量满足其需求等。扩展服务将更改运行该软件的容器实例数，并将多个计算资源分配给进程中的服务

幸运的是，很容易使用 Docker 平台定义、运行和扩展服务 – 只需编写一个 `docker-compose.yml` 文件即可

##  您的第一个 `docker-compose.yml` 文件

`docker-compose.yml` 文件是一个 YAML 文件，用于定义 Docker 容器在生产中的行为方式

### `docker-compose.yml`

需要时，将此文件另存为 `docker-compose.yml`。确保您已推送镜像（在第 2 部分中创建）至镜像库，并通过将 `username/repo:tag` 替换为镜像详细信息来更新此 `.yml`
```
version:"3"
services:
  web:
    # 将 username/repo:tag 替换为您的名称和镜像详细信息
    image: username/repository:tag
    deploy:
      replicas:5
      resources:
        limits:
          cpus:"0.1"
          memory:50M
      restart_policy:
        condition: on-failure
    ports:
      - "80:80"
    networks:
      - webnet
networks:
  webnet:
```

此 `docker-compose.yml` 文件会告诉 Docker 执行以下操作：
-   从镜像库中拉取我们在步骤 2 中上传的镜像
-   将该镜像的五个实例作为服务 web 运行，并将每个实例限制为最多使用 10% 的 CPU（在所有核心中）以及 50MB RAM
-   如果某个容器发生故障，立即重启容器
-   将主机上的端口 80 映射到 web 的端口 80
-   指示 `web` 容器通过负载均衡的网络 `webnet` 共享端口 80。（在内部，容器自身将在临时端口发布到 web 的端口 80。）
-   使用默认设置定义 `webnet` 网络（此为负载均衡的 overlay 网络）

##  运行新的负载均衡的应用

需要先运行以下命令，然后才能使用 `docker stack deploy` 命令：
```
docker swarm init
```

现在，运行此命令。您必须为应用指定一个名称。在此处该名称设置为 `getstartedlab`：
```
docker stack deploy -c docker-compose.yml getstartedlab
```

查看您刚才启动的五个容器的列表：
```
docker stack ps getstartedlab
```

您可以多次在一行中运行 `curl http://localhost`，也可以在浏览器中转至该 URL 并多次点击“刷新”。无论采用哪种方式，您都将看到容器 ID 更改，从而说明负载均衡；借助每项请求，将以循环方式选择五个从节点之一做出响应

>   `注`：在此阶段，容器最多可能需要 30 秒来响应 HTTP 请求。这并不代表 Docker 或 swarm 的性能，而是一项未满足的 Redis 依赖关系，我们稍后将在本教程中讨论此依赖关系


##  扩展应用

您可以通过在 `docker-compose.yml` 中更改 `replicas` 值，保存更改并重新运行 `docker stack deploy` 命令来扩展应用：
```
docker stack deploy -c docker-compose.yml getstartedlab
```

Docker 将执行原地更新，而无需先清除技术栈或终止任何容器

现在，重新运行 `docker stack ps` 命令以查看经过重新配置的已部署实例。例如，如果您扩展了从节点，将有更多处于运行状态的容器

### 清除应用和 swarm
使用 `docker stack rm` 清除应用：
```
docker stack rm getstartedlab
```

这将删除应用，但我们的单节点 swarm 仍处于正常运行状态（如 docker node ls 所示）。使用 `docker swarm leave --force` 清除 swarm

这与使用 Docker 启动并扩展应用一样简单。您已朝向了解如何在生产中运行容器前进了一大步。下面您将了解如何在 Docker 机器集群上将此应用作为真正的 swarm 运行

##  概要和速查表
如需提供概要，输入 `docker run` 非常简单，在生产中容器的实际实施将其作为服务运行。服务会在 Compose 文件中编制容器的行为，并且此文件可用于扩展限制和重新部署应用。在它运行时，可以使用启动服务的命令在适当的位置应用对服务的更改： `docker stack deploy`

可以在此阶段探索的一些命令：
```
docker stack ls              # 列出此 Docker 主机上所有正在运行的应用
docker stack deploy -c <composefile> <appname>  # 运行指定的 Compose 文件
docker stack services <appname>       # 列出与应用关联的服务
docker stack ps <appname>   # 列出与应用关联的正在运行的容器
docker stack rm <appname>                             # 清除应用
```



