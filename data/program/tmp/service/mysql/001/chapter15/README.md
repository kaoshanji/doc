#   组复制

MySQL组复制是一个MySQL服务器插件，使您能够创建弹性，高可用性，容错复制拓扑。

组可以在具有自动初选的单主模式下运行，其中一次只有一台服务器接受更新。或者，对于更高级的用户，可以将多个组以多主模式进行部署，即所有服务器都可以接受更新，即使它们是同时发布的。

有一个内置的组成员资格服务，可以在任何给定的时间点保持组的视图一致并适用于所有服务器。服务器可以离开并加入组，并且相应地更新视图。有时服务器可能会意外离开组，在这种情况下，故障检测机制会检测到此情况并通知组该视图已更改。这全是自动的。

##  目录
-   组复制背景
-   入门
-   监视组复制
-   组复制操作
-   组复制安全性
-   组复制系统变量
-   要求和限制
-   经常问的问题
-   组复制技术细节

