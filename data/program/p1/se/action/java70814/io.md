#   Java IO

对于I/O操作来说，其根本的作用在于传输数据。输入和输出指的仅是数据的流向，实际传输是通过某些具体的媒介来完成的，这其中最主要的媒介是文件系统和网络连接。最早的java.io包把I/O操作抽象成数据的流动，进而有了流的概念，在Java NIO中，则把I/O操作抽象成端到端的一个数据连接，这就有了通道的概念，推荐开发人员使用Java NIO中的新的通道概念

----

##  流

不管是内存中的数据、磁盘上的数据，还是通过网络传输的数据，其基本格式都是一系列的字节，所不同的是，不同的程序对这一系列的字节有不同的解释方式。将一组字节按照特定的方式进行解释，就形成了编程语言中的不同的基本类型。

Java中最基本的流是在字节这个层次上进行操作的。也就是说基本的流只负责在来源和目的之间传输字节，并不负责对字节的含义进行解释。在基本的字节基础上，Java也提供了一些过滤流的实现，这些过滤流实际上是基本字节流上的一个封装，在其上增加了不同的处理能力，如基本类型域字节序列之间的转换等

1.  基本输入流

如果流的实现只对使用者暴露字节这个层次的细节，那么可以直接继承 InputStream 或 OutputStream类，并提供自己额外的能力。

-   输入流 InputStream 类中包含两类功能
    -   一类是与读取流中字节数据相关的功能：read方法
    -   一类是流的控制功能：close、skip等方法

2.  基本输出流

把数据从程序中输出到其他地方，基本的OutputStream类的对象也是在字节这个层次上进行操作的

-   输出流 OutputStream 类中包含两类功能
    -   写入数据的 write 方法
    -   流的控制功能：close、flush等方法

3.  输入流的复用

在很多的场景下，每个数据源仅有一个接收者，如java.net.HttpURLConnetion类的对象打开一个网络连接，得到用来读取其中数据的InputStream类的对象，但是如果有多个接收者，那么就有些复杂。主要的原因在于，从另一个方面出发，按照流本身多代表的抽象含义，数据一旦流过去，就无法被再次使用，如果直接把一个 InputStream类的对象传递给一个接收者使用之后再传递给另外一个接收者，后者不能读取到流中的任何数据，因为流的当前读取位置已经到了末尾。

数据的使用方式和数据本身有根本的区别，InputStream类表示的是数据的使用方式，而并不是数据本身，两者的根本区别在于每个InputStream类的对象作为Java虚拟机中的对象，是有其内部状态的，无法被简单的复用，而纯粹的数据本身是无状态的

-   解决需要对输入流复用的需求，基本上有两种方式：
    -   利用输入流提供的标记和重置的控制能力：BufferedInputStream
    -   把输入流转换成数据来使用：ByteArrayInputStream
-   BufferedInputStream
    -   使用内部的缓冲区提升性能
    -   提供了对标记和重置的支持
-   ByteArrayInputStream
    -   首先被写入 ByteArrayOutputStream类的对象
    -   再把得到的字节数组保存下来

4.  过滤输入输出流

在基本的输入输出流之上，java.io包还提供了多种功能更强的过滤输入输出流。这些过滤流锁提供的增强能力各部相同
-   使用了内部的缓冲区来提供读写操作时的性能
-   在基本的字节流基础上提供了读写Java基本类型的支持
-   读写Java对象的支持
-   流重复读取
-   进行文件读写操作
-   作为字节数组和流之间的桥梁
-   通过管道方式连接在一起的输入和输出流
-   把多个输入流按顺序连接起来，形成一个完整的输入流

5.  字符流

字节流主要由机器来处理，而对于用户来说，更原因看到直接可读的字符，即java.io.Reader和java.io.Writer类及其子类，字符流适合用于处理程序中包含的文本类型的内容

创建一个字符流的最常见做法是通过一个字节流InputStream类或OutputStream类的对象进行创建，对应的是InputStreamReader类和OutStreamWriter类，在从字节流转成字符流时，需要指定字符的编码格式。

