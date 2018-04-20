#   核心技术

##  [IOC容器](section010000.md)

IOC容器由以下模块`spring-core`， `spring-beans`，`spring-context`，`spring-context-support`，和`spring-expression`组成

在`org.springframework.beans`和`org.springframework.context`包是Spring框架的IoC容器的基础。该 `BeanFactory` 接口提供了一种能够管理任何类型对象的高级配置机制。 `ApplicationContext` 是一个子接口`BeanFactory`。它增加了与Spring的AOP功能更容易的集成; 消息资源处理（用于国际化），事件发布; 和特定于应用层的上下文（例如，`WebApplicationContext` 用于Web应用程序中）。

简而言之，它`BeanFactory`提供了配置框架和基本功能，并`ApplicationContext`增加了更多的企业特定功能。这`ApplicationContext`是一个完整的超集`BeanFactory`，并在本章中专门用于描述Spring的IoC容器。有关使用的详细信息`BeanFactory`，而不是`ApplicationContext`。


### 依赖注入和控制反转

一个Java应用程序 - 一个宽松的术语，将受限制的嵌入式应用程序运行到n层服务器端企业应用程序 - 通常由协作形成应用程序的对象组成。因此，应用程序中的对象相互依赖。

尽管Java平台提供了丰富的应用程序开发功能，但它缺乏将基本构建块组织成一个整体的手段，从而将这一任务交给了架构师和开发人员。尽管您可以使用诸如Factory，Abstract Factory，Builder，Decorator和Service Locator等设计模式 来组合应用程序的各种类和对象实例，但这些模式仅仅是：给定名称的最佳实践，以及描述该模式做了什么，在哪里应用它，它解决的问题等等。模式是你必须在你的应用程序中实现的正式最佳实践。

Spring框架控制反转（IoC）组件解决了这个问题，它提供了一种将不同组件组合到完全可用的应用程序中的正式手段。Spring框架将形式化的设计模式编码为可以集成到自己的应用程序中的第一类对象。许多组织和机构以这种方式使用Spring框架来设计强大的可维护应用程序。

IoC也被称为依赖注入（DI）。它是一个过程，对象通过构造函数参数，工厂方法的参数或在工厂方法构造或返回后在对象实例上设置的属性来定义它们的依赖关系，即它们使用的其他对象。

`容器` 在创建bean时会注入这些依赖关系。这个过程从根本上来说是相反的，因此名为控制反转（IoC），bean本身通过使用类的直接构造来控制其依赖关系的实例化或位置，或者诸如服务定位器模式。


### 核心基础

`spring-core`和`spring-beans`模块提供框架基础支持，包括IOC和依赖注入特征。这 BeanFactory是工厂模式的复杂实现。它消除了对程序化单例的需求，并允许将实际程序逻辑中的依赖关系的配置和规范分离。

### 上下文

`spring-context`模块建立在核心基础之上，它是访问一个框架式的方式是类似于一个JNDI注册表对象的装置。Context模块继承Beans模块的特性，并通过例如Servlet容器添加对国际化（例如使用资源包），事件传播，资源加载以及上下文透明创建的支持。Context模块还支持Java EE功能，如EJB，JMX和基本远程处理。该`ApplicationContext`接口是语境模块的焦点。 `spring-context-support`（EhCache，Guava，JCache），邮件（JavaMail），日程安排（CommonJ，Quartz）和模板引擎（FreeMarker，JasperReports，Velocity）提供支持，以将常见的第三方库集成到Spring应用程序上下文中。

----

##  [资源](section020000.md)

`java.net.URL`不幸的是，对于各种URL前缀，Java的标准类和标准处理程序不足以满足所有对低级资源的访问。例如，没有`URL`可用于访问需要从类路径获取的资源的标准化实现，或者相对于某个资源的获取 `ServletContext`。尽管可以为专用`URL` 前缀注册新的处理程序（类似于诸如前缀的现有处理程序`http:`），但这通常非常复杂，并且URL界面仍然缺乏某些期望的功能，例如检查资源是否存在的方法指出

----

##  [验证、数据绑定和类型转换](section030000.md)

将验证视为业务逻辑有优点和缺点，Spring提供了验证（和数据绑定）设计，不排除其中任何一个。具体的验证不应该绑定到Web层，应该易于本地化，应该可以插入任何可用的验证器。考虑到上述情况，Spring已经提出了一个`Validator`接口，它在应用程序的每一层都是基本的和显着的可用的。

数据绑定对于允许用户输入动态绑定到应用程序的域模型（或用于处理用户输入的任何对象）很有用。Spring提供了所谓的`DataBinder`完成。在`Validator`和 `DataBinder`补`validation`包，它主要在使用，但不限于MVC框架。

这`BeanWrapper`是Spring框架中的一个基本概念，并在很多地方使用。但是，您可能不需要`BeanWrapper` 直接使用。因为这是参考文件，所以我们觉得有些解释可能是按顺序的。我们将`BeanWrapper`在本章中解释这一点，因为如果您打算使用它，那么在尝试将数据绑定到对象时很可能会这样做。

Spring的DataBinder和较低级的BeanWrapper都使用PropertyEditor来解析和格式化属性值。这个`PropertyEditor`概念是JavaBeans规范的一部分，本章也对此进行了解释。Spring 3引入了一个“core.convert”包，它提供了一个通用的类型转换工具，以及一个用于格式化UI字段值的高级“格式”包。这些新软件包可以作为PropertyEditor的简单替代品，本章也将对此进行讨论

----

##  [SpEL](section040000.md)

`spring-expression`模块提供了强大的表达式语言，用于在运行时查询和操作对象图。它是JSP 2.1规范中指定的统一表达式语言（统一EL）的扩展。该语言支持设置和获取属性值，属性分配，方法调用，访问数组内容，集合和索引器，逻辑和算术运算符，命名变量以及从Spring的IoC容器中按名称检索对象。它还支持列表预测和选择以及常用列表聚合

----


##  [AOP](section050000.md)

`spring-aop`模块提供符合AOP联盟的面向方面编程实现，允许您定义方法拦截器和切入点，以便干净地分离实现应该分离的功能的代码。使用源代码级元数据功能，您还可以将行为信息以类似于.NET属性的方式整合到您的代码中。

`spring-aspects`模块提供与AspectJ的集成。

`spring-instrument`模块提供了在特定应用程序服务器中使用的类工具支持和类加载器实现。该`spring-instrument-tomcat` 模块包含Tomcat的Spring工具代理。

----
