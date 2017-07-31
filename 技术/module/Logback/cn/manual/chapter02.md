## 第2章：结构

### logback的结构
Logback的基础架构是非常通用的，以便在不同的情况下应用。目前，logback分为三个模块：logback-core、logback-classic和logback-access.

`core`模块为其他两个模块奠定了基础.`classic`模块继承`core`,它对 `log4j`有着显著改进，实现 `SLF4J API`,所以可以很容易的替换其他实现，如：log4j 或 java.util.logging (JUL).第三个访问模块与Servlet容器集成，提供HTTP访问日志功能，[单独的文档](../access.html).

在本文档的其余部分，我们将写"logback"来引用`logback-classic`模块.

### Logger, Appenders and Layouts
Logback 建立在三个主要的类：`Logger`,`Appender`,`Layout`,这三种类型的组件一起工作，使开发人员可以根据消息类型和级别来记录消息，并在运行时控制这些消息的格式和报告的位置.

`Logger`类是 `logback-classic`模块的一部分,另一方面,`Appender` 和 `Layout` 接口是 `logback-core` 的一部分, 作为通用模块，`logback-core` 没有记录器的概念。

#### Logger 上下文
任何日志记录API的首要优点是通过纯System.out.println来保留其禁用某些日志语句的能力，同时允许其他人打印不受影响。此功能假设记录空间，即所有可能的日志记录语句的空间，根据某些开发人员选择的标准进行分类。在`logback-classic`中，这种分类是记录器的固有部分。 每一个记录器都附加到一个LoggerContext，它负责制造记录器，并将它们排列在一个类似层次结构中。

记录器是命名实体。 他们的名字区分大小写，他们遵循分层命名规则：
> 命名层次结构

> 如果记录器的名称后跟一个点是后代记录器名称的前缀，则记录器被称为另一个记录器的祖先。 如果记录器本身和后代记录器之间没有祖先，则记录器被认为是子记录器的父级。

例如，名为 `com.foo` 的记录器是名为 `com.foo.Bar` 的记录器的父级,同样, `java` 是 `java.util`的父代，也是 `java.util.Vector` 的祖先。 这个命名方案应该是大多数开发人员所熟悉的.

根记录器驻留在记录器层次结构的顶部.它是特殊的,因为它是开始时的每个层次结构的一部分.像每个记录器一样,它可以通过其名称检索,如下所示：

        Logger rootLogger = LoggerFactory.getLogger(org.slf4j.Logger.ROOT_LOGGER_NAME);

所有其他记录器也使用 `org.slf4j.LoggerFactory` 类中静态方法 `getLogger`方法检索.此方法将所需记录器的名称作为参数. `Logger`接口中的一些基本方法如下所示.

        package org.slf4j; 
        public interface Logger {

            // Printing methods: 
            public void trace(String message);
            public void debug(String message);
            public void info(String message); 
            public void warn(String message); 
            public void error(String message); 
        }

#### 有效等级又名级继承

`Loggers`可以分配级别，可能的级别集(TRACE, DEBUG, INFO, WARN and ERROR)在`ch.qos.logback.classic.Level` 类中定义。请注意，在`logback`中，`Level`类是`final`，不能被覆盖，因为以Marker对象的形式存在是一种更加灵活的方法。

如果给定的记录器没有分配一个级别，那么它将从其最接近的祖先中继承一个具有指定级别的记录器。

为了确保所有的记录器最终能够继承一个级别，根记录器总是具有一个分配的级别。默认情况下，此级别为DEBUG。

以下是具有各种分配级别值的四个示例，以及根据级别继承规则生成的有效（继承）级别。

例1

|   Logger name |   分配 level      |   有效 level       |
|   ----------- |   :------------:  |   --------------: |
|   root        |   DEBUG           |   DEBUG           |
|   X           |   none            |   DEBUG           |
|   X.Y         |   none            |   DEBUG           |
|   X.Y.Z       |   none            |   DEBUG           |
在上面的示例1中，只有根记录器被分配了一个级别。 该级别DEBUG由其他记录器X，X.Y和X.Y.Z继承

例2

|   Logger name |   Assigned level  |   Effective level |
|   ----------- |   :------------:  |   --------------: |
|   root        |   ERROR           |   ERROR           |
|   X           |   INFO            |   INFO            |
|   X.Y         |   DEBUG           |   DEBUG           |
|   X.Y.Z       |   WARN            |   WARN            |
在上面的示例2中，所有记录器都具有分配的级别值，级继承不起作用。

