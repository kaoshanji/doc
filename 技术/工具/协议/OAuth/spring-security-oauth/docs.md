### OAuth 2.0 Provider(服务)
OAuth 2.0提供者机制负责公开OAuth 2.0受保护的资源。配置包括建立可独立或代表用户访问其受保护资源的OAuth 2.0客户端。提供者通过管理和验证用于访问受保护资源的OAuth 2.0令牌来执行此操作。在适用的情况下，提供商还必须为用户提供接口，以确认客户端可以被授权访问受保护资源（即，确认页面）

#### OAuth 2.0 Provider Implementation
OAuth 2.0中的提供者角色实际上是在授权服务和资源服务之间分割的，而有时它们位于同一个应用程序中，使用Spring Security OAuth，您可以选择在两个应用程序之间进行拆分，还可以使用多个资源服务共享 授权服务，令牌的请求由Spring MVC控制器端点处理，对受保护资源的访问由标准的Spring Security请求过滤器处理。为了实现OAuth 2.0授权服务器，Spring Security过滤器链中需要以下端点：
  - AuthorizationEndpoint
    - 用于服务请求授权
    - Default URL: /oauth/authorize
  - TokenEndpoint
    - 用于服务访问令牌的请求
    - Default URL: /oauth/token

实施OAuth 2.0资源服务器需要以下过滤器：
  - OAuth2AuthenticationProcessingFilter
    - 用于加载认证请求给定一个经过身份验证的访问令牌

对于所有的OAuth 2.0提供者的功能，使用特殊的Spring OAuth @Configuration 适配器简化了配置。

#### Authorization Server Configuration(授权)
在配置授权服务器时，您必须考虑客户端用于从最终用户获取访问令牌（例如授权代码，用户凭据，刷新令牌）的授权类型。服务器的配置用于提供客户端详细信息服务和令牌服务的实现，并且能够全局启用或禁用机制的某些方面。但是，请注意，每个客户端都可以特别配置，以便能够使用某些授权机制和访问授权。即 只是因为您的提供商配置为支持“客户端凭据”授权类型，并不意味着特定客户端被授权使用该授权类型

@EnableAuthorizationServer 注解用于配置OAuth 2.0授权服务器机制，以及实现 AuthorizationServerConfigurer 的任何@Beans（有一个方便的适配器实现）。将以下功能委派给由Spring创建并传递给AuthorizationServerConfigurer的单独配置程序：
  - ClientDetailsServiceConfigurer
    - 一个定义客户端详细信息服务的配置程序。 客户端的详细信息可以初始化，也可以参考现有的存储。
  - AuthorizationServerSecurityConfigurer
    - 定义令牌端点上的安全约束
  - AuthorizationServerEndpointsConfigurer
    - 定义授权、令牌端点和令牌服务

提供者配置的一个重要方面是将授权码提供给OAuth客户端（授权代码授权）的方式。 授权代码由OAuth客户端通过将最终用户指向用户可以输入其凭据的授权页面获得，导致从提供商授权服务器重定向到具有授权码的OAuth客户端。这在OAuth 2规范中有详细阐述。

#### Configuring Client Details
ClientDetailsServiceConfigurer（来自AuthorizationServerConfigurer的回调）可用于定义客户端详细信息服务的内存或JDBC实现，客户端的重要属性是：
  - clientId
    - （必填）客户端ID
  - secret
    - （可信客户端需要）客户机密码（如果有）
  - scope
    - 客户受限的范围。 如果范围未定义或为空（默认），客户端不受范围限制
  - authorizedGrantTypes
    - 授予客户端使用的授予类型。 默认值为空
  - authorities
    - 授予客户的当局（普通的Spring Security Authority）

可以通过直接访问底层支持，在正在运行的应用程序中更新客户端详细信息

#### Managing Tokens
AuthorizationServerTokenServices接口定义了管理OAuth 2.0令牌所必需的操作。请注意以下几点：
  - 当创建访问令牌时，必须存储身份验证，以便接受访问令牌的资源可以稍后引用
  - 访问令牌用于加载用于授权其创建的认证

