现在所有的网络都是通过LSTM 一个词一个词进行预测，怎么样才能做到先将整个语句的框架给出（可以使用scene graph）。然后将
这些短语合成一个句子（感觉可以用gan做）
# Scene Graph 产生
先产生场景图，然后根据短语节点的特征[论文](./Scene Graph Generation from object,Phrases and Region Captions.md)
然后再将图像特征，短语特征进行融合 产生图像描述
# 将产生的scene graph 对应的图像特征送入LSTM，（ feature 与他们之间的关系），那么LSTM输出的该是什么，