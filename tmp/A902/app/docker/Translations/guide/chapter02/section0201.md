#   网络容器

如果您按照用户指南的方式工作，则只需构建并运行一个简单的应用程序即可。你也建立了自己的图像。本节将教您如何联网您的容器

##  在默认网络上启动容器

Docker通过使用网络驱动程序支持网络容器。默认情况下，Docker为您提供两种网络驱动程序：`bridge`和`overlay`驱动程序。您也可以编写网络驱动程序插件，以便您可以创建自己的驱动程序，但这是一项高级任务

Docker Engine的每次安装都会自动包含三个默认网络。你可以列出它们：
```
$ docker network ls

NETWORK ID          NAME                DRIVER
18a2866682b8        none                null
c288470c46f6        host                host
7b369448dccb        bridge              bridge
```

被命名的网络`bridge`是一个特殊的网络。除非另有说明，否则Docker会始终在此网络中启动您的容器。现在试试这个：
```
$ docker run -itd --name=networktest ubuntu

74695c9cea6d9810718fddadc01a727a5dd3ce6a69d09752239736c030599741
```

![bridge1](image/bridge1.png)

检查网络是查找容器IP地址的简单方法

```
$ docker network inspect bridge

[
    {
        "Name": "bridge",
        "Id": "f7ab26d71dbd6f557852c7156ae0574bbf62c42f539b50c8ebde0f728a253b6f",
        "Scope": "local",
        "Driver": "bridge",
        "EnableIPv6": false,
        "IPAM": {
            "Driver": "default",
            "Options": null,
            "Config": [
                {
                    "Subnet": "172.17.0.1/16",
                    "Gateway": "172.17.0.1"
                }
            ]
        },
        "Internal": false,
        "Containers": {
            "3386a527aa08b37ea9232cbcace2d2458d49f44bb05a6b775fba7ddd40d8f92c": {
                "Name": "networktest",
                "EndpointID": "647c12443e91faf0fd508b6edfe59c30b642abb60dfab890b4bdccee38750bc1",
                "MacAddress": "02:42:ac:11:00:02",
                "IPv4Address": "172.17.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {
            "com.docker.network.bridge.default_bridge": "true",
            "com.docker.network.bridge.enable_icc": "true",
            "com.docker.network.bridge.enable_ip_masquerade": "true",
            "com.docker.network.bridge.host_binding_ipv4": "0.0.0.0",
            "com.docker.network.bridge.name": "docker0",
            "com.docker.network.driver.mtu": "9001"
        },
        "Labels": {}
    }
]
```

您可以通过断开容器从网络中移除容器。为此，您提供网络名称和容器名称。您也可以使用容器标识。但在这个例子中，名字更快。

```
$ docker network disconnect bridge networktest
```

虽然可以从网络断开容器，但不能删除已`bridge`命名的内置网络`bridge`。网络是将容器与其他容器或其他网络隔离的自然方式。所以，当你更熟悉Docker时，你会想创建自己的网络

##  创建您自己的桥梁网络

Docker引擎本身支持桥网络和覆盖网络。桥接网络仅限于运行Docker Engine的单个主机。覆盖网络可以包括多个主机，并且是更高级的主题。对于这个例子，你将创建一个桥梁网络：

```
$ docker network create -d bridge my_bridge
```

该`-d`标志告诉Docker `bridge`为新网络使用驱动程序。这个标志`bridge`的默认值是可以离开这个标志的。继续并在您的机器上列出网络：

```
$ docker network ls

NETWORK ID          NAME                DRIVER
7b369448dccb        bridge              bridge
615d565d498c        my_bridge           bridge
18a2866682b8        none                null
c288470c46f6        host                host
```

如果你检查网络，你会发现它没有任何内容