----

##  缓冲区

Java中的流实现采用了一种简单而朴素的做法，即以字节流为基础，在字节流上再通过过滤流来满足不同的需要。对于开发人员来说，流加上字节数组的使用方式的抽象层次较低，使用起来比较繁琐，更好的做法是使用Java NIO中新的缓冲区实现

1.  基本用法

Java NIO中的缓冲区在某些特性上类似于Java中的基本类型的数组，区别在于缓冲区提供的功能比数组丰富，也执行存储类型异构的数据。要理解缓冲区的使用，需要理解缓冲区的3个状态变量，分别是容量、读写限制和读写位置。

-   缓冲区的容量，指的是缓冲区的额定大小，在创建时指定，无法在创建后更改，任何时候缓冲区中的数据总数都不可能超过容量。
-   读写限制，表示的是在缓冲区中进行读写操作时的最大允许位置
-   读写位置，表示的是当前进行读写操作时的位置，当在缓冲区中进行相对读写操作时，在这个位置上进行。

缓冲区同样也支持标记和重置的特性

缓冲区进行的读写操作分成两类：一类是根据当前读写位置进行的相对读写操作，另外一类是根据在缓冲区中的绝对位置进行读写操作，两者的差别在于相对读写会改变当前读写位置，而绝对对鞋则不会

2.  字节缓冲区

对于Java中的基本类型，除了布尔类型之外，都有对应的缓冲区实现，用来存储此类型的数据。

在创建 ByteBuffer类的对象时，只能通过其静态工厂方法allocate来分配新空间，或者通过wrap方式来包装一个已有的字节数组，在创建ByteBuffer类的对象时需要指定缓冲区的容量，在创建完成之后，可以通过 put 方法向缓冲区中添加数据，而get方法则从其中读取数据

由于ByteBuffer类支出对基本数据类型的处理，因此必须要考虑字节顺序，同样的字节序列按照不同的顺序去解释，所得到的结果是不同的

ByteBuffer类支持的另外一个操作时压缩，压缩操作的一个典型的应用场景是把ByteBuffer类的对象作为数据传输时的缓冲区来使用

3.  缓冲区视图

ByteBuffer类的另一个常见的使用方式是在一个已有的ByteBuffer类的对象上创建出各种不同的视图，这些视图与他所基于的ByteBuffer类的对象共享同样的存储空间，但是提供额外的实用功能。在功能上，ByteBuffer类的视图与他所基于的ByteBuffer类的对象之间的关系类似过滤流和他所包装的流的关系，正因为这种共享存储空间的特性，在视图中对数据所做的修改会反映在原始的ByteBuffer类对象中

最常见的ByteBuffer类的视图是转换成对基本数据类型进行操作的缓冲区对象

除了数据本身之外，两者的读写位置、读写限制和标记位置等都是相互独立的。

除了基本类型的缓冲区视图之外，另外一种视图是类型相同的ByteBuffer类的对象

----

##  通道

通道是Java NIO对I/O操作提供的另外一种新的抽象方式。通道不是从I/O操作所处理的数据这个层次上去抽象，而是表示为一个已经建立好的到支持I/O操作的实体的连接。这个连接一旦建立，就可以在这个连接上进行各种I/O操作，在通道上所进行的I/O操作的类型取决于通道的特性，一般的操作包括数据的读取和写入等。在Java NIO中，不同的实体有不同的通道实现，比如文件通道和网络通道等。

Java NIO中的通道都实现了java.nio.channels.Channel接口。

-   读写操作
    -   移动读写操作
    -   ByteBuffer对象数组作为参数的读写

### 文件通道

文件是I/O操作的一个常见实体，由java.nio.channels.FileChannel类表示。

1.  基本用法

-   FileChannel类的对象既可以通过直接打开文件的方式来创建
-   另外一种是从已有的FileInputStream类、FileOutStream类和RandomAccessFile类的对象中得到

