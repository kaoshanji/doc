静态资源 doc

### 场景
- 网站图片、js脚本、CSS样式等
- 纯粹的文件，例如：html/PDF/txt等
- 可以单独使用`虚拟主机`完成

### 示例
- 文件结构
    - /opt
        - /project
            - images
            - pdfs
            - htmls
            - index.html
- 配置
```conf
server {                                                        # 服务节点
        listen       8011;                                          # 监听端口
        server_name  static.localhost;                              # 虚拟主机 外界访问

        location / {                                                # 内部?
            root   /opt/project;                                        # 根目录 
            index  index.html index.htm;                                # 示例索引首页
        }
    }
```