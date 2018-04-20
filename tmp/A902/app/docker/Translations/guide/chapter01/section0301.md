#   适用于 Linux 的安装后步骤
>   本节包含用于配置 Linux 主机以便更好地与 Docker 配合工作的可选过程

##  以非 root 用户身份管理 Docker
`docker` 守护进程绑定至 Unix 套接字，而不是 TCP 端口。默认情况下，该 Unix 套接字由用户 `root` 所有，而其他用户只能使用 `sudo` 访问它。`docker` 守护进程始终以 `root` 用户身份运行

在使用 `docker` 命令时，如果您不想使用 `sudo`，请创建名为 `docker` 的 Unix 组并向其中添加用户。`docker` 守护进程启动时，它将使 Unix 套接字的所有权可由 `docker` 组进行读取/写入
>   `警告`： `docker` 组将授予等同于 `root` 用户的特权

如需创建 `docker` 组并添加您的用户，请执行下列操作
1.  创建 `docker` 组
```
$ sudo groupadd docker
```

2.  向 `docker` 组中添加您的用户
```
$ sudo usermod -aG docker $USER
```

3.  注销并重新登录，以便对您的组成员资格进行重新评估

4.  验证您是否可以在不使用 `sudo` 的情况下运行 `docker` 命令
```
$ docker run hello-world
```
此命令将下载一个测试镜像并在容器中运行它。容器运行时，它将输出一条参考消息并退出

##  将 Docker 配置为在启动时启动
大多数最新的 Linux 分发版（RHEL、CentOS、Fedora、Ubuntu 16.04 及更高版本）都使用 `systemd` 来管理在系统启动时启动的服务。 Ubuntu 14.10 及更低版本使用 `upstart`

`systemd`
```
$ sudo systemctl enable docker
```
如需禁用此性能，请改为使用 disable
```
$ sudo systemctl disable docker
```

`upstart`
Docker 是使用 `upstart` 自动配置为在启动时启动的。如需禁用此行为，请使用以下命令
```
$ echo manual | sudo tee /etc/init/docker.override
```

`chkconfig`
```
$ sudo chkconfig docker on
```

##  故障排除

### 内核兼容性
如果内核版本低于 3.10，或者它缺少某些模块，Docker 将无法正常运行。如需检查内核兼容性，您可以下载并运行 `check-compatibility.sh` 脚本
```
$ curl https://raw.githubusercontent.com/docker/docker/master/contrib/check-config.sh > check-config.sh

$ bash ./check-config.sh
```
此脚本仅适用于 Linux，而不适用于 macOS

### 无法连接到 Docker 守护进程
如果您看到类似于以下内容的错误，这表示您的 Docker 客户端可能配置为连接到另一台主机上的 Docker 守护进程，并且该主机可能无法访问
```
无法连接到 Docker 守护进程。'docker daemon' 是否在此主机上运行？
```

如需查看您的客户端配置为连接到哪台主机，请检查您的环境中 `DOCKER_HOST` 变量的值
```
$ env | grep DOCKER_HOST
```

如果此命令返回某个值，Docker 客户端将设置为连接到该主机上运行的 Docker 守护进程。如果未进行设置，Docker 客户端将设置为连接到本地主机上运行的 Docker 守护进程。如果错误地进行了设置，请使用以下命令对其取消设置
```
$ unset DOCKER_HOST
```

您可能需要在文件（例如，`~/.bashrc` 或 `~/.profile`）中编辑环境，以避免错误地设置 `DOCKER_HOST` 变量

如果按预期设置了 `DOCKER_HOST`，请验证 Docker 守护进程是否在远程主机上运行并确认防火墙或网络中断未导致您无法连接

### IP 转发问题
如果您将 `systemd-network` 和 `systemd` 版本 219 或更高版本配合使用来手动配置网络，Docker 容器可能无法访问您的网络。从 `systemd` 版本 220 开始，给定网络的转发设置 (`net.ipv4.conf.<interface>.forwarding`) 默认为关。此设置用于阻止 IP 转发。它也与启用了容器中的 `net.ipv4.conf.all.forwarding` 设置的 Docker 行为相冲突

如需在 RHEL、CentOS 或 Fedora 上解决此问题，请编辑 Docker 主机上 `/usr/lib/systemd/network/` 中的 `<interface>.network` 文件（例如：`/usr/lib/systemd/network/80-container-host0.network`）并在 [`Network`] 部分中添加以下块
```
[Network]
...
IPForward=kernel
# OR
IPForward=true
...
```

此配置允许按预期从容器进行 IP 转发

### `在 resolv.conf 中找到 DNS 解析程序并且容器无法使用它`
使用 GUI 的 Linux 系统通常会运行网络管理器，它使用在环回地址（例如，`127.0.0.1` 或 `127.0.1.1`）上运行的 `dnsmasq` 实例来缓存 DNS 请求，并将此条目添加到 `/etc/resolv.conf` 中。`dnsmasq` 服务可以提高 DNS 查找的速度，并且还可以提供 DHCP 服务。此配置不适用在具有其自己的网络名称空间的 Docker 容器内，因为该 Docker 容器会将环回地址（例如，`127.0.0.1`）解析为 `它自己`，并且很可能无法在它自己的环回地址上运行 DNS 服务器

