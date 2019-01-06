#   class文件格式

描述JVM中定义的 class 文件格式。

每一个 class 文件都对应着唯一一个类或接口的定义信息，但是相应的，类或接口并不一定都必须定义在文件里。

每个 class 文件都由字节流组成，每个字节含有8个二进制位所有16位、32位和64位长度的数据将通过构造成2个、4个和8个连续的8位字节来表示。

##  ClassFile 结构

每个class文件对应一个如下所示的 ClassFile 结构。
```Java
ClassFile {
    u4                 magic; // 魔数
    u2                 minor_version;//副版本号
    u2                 major_version;//主版本号
    u2                 constant_pool_count;//常量池计数器
    cp_info            constant_pool[constant_pool_count-1];//常量池
    u2                 access_flags;//访问标志
    u2                 this_class;//类索引
    u2                 super_class;//父类索引
    u2                 interfaces_count;//接口计数器
    u2                 interfaces[interfaces_count];//接口表
    u2                 fields_count;//字段计数器
    field_info         fields[fields_count];//字段表
    u2                 methods_count;//方法计数器
    methods_info       methods[methods_count];//方法表
    u2                 attributes_count;//属性计数器
    attributes_info    attributes[attributes_count];//属性表     

}
```

##  各种名称的内部表示形式