当创建 AuthorizationServerTokenServices 实现时，您可能需要考虑使用具有许多可插入策略的 DefaultTokenServices 来更改访问令牌的格式和存储。默认情况下，它通过随机值创建令牌，并处理除 TokenStore 所代表的令牌的持久性以外的所有内容，默认存储是内存中的实现，但还有一些可用的实现，这是一个关于每个可能的一些讨论的描述：
  - 默认的 InMemoryTokenStore 对于单个服务器来说是可用的（即，在出现故障的情况下，流量较少且没有热备份到备份服务器）。大多数项目可以从这里开始，也可以在开发模式下运行，以便轻松启动没有依赖关系的服务器
  - JdbcTokenStore 是JDBC版本的，其将令牌数据存储在关系数据库中。如果可以在服务器之间共享数据库，请使用JDBC版本，如果只有一个服务器，则扩展同一服务器的实例，或者如果有多个组件，则授权和资源服务器
  -  JSON Web Token (JWT) 版本是把所有数据编码到令牌本身（因此，根本没有后端存储是显着的优点）。一个缺点是您不能轻易地撤销访问令牌，因此通常被授予短期到期权，并且撤销在刷新令牌处理。另一个缺点是如果您在其中存储了大量用户凭据信息，令牌可能会变得非常大。JwtTokenStore 并不是真正的“存储”，它不会保留任何数据，而是在DefaultTokenServices中的令牌值和认证信息之间进行翻译的角色相同

#### Grant Types
AuthorizationEndpoint支持的授权类型可以通过AuthorizationServerEndpointsConfigurer进行配置。默认情况下，除密码外，所有授权类型均受支持（有关如何切换的详细信息，请参阅下文），以下属性会影响授权类型：
  - authenticationManager
    - 通过注入AuthenticationManager来打开密码授权
  - userDetailsService
    - 如果您注入UserDetailsService或全局配置（例如在GlobalAuthenticationManagerConfigurer中），则刷新令牌授权将包含对用户详细信息的检查，以确保该帐户仍处于活动状态
  - authorizationCodeServices
    - 定义授权代码服务（AuthorizationCodeServices的实例）用于验证码授权。
  - implicitGrantService
    - 在隐性授予期间管理状态
  - tokenGranter
    - 完全控制授予和忽视上述其他属性

#### Configuring the Endpoint URLs
AuthorizationServerEndpointsConfigurer 有个pathMapping()方法，有两个参数：
  - 端点的默认（框架实现）URL路径
  - 需要的自定义路径（以“/”开头）

框架提供的URL路径：
  - /oauth/authorize
    - 授权端点
  - /oauth/token
    - 令牌端点
  - /oauth/confirm_access
    - 开放支持
  - /oauth/error
    - 用于在授权服务器中呈现错误
  - /oauth/check_token
    - 资源服务器用来解码访问令牌
  - /oauth/token_key
    - 如果使用JWT令牌，则公开令牌验证公钥

注： 授权端点/ oauth / authorize（或其映射的备选方案）应使用Spring Security进行保护，以使其只能由经过身份验证的用户访问，例如使用标准的Spring Security WebSecurityConfigurer：

        @Override
        protected void configure(HttpSecurity http) throws Exception {
        http
        .authorizeRequests().antMatchers("/login").permitAll().and()
        // default protection for all resources (including /oauth/authorize)
        .authorizeRequests()
         .anyRequest().hasRole("USER")
        // ... more configuration, e.g. for form login
        }

    注意：如果您的授权服务器也是资源服务器，则还有另一个安全过滤器链，优先级较低，控制API资源。通过访问令牌来保护这些请求，您需要将其路径与主用户面临的过滤器链中的路径不匹配，因此请务必在上述WebSecurityConfigurer中包含一个仅选择非API资源的请求匹配器

默认情况下，通过Spring OAuth在@Configuration支持中使用客户机密码的HTTP Basic认证为您保护令牌端点。