```
$ docker network inspect my_bridge

[
    {
        "Name": "my_bridge",
        "Id": "5a8afc6364bccb199540e133e63adb76a557906dd9ff82b94183fc48c40857ac",
        "Scope": "local",
        "Driver": "bridge",
        "IPAM": {
            "Driver": "default",
            "Config": [
                {
                    "Subnet": "10.0.0.0/24",
                    "Gateway": "10.0.0.1"
                }
            ]
        },
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]
```

##  将容器添加到网络

要构建一致行动但可以安全执行的Web应用程序，请创建一个网络。根据定义，网络为容器提供完全的隔离。首次运行容器时，您可以将容器添加到网络

启动一个运行PostgreSQL数据库的容器，并将其传递给它--net=my_bridge以将其连接到新网络的标志：

```
$ docker run -d --net=my_bridge --name db training/postgres
```

如果你检查`my_bridge`你会看到它有一个容器。您还可以检查您的容器以查看它连接的位置：

```
$ docker inspect --format='{{json .NetworkSettings.Networks}}'  db


{"my_bridge":{"NetworkID":"7d86d31b1478e7cca9ebed7e73aa0fdeec46c5ca29497431d3007d2d9e15ed99",
"EndpointID":"508b170d56b2ac9e4ef86694b0a76a22dd3df1983404f7321da5649645bf7043","Gateway":"10.0.0.1","IPAddress":"10.0.0.254","IPPrefixLen":24,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:02"}}
```

现在，继续，开始你现在熟悉的Web应用程序。这次不指定网络。

```
$ docker run -d --name web training/webapp python app.py
```

![bridge2](image/bridge2.png)

您的`web`应用程序在哪个网络下运行？检查应用程序，你会发现它运行在默认`bridge`网络中。

```
$ docker inspect --format='{{json .NetworkSettings.Networks}}'  web


{"bridge":{"NetworkID":"7ea29fc1412292a2d7bba362f9253545fecdfa8ce9a6e37dd10ba8bee7129812",
"EndpointID":"508b170d56b2ac9e4ef86694b0a76a22dd3df1983404f7321da5649645bf7043","Gateway":"172.17.0.1","IPAddress":"10.0.0.2","IPPrefixLen":24,"IPv6Gateway":"","GlobalIPv6Address":"","GlobalIPv6PrefixLen":0,"MacAddress":"02:42:ac:11:00:02"}}
```

然后，获取你的IP地址 `web`

```
$ docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' web


172.17.0.2
```

现在，打开一个shell到你正在运行的`db`容器中：

```
$ docker exec -it db bash

root@a205f0dd33b2:/# ping 172.17.0.2
ping 172.17.0.2
PING 172.17.0.2 (172.17.0.2) 56(84) bytes of data.
^C
--- 172.17.0.2 ping statistics ---
44 packets transmitted, 0 received, 100% packet loss, time 43185ms
```

稍等片刻，`CTRL-C`用来结束`ping`，你会发现ping失败。这是因为两个容器在不同的网络上运行。你可以解决这个问题。然后，使用该`exit`命令关闭容器

Docker网络允许您将容器附加到尽可能多的网络上。您也可以附加一个已经运行的容器。继续并将您正在运行的`web`应用程序附加到`my_bridge`

```
$ docker network connect my_bridge web
```

![bridge3](image/bridge3.png)

`db`再次打开一个shell到应用程序中，然后尝试`ping`命令。这次只需使用容器名称`web`而不是IP地址。

```
$ docker exec -it db bash

root@a205f0dd33b2:/# ping web
PING web (10.0.0.2) 56(84) bytes of data.
64 bytes from web (10.0.0.2): icmp_seq=1 ttl=64 time=0.095 ms
64 bytes from web (10.0.0.2): icmp_seq=2 ttl=64 time=0.060 ms
64 bytes from web (10.0.0.2): icmp_seq=3 ttl=64 time=0.066 ms
^C
--- web ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2000ms
rtt min/avg/max/mdev = 0.060/0.073/0.095/0.018 ms
```

`ping`表明它是接触不同的IP地址，在地址`my_bridge`是从其上地址不同`bridge`的网络