例3

|   Logger name |   Assigned level  |   Effective level |
|   ----------- |   :------------:  |   --------------: |
|   root        |   DEBUG           |   DEBUG           |
|   X           |   INFO            |   INFO            |
|   X.Y         |   none            |   INFO            |
|   X.Y.Z       |   ERROR           |   ERROR           |
在上面的示例3中，记录器`root`，`X`和`X.Y.Z`分别被分配给`DEBUG`，`INFO`和`ERROR`。 Logger `X.Y`从其父级`X`继承其级别值。

例4

|   Logger name |   Assigned level  |   Effective level |
|   ----------- |   :------------:  |   --------------: |
|   root        |   DEBUG           |   DEBUG           |
|   X           |   INFO            |   INFO            |
|   X.Y         |   none            |   INFO            |
|   X.Y.Z       |   none            |   INFO            |
在上面的示例4中，记录器`root`和`X`分别被分配给`DEBUG`和`INFO`.记录器`X.Y`和`X.Y.Z`从其最近的父级`X`继承其级别值，该父级`X`具有分配级别.

#### 打印方法和基本选择规则

根据定义，打印方法确定记录请求的级别。例如，如果 `L` 是一个 logger 接口，那么 `L.info("..")` 声明的记录器级别是 INFO.

如果记录请求的级别高于或等于其记录器的有效级别，则说记录请求被启用.否则，该请求被称为禁用. 如前所述，没有分配级别的记录器将从其最近的祖先继承一个,这个规则总结如下:
> 如果p> = q，则启用对具有有效等级q的记录器发出的级别p的日志请求。

这个规则是logback的核心。 它假定级别的顺序如下：TRACE <DEBUG <INFO <WARN <ERROR。

以更为图形的方式，这里是选择规则的工作原理.在下表中，垂直标题显示由p指定的日志记录请求的级别，而水平标题显示记录器的有效级别，由q指定.行（级别请求）和列（有效级别）的交集是从基本选择规则生成的布尔值。

<table>
      <tbody>
                <tr> 
                        <td rowspan="2">level of <br>request <em>p</em></td>
			<td style="border-top: 1px solid #DDDDDD;" align="center" colspan="6">effective level <em>q</em></td>
		</tr>
		<tr align="left">
			<th style="border-bottom: 1px solid #DDDDDD;">TRACE</th>
			<th style="border-bottom: 1px solid #DDDDDD;">DEBUG</th>
			<th style="border-bottom: 1px solid #DDDDDD;">INFO</th>
			<th style="border-bottom: 1px solid #DDDDDD;">WARN</th>
			<th style="border-bottom: 1px solid #DDDDDD;">ERROR</th>	
                        <th style="border-bottom: 1px solid #DDDDDD;">OFF</th>    			
		</tr>
		<tr align="left">
			<th>TRACE</th>
			<td style="color:green">YES</td>
			<td style="color:red">NO</td>
			<td style="color:red">NO</td>
			<td style="color:red">NO</td>
			<td style="color:red">NO</td>
                        <td style="color:red">NO</td>
		</tr>
		<tr align="left">
                        <th>DEBUG</th>
                        <td style="color:green">YES</span></td>
                        <td style="color:green">YES</span></td>
                        <td style="color:red">NO</span></td>
                        <td style="color:red">NO</td>
                        <td style="color:red">NO</td>
                        <td style="color:red">NO</td>
		</tr>
		<tr align="left">
                        <th>INFO</th>
                        <td style="color:green">YES</td>
                        <td style="color:green">YES</td>
                        <td style="color:green">YES</td>
                        <td style="color:red">NO</td>
                        <td style="color:red">NO</td>
                        <td style="color:red">NO</td>
		</tr>
                <tr align="left">
                        <th>WARN</th>
                        <td style="color:green">YES</td>
                        <td style="color:green">YES</td>
                        <td style="color:green">YES</td>
                        <td style="color:green">YES</td>
                        <td style="color:red">NO</td>
                        <td style="color:red">NO</td>
                </tr>
		<tr align="left">
			<th>ERROR</th>
			<td style="color:green">YES</td>
			<td style="color:green">YES</td>
			<td style="color:green">YES</td>
			<td style="color:green">YES</td>
			<td style="color:green">YES</td>
                        <td style="color:red">NO</td>
		</tr>		
	</tbody>
</table>

