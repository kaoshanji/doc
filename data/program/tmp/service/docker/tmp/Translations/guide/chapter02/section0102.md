#   入门，第 2 部分：容器

##  先决条件
-   安装 Docker 版本 1.13 或更高版本。
-   阅读第 1 部分中的新用户导引。
-   对环境进行快速的测试运行，以确保您已做好准备：
```
docker run hello-world
```

##  简介
现在可以开始按照 Docker 方式构建应用。我们将从此类应用的层次结构的底层（即，容器）开始，这是本页面上涵盖的内容。在此级别之上是服务，它定义了容器在生产中的行为方式（请参阅第 3 部分）。最后，处于最高级别的是技术栈，用于定义所有服务的交互（请参阅第 5 部分）
-   技术栈
-   服务
-   `容器`（您在此处）

##  您的新开发环境
过去，如果要开始编写 Python 应用，您的第一项业务是将 Python 运行时安装到机器上。但是，这会导致机器上的环境必须如此，才能使应用按预期运行；对于运行应用的服务器来说，也同样如此

借助 Docker，您只需将可移植的 Python 运行时抓取为镜像，而无需进行安装。然后，您的构建可以将基本 Python 镜像与应用代码包含在一起，从而确保应用、其依赖项及运行时都一起提供

这些可移植的镜像由 `Dockerfile` 定义

##  使用 `Dockerfile` 定义容器
`Dockerfile` 将在您的容器内定义环境中执行的操作。对网络接口和磁盘驱动器等资源的访问在此环境内实现虚拟化，这将独立于系统的其余部分，因此您必须将端口映射到外部，并具体说明您要“复制”到该环境的文件。但是，在执行此操作后，您可以期望此 `Dockerfile` 中定义的应用构建的行为在运行时始终相同

### `Dockerfile`
创建空目录并将名为 `Dockerfile` 的此文件放入其中。记录说明每个语句的注释
```
# 将官方 Python 运行时用作父镜像
FROM python:2.7-slim

# 将工作目录设置为 /app
WORKDIR /app

# 将当前目录内容复制到位于 /app 中的容器中
ADD . /app

# 安装 requirements.txt 中指定的任何所需软件包
RUN pip install -r requirements.txt

# 使端口 80 可供此容器外的环境使用
EXPOSE 80

# 定义环境变量
ENV NAME World

# 在容器启动时运行 app.py
CMD ["python", "app.py"]
```

此 `Dockerfile` 引用了我们尚未创建的内容，名为 `app.py` 和 `requirements.txt`。在后续步骤中，我们会准备好这些内容

##  应用自身
抓取这两个文件并将其放入 `Dockerfile` 所在的文件夹。这将完成我们的应用，如您所见它非常简单。将上述 `Dockerfile` 构建到镜像中时，由于 `Dockerfile` 的 `ADD` 命令而显示 `app.py` 和 `requirements.txt`，并且借助 `EXPOSE` 命令，将能够通过 HTTP 访问 `app.py` 的输出

### requirements.txt
```
Flask
Redis
```

### app.py
```
from flask import Flask
from redis import Redis, RedisError
import os
import socket

# Connect to Redis
redis = Redis(host="redis", db=0, socket_connect_timeout=2, socket_timeout=2)

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis, counter disabled</i>"

    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
```

现在，我们可以看到，`pip install -r requirements.txt` 将安装 Python 的 Flask 和 Redis 库，而此应用将输出环境变量 `NAME` 以及对 `socket.gethostname()` 调用的输出。最后，由于 Redis 未在运行（因为我们仅安装了 Python 库，而未安装 Redis 自身），因此我们应期望尝试在此处使用它将失败并生成错误消息

>   `注`：在容器内时访问主机的名称将检索容器 ID，这类似于正在运行的可执行文件的进程 ID

##  构建应用
好的！您不需要 Python 或系统上 `requirements.txt` 中的任何内容，也不会构建或运行此镜像来将它们安装在系统上。似乎您尚未真正使用 Python 和 Flask 设置环境，但已进行设置

以下是 `ls` 应显示的内容：

```
$ ls
Dockerfile		app.py			requirements.txt
```

现在，运行构建命令。这将创建 Docker 镜像，我们将使用 -t 对其进行标记，以使其具有友好名称
```
docker build -t friendlyhello .
```

您已构建的镜像在何处？它位于您的机器上的本地 Docker 镜像库中：
```
$ docker images

REPOSITORY            TAG                 IMAGE ID
friendlyhello         latest              326387cea398
```

##  运行应用
运行应用，使用 `-p` 参数将机器的 4000 端口映射到容器暴露的 80 端口：
```
docker run -p 4000:80 friendlyhello
```

您将看到 Python 正在为应用提供服务（网址为 `http://0.0.0.0:80`）的通知。但是，该消息来自不知道您已将其 80 端口映射到 4000 端口的容器的内部，因此需要将正确 URL 更改为 `http://localhost:4000`

在 Web 浏览器中访问该 URL，以查看网页上提供的显示内容，包括“Hello World”文本、容器 ID以及 Redis 错误消息

![app-in-browser](image/app-in-browser.png)

您还可以在 shell 中使用 `curl` 命令查看相同内容

```
$ curl http://localhost:4000

<h3>Hello World!</h3><b>Hostname:</b> 8fc990912a14<br/><b>Visits:</b> <i>cannot connect to Redis, counter disabled</i>
```

>   `注`：此端口重映射 `4000:80` 用于说明您在 `Dockerfile` 中暴露的内容与使用 `docker run -p` 发布的内容之间的差异。在后续步骤中，我们只需将主机上的 80 端口映射到容器中的 80 端口并使用 `http://localhost`

在终端上按 `CTRL+C` 退出

