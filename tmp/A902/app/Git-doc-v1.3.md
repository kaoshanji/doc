# 安装与设置

##  设置账户
-   设置本设备用户名
    ```
    git config –global user.name ‘kaoshanji-X550JX’(使用用户名-设备名…当使用多台电脑时,这也算预留)
    ```
-   设置邮箱
    ```
    git config –global user.email ‘email@qq.com’
    ```
-   设置命令行
    ```
    git config –global color.ui auto
    ```
-   生成秘钥
    ```
    ssh-keygen -t rsa -C ‘email@qq.com’
    ```
-   在账户里添加
    -   [登录GitHub](https://github.com/)
    -   点击主页图标下`settings`,选择`SSH and GPG keys`
    -   点击`New SSK key`
    -   填写标题，复制生成的密钥目录下`id_rsa.pub`文件里的数据
    -   建议标题使用上面`设置本设备用户名`,这样,比较好对应
-   验证
    -   输入
    ```
    ssh -T git@github.com
    ```
    -   在上面填写的邮箱里会收到一封邮件

## 基本使用
>   默认使用主分支：master
-   初始化
    ```
    某目录Github 下 
    git clone git@… // 下载主分支
    //git clone -b v2.2 git@… // 下载 v2.2 分支
    ```
-   添加到暂存区
    ```
    git add/rm (./加全部)
    ```
-   提交至版本区
    ```
    git commit -m '说明'
    ```
-   查看提交文件
    ```
    git log --name-only -1
    ```
-   推送服务器
    ```
    git push
    ```
-   拉取最新
    ```
    git pull
    ```

## 线上版本
>   系统上线后，切割出一个分支保留，主分支可以继续，当线上出现问题时，可以在对应的分支上修改而不影响主分支
-   创建分支
    ```
    直接在网上上创建..
    // git branch v2.1
    // git checkout -b dev // 切换指定分支
    ```
-   查看分支
    ```
    git branch // 前面有 * 是当前分支
    ```
-   切换分支
    ```
    git checkout xxx(分支名称)
    // 更新、提交与上面操作一致
    ```
-   分支提交和合并
    ```
    // 提交
    git add ./
    git commit -m '说明'
    git push  -f origin HEAD:v2.1(指定分支名称)
    // 合并
    git checkout master // 切换到主分支
    git merge origin/v2.1 // 把v2.1更改的合并到主分支里
    git push origin master // 更新主分支
    ```