``` Java
// 打开文件通道并写入数据的示例
public void openAndWrite() throws IOException {
    FileChannel channel = FileChannel.open(Paths.get("my.txt"), StandardOpenOption.CREATE, StandardOpenOption.WRITE);
		ByteBuffer buffer = ByteBuffer.allocate(64);
		buffer.putChar('A').flip();
		channel.write(buffer);
}

// 对文件通道的绝对位置进行读写操作的示例
public void readWriteAbsolute() throws IOException {
    FileChannel channel = FileChannel.open(Paths.get("absolute.txt"), StandardOpenOption.READ, 
				StandardOpenOption.CREATE,StandardOpenOption.WRITE);
		ByteBuffer writeBuffer = ByteBuffer.allocate(4).putChar('A').putChar('B');
		writeBuffer.flip();
		
		channel.write(writeBuffer, 1024);
		ByteBuffer readBuffer = ByteBuffer.allocate(2);
		channel.read(readBuffer, 1026);
		readBuffer.flip();
		char result = readBuffer.getChar(); // 值为 'B'
}

```

2.  文件数据传输

在使用文件进行I/O操作时的一些典型场景包括把来自其他实体的数据写入文件中，以及把文件中的内容读取到其他实体中，按照通道的概念来说，就是文件通道和其他通道之间的数据传输，对于这种常见的需求，FileChannel类提供了 transferFrom 和 transferTo 方法用来快速的传输数据。
``` Java
// 使用文件通道保存网页内容的示例
public void loadWebPage(String url) throws IOException {
    try (FileChannel destChannel = FileChannel.open(Paths.get("content.txt"), StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
			InputStream input = new URL(url).openStream();
			ReadableByteChannel srcChannel = Channels.newChannel(input);
			destChannel.transferFrom(srcChannel, 0, Integer.MAX_VALUE);
		}
}
// 使用文件通道进行文件复制的示例
String srcFilename = "src.data";
String destFilename = "dest.data";
public void copyUseChannelTransfer() throws IOException {
    try (FileChannel src = FileChannel.open(Paths.get(srcFilename), StandardOpenOption.READ);
            FileChannel dest = FileChannel.open(Paths.get(destFilename), StandardOpenOption.WRITE, StandardOpenOption.CREATE)) {
        src.transferTo(0, src.size(), dest);
    }
}

```

3.  内存映射文件

在对大文件进行操作时，通过操作系统地内存映射文件支持，可以比较快速的对大文件进行操作。内存映射文件的原理在于把系统地内存地址映射到要操作的文件上。读取这些内存地址就相当于读取文件的内容，而改变这些内存地址的值就相当于修改内存中的文件。被映射到内存地址上的文件在使用上类似于操作系统中使用的虚拟内存文件。通过内存映射的方式对文件进行操作时，不再需要通过I/O操作来完成，而是直接通过内存地址访问操作来完成。

FileChannel类的map方法可以把一个文件的全部或部分内容映射到内存中，所得到的是一个ByteBuffer类的子类MappedByteBuffer的对象，程序只需要对这个MappedByteBuffer类的对象进行操作即可，对这个MappedByteBuffer类的对象所做的修改会自动同步到文件内容中。
``` Java
// 内存映射文件的使用示例
public void mapFile() throws IOException {
    try (FileChannel channel = FileChannel.open(Paths.get("src.data"), StandardOpenOption.READ, StandardOpenOption.WRITE)) {
			MappedByteBuffer buffer = channel.map(FileChannel.MapMode.READ_WRITE, 0, channel.size());
			byte b = buffer.get(1024 * 1024);
			buffer.put(5*1024*1024, b);
			buffer.force(); // 对象所做的修改被立即同步到文件中
		}
}

```

4.  锁定文件

