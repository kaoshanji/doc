#   [包java.lang.management](https://docs.oracle.com/javase/8/docs/api/java/lang/management/package-summary.html)


提供用于监视和管理Java虚拟机以及Java运行时中的其他组件的管理界面

##  描述

提供用于监视和管理Java虚拟机以及Java运行时中的其他组件的管理界面。它允许对正在运行的Java虚拟机进行本地和远程监视和管理。

### 平台MXBean

平台MXBean是一个托管bean，它符合JMX Instrumentation Specification并且只使用一组基本数据类型。每个平台MXBean都PlatformManagedObject 具有唯一的 名称。

### ManagementFactory

该ManagementFactory班是针对Java平台的管理工厂类。此类提供一组静态工厂方法，以获取Java平台的MXBeans，以允许应用程序直接访问MXBean。

一个MBeanServer的平台可以与访问 getPlatformMBeanServer方法。在第一次调用此方法时，它会创建平台MBeanServer并注册所有平台MXBeans，包括平台MXBeans。每个平台MXBean都使用管理界面规范中定义的唯一名称进行注册。这是一个MBeanServer，可以由在同一Java虚拟机中运行的不同托管组件共享。

### 互通性

管理应用程序和正在运行的虚拟机的平台MBeanServer可以互操作，而无需平台MXBean接口使用的类。在JMX连接器服务器和连接器客户端之间传输的数据类型是JMX 开放类型，这允许跨版本进行互操作。MXBean接口使用的数据类型在通过MBeanServer接口访问时映射到开放类型。有关详细信息，请参阅 MXBean规范。

### 访问MXBeans的方法

应用程序可以通过以下方式监视Java虚拟机和运行时的检测：

1.  直接访问MXBean接口

-   在正在运行的Java虚拟机中本地获取MXBean实例：

```
   RuntimeMXBean mxbean = ManagementFactory.getRuntimeMXBean（）;

   //获取标准属性“VmVendor”
   String vendor = mxbean.getVmVendor（）;
```

或者通过调用 getPlatformMXBean或 getPlatformMXBeans方法：

```
   RuntimeMXBean mxbean = ManagementFactory.getPlatformMXBean（RuntimeMXBean.class）;

   //获取标准属性“VmVendor”
   String vendor = mxbean.getVmVendor（）;
```

-   构造一个MXBean代理实例，将方法调用转发给给定的MBeanServer：
```
   MBeanServerConnection mbs;

   //连接到正在运行的JVM（或自身）并获取MBeanServerConnection
   //在其中注册了JVM MBean
   ...

   //获取RuntimeMXBean接口的MBean代理
   RuntimeMXBean proxy =
       ManagementFactory.getPlatformMXBean（MBS，
                                           RuntimeMXBean.class）;
   //获取标准属性“VmVendor”
   String vendor = proxy.getVmVendor（）;
```

代理通常用于访问远程Java虚拟机中的MXBean。另一种创建MXBean代理的方法是：

```
   RuntimeMXBean proxy =
        ManagementFactory.newPlatformMXBeanProxy（mbs，
                                                ManagementFactory.RUNTIME_MXBEAN_NAME，
                                                RuntimeMXBean.class）;
```

2.  通过MBeanServer间接访问MXBean接口

-   浏览 platform MBeanServer本地访问MXBeans或MBeanServerConnection远程访问MXBeans。MXBean的属性和操作仅使用 包含基本数据类型的JMX开放类型CompositeData，并TabularData 在其中 定义OpenType。

```
   MBeanServerConnection mbs;

   //连接到正在运行的JVM（或自身）并获取MBeanServerConnection
   //在其中注册了JVM MXBeans
   ...

   尝试{
       //假设RuntimeMXBean已在mbs中注册
       ObjectName oname = new ObjectName（ManagementFactory.RUNTIME_MXBEAN_NAME）;

       //获取标准属性“VmVendor”
       String vendor =（String）mbs.getAttribute（oname，“VmVendor”）;
   } catch（....）{
       //捕获ObjectName构造函数抛出的异常
       //和MBeanServer.getAttribute方法
       ...
   }
```

### 平台扩展

Java虚拟机实现可以通过定义依赖于平台的接口将其平台扩展添加到管理接口，该接口扩展标准管理接口以包括特定于平台的度量和管理操作。ManagementFactory类中的静态工厂方法将返回具有平台扩展的MXBeans。

建议使用特定于供应商的前缀（例如供应商名称）命名特定于平台的属性，以避免在将来的标准管理接口扩展与平台扩展之间发生属性名称冲突。如果标准管理接口的未来扩展定义了管理接口的新属性，并且属性名称恰好与某个供应商特定属性的名称相同，则必须修改访问该供应商特定属性的应用程序以应对版本控制和兼容性问题。

下面是一个示例，说明如何从平台扩展访问属性：

1）直接访问特定于Oracle的MXBean接口

```
   List<com.sun.management.GarbageCollectorMXBean> mxbeans =
       ManagementFactory.getPlatformMXBeans（com.sun.management.GarbageCollectorMXBean.class）;

   for（com.sun.management.GarbageCollectorMXBean gc：mxbeans）{
       //获取标准属性“CollectionCount”
       String count = mxbean.getCollectionCount（）;

       //获取特定于平台的属性“LastGcInfo”
       GcInfo gcinfo = gc.getLastGcInfo（）;
       ...
   }
```

2） 通过代理 通过MBeanServer访问Oracle特定的MXBean接口

```
   MBeanServerConnection mbs;

   //连接到正在运行的JVM（或自身）并获取MBeanServerConnection
   //在其中注册了JVM MXBeans
   ...

   List<com.sun.management.GarbageCollectorMXBean> mxbeans =
       ManagementFactory.getPlatformMXBeans（mbs，com.sun.management.GarbageCollectorMXBean.class）;

   for（com.sun.management.GarbageCollectorMXBean gc：mxbeans）{
       //获取标准属性“CollectionCount”
       String count = mxbean.getCollectionCount（）;

       //获取特定于平台的属性“LastGcInfo”
       GcInfo gcinfo = gc.getLastGcInfo（）;
       ...
   }
```
除非另有说明，否则将null参数传递给此包中任何类或接口中的构造函数或方法将导致NullPointerException抛出。

java.lang.management API是线程安全的。

----