以下是基本选择规则的示例。

        import ch.qos.logback.classic.Level;
        import org.slf4j.Logger;
        import org.slf4j.LoggerFactory;
        ....

        // get a logger instance named "com.foo". Let us further assume that the
        // logger is of type  ch.qos.logback.classic.Logger so that we can
        // set its level
        ch.qos.logback.classic.Logger logger = 
                (ch.qos.logback.classic.Logger) LoggerFactory.getLogger("com.foo");
        //set its Level to INFO. The setLevel() method requires a logback logger
        logger.setLevel(Level. INFO);

        Logger barlogger = LoggerFactory.getLogger("com.foo.Bar");

        // This request is enabled, because WARN >= INFO
        logger.warn("Low fuel level.");

        // This request is disabled, because DEBUG < INFO. 
        logger.debug("Starting search for nearest gas station.");

        // The logger instance barlogger, named "com.foo.Bar", 
        // will inherit its level from the logger named 
        // "com.foo" Thus, the following request is enabled 
        // because INFO >= INFO. 
        barlogger.info("Located nearest gas station.");

        // This request is disabled, because DEBUG < INFO. 
        barlogger.debug("Exiting gas station search");

#### 检索 Loggers

调用具有相同名称的 `LoggerFactory.getLogger` 方法将始终返回对完全相同的记录器对象的引用。

例如：

        Logger x = LoggerFactory.getLogger("wombat"); 
        Logger y = LoggerFactory.getLogger("wombat");

`x` 和 `y` 指的是完全相同的记录器对象。

因此，可以配置记录器，然后在代码中的其他地方检索相同的实例，而不会绕过引用

logback环境的配置通常在应用程序初始化时完成。 首选方法是读取配置文件。 这种做法将在稍后讨论。

Logback可以轻松地通过软件组件命名记录器。这可以通过在每个类中实例化记录器来实现，记录器名称等于类的完全限定名称。这是定义记录器的有用和直接的方法。由于日志输出是生成记录器的名称，因此这个命名策略可以轻松识别日志消息的来源。但是，这只是命名记录器的一个可能的常见策略。 Logback不限制可能的一组记录器。 作为开发人员，您可以随意命名记录器。

#### Appender和Layouts

基于其记录器选择性地启用或禁用日志记录请求的功能只是需求的一部分。 回溯允许记录请求打印到多个目的地，在logback中，输出目的地称为`appender`。 目前，控制台，文件，远程套接字服务器，MySQL，PostgreSQL，Oracle等数据库，JMS和远程UNIX Syslog守护程序都存在追加器。

可以将多个`appender`连接到记录器。

`addAppender`方法向给定的记录器添加一个`appender`。给定记录器的每个启用的日志记录请求将被转发到该记录器中的所有追加者以及层次结构中较高的追加者,换句话说，追加者是从记录器层次结构中继承的.例如，如果将`consoleappender`添加到根记录器中，那么所有启用的记录请求将至少在控制台上打印。如果另外还有一个文件追加器被添加到记录器中，比如说L，然后启用L的记录请求，L的孩子将打印在文件和控制台上.可以覆盖此默认行为，以便通过将记录器的加性标志设置为false，使追加者累积不再加和。

关于追加者相加性的规则总结如下：
> 记录器L的日志声明的输出将转到L及其祖先中的所有追加者。 这是术语“appender additivity”的含义。
 然而，如果记录器L的祖先（称P）的加性标志设置为false，则L的输出将被引导到L及其祖先的所有追加者，直到并包括P，而不是任何祖先的追加者P.
 默认情况下，记录器的加性标志设置为true。

 下表显示了一个例子：

 <table>
	<tbody>
                <tr>
		        <th>Logger Name</th>
			<th>Attached Appenders</th>
			<th>Additivity Flag</th>
			<th>Output Targets</th>
			<th>Comment</th>
		</tr>
		<tr>
			<td>root</td>
			<td>A1</td>
			<td>not applicable</td>
			<td>A1</td>
			<td>Since the root logger stands at the top of the logger
				hierarchy, the additivity flag does not apply to it.
			</td>
		</tr>
		<tr>
			<td>x</td>
			<td>A-x1, A-x2</td>
			<td>true</td>
			<td>A1, A-x1, A-x2</td>
			<td>Appenders of "x" and of root.</td>
		</tr>
		<tr>
			<td>x.y</td>
			<td>none</td>
			<td>true</td>
			<td>A1, A-x1, A-x2</td>
			<td>Appenders of "x" and of root.</td>
		</tr>
		<tr>
			<td>x.y.z</td>
			<td>A-xyz1</td>
			<td>true</td>
			<td>A1, A-x1, A-x2, A-xyz1</td>
			<td>Appenders of "x.y.z", "x" and of root.</td>
		</tr>
		<tr>
			<td>security</td>
			<td>A-sec</td>
			<td class="blue"><span class="blue">false</span></td>
			<td>A-sec</td>
			<td>No appender accumulation since the additivity flag is set to
				<code>false</code>. Only appender A-sec will be used.
			</td>
		</tr>
		<tr>
			<td>security.access</td>
			<td>none</td>
			<td>true</td>				
                        <td>A-sec</td>
			<td>Only appenders of "security" because the additivity
				flag in "security" is set to
				<code>false</code>.
			</td>
		</tr>
	</tbody>