当需要在多个程序之间进行数据交换时，文件通常是一个很好的选择。一个程序把产生的输出保存在指定的文件中，另一个程序进行读取即可。双方中需要在文件的格式上达成一致就可以了，内部逻辑的实现都是独立的。但是在这种情况下，对这个文件的访问操作容易产生冲突，而且对两个独立的应用程序来说，也没有什么比较好的方式来实现操作的同步，对于这种情况，最好的办法是对文件进行加锁，在一个程序完成操作之前，阻止另外一个程序对该文件的访问。
``` Java
// 锁定文件的示例
public void updateWithLock() throws IOException {
    ttry (FileChannel channel = FileChannel.open(Paths.get("settings.config"), StandardOpenOption.READ, StandardOpenOption.WRITE);
				FileLock lock = channel.lock()) {
			// 更新文件内容
		}
}
```

对文件进行加锁操作的主体是当前的Java虚拟机，也就是说这个加锁的功能用来协同当前Java虚拟机上运行的Java程序和操作系统上运行的其他程序，对于Java虚拟机上运行的多线程程序，不能用这种机制来协同不同线程对文件的访问。

### 套接字通道

除了文件之外，另外一个在应用开发中经常需要处理的I/O实体是网络连接。通过套接字API可以很容易的实现自己的网络服务器和客户端程序。

java.net包中的套接字实现的最大问题不是来自于API本身，而是出于性能方面的考虑。Socket类和ServerSocket类中提供的与建立连接和数据传输相关的方法都是阻塞式的，也就是说，如果操作没有完成，当前线程会处于等待状态。

为了解决与网络操作相关的问题，Java NIO提供了非阻塞式和多路复用的套接字连接，与文件操作一样，网络操作也被抽象成通道的概念。

1.  阻塞式套接字通道

Java NIO中提供了SocketChannel类和ServerSocketChannel类两种不同的套接字通道实现，这两种通道都支持阻塞和非阻塞两种模式
``` Java
// 阻塞式客户端套接字的使用示例
public void loadWebPageUseSocket() throws IOException {
    try (FileChannel destChannel = FileChannel.open(Paths.get("content.txt"), StandardOpenOption.WRITE, StandardOpenOption.CREATE);
				SocketChannel sc = SocketChannel.open(new InetSocketAddress("www.baidu.com", 80))) {
			String request = "GET / HTTP/1.1 \r\n\r\nHost: www.baidu.com\r\n\r\n";
			ByteBuffer header = ByteBuffer.wrap(request.getBytes("UTF-8"));
			sc.write(header);
			destChannel.transferFrom(sc, 0, Integer.MAX_VALUE);
		}
}
// 阻塞式服务器端套接字的使用示例
public void startSimpleSocket() throws IOException {
    ServerSocketChannel channel = ServerSocketChannel.open();
    channel.bind(new InetSocketAddress("localhost", 10800));
    while (true) {
        try (SocketChannel sc = channel.accept()) {
            sc.write(ByteBuffer.wrap("Hello".getBytes("UTF-8")));
        }
    }
}
```
套接字通道的阻塞模式总体来说与java.net包中的Socket类和ServerSocket类的使用方式非常类似，区别在于使用了NIO中新的通道的概念

2.  多路复用套接字通道

如果程序对网络操作的并发性和吞吐量要求比较高，那么比较好的办法是通过非阻塞式的套接字通道实现多路复用或者使用NIO.2中的异步套接字通道。

套接字通道的多路复用是通过一个专门的选择器(selector)来同时对多个套接字通道进行监听。当其中的某些套接字通道上有他感兴趣的事件发生时，这些通道会变成可用的状态，可以在选择器的选择操作中被选中。选择器通过一次选择操作可以获取这些被选中的通道的列表，然后根据所发生的事件类型分别进行处理。

这种基于选择器的做法的优势在于可以同时管理多个套接字通道，而且可用通道的选择一般是通过操作系统提供的底层系统调用来实现的，性能也比较高。

多路复用的实现方式的核心是选择器，即java.nio.channels.Selector类的对象
-   非阻塞式的套接字通道可以通过register方法注册到某个Selector类的对象上，以声明由该Selector类的对象来管理当前这个套接字通道
-   在进行注册时，需要提供一个套接字通道感兴趣的事件的列表
    -   这些事件包括连接完成、接收到新连接请求、有数据可读和可以写入数据等
    -   事件定义在java.nio.channels.SelectionKey类中
