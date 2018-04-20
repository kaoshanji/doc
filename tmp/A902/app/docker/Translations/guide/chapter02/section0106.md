#   入门，第 6 部分：部署您的应用

##  先决条件
-   安装 Docker 版本 1.13 或更高版本。
-   按照第 3 部分：先决条件中所述，获取 Docker Compose。
-   按照第 4 部分：先决条件中所述，获取 Docker Machine。
-   阅读第 1 部分中的新用户导引
-   在第 2 部分中了解如何创建容器
-   确保您已发布通过将其推送到镜像库创建的 `friendlyhello` 镜像。我们将在此处使用该共享镜像
-   确保您的镜像充当已部署的容器。运行以下命令，并填写 `username`、`repo` 和 `tag` 信息：`docker run -p 80:80 username/repo:tag`，然后访问 `http://localhost/`
-   就近获取第 5 部分中最终版本的 `docker-compose.yml`

##  简介

在整个教程中，您一直在编辑同一 Compose 文件。好消息是，和在您的机器上一样，该 Compose 文件在生产中正常运行。我们将在此完成用于运行 Docker 化应用程序的一些选项

##  选择选项

如果可以在生产中使用 Docker 社区版，您可以使用 Docker 云帮助在常用服务提供商（例如，Amazon Web Services、DigitalOcean 和 Microsoft Azure）处管理您的应用

如需进行设置和部署：
-   将 Docker 云连接到您的首选供应商，为 Docker 云授予自动供应并为您实现 VM“Docker 化”的权限
-   使用 Docker 云创建您的计算资源并创建您的 swarm
-   部署您的应用

>   `注`：我们将在此处链接到 Docker 云文档；请确保在完成每个步骤后返回到此页面

##  创建 swarm

已准备好创建 swarm？

##  部署应用

通过 Docker 云连接到 swarm。在适用于 Mac 的 Docker 或适用于 Windows 的 Docker（Edge 版本）上，您可以通过桌面应用菜单直接连接到 swarm。

无论使用哪种方式，这都将打开一个终端，其环境为您的本地机器，但其 Docker 命令路由到云服务提供商上运行的 swarm。这与您已遵循的范例略有不同，在范例中您通过 SSH 发送命令。现在，您可以直接访问本地文件系统和远程 swarm，从而实现了非常简洁的命令：
```
docker stack deploy -c docker-compose.yml getstartedlab
``` 

好的！您的应用正在生产中运行，并且由 Docker 云管理
