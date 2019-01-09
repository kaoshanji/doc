#   IOC

解耦组件之间复杂关系，管理对象及对象之间依赖，IoC容器是用来管理对象依赖关系

##  概述

使用IoC容器，把资源获取的方向反转，让IoC容器主动管理依赖关系，将这些依赖关系注入到组件中。在具体的注入实现中，`接口`注入、`setter`注入、`构造器`注入是主要的注入方式

在应用管理依赖关系时，可以通过IoC容器将控制关系反转，在反转的实现中，如果通过可读的文本来完成配置，并且还能通过工具对这些配置信息进行可视化的管理和浏览，那么肯定是能够提高对组件关系的管理水平，并且如果耦合关系需要变动，并不需要重新修改和编译Java源代码

Spring IoC容器是一个产品实现。作为产品实现，他对多种应用场景的适配是通过Spring设计的IoC的容器系列来实现的，比如在某个容器系列中可以看到各种带有不同容器特性的实现，可以读取不同配置信息的各种容器，从不同I/O源读取配置信息的各种容器设计，更加面向框架的容器应用上下文的容器设计

----

##  目录

[主要接口](001.md)
[IoC容器的初始化过程](002.md)
[IoC容器的依赖注入](003.md)
[容器其他相关特性的设计与实现](004.md)

----