-   在完成注册之后，可以调用Selector类的对象的select方法来进行选择
-   选择操作完成之后，可以从Selector类的对象中得到一个可用的套接字通道的列表

-   通过套接字连接同时下载多个网页：books.java70814.s3.LoadWebPageUseSelector
    -   通过Selector类的open方法可以创建一个选择器
    -   有了选择器之后，下一步是把套接字通道注册到选择器上
        -   在私有方法 register中完成
        -   首先创建连接HTTP服务器的套接字通道，并通过configureBlocking方法将通道设置成非阻塞模式
        -   再注册到选择器上
        -   在注册时要指定套接字通道感兴趣的事件
    -   套接字通道注册完成之后，下一步就是调用Select类的对象的select方法来进行通道选择操作
    -   直接调用select方法是会阻塞的，直到所监听的套件字通道中至少有一个他们所感兴趣的时间发生为止
    -   在执行完select方式之后，通过调用selectedKey方法可以获取到表示被选中的通道的SelectionKey类的对象的集合
    -   每个SelectionKey类的对象与一个被监听的通道相对应
    -   接下来的操作就是对选中的每个SelectionKey类的对象所发生的是什么类型的事件进行判断，再进行相应的处理

----

##  nio.2

Java NIO在Java I/O库的基础上增加了通道的概念，提升了I/O操作的性能，使用起来也更加简单。Java 7 中的I/O库得到了进一步增强，称为NIO.2，NIO.2中包含的主要内容包括文件系统访问和异步I/O通道。

### 文件系统访问

Java 7加强了文件操作相关的功能，即新的java.nio.file包，其所提供的新功能包括文件路径的抽象、文件目录列表流、文件目录树遍历、文件属性和文件变化监视服务等

1.  文件路径的抽象

NIO.2中引入的java.nio.file.Path接口作为文件系统中路径的一个抽象，除了带来类型安全的好处之外，还提供了操作路径的很多实用方法。Path接口相当于将一个字符串表示的文件路径重新细分，使之赋有语义。

有了Path接口之后，对文件路径进行的很多操作变得很简单，不再需要依靠复杂的字符串操作。

2.  文件目录列表流

NIO.2中引入了一个新的接口java.nio.file.DirectoryStream 来支持列出一个目录下的子目录和文件这种遍历操作。

在使用的使用中，DirectoryStream接口的实现对象时通过java.nio.file.Files类的工厂方法来创建的，在创建时，可以指定遍历时的过滤条件，即满足何种条件的目录和文件才会被包括进来
``` Java
// 目录列表流：遍历当前目录下所有的"*.java"文件
public void listFiles() throws IOException {
    Path path = Paths.get("*");
    try(DirectoryStream<Path> stream = Files.newDirectoryStream(path, "*.java")) {
        for (Path entry: stream) {
            // 使用entry
        }
    }
}
```

2.  文件目录树遍历

如果希望对整个目录树进行遍历，需要使用java.nio.file.FileVisitor接口。FileVisitor接口是典型的访问者模式的实现

java.nio.file.SimpleFileVisitor类是一个简单的FileVisitor接口的适配器，通过继承SimpleFileVisitor类的方式可以不必实现FileVisitor接口中的全部方法

-   文件目录树遍历：books.java70814.s3.WalkFileTree

3.  文件属性

文件属性是文件除了本身的数据之外的元数据。NIO.2提供了专门的java.nio.file.attribute包来对文件属性进行处理。由于不同操作系统上的文件系统对文件属性的支持是不同的，NIO.2对文件属性进行了抽象，采用了文件属性视图的概念。

-   接口java.nio.file.attribute.AttributeView是所有属性视图的父接口
-   子接口java.nio.file.attribute.FileAttributeView表示的是文件的属性视图
    -   一类由java.nio.file.attribute.BaseFileAttributeView接口表示的包含基本文件属性的视图
    -   一类是java.nio.file.attribute.FileOwnerAttributeView接口表示的包含文件所有者信息的属性视图