#### Customizing the UI(定制界面)
大多数授权服务器端点主要由机器使用，但有一些资源需要一个UI，那些是/ oauth / confirm_access的GET和/ oauth / error的HTML响应。它们是在框架中使用白名单实现提供的，因此授权服务器的大多数真实世界实例都希望提供自己的实例，以便他们可以控制样式和内容，所有您需要做的是为这些端点提供一个具有@RequestMappings的Spring MVC控制器，并且框架默认值在调度程序中将占用较低的优先级。在/ oauth / confirm_access端点中，您可以期待授权对象的绑定，并承载所有需要用户批准的数据（默认实现为WhitelabelApprovalEndpoint）。您可以从该请求中获取所有数据，然后根据需要进行渲染，然后所有用户需要执行的操作是将POST返回到/ oauth / authorize，其中包含有关批准或拒绝授权的信息。请求参数直接传递给AuthorizationEndpoint中的UserApprovalHandler，因此您可以根据需要多次解释数据。默认的UserApprovalHandler取决于您是否在AuthorizationServerEndpointsConfigurer中提供了一个ApprovalStore（在这种情况下它是一个ApprovalStoreUserApprovalHandler）（在这种情况下它是一个TokenStoreUserApprovalHandler），标准审批处理程序接受以下内容：
  - TokenStoreUserApprovalHandler
    - 通过user_oauth_approval的简单 是/否 决定等于“true”或“false”
  - ApprovalStoreUserApprovalHandler
    - 一组范围。* 参数键与 "\*" 等于所请求的范围 。该参数的值可以是 “ture” 或 “approved”（如果用户批准了授权），否则该用户被认为已经拒绝了该范围。如果批准了至少一个范围，则授权将成功。
  - 不要忘记在您为用户呈现的表单中包含CSRF保护。默认情况下，Spring Security正期待一个名为"\_csrf"的请求参数（它在请求属性中提供值）

#### Enforcing SSL
纯HTTP可用于测试，但授权服务器只能在生产中使用SSL。您可以在安全容器或代理服务器后面运行应用程序，如果您正确设置代理和容器（这与OAuth2无关），则应该可以正常运行）。您也可能希望使用Spring Security requireChannel（）约束保护端点。对于/授权终结点，您可以将其作为正常应用程序安全性的一部分。对于/ token端点，在AuthorizationServerEndpointsConfigurer中有一个可以使用sslOnly（）方法设置的标志。在这两种情况下，安全通道设置是可选的，但是如果Spring Security检测到不安全通道上的请求，Spring Security将重定向到安全通道

#### Customizing the Error Handling
授权服务器中的错误处理使用标准的Spring MVC功能，即端点本身的@ExceptionHandler方法。用户还可以向端点本身提供WebResponseExceptionTranslator，这是更改响应内容的最佳方式，而不是渲染方式。在授权端点的情况下，在令牌端点的情况下，异常的呈现委托给HttpMesssageConverters（可以添加到MVC配置）和OAuth错误视图（/ oauth / error）。为HTML响应提供了白名单错误端点，但用户可能需要提供自定义实现（例如，只需使用@RequestMapping（“/ oauth / error”）添加@Controller即可）。

#### Mapping User Roles to Scopes
限制标记的范围有时也不仅仅是分配给客户端的范围，还可以根据用户自己的权限。如果在 AuthorizationEndpoint 中使用 DefaultOAuth2RequestFactory，您可以设置一个标志 checkUserScopes = true，以将允许的范围限制为仅与那些与用户角色匹配的范围。您还可以将 OAuth2RequestFactory 注入到TokenEndpoint中，但只有在安装了 TokenEndpointAuthenticationFilter 的情况下才可以使用（即使用密码授权） - 您只需要在HTTP BasicAuthenticationFilter之后添加该过滤器。当然，您还可以实现自己的规则，将作用域映射到角色，并安装自己的 OAuth2RequestFactory 版本。AuthorizationServerEndpointsConfigurer 允许您注入自定义 OAuth2RequestFactory，以便您可以使用该功能设置工厂，如果您使用 @EnableAuthorizationServer

