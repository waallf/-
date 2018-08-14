现在所有的网络都是通过LSTM 一个词一个词进行预测，怎么样才能做到先将整个语句的框架给出（可以使用scene graph）。然后将这些短语合成一个句子（感觉可以用gan做）
# 怎么在预测单词的时候将 scene graph预测的目标间的关系当作约束加进去
先产生场景图，然后根据短语节点的特征[论文](./Scene Graph Generation from object,Phrases and Region Captions.md)
然后再将图像特征，短语特征进行融合 产生图像描述
# 将产生的scene graph 对应的图像特征送入LSTM（ feature 与他们之间的关系），那么LSTM输出的该是什么，



# ==结构图==

![1534142404139](TODO.assets/1534142404139.png)

[参考代码](https://github.com/chapternewscu/image-captioning-with-semantic-attention) 

F：

$x_{t1} = W^{x,Y}(Ey_{t-1}+diag(w^{x,A})\sum_{i}\alpha^{i}_{t}Ey^{i})$       此公示具体计算方法见 Image Captioning with Semantic Attention 中的Input attention model

$x_{t2} = A(h_{t-1},v,\sum_{i}\alpha_{t}^{i}Ey^{i})$    ==暂时没有想到A的实现方法==

* 另一种$x_{t2}$ 

  ​	**使用GT训练**，不需要使用目标检测网络，用给定的目标检测的标签来实现短语与对应的目标特征的匹配，然后利用上面的方法，每个短语都获得了一个分数，这个短语相对应的object特征也是这个分数，然后和上面方法一样，每个特征乘以相应的分数再相加，就形成了Image attention 

  ​	**使用目标检测网络**，和上面一样，就是使用目标检测网络来找出目标，然后再生成它们之间的关系，然后再产生Image attention.