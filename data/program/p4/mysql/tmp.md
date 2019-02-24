yum update

https://dev.mysql.com/downloads/repo/yum/

yum localinstall 文件名

yum repolist enabled | grep "mysql.*-community.*"

yum install mysql-community-server


https://dev.mysql.com/doc/refman/5.7/en/linux-installation-yum-repo.html


[如何让Tomcat在指定JDK版本下启动 而不依赖环境变量中配置的版本](https://blog.csdn.net/liufangbaishi2014/article/details/76937682)


[使用CentOS7卸载自带jdk安装自己的JDK1.8](https://blog.csdn.net/hui_2016/article/details/69941850)


[阿里云CentOS7 64位下安装MySQL5.7](https://blog.csdn.net/zxd1435513775/article/details/78269838)


[CentOS7通过yum安装Mysql5.7+修改默认密码+远程登录](https://blog.csdn.net/csdn2193714269/article/details/72897815)


``` sql
--打开mysql数据库服务  
mysql -u root -p  
  
--打开mysql数据库文件  
mysql>use mysql;  
  
--将mysql数据库中user表中user字段下的root用户的host值改为通配符%（默认是localhost）  
mysql>UPDATE user SET host ='%' WHERE user = 'root';  
  
--修改之后再刷新一下权限  
mysql>flush privileges; 
```


