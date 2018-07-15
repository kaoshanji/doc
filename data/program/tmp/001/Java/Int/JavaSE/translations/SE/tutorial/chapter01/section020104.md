#   什么是接口？
正如你已经知道的那样，对象通过它们公开的方法来定义它们与外界的交互。方法形成对象与外界的接口 ; 例如，电视机前面的按钮就是您和塑料外壳另一侧电线之间的接口。您按下“电源”按钮打开和关闭电视机。

在其最常见的形式中，接口是一组具有空体的相关方法。如果指定为接口，自行车的行为可能如下所示：

``` Java
interface Bicycle {

    //  wheel revolutions per minute
    void changeCadence(int newValue);

    void changeGear(int newValue);

    void speedUp(int increment);

    void applyBrakes(int decrement);
}
```


为了实现这个接口，你的类的名字会改变（例如，某个特定品牌的自行车ACMEBicycle），并且implements在类声明中使用关键字：

``` Java
class ACMEBicycle implements Bicycle {

    int cadence = 0;
    int speed = 0;
    int gear = 1;

   // The compiler will now require that methods
   // changeCadence, changeGear, speedUp, and applyBrakes
   // all be implemented. Compilation will fail if those
   // methods are missing from this class.

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

实现一个接口允许一个类对它承诺提供的行为变得更加正式。接口形成了类和外部世界之间的契约，并且这个契约在编译器的编译时执行。如果您的类声明实现了一个接口，那么在该类成功编译之前，由该接口定义的所有方法都必须出现在其源代码中。

>   要实际编译ACMEBicycle该类，您需要将public关键字添加到实现的接口方法的开头。

