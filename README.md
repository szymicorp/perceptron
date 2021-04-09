# Perceptron classifier with 3D plot live visualization in Python

<img src="Assets/perceptron-demo.gif" width="757" height="862"/>

## Mathematical representation of neuron

**Neuron** receives and analysis data from [dendrites](https://en.wikipedia.org/wiki/Dendrite). It performs simple biological tasks to support thinking processes in brain. [Perceptron](https://en.wikipedia.org/wiki/Perceptron) is artificial representation of it. To understand the artificial concept, image below shows real neuron described by math.

<dl>
  <dt>X</dt>
  <dd>1-dimensional matrix of input values</dd>
  <dt>W</dt>
  <dd>1-dimensional matrix of weights</dd>
  <dt>Θ</dt>
  <dd>bias</dd>
</dl>

Now, we know how **perceptron** is build. Next thing we need is formula to generate output. Output is discrete and unipolar -> {0,1}.
Output will be produced by this formula:<br />
![equation](https://latex.codecogs.com/png.image?\dpi{110}%20W^{T}X\geqslant%20\theta)

To understand it well, let's simplify it. We can now set ![equation](https://latex.codecogs.com/png.image?\dpi{110}%20\theta%20=%200) and ![equation](https://latex.codecogs.com/png.image?\dpi{110}%20W=\begin{bmatrix}3%20\\%200\end{bmatrix}) . Now, formula will look like this:<br />
![equation](https://latex.codecogs.com/png.image?\dpi{110}%20\begin{bmatrix}3\\0\end{bmatrix}^T%20*%20X\geqslant%200)<br />
From matrix multiplication rules we know that ![equation](https://latex.codecogs.com/png.image?\dpi{110}%20W^TX) will return integer. Whether this integer is less then 0 or more, we can classify this data sample to class 0 or 1.<br />
Changing value of Θ will move our red [hyperplane](https://en.wikipedia.org/wiki/Hyperplane) from (0,0). This will help to divide data into classes if we needed so.

## Perceptron learning process

As we already know, **X** represents inputs - they change all the time. **W** and **Θ** are internal components of perceptron. So, learning process will be based on changing values of them. **W** will point where one class is and will define angle of **hyperplane**, **Θ** it's distance from (0,0).<br />
When we train our perceptron, we use [supervised training](https://en.wikipedia.org/wiki/Supervised_learning), which means we know right answers for data we provide to perceptron. If guess of perceptron is right, we continue with training, but when it is wrong, we want it to calibrate **W** and **Θ** values.<br />
>**W** training formula:<br /><br />
![equation](https://latex.codecogs.com/png.image?\dpi{110}%20W^\prime=W+(d-y)\alpha%20X)
<dl>
  <dt>W'</dt>
  <dd>new vector</dd>
  <dt>W</dt>
  <dd>old vector</dd>
  <dt>d</dt>
  <dd>desired output {0,1}</dd>
  <dt>y</dt>
  <dd>perceptron output {0,1}</dd>
  <dt>alpha</dt>
  <dd>training factor</dd>
  <dt>X</dt>
  <dd>vector of inputs</dd>
</dl>

> **Θ** training formula:<br /><br />
![equation](https://latex.codecogs.com/png.image?\dpi{110}%20\theta^\prime=\theta+(d-y)\alpha)

When perceptron training process is done, on 3d scatter plot it should look like this:

## Program workflow
### 1. Input files
Provide path to **train set** and **test set**. Both should:
  * be *.csv* files
  * contain same number of columns in the same order
  * have last column containing class

Load data.
If files were read correctly, input fields should appear green.
### 2. Training and testing
When data has been loaded properly, next step is to set value of **alpha**. Then, you can start process of training perceptron with **train set** data. This is all done by clicking "Train perceptron" button. 3D scatter plots should appear. They represent every 3d projection of all data dimensions. For example, if your data has 4 numeric columns, ![equation](https://latex.codecogs.com/png.image?\dpi{110}%20\binom{4}{3}) plots should appear.<br />
On these 3D plots, you can observe how **W** plane is changing due to learning process (including **Θ**). Currently computed data sample is highlighted on red.<br />
When learning process is done, you can test accuracy of trained perceptron with **test set** data. Scores of tests will be shown afterwards.
### 3. Classify data
If you are happy with scores of perceptron classification, here you can classify unclassified samples. Csv format expected.