</table>

通常情况下，用户不仅要自定义输出目的地，还要自定义输出格式,这是通过将`layout`与`appender`相关联来实现的。`layout`负责根据用户的意愿格式化日志记录请求，而`appender`负责将格式化的输出发送到目的地。`PatternLayout` 是标准 Logback 分发的一部分，允许用户根据与 `C语言printf函数` 类似的转换模式来指定输出格式。

例如，具有转换模式 `%-4relative [%thread]%-5level%logger {32} - %msg%n` 的 `PatternLayout`将输出类似于：

        176  [main] DEBUG manual.architecture.HelloWorld2 - Hello world.

第一个字段是自程序启动以来经过的毫秒数,第二个字段是发出日志请求的线程,第三个字段是日志请求的级别,第四个字段是与日志请求关联的记录器的名称,"-"之后的文本是请求的消息。

#### logging 参数

鉴于logback-classic中的记录器实现了 `SLF4J` 的Logger 接口，某些打印方式允许多个参数。这些打印方法变体主要是为了提高性能，同时最小化对代码可读性的影响。

对于一些Logger记录器，写作，

        logger.debug("Entry number: " + i + " is " + String.valueOf(entry[i]));

导致构造消息参数的成本，即将整数i和条目[i]转换为字符串，并连接中间字符串,这是不管消息是否被记录。

避免参数构建成本的一种可能办法是通过测试来围绕log语句。 这是一个例子:

        if(logger.isDebugEnabled()) { 
                logger.debug("Entry number: " + i + " is " + String.valueOf(entry[i]));
        }

这样，如果对于记录器禁用了调试，则不会导致参数构造的成本,另一方面，如果为DEBUG级别启用了记录器，则会产生评估记录器是否启用的成本，两次：一次在debugEnabled中，一次在调试中。在实践中，这种开销是不重要的，因为评估一个记录器的时间不到实际记录一个请求所需的时间的1%。

#### 更好的选择

存在基于消息格式的方便的替代方案。 假设条目是一个对象，你可以写：

        Object entry = new SomeObject(); 
        logger.debug("The entry is {}.", entry);

只有在评估是否记录后，只有在判定为肯定的情况下，记录器实现格式化消息，并将“{}”对替换为条目的字符串值.换句话说，当禁用日志语句时，此表单不会导致参数构造的成本。

以下两行将产生完全相同的输出。 然而，在禁用日志记录的情况下，第二个变体的优先级至少为30。

        logger.debug("The new entry is "+entry+".");
        logger.debug("The new entry is {}.", entry);

也有两个参数变体。 例如，你可以写：

        logger.debug("The new entry is {}. It replaces {}.", entry, oldEntry);

如果需要传递三个或更多个参数，则还可以使用Object []变体。 例如，你可以写：

        Object[] paramArray = {newVal, below, above};
        logger.debug("Value {} was inserted between {} and {}.", paramArray);


#### 继续向下看

在我们引入了必要的logback组件之后，我们现在准备好描述当用户调用记录器的打印方法时logback框架采取的步骤。现在让我们分析当用户调用名为 `com.wombat `的记录器的 `info()` 方法时 logback 所采取的步骤。

1. 获取过滤器链

如果存在，则调用 `TurboFilter链` . `Turbo过滤器` 可以设置上下文范围的阈值，或者根据诸如标记，级别，记录器，消息或与每个记录请求相关联的 `Throwable` 等信息过滤出某些事件。如果过滤器链的回复为`FilterReply.DENY`，则记录请求将被删除.如果是 `FilterReply.NEUTRAL` ，那么我们继续下一个步骤，即步骤2.如果答复是 `FilterReply.ACCEPT` ，我们跳过下一个，直接跳到步骤3。