-   OS
    -   Windows操作系统：java.nio.file.attribute.DosFileAttributeView
    -   UNIX和Linux系统：java.nio.file.attribute.PosixFileAttributeView

实际的获取和设置文件属性的操作是通过Files类中的静态方法来完成的。Files类提供的与文件属性相关的方法比较多，分成获取和设置属性两类。
``` Java
// 文件属性视图的使用示例：文件的"是否只读"属性的值
public void useFileAttributeView() throws IOException {
    Path path = Paths.get("content.txt");
    DosFileAttributeView view = Files.getFileAttributeView(path, DosFileAttributeView.class);
    if (view != null) {
        DosFileAttributes attrs = view.readAttributes();
        System.out.println(attrs.isReadOnly());
    }
}
// 获取文件的上次修改时间的示例
public void checkUpdatesRequired(Path path, int intervalInMillis) throws IOException {
    FileTime lastModifiedTime = (FileTime)Files.getAttribute(null, "lastModifiedTime");
		long now = System.currentTimeMillis();
		return now - lastModifiedTime.toMillis() > intervalInMillis;
}
```

5.  监视目录变化

可能需要监视某个目录下的文件所发生的变化，比如支持热部署的Web容器，或程序的输入来自某个特定目录下面的文本文件，NIO.2中提供了新的目录监视服务，使用该服务可以在指定目录中的子目录或文件被创建、更新或删除时得到事件通知，基于这些通知，程序可以进行相应的处理。

-   被监视的对象要实现java.nio.file.Watchable接口，并通过 register方法注册到表示监视服务的java.nio.file.WatchService接口的实现对象上，注册时需要指定被监视对象感兴趣的事件类型
-   注册成功之后，调用者可以得到一个表示这次注册行为的java.nio.file.WatchKey接口的实现对象
-   通过WatchKey接口可以获取在对应的被监视对象上所产生的事件，每个事件用java.nio.file.WatchEvent接口来表示
-   Watchable接口也提供了类似的方法来获取当前所有被监视的对象上的可用事件，查询的方式分成阻塞式和非阻塞式两种：阻塞式使用take方法，非阻塞式使用poll方法
-   查询结果的返回值是WatchKey接口的实现对象，调用WatchKey接口的 pollEvents方法可以得到对应监视对象上所发生的所有事件
``` Java
// 目录监视服务的使用示例：监视当前的工作目录，当有新的文件被创建时，输出该文件的大小
public void calculate () throws IOException, InterruptedException {
		
    WatchService service = FileSystems.getDefault().newWatchService();
    Path path = Paths.get("").toAbsolutePath();
    path.register(service, StandardWatchEventKinds.ENTRY_CREATE);
    while (true) {
        WatchKey key = service.take();// 阻塞方式获取结果
        for (WatchEvent<?> event : key.pollEvents()) {
            Path createPath = (Path)event.context();
            createPath = path.resolve(createPath);
            long size = Files.size(createPath);
            System.out.println(createPath +  " ==> " + size);
        }
        key.reset();
    }
}
// 想要取消对一个目录的监视，只需要调用对应的 WatchKey接口实现对象的 cancel方法即可
```

6.  文件操作的实用方法

在程序中进行文件操作时，经常会使用一些通用操作。Files类中提供了一系列的静态方法。
-   创建目录和文件的功能
-   复制文件的功能
-   支持两个文件之间的数据传输
-   支持一次性读入文件所有字节或所有行

### zip/jar文件系统

NIO.2的一个重要新特性是允许开发人员创建自定义的文件系统实现，把对文件系统的表示抽象出来，形成java.nio.file.FileSystem接口。

除了实现FileSystem接口之外，自定义文件系统地实现还需要实现java.nio.file.spi.FileSystemProvider接口，把自定义的文件系统注册到Java平台中，每个文件系统都有一个对应的URI模式作为该文件系统地标识符。

