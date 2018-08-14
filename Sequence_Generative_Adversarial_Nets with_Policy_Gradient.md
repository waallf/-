# Sequence_Generative_Adversarial_Nets with_Policy_Gradient

[代码](https://github.com/LantaoYu/SeqGAN)

[论文](./papper/Sequence_Generative_Adversarial_Nets with_Policy_Gradient.pdf)

[参考](https://www.jianshu.com/p/b8c3d2a42ba7)

* 使用GAN来产生句子，由于句子的不连续性，用增强学习来更新网络

![整体结构](.\images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/整体结构.png)

* 使用GAN来产生句子存在两个问题：

  * 预测的句子不连续，不能利用鉴别器返回的梯度来更新参数（由于梯度这种微小的变化，在有限的字典空间中没有相应的反映）  												--使用增强学习解决

  * 鉴别器只能对整个句子进行评价，因为它无法平衡部分句子的得分与未来的得。

    ​																	--使用蒙特卡洛树搜索

### 整体思路

如上图（左）所示，仍然是对抗的思想，真实数据加上G的生成数据来训练D。但是从前边**背景**章节所述的内容中，我们可以知道G的离散输出，让D很难回传一个梯度用来更新G，因此需要做一些改变，看上图（右），paper中将policy network当做G，已经存在的红色圆点称为现在的状态（state），要生成的下一个红色圆点称作动作（action），因为D需要对一个完整的序列评分，所以就是用**MCTS**（蒙特卡洛树搜索）将每一个动作的各种可能性补全，D对这些完整的序列产生reward，回传给G，通过增强学习更新G。这样就是用Reinforcement learning的方式，训练出一个可以产生下一个最优的action的生成网络。



### 主要内容

生成器的目标是生成sequence来最大化reward的期望

![gongshi1](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongsgi1.PNG) 

 

$G~\theta$代表生成器，$Q_{G_{\theta }}^{D_{\psi }}$表示action-value function，用于评估整个句子的得分。

我们可以认为：G 生成一个y1的概率乘以这个y1的Q值，再求和，这就是生成模型想要最大化的函数

#### 求Q值

论文中使用的是REINFORCE algorithm ，并把Q值看作鉴别器的返回值

![公示2](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi2.PNG)



因为不完整的轨迹产生的reward没有意义，因此在$y_1$,$t_{t-1}$的情况下产生的$y_t$的Q值并不能直接计算，除非预测完了最后一个，论文中使用蒙特卡洛搜素（相当于“随意”）句子补全。既然是补全，就会有多种补全的情况。将$y_t$后的内容全部补全后的所有可能句子都计算reward，然后求平均。

 ![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi3.PNG)

$MC^{G~{\beta}}(Y~{1:t};N)$表示从t开始执行蒙特卡洛搜索，执行N次

 然后用下面的方式训练D

![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi4.PNG)

D训练了一轮或者多轮（因为GAN的训练一直是个难题，找好G和D的训练轮数比例是关键）之后，就得到了一个更优秀的D，此时要用D去更新G。G的更新可以看做是梯度下降。 

![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi5.PNG)

单个时间的梯度为：

![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi6.PNG)

所有时间的梯度为：

![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/gongshi7.PNG)

#### 算法流程图

![](./images/Sequence_Generative_Adversarial_Nets with_Policy_Gradient/suanfaliuchengtu.PNG)