#### Resource Server Configuration
资源服务器（可以与授权服务器或单独的应用程序相同）提供受OAuth2令牌保护的资源。Spring OAuth 提供实现此保护的 Spring Security认证过滤器。您可以在@Configuration类上使用 @EnableResourceServer 进行打开，并使用 ResourceServerConfigurer 进行配置（必要时），可以配置以下功能：
  - tokenServices
    - 定义令牌服务的bean（ResourceServerTokenServices的实例）
  - resourceId
    - 资源的ID（可选，但建议并由验证服务器验证）。
  - 资源服务器的其他扩展点（例如，令牌提取器，用于从传入请求中提取令牌）
  - 请求匹配的受保护资源（默认为全部）
  - 受保护资源的访问规则（默认为"authenticated"）
  - Spring Security中HttpSecurity配置程序允许的受保护资源的其他自定义

@EnableResourceServer 注释将自动将一个 OAuth2AuthenticationProcessingFilter 类型的过滤器添加到 Spring Security 过滤器链.

你的 ResourceServerTokenServices 是与授权服务器的合同的另一半。如果资源服务器和授权服务器在同一个应用程序中，并且您使用DefaultTokenServices，那么您不需要太过分考虑这一点，因为它实现了所有必要的接口，因此它是自动一致的。如果您的资源服务器是单独的应用程序，则必须确保与授权服务器的功能相匹配，并提供一个ResourceServerTokenServices，该服务器知道如何正确解码该令牌。与授权服务器一样，您经常可以使用DefaultTokenServices，并且选择主要通过TokenStore（后端存储或本地编码）来表示。一个替代方案是 RemoteTokenServices，它是 Spring OAuth功能（不是规范的一部分），允许资源服务器通过授权服务器（/ oauth / check_token）上的HTTP资源解码令牌。 如果资源服务器中没有巨大的流量，RemoteTokenServices 就会很方便（每个请求都必须与授权服务器进行验证），或者如果能够缓存结果。要使用/ oauth / check_token端点，您需要通过更改其访问规则（默认为“denyAll（）”）在AuthorizationServerSecurityConfigurer中公开，例如：

          @Override
          		public void configure(AuthorizationServerSecurityConfigurer oauthServer) throws Exception {
          			oauthServer.tokenKeyAccess("isAnonymous() || hasAuthority('ROLE_TRUSTED_CLIENT')").checkTokenAccess(
          					"hasAuthority('ROLE_TRUSTED_CLIENT')");
          		}

在这个例子中，我们配置了/ oauth / check_token端点和/ oauth / token_key端点（所以信任的资源可以获得JWT验证的公钥）。这两个端点受到使用客户端凭据的HTTP基本身份验证的保护。

#### Configuring An OAuth-Aware Expression Handler
您可能希望利用Spring Security基于表达式的访问控制。默认情况下，@EnableResourceServer安装程序将注册表达式处理程序。这些表达式包括＃oauth2.clientHasRole，＃oauth2.clientHasAnyRole和＃ oath2.denyClient，可用于基于oauth客户端的角色提供访问（请参阅 OAuth2SecurityExpressionMethods 作为综合列表）。


### OAuth 2.0 Client
OAuth 2.0客户端机制负责访问其他服务器的OAuth 2.0保护资源，该配置包括建立用户可能访问的相关受保护资源，客户端还可能需要提供用于存储用户的授权码和访问令牌的机制。

#### Protected Resource Configuration
可以使用OAuth2ProtectedResourceDetails类型的bean定义来定义受保护的资源（或“远程资源”），受保护的资源具有以下属性：
  - id
    - 资源的id。 该id仅由客户端用于查找资源; 它从未在OAuth协议中使用。 它也被用作bean的id。
  - clientId
    - OAuth客户端ID。 这是OAuth提供商识别您的客户端的ID
  - clientSecret
    - 与资源相关的秘密。 默认情况下，没有秘密是空的。
  - accessTokenUri
    - 提供访问令牌的提供者OAuth端点的URI
  - scope
    - 逗号分隔的字符串列表，指定对资源的访问范围。 默认情况下，不指定范围
  - clientAuthenticationScheme
    - 您的客户端使用的方案来验证访问令牌端点。 建议的值：“http_basic”和“form”。 默认值为“http_basic”。

