## 在产生句子这块和seqGAN完全一样。。。。。

使用conditional GAN产生句子，不像其他的方法，仅仅是为了训练一个交叉熵的相似度，这样的训练方法导致训练出来的句子非常相似。

等到全部预测完句子（相当于把所有动作都做完，才进行奖励与惩罚）再进行reward会导致梯度消失和收敛速度慢，所以使用蒙特卡洛搜索将整个句子补全，然后进行评价。

#### 结构图

![jiegoutu](.\towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets\jiegoutu.PNG)

==目标函数：==

与所有的GAN目标函数相似

![mubiaohanshu](towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets/mubiaohanshu.PNG) 

S表示GT句子，$P_I$表示 I提供的描述集合

### G：生成器

把预测下一个单词当作是一个行为，$\pi_{\theta}$表示这个行为选择器，根据之前状态，随机噪声$Z$，图像特征来选择下一个行为：$\pi_{\theta}(w_{t}|(f_{I},Z,S_{1:t-1}))$（由LSTM实现）。一步一步预测，直到预测到结束标志e，或者达到最大长度。

由于只能在得到整个预测的句子时候才能进行reward，但是这样会导致梯度消失和收敛速度慢。所以采用蒙特卡洛搜索将整个句子补全（预测到结束标志e）。

所以生成器的训练目标是最大化：

![shengchegnqimubiao](towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets/shengchegnqimubiao.PNG)

倒数为：

![daoshu](towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets/daoshu.PNG)

$V$是词汇表，$T_{max}$是预测的最大长度，$\theta^{'}$是在一开始更新生成器时$\theta$的复制，在此过程中，生成器将多次更新，。每次更新都会从新复制一遍参数$\theta^{'}$

### D：鉴别器

#### reward指标:

![gongshi2](towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets/gongshi2.PNG)

$f(I,)$将图像 $I$ 编码为向量。

$h(S,)$ 通过LSTM将单词编码为与$f(I,)$维度相同的向量

$< >$点乘运算

$\sigma$将值固定到[0,1]

#### 训练鉴别器

![jianbieqisunshi](towards_diverse_and_natural_image_descriptions_via_a_conditional_GAN.assets/jianbieqisunshi.PNG)

通过三个集合来计算鉴别器的损失：

第一个$S_{I}$表示GT,

第二个$S_{G}$表示产生器产生的，将会训练鉴别器鉴别出哪个是产生的，哪个是GT

第三个$S_{\I}$表示其他图像的描述，用来分辨鉴别器是鉴别句子是否与图像内容相关