现在，我们从后台在分离模式下运行应用
```
docker run -d -p 4000:80 friendlyhello
```

您将获得应用的长容器 ID，然后将返回到终端。容器现在在后台运行。您还可以使用 `docker ps` 查看缩写容器 ID（这两种 ID 可以在运行命令时交换工作）：
```
$ docker ps
CONTAINER ID        IMAGE               COMMAND             CREATED
1fa4ab2cf395        friendlyhello       "python app.py"     28 seconds ago
```

您将看到 `CONTAINER ID` 与 `http://localhost:4000` 上的内容相匹配

现在，使用 `docker stop` 及 `CONTAINER ID` 结束该进程，如下所示
```
docker stop 1fa4ab2cf395
```

##  共享镜像
为了说明我们刚才创建的可移植性，可以上传已构建的镜像并在其他地方运行它。但是，在您要将容器部署到生产环境中时，需要了解如何推送到镜像库

镜像库是镜像仓库的集合，而镜像仓库是镜像的集合 - 除了代码已构建之外，类似于 GitHub 镜像仓库。镜像库中的一个帐户可以创建很多镜像仓库。默认情况下，`docker` CLI 使用 Docker 的公用镜像库

>   `注`：我们将在此处使用 Docker 的公用镜像库，仅仅因为它是免费的并且经过预先配置，但有许多公用镜像库可供选择，并且您甚至可以使用 Docker Trusted Registry 设置您自己的专用镜像库

### 使用 Docker ID 登录
如果您没有 Docker 帐户，请在 [cloud.docker.com](https://cloud.docker.com/) 中进行注册。记录您的用户名

登录本地机器上的 Docker 公用镜像库
```
docker login
```

### 标记镜像
用于将本地镜像与镜像库中的镜像仓库相关联的表示法为 `username/repository:tag`。tag 是可选项，但建议使用它，因为这是镜像库用于为 Docker 镜像指定版本的机制。针对上下文为镜像库和 tag 指定有意义的名称，例如 `get-started:part1`.这会将镜像放入 `get-started` 镜像仓库并将其标记为 `part1`

现在，将其合并到一起，以标记镜像。使用您的用户名、镜像仓库和标签名称运行 `docker tag image`，以便镜像将上传到所需目的地。此命令的语法为：
```
docker tag image username/repository:tag
```

例如：
```
docker tag friendlyhello john/get-started:part1
```

运行 `docker images` 以查看新标记的镜像。（您还可以使用 `docker image ls`。）
```
$ docker images
REPOSITORY               TAG                 IMAGE ID            CREATED             SIZE
friendlyhello            latest              d9e555c53008        3 minutes ago       195MB
john/get-started         part1               d9e555c53008        3 minutes ago       195MB
python                   2.7-slim            1c7128a655f6        5 days ago          183MB
...
```

##  发布镜像
将已标记的镜像上传到镜像仓库：
```
docker push username/repository:tag
```

完成后，将公开此上传的结果。如果登录 Docker Hub，可以使用其 pull 命令看到新的镜像

##  从远程镜像仓库中拉取并运行镜像
从现在开始，您可以使用 `docker run`，并且可以使用以下命令在任何机器上运行您的应用
```
docker run -p 4000:80 username/repository:tag
```

如果镜像在机器本地不可用，Docker 将从镜像仓库中拉取它
```
$ docker run -p 4000:80 john/get-started:part1
Unable to find image 'john/get-started:part1' locally
part1:Pulling from orangesnap/get-started
10a267c67f42:Already exists
f68a39a6a5e4:Already exists
9beaffc0cf19:Already exists
3c1fe835fb6b:Already exists
4c9f1fa8fcb8:Already exists
ee7d8f576a14:Already exists
fbccdcced46e:Already exists
Digest: sha256:0601c866aab2adcc6498200efd0f754037e909e5fd42069adeff72d1e2439068
Status: Downloaded newer image for john/get-started:part1
 * Running on http://0.0.0.0:80/ (Press CTRL+C to quit)
```

>   `注`：如果您未指定这些命令中的 `:tag` 部分，在进行构建和运行镜像时，将使用标签 `:latest` 。Docker 将使用在未指定标签的情况下运行的镜像的最新版本（可以不是最新镜像）

无论 `docker run` 在何处执行，它将从 `requirements.txt` 拉取您的镜像及 Python 和所有依赖项，然后运行代码。所有内容都在一个小软件包中提供，并且主机只需安装 Docker 来运行它

##  第 2 部分总结
以下是此页面上的基本 Docker 命令列表，以及一些相关命令（如果您要在继续之前进行进一步探索）
```
docker build -t friendlyname .# 使用此目录的 Dockerfile 创建镜像
docker run -p 4000:80 friendlyname  # 运行端口 4000 到 90 的“友好名称”映射
docker run -d -p 4000:80 friendlyname         # 内容相同，但在分离模式下
docker ps                                 # 查看所有正在运行的容器的列表
docker stop <hash>                     # 平稳地停止指定的容器
docker ps -a           # 查看所有容器的列表，甚至包含未运行的容器
docker kill <hash>                   # 强制关闭指定的容器
docker rm <hash>              # 从此机器中删除指定的容器
docker rm $(docker ps -a -q)           # 从此机器中删除所有容器
docker images -a                               # 显示此机器上的所有镜像
docker rmi <imagename>            # 从此机器中删除指定的镜像
docker rmi $(docker images -q)             # 从此机器中删除所有镜像
docker login             # 使用您的 Docker 凭证登录此 CLI 会话
docker tag <image> username/repository:tag  # 标记 <image> 以上传到镜像库
docker push username/repository:tag            # 将已标记的镜像上传到镜像库
docker run username/repository:tag                   # 运行镜像库中的镜像
```











