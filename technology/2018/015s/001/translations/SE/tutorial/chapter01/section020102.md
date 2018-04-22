#   什么是类？

在现实世界中，你经常会发现很多单独的物体都是同一种物体。可能有成千上万的其他自行车存在，所有相同的品牌和型号。每辆自行车都由同一套蓝图构成，因此包含相同的部件。在面向对象的术语，我们说你的自行车是一个实例中的类的对象被称为自行车。一个类是创建单个对象的蓝图。

以下 Bicycle班级是自行车的一种可能实施方式：

``` Java
class Bicycle {

    int cadence = 0;
    int speed = 0;
    int gear = 1;

    void changeCadence(int newValue) {
         cadence = newValue;
    }

    void changeGear(int newValue) {
         gear = newValue;
    }

    void speedUp(int increment) {
         speed = speed + increment;   
    }

    void applyBrakes(int decrement) {
         speed = speed - decrement;
    }

    void printStates() {
         System.out.println("cadence:" +
             cadence + " speed:" + 
             speed + " gear:" + gear);
    }
}
```

Java编程语言的语法对你来说看起来很新，但这个类的设计是基于前面对自行车对象的讨论。的字段cadence，speed和gear表示该对象的状态，并且这些方法（changeCadence，changeGear，speedUp等）限定与外部世界的相互作用。

您可能已经注意到Bicycle该类不包含main方法。那是因为它不是一个完整的应用程序; 这只是可能用于应用程序的自行车蓝图。创建和使用新Bicycle对象的责任属于应用程序中的其他类。

这是一个 BicycleDemo创建两个独立Bicycle对象并调用其方法的类：

``` Java
class BicycleDemo {
    public static void main(String[] args) {

        // Create two different 
        // Bicycle objects
        Bicycle bike1 = new Bicycle();
        Bicycle bike2 = new Bicycle();

        // Invoke methods on 
        // those objects
        bike1.changeCadence(50);
        bike1.speedUp(10);
        bike1.changeGear(2);
        bike1.printStates();

        bike2.changeCadence(50);
        bike2.speedUp(10);
        bike2.changeGear(2);
        bike2.changeCadence(40);
        bike2.speedUp(10);
        bike2.changeGear(3);
        bike2.printStates();
    }
}
```

该测试的输出结果为两辆自行车打印结束踏板节奏，速度和齿轮：

节奏：50速度：10档：2
节奏：40速度：20档：3