Java标准库中包含了两种文件系统地实现：一种是默认的基于底层操作系统地文件系统地实现，另外一种是NIO.2中新增的操作zip和jar文件的文件系统
``` Java
// 基于zip/jar文件系统实现的添加新文件到已有zip文件的做法
public void addFileToZip (File zipFile, File fileToAdd) throws IOException {
    Map<String,String> env = new HashMap<>();
    env.put("create", "true");
    try (FileSystem fs = FileSystems.newFileSystem(URI.create("jar:" + zipFile.toURI()), env)) {
        Path pathToAddFile = fileToAdd.toPath();
        Path pathInZipfile = fs.getPath("/" + fileToAdd.getName());
        Files.copy(pathToAddFile, pathInZipfile, StandardCopyOption.REPLACE_EXISTING);
        
    }
}

```

### 异步I/O通道

NIO.2中引入了新的异步通道的概念，并提供了异步文件通道和异步套接字通道的实现。

异步通道一般提供两种使用方法：一种是通过Java同步工具包中的java.util.concurrent.Future类的对象来表示异步操作的结果，另外一种是在执行操作时传入一个java.nio.channels.CompletionHandler接口的实现对象作为操作完成时的回调方法。这两种使用方法的区别只在于调用者通过何种方式来使用异步操作的结果。在Future类的对象时，要求调用者在合适的时机显式的通过Future类的对象的get方法来得到实际的操作结果；而在使用CompletionHandler接口时，实际的调用结果作为回调方法的参数来给出

```Java
// 向异步文件通道中写入数据的示例
public void asyncWrite () throws IOException, InterruptedException, ExecutionException {
    AsynchronousFileChannel channel = AsynchronousFileChannel.open(Paths.get(""),
            StandardOpenOption.CREATE, StandardOpenOption.WRITE);
    ByteBuffer buffer = ByteBuffer.allocate(32 * 1024 * 1024);
    Future<Integer> result = channel.write(buffer, 0);
    // 其他操作
    Integer len = result.get();
}

// 异步套接字通道的使用示例
public void startAsyncSimpleServer () throws IOException {
    // 一个异步通道的分组，每一个分组都有一个线程池与之关联，处理I/O事件
    AsynchronousChannelGroup group = AsynchronousChannelGroup.withFixedThreadPool(10, Executors.defaultThreadFactory());
    final AsynchronousServerSocketChannel serverChannel = AsynchronousServerSocketChannel.open(group).bind(new InetSocketAddress(10080));
    
    serverChannel.accept(null, new CompletionHandler<AsynchronousSocketChannel, Void>() {

        @Override
        public void completed(AsynchronousSocketChannel clientChannel, Void attachment) {
            serverChannel.accept(null, this);
            // 使用 clientChannel
        }

        @Override
        public void failed(Throwable exc, Void attachment) {
            // 错误处理..
        }
    });
}
```

### 套接字通道绑定与配置

NIO.2中新增的接口java.nio.channels.NetworkChannel，所有与套接字相关的通道的接口和实现类都继承或实现了NetworkChannel接口，他是连接网络套接字的通道的抽象表示，提供了套接字通道的绑定与配置功能

### IP组播通道

通过IP协议的组播支持可以将数据报文传输给属于同一分组的多个主机，当不同主机上的程序都需要接收相同的数据报文时，使用IP组播是最自然的方式，每一条组播消息都会被属于特定分组的所有主机接收到。

NIO.2中新增了java.nio.channels.MulticastChannel接口来表示支持IP组播的网络通道，调用MulticastChannel接口的join方法可以使当前通道加入到由参数指定的组播分组中，可以接收发送给该分组的消息。调用join方法的返回值是java.nio.channels.MembershipKey类的对象，表示该通道在组播分组中的成员身份。

-   在网络中有一个主机定时向特定组播广播当前的时间
    -   books.java70814.s3.TimeServer
    -   books.java70814.s3.TimeClient


----

##  使用案例

开发一个简单的基于文件系统中静态文件的HTTP服务器

基本的实现方式是把HTTP请求中的路径映射为文件系统中对应文件的路径，再把文件的内容作为HTTP请求的响应。

-   基于文件系统中静态文件的HTTP服务器：books.java70814.s3.StaticFileHttpServer

----