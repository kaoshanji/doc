logback.qos.ch 文档 - 2017-08

1. 简介
> Logback旨在作为流行的log4j项目的继承者，它是由log4j的创始人CekiGülcü设计的，实现 SLF4J API.

2. 组成
- logback-core 为其他项目提供基础
- logback-classic 常用主要场景
- logback-access 配合Tomcat等容器使用，记录HTTP

3. 主要对象
- appenders
- encoders
- layouts
- filters
- 上下文

4. 替代 `System.out`

        pom.xml:
            <dependency>
                <groupId>ch.qos.logback</groupId>
                <artifactId>logback-classic</artifactId>
                <version>1.2.3</version>
            </dependency>

        HelloWorld.java:
            import org.slf4j.Logger;
            import org.slf4j.LoggerFactory;
            /**
            * Created by kaoshanji on 2017/8/3 17:50
            */
            public class HelloWorld {
                public static void main( String[] args ) {
                    Logger logger = LoggerFactory.getLogger("HelloWorld====>>>>>>");
                    logger.debug("Hello world...");
                }
            }

    示例：[h-logback](https://github.com/kaoshanji/x-java/tree/master/logback/h-logback)

5. 控制台与文件同步输出