不同的授权类型具有OAuth2ProtectedResourceDetails的不同具体实现，（例如，“client_credentials”授权类型的ClientCredentialsResource）。 对于需要用户授权的授权类型，还有其他属性：
  - userAuthorizationUri
    - 如果用户需要授权访问资源，用户将被重定向到该uri。 请注意，这并不总是需要，具体取决于支持哪个OAuth 2配置文件。

#### Client Configuration
对于OAuth 2.0客户端，使用@ EnableOAuth2Client简化配置，这有两件事情：
  - 创建一个过滤器bean（ID为oauth2ClientContextFilter）来存储当前请求和上下文。 在需要在请求期间进行身份验证的情况下，管理重定向到和从OAuth认证uri。
  - 在请求范围内创建AccessTokenRequest类型的bean。 授权代码（或隐式）授权客户端可以使用这种方式来保持与个别用户的状态相关。

过滤器必须连接到应用程序中（例如，对于具有相同名称的DelegatingFilterProxy使用Servlet初始化程序或web.xml配置）。

AccessTokenRequest可以在OAuth2RestTemplate中使用，如下所示：

        @Autowired
        private OAuth2ClientContext oauth2Context;

        @Bean
        public OAuth2RestTemplate sparklrRestTemplate() {
        	return new OAuth2RestTemplate(sparklr(), oauth2Context);
        }

OAuth2ClientContext 在会话范围中放置（为您），以保持不同用户的状态分离，没有了，您将不得不自己在服务器上管理等效的数据结构，将传入的请求映射到用户，并将每个用户与 OAuth2ClientContext 的单独实例相关联。

#### Accessing Protected Resources
一旦您提供了资源的所有配置，您现在可以访问这些资源。用于访问这些资源的建议方法是使用Spring 3中引入的RestTemplate，Spring Security的OAuth提供了 RestTemplate的扩展，只需要提供一个 OAuth2ProtectedResourceDetails 的实例，要使用用户令牌（授权代码授权），您应考虑使用 @ EnableOAuth2Client配置。

作为一般规则，Web应用程序不应使用密码授权，因此如果可以支持 AuthorizationCodeResourceDetails，则避免使用 ResourceOwnerPasswordResourceDetails。如果您非常需要密码授权来从Java客户端工作，那么请使用相同的机制来配置OAuth2RestTemplate，并将凭据添加到 AccessTokenRequest（它是Map并且是短暂的），而不是 ResourceOwnerPasswordResourceDetails（在所有访问令牌之间共享）。

#### Persisting Tokens in a Client
客户端不需要持久化令牌，但是每次重新启动客户端应用程序时，用户都不需要批准新的令牌授权，这是很好的。 ClientTokenServices 接口定义了为特定用户维护OAuth 2.0令牌所必需的操作。提供了一个JDBC实现，但如果您希望实现自己的服务来将持久性数据库中的访问令牌和关联的身份验证实例存储起来，那么您可以使用。如果要使用此功能，则需要向OAuth2RestTemplate提供特殊配置的TokenProvider。

        @Bean
        @Scope(value = "session", proxyMode = ScopedProxyMode.INTERFACES)
        public OAuth2RestOperations restTemplate() {
        	OAuth2RestTemplate template = new OAuth2RestTemplate(resource(), new DefaultOAuth2ClientContext(accessTokenRequest));
        	AccessTokenProviderChain provider = new AccessTokenProviderChain(Arrays.asList(new AuthorizationCodeAccessTokenProvider()));
        	provider.setClientTokenServices(clientTokenServices());
        	return template;
        }

#### Customizations for Clients of External OAuth2 Providers
一些外部OAuth2提供者（例如Facebook）不能正确地实现规范，或者他们只是停留在旧版本的规范上，而不是 Spring Security OAuth。要在客户端应用程序中使用这些提供程序，您可能需要调整客户端基础架构的各个部分。

要以Facebook为例，在tonr2应用程序中有一个Facebook功能（您需要更改配置以添加您自己的，有效的客户端ID和密码 - 它们很容易在Facebook网站上生成）。

Facebook令牌响应还包含令牌到期时间的不合规JSON条目（它们使用到期而不是expires_in），因此如果要在应用程序中使用到期时间，则必须使用自定义OAuth2SerializationService手动解码它。
