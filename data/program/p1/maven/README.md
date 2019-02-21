#   Maven

Apache Maven是一个软件项目管理和标准化工具。 基于项目对象模型（POM）的概念，Maven可以从一个中心信息管理项目的构建、报告和文档。

----

##  混个脸熟

标准化项目创建、开发、部署等流程

### 起步
- 安装
- Settings

### 概念
- 业务处理：插件和目标
- 项目管理：生命周期
- 你在哪里：坐标
- 资源来源：仓库
- 集成支持：依赖管理

### 项目
- POM
- 项目总体信息
  - 构建设置
  - 构建环境
  - POM关系
- 描述项目
  - groupId、artifactId、version
- 构建简单项目
```
JAR：mvn archetype:generate  -DgroupId=org.sonatype.mavenbook.ch03  -DartifactId=simple -Dversion=1 -DpackageName=org.sonatype.mavenbook
```
- 构建定制项目
```
web：mvn archetype:generate -DgroupId=com.mycompany.app -DartifactId=my-webapp -Dversion=1 -DarchetypeGroupId=org.apache.maven.archetypes -DarchetypeArtifactId=maven-archetype-webapp  
```

- 多模块项目
  -  继承
  -  组合

### 开发
1.  项目依赖

- 第三方依赖(传递、排除、范围、依赖版本号)、添加本地包
- 仓库、私服

2.  抽象项目生命周期，对项目做什么

- clean 清理项目
```
  pre-clean 执行一些清理前需要完成的工作
  clean 清理上一次构建生成的文件
  post-clean 执行一些清理后需要完成的工作
```
- default 构建所需执行的步骤
```
  validate 验证
  initialize 初始化
  generate-sources
  process-sources 项目主资源文件
  generate-resources
  process-resources
  complie 编译项目的主源码
  process-classes
  generate-test-sources
  process-test-sources 项目测试文件
  generate-test-resources
  process-test-resources
  test-complie 编译项目的测试代码
  process-test-classes
  test 测试 使用单元测试框架运行测试
  prepare-package
  package 打包、过滤、特殊环境 接收编译好的代码，打包成可发布的格式，如 JAR
  pre-integration-test
  integration-test
  post-integration-test
  verify
  install 部署 将包安装到 maven 本地仓库，供本地其他 maven 项目使用
  deploy 部署 将最终的包复制到远程仓库，供其他开发人员和 maven 项目使用
```
- site 建立和发布项目站点

3.  持续集成

----

##  资料
-   [官网](http://maven.apache.org/)
-   maven-definitive-guide_zh
-   Maven实战