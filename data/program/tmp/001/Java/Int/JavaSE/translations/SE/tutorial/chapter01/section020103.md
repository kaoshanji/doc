#   什么是继承？

不同种类的物体通常具有一定的共同点。例如，山地自行车，公路自行车和双人自行车都具有自行车的特征（当前速度，当前踏板节奏，当前档位）。然而每一个也定义了使它们不同的附加特征：双人自行车有两个座位和两组把手; 公路自行车有把手; 一些山地自行车有一个额外的链环，给他们一个较低的传动比。

面向对象编程允许类从其他类继承常用的状态和行为。在这个例子中，Bicycle现在变成了父的MountainBike，RoadBike和TandemBike。在Java编程语言中，每个类都允许有一个直接超类，每个超类都有可能有无数个子类：

`自行车课程的层次结构`

![concepts-bikeHierarchy.gif](image/concepts-bikeHierarchy.gif)

创建子类的语法很简单。在类声明的开始处，使用extends关键字，然后使用要继承的类的名称：

``` Java
class MountainBike extends Bicycle {

    // new fields and methods defining 
    // a mountain bike would go here

}
```

这给出MountainBike了Bicycle与之相同的所有字段和方法，但允许其代码专注于使其独特的功能。这使得您的子类的代码易于阅读。但是，必须注意正确记录每个超类定义的状态和行为，因为该代码不会出现在每个子类的源文件中。