如果 Docker 检测到 `/etc/resolv.conf` 中引用的任何 DNS 服务器都不是正常运行的 DNS 服务器，将出现下列警告消息，并且 Docker 将使用 Google 提供的 DNS 服务器 `8.8.8.8` 和 `8.8.4.4` 进行 DNS 解析
```
警告：在 resolv.conf 中发现了本地 (127.0.0.1) DNS 解析程序，并且容器无法使用它。使用默认的外部服务器：[8.8.8.8 8.8.4.4]
```

如果您看到此警告消息，请首先确认您是否使用了 `dnsmasq`
```
$ ps aux |grep dnsmasq
```

如果容器需要解析网络外部的主机，公用名称服务器无法满足要求。您有两种选择
-   指定 Docker 要使用的 DNS 服务器
-   在 NetworkManager 中禁用 `dnsmasq`。如果您执行此操作，NetworkManager 会将真实的 DNS 名称服务器添加到 `/etc/resolv.conf` 中，但您会失去可能的`dnsmasq` 优点

##  为 Docker 指定 DNS 服务器
配置文件的默认位置为 `/etc/docker/daemon.json`。您可以使用 `--config-file` 守护进程标志更改配置文件的位置。以下文档假定配置文件位于 `/etc/docker/daemon.json` 中
1.  创建或编辑 Docker 守护进程配置文件，它默认为 `/etc/docker/daemon.json` 文件，用于控制 Docker 守护进程配置
```
$ sudo nano /etc/docker/daemon.json
```

2.  添加 dns 键并以一个或多个 IP 地址作为值。如果此文件包含现有内容，您只需添加或编辑 dns 行
```
{
 	"dns":["8.8.8.8", "8.8.4.4"]
 }
```

如果您的内部 DNS 服务器无法解析公用 IP 地址，请至少包含一个可以进行解析的 DNS 服务器，以便您能够连接到 Docker Hub 并且容器能够解析互联网域名

保存并关闭文件

3.  重启 Docker 守护进程
```
$ sudo service docker restart
```

4.  通过尝试拉取镜像来验证 Docker 是否可以解析外部 IP 地址
```
$ docker pull hello-world
```

5.  如有必要，请通过对内部主机名执行 ping 操作来验证 Docker 容器是否可以解析此主机名
```
 $ docker run --rm -it alpine ping -c4 <my_internal_host>

 对 google.com (192.168.1.2) 执行 ping 操作：56 data bytes
 64 bytes from 192.168.1.2: seq=0 ttl=41 time=7.597 ms
 64 bytes from 192.168.1.2: seq=1 ttl=41 time=7.635 ms
 64 bytes from 192.168.1.2: seq=2 ttl=41 time=7.660 ms
 64 bytes from 192.168.1.2: seq=3 ttl=41 time=7.677 ms
```

## 禁用 `DNSMASQ`
### RHEL、CentOS 或 Fedora
如需在 RHEL、CentOS 或 Fedora 上禁用 dnsmasq，请执行下列操作
1.  禁用 `dnsmasq` 服务
```
 $ sudo service dnsmasq stop

 $ sudo systemctl disable dnsmasq
```

##  允许穿过防火墙访问远程 API
如果您在运行 Docker 的主机上运行了防火墙且希望从另一台主机访问 Docker 远程 API，并且已启用远程访问，您需要将防火墙配置为允许 Docker 端口上的传入连接。如果已启用 TLS 加密传输，此端口的默认值为 `2376`，否则为 `2375`

### UFW 的特定说明
默认情况下，`UFW（简单防火墙)`会删除所有转发流量和所有传入流量。如果您要从另一台主机访问 Docker 远程 API 并且已启用远程访问，您需要将 UFW 配置为允许 Docker 端口上的传入连接。如果已启用 TLS 加密传输，此端口的默认值为 `2376`，否则为 `2375`。默认情况下， Docker 运行时 TLS 未启用。如果不使用 TLS，强烈建议您禁止从远程主机访问 Docker 远程 API，以防范远程权限升级攻击

如需配置 UFW 并允许 Docker 端口上的传入连接，请执行下列操作
1.  验证是否启用了 UFW
```
$ sudo ufw status
```
如果未启用 `ufw`，剩余步骤没有任何用处

2.  编辑 UFW 配置文件，通常为 `/etc/default/ufw` 或`/etc/sysconfig/ufw`。将 `DEFAULT_FORWARD_POLICY` 策略设置为 `ACCEPT`
```
DEFAULT_FORWARD_POLICY="ACCEPT"
```
保存并关闭文件

3.  如果您需要启用从外部主机对 Docker 远程 API 的访问并了解安全含义。可将 UFW 配置为允许 Docker 端口上的传入连接。如果未使用 TLS，此端口为 `2375`，否则为 `2376`
```
$ sudo ufw allow 2376/tcp
```

4.  重新加载 UFW
```
$ sudo ufw reload
```