2. 应用基本选择规则

在此步骤中，logback将记录器的有效级别与请求级别进行比较.如果根据此测试禁用日志记录请求，则logback将丢弃请求，而无需进一步处理。 否则，它进行到下一步。

3. 创建一个 `LoggingEvent` 对象

如果请求在先前的过滤器中还存在，logback 将创建一个包含请求的所有相关参数的`ch.qos.logback.classic.LoggingEvent` 对象，例如请求的记录器，请求级别，消息本身，异常 可能已经随请求，当前时间，当前线程，发出日志记录请求和MDC的类的各种数据一起传递。请注意，这些字段中的某些字段被y延迟初始化，只有在实际需要时才会这样。 MDC用于使用附加的上下文信息来装饰日志记录请求。MDC的讨论在[这里](chapter08.html)

4. 调用 appenders

创建`LoggingEvent对象`后，logback 将调用所有适用的 `appender#doAppend()`方法，即从记录器上下文继承的`appenders`。

随着Logback分发器的所有追加器都将`AppenderBase`抽象类扩展到同步块中实现`doAppend`方法，确保线程安全.`AppenderBase#doAppend()`方法也会调用附加到`appender`的自定义过滤器，如果存在这样的过滤器。 自定义过滤器，可以动态附加到任何`appender，在一个单独的[章节](chapter07.html)。

5. 格式化输出

被调用的追加者负责格式化日志记录事件。但是，一些（但不是全部）`appender`将将日志记录事件格式化到 `layout` 的任务,`layout` 格式化 `LoggingEvent`实例，并将结果作为String返回.请注意，某些`appender`（如`SocketAppender`）不会将日志事件转换为字符串，而是将其序列化。 因此，他们没有也不需要`layout`。

6. 发送 `LoggingEvent`

日志记录事件完全格式化后，每个 `appender` 将其发送到目的地。这是一个序列UML图，以显示一切如何工作.

![图](images/underTheHoodSequence2.gif)

#### 性能

经常引用的 日志 的论据之一是其计算成本.这是一个合理的问题，即使中等大小的应用程序可以生成数千个日志请求.我们的大部分开发工作都用于测量和调整对数的性能.基于于这些努力，用户仍然应该注意以下性能问题.

1. 记录完全关闭时的记录性能

您可以通过将根记录器的级别设置为Level.OFF（尽可能高的级别）来完全关闭日志记录。当完全关闭日志记录时，日志请求的成本包括方法调用和整数比较。在3.2Ghz奔腾D机上，这个成本通常在20纳秒左右。

然而，任何方法调用涉及参数构建的“隐藏”成本。 例如，对于某些记录器x写入，

        x.debug("Entry number: " + i + "is " + entry[i]);

导致构造消息参数的成本，即将整数i和条目[i]转换成字符串，并且连接中间字符串，而不管该消息是否被记录。

参数构建的成本可能相当高，取决于所涉及参数的大小。 为了避免参数构建的成本，您可以利用SLF4J的参数化日志记录功能：

        x.debug("Entry number: {} is {}", i, entry[i]);

该变型不会招致参数构建的成本.与之前调用的`debug()`方法相比，它的速度会更快.只有将日志记录请求发送到附加的追加器，消息将被格式化. 此外，格式化消息的组件被高度优化.

尽管上述放置日志语句处于紧密循环中，即非常频繁地被调用的代码，是失败的提案，可能导致性能下降.登录紧密循环将减慢应用程序的速度，即使关闭记录，并且如果记录打开，将会产生大量（因此无用的）输出。

2. 打开日志记录时决定是否记录日志的性能

在logback中，不需要关注Logger层次结构.记录器知道其有效级别（即其级别，一旦级别继承被考虑在内）.如果父记录器的级别被更改，则所有的记录器都被联系以通知变更.因此，在接受或拒绝基于有效级别的请求之前，记录器可以进行准即时决定，而不需要咨询其祖先.

3. 实际记录（格式化和写入输出设备）

这是格式化日志输出并将其发送到目标的成本。再次，我们认真地努力使`layout`（格式化程序）尽可能快地执行,追加者也是如此。当登录到本地机器上的文件时，实际记录的典型成本约为9至12微秒。当登录到远程服务器上的数据库时，可能会达到几毫秒。

虽然功能丰富，但是Logback的最重要的设计目标之一是执行速度，这是仅次于可靠性的要求。一些对数组件已被重写几次以提高性能。