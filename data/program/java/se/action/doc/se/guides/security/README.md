#   [安全](https://docs.oracle.com/javase/8/docs/technotes/guides/security/index.html)

Java安全技术包括大量API，工具以及常用安全算法，机制和协议的实现。Java安全API涉及广泛的领域，包括加密，公钥基础结构，安全通信，身份验证和访问控制。Java安全技术为开发人员提供了用于编写应用程序的全面安全框架，还为用户或管理员提供了一组安全管理应用程序的工具。

----

##  程序员指南

### 一般安保
-   [Java安全概述](https://docs.oracle.com/javase/8/docs/technotes/guides/security/overview/jsoverview.html)
-   [安全架构](https://docs.oracle.com/javase/8/docs/technotes/guides/security/spec/security-spec.doc.html)
-   [Java密码体系结构（JCA）参考指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/CryptoSpec.html)
-   [如何为Java加密体系结构实现提供程序](https://docs.oracle.com/javase/8/docs/technotes/guides/security/crypto/HowToImplAProvider.html)
-   [标准算法名称](https://docs.oracle.com/javase/8/docs/technotes/guides/security/StandardNames.html)
-   [Oracle提供商](https://docs.oracle.com/javase/8/docs/technotes/guides/security/SunProviders.html)
-   [政策许可](https://docs.oracle.com/javase/8/docs/technotes/guides/security/permissions.html)
-   [默认策略实现和策略文件语法](https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyFiles.html)
-   [特权块的API](https://docs.oracle.com/javase/8/docs/technotes/guides/security/doprivileged.html)
-   [设置Java客户端的安全级别](https://docs.oracle.com/javase/8/docs/technotes/guides/deploy/client-security.html)
-   [安全问题排查](https://docs.oracle.com/javase/8/docs/technotes/guides/security/troubleshooting-security.html)

### Java身份验证和授权服务（JAAS）
-   [JAAS参考指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASRefGuide.html)
-   [JAAS教程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/tutorials/index.html)
-   [JAAS LoginModule开发人员指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/JAASLMDevGuide.html)

###  Java通用安全服务（Java GSS-API）
-   [用于Kerberos的Java GSS-API和JAAS教程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/index.html)
-   [在Java中使用Kerberos进行单点登录](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/single-signon.html)
-   [Java GSS安全功能](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/jgss-features.html)
-   [Java GSS高级安全编程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/lab/index.html)
-   [Kerberos 5 GSS-API机制](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/jgss-api-mechanism.html)

###  Java PKCS＃11参考指南
-   [Java PKCS＃11参考指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/p11guide.html)

###  Java安全套接字扩展（JSSE）
-   [JSSE参考指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jsse/JSSERefGuide.html)

###  公钥基础设施（PKI）
-   [Java PKI程序员指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/certpath/CertPathProgGuide.html)
-   [X.509证书和证书撤销列表](https://docs.oracle.com/javase/8/docs/technotes/guides/security/cert3.html)

###  简单身份验证和安全层（SASL）
-   [Java SASL API编程和部署指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/sasl/sasl-refguide.html)

###  XML数字签名
-   [XML数字签名API规范](https://docs.oracle.com/javase/8/docs/technotes/guides/security/xmldsig/overview.html)
-   [XML数字签名API参考和教程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/xmldsig/XMLDigitalSignature.html)

----

##  API规范

### 一般安保
-   [java.security包](https://docs.oracle.com/javase/8/docs/api/java/security/package-summary.html)
-   [javax.crypto包](https://docs.oracle.com/javase/8/docs/api/javax/crypto/package-summary.html)
-   [java.security.cert包](https://docs.oracle.com/javase/8/docs/api/java/security/cert/package-summary.html)
-   [java.security.spec包](https://docs.oracle.com/javase/8/docs/api/java/security/spec/package-summary.html)
-   [javax.crypto.spec包](https://docs.oracle.com/javase/8/docs/api/javax/crypto/spec/package-summary.html)
-   [java.security.interfaces包](https://docs.oracle.com/javase/8/docs/api/java/security/interfaces/package-summary.html)
-   [javax.crypto.interfaces包](https://docs.oracle.com/javase/8/docs/api/javax/crypto/interfaces/package-summary.html)
-   [javax.rmi.ssl包](https://docs.oracle.com/javase/8/docs/api/javax/rmi/ssl/package-summary.html)

### 认证路径
-   [java.security.cert包](https://docs.oracle.com/javase/8/docs/api/java/security/cert/package-summary.html)

### JAAS
-   [javax.security.auth包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/package-summary.html)
-   [javax.security.auth.callback包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/callback/package-summary.html)
-   [javax.security.auth.kerberos包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/kerberos/package-summary.html)
-   [javax.security.auth.login包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/login/package-summary.html)
-   [javax.security.auth.spi包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/spi/package-summary.html)
-   [javax.security.auth.x500包](https://docs.oracle.com/javase/8/docs/api/javax/security/auth/x500/package-summary.html)
-   [com.sun.security.auth包](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/package-summary.html)
-   [com.sun.security.auth.callback包](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/callback/package-summary.html)
-   [com.sun.security.auth.login包](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/login/package-summary.html)
-   [com.sun.security.auth.module包](https://docs.oracle.com/javase/8/docs/jre/api/security/jaas/spec/com/sun/security/auth/module/package-summary.html)


### Java GSS-API
-   [org.ietf.jgss包](https://docs.oracle.com/javase/8/docs/api/org/ietf/jgss/package-summary.html)
-   [com.sun.security.jgss包](https://docs.oracle.com/javase/8/docs/jre/api/security/jgss/spec/com/sun/security/jgss/package-summary.html)

### JSSE
-   [javax.net包](https://docs.oracle.com/javase/8/docs/api/javax/net/package-summary.html)
-   [javax.net.ssl包](https://docs.oracle.com/javase/8/docs/api/javax/net/ssl/package-summary.html)
-   javax.security.cert包（已删除，请改用[java.security.cert](https://docs.oracle.com/javase/8/docs/api/java/security/cert/package-summary.html) ）


### Java SASL
-   [javax.security.sasl包](https://docs.oracle.com/javase/8/docs/api/javax/security/sasl/package-summary.html)


### 基于SSL / TLS的RMI套接字工厂
-   [javax.rmi.ssl包](https://docs.oracle.com/javase/8/docs/api/javax/rmi/ssl/package-summary.html)

### XML数字签名
-   [javax.xml.crypto包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/package-summary.html)
-   [javax.xml.crypto.dom包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/dom/package-summary.html)
-   [javax.xml.crypto.dsig包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/dsig/package-summary.html)
-   [javax.xml.crypto.dsig.dom包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/dsig/dom/package-summary.html)
-   [javax.xml.crypto.dsig.keyinfo包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/dsig/keyinfo/package-summary.html)
-   [javax.xml.crypto.dsig.spec包](https://docs.oracle.com/javase/8/docs/api/javax/xml/crypto/dsig/spec/package-summary.html)


### 教程
-   该[安全功能在Java SE](https://docs.oracle.com/javase/tutorial/security/index.html)中的线索Java教程
-   [JAAS教程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jaas/tutorials/index.html)。
-   [用于Kerberos的Java GSS-API和JAAS教程](https://docs.oracle.com/javase/8/docs/technotes/guides/security/jgss/tutorials/index.html)
-   [Policytool用户指南](https://docs.oracle.com/javase/8/docs/technotes/guides/security/PolicyGuide.html)

### 更多信息
-   [在 Java SE的安全主页](https://www.oracle.com/technetwork/java/javase/tech/index-jsp-136007.html)

----