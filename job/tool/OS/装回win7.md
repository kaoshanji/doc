### 装回win7

在装win系统时，有时会遇到磁盘不兼容情况，比如，win10装回win7，其中,win8也和win7磁盘不兼容，那么在装win7时是装不上的，至于为什么要装回win7，能说下，只是为了体验下么？

安装过程如下：
  1. 下载win7原始镜像，使用老毛桃制作U盘启动(没有使用老毛桃工具处理多个磁盘格式)
  2. 设置开机启动为U盘启动
  3. 进入安装win7界面
  4. 按Shift + F10打开命令提示符
  5. 输入"Diskpart"（不用输入引号，下面也一样），并按回车，进入操作界面
  6. 输入"list disk"查看磁盘信息，注意看磁盘容量来选择，最好选择靠前的硬盘，win系统不区分机械硬盘还是普通硬盘，只会装在靠前的那个硬盘
  7. 输入"select disk 0"，选择disk 0 为当前操作磁盘
  8. 输入"clean"，清空当前磁盘分区
  9. 输入"convert mbr"转换为mbr分区

注：convert 命令的其他用法：
  - convert basic     -将磁盘从动态转换为基本
  - convert dynamic   -将磁盘从基本转换为动态
  - convert gpt       -将磁盘从MBR转换为GPT
  - convert mbr       -将磁盘从GPT转换为MBR
