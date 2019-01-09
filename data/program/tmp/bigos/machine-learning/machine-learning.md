#   机器学习

##  概念

分析数据，找到规律

在已知的样本数据中寻找数据的规律，在未知的数据中找数据的关系

统计学习方法，是概率论与统计学的范畴；

计算机利用已有的数据(经验)，得出了某种模型(规律)，并利用此模型预测未来(结果)的一种方法。

机器学习严格来说与数据挖掘不是对等概念，仍属于数据挖掘范畴，只不过更多的基于大数据理念出发，直接在数据全集中进行分析，故而有"学习"一说

机器学习按照学习方式的维度划分，可以分为监督学习（输入数据有一个明确的标识或结果）、无监督学习、半监督学习、强化学习。当然，深度学习也包括有监督深度学习和无监督深度学习。

machine learning，是计算机科学和统计学的交叉学科，基本目标是学习一个x->y的函数（映射），来做分类或者回归的工作。之所以经常和数据挖掘合在一起讲是因为现在好多数据挖掘的工作是通过机器学习提供的算法工具实现的，例如广告的ctr预估，PB级别的点击日志在通过典型的机器学习流程可以得到一个预估模型，从而提高互联网广告的点击率和回报率；个性化推荐，还是通过机器学习的一些算法分析平台上的各种购买，浏览和收藏日志，得到一个推荐模型，来预测你喜欢的商品。


-   [GitHub](https://github.com/collections/machine-learning)
-   教程
    -   [pytorch-tutorial](https://github.com/yunjey/pytorch-tutorial)
    -   [cheatsheets-ai](https://github.com/kailashahirwar/cheatsheets-ai)
    -   [awesome-datascience](https://github.com/bulutyazilim/awesome-datascience)
    -   [lectures](https://github.com/oxford-cs-deepnlp-2017/lectures)
    -   [机器学习资源](https://github.com/allmachinelearning/MachineLearning)
    -   [machine-learning-yearning](https://github.com/xiaqunfeng/machine-learning-yearning)
    -   [机器学习&深度学习资料](https://github.com/ty4z2008/Qix)
    -   [100-Days-Of-ML-Code](https://github.com/Avik-Jain/100-Days-Of-ML-Code)
-   机器学习
    -   [斯坦福大学公开课 ：机器学习课程](http://open.163.com/special/opencourse/machinelearning.html)
    -   [吴恩达机器学习](https://github.com/fengdu78)
    -   [CycleGAN](https://github.com/junyanz/CycleGAN)
    -   [seq2seq](https://github.com/google/seq2seq)
    -   [pix2code](https://github.com/tonybeltramelli/pix2code)
    -   [deep-photo-styletransfer](https://github.com/luanfujun/deep-photo-styletransfer)
    -   [visdom](https://github.com/facebookresearch/visdom)
    -   [中文自然语言处理](https://github.com/FudanNLP/fnlp)
    -   [paddle-mobile](https://github.com/PaddlePaddle/paddle-mobile)
    -   [openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
    -   [DeepSpeech](https://github.com/mozilla/DeepSpeech)
    -   [turicreate](https://github.com/apple/turicreate)
    -   [tensorflow](https://github.com/tensorflow/tensorflow)
    -   [Machine-Learning-Tutorials](https://github.com/ujjwalkarn/Machine-Learning-Tutorials)
    -   [机器学习要领](https://github.com/AlbertHG/Machine-Learning-Yearning-Chinese-ver)
    -   [如何构建机器学习项目](https://github.com/yucc2018/machine-learning-yearning)
    -   [MLonCode](https://github.com/src-d/awesome-machine-learning-on-source-code)
    -   [medical-data](https://github.com/beamandrew/medical-data)
    -   [FiveThirtyEight文章和图形背后的数据和代码](https://github.com/fivethirtyeight/data)
    -   [计算机视觉](https://github.com/jbhuang0604/awesome-computer-vision)
    -   [Oxford Deep NLP 2017课程](https://github.com/oxford-cs-deepnlp-2017/lectures)
    -   [`Kivy Developers From China，有很多译文`](https://github.com/Kivy-CN)

##  模式
-   监督式学习
    -   简述
        -   从样本数据中学习规律判断非样本数据
        -   如：从一堆`狗`的图片找到`狗`的规律，在其他图片中判断是否是`狗`
    -   算法
        -   决策树：自动化房贷、风控
        -   朴素贝叶斯分类：垃圾邮件、新闻分类
        -   最小二乘法：算是一种线性回归
        -   逻辑回归：一种强大的统计学方法，用于信用评分、计算营销活动的成功率
        -   支持向量机：基于图像的性别检测、图像分类
        -   集成方法：构建一组分类器，根据他们的预测结果进行加权投票来对新的数据点进行分类
-   非监督式学习
    -   简述
        -   找到数据之间的共性
        -   分类，关联关系
    -   算法
        -   聚类算法：给数据分类
        -   主成分分析(PCA)：压缩、简化数据，便于学习和可视化
        -   奇异值分解(SVD)：PCA是SVD的一个简单应用
        -   独立成分分析(ICA)：一种统计技术，揭示随机变量、测量值或信号集中的隐藏因素

----

##  流程
-   方法论
    -   要找到数据中的规律，需要找到数据中的特征点
    -   把特征点抽象成数学中的向量，也就是所谓的坐标轴，一个复杂的学习可能会有成十上百的坐标轴
    -   抽象成数学向量后，就可以通过某种数据公式来表达这类数据，这就是数据建模
-   数据搅拌机
    -   把数据中的特征点抽象数学中的向量
    -   每个向量一个权重
    -   写个算法来找各个向量的权重是什么

----

##  数学
-   高数
-   线性代数
-   概率论
-   数据建模

----

##  资料
-   视频
    -   吴恩达
-   书籍
    -   机器学习(汤姆*米切尔)
    -   机器学习(周志华)
    -   深度学习