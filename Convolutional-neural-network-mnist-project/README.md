
#  Convolutional neural network

in this project, we try to use tensorflow API to create a Convolutional neural network work with mnist dataset and get results

**The [MNIST dataset](http://yann.lecun.com/exdb/mnist/) comprises 60,000 training examples and 10,000 test examples of the handwritten digits 0–9, formatted as 28x28-pixel monochrome images.**

with the power of the tensorflow and its powerful documentations we build a Convolutional neural network as the tutorial said :
we follow the steps of tensorflow tutorial about mnist CNN 
https://www.tensorflow.org/tutorials/estimators/cnn

## Layers : 
 input layer :
to create an input layer in tensorflow 

``` python 
input_layer = tf.reshape(features["x"],  [-1,  28,  28,  1])  
```
MNIST dataset is composed of monochrome 28x28 pixel images, so the desired shape for our input layer is `[_batch_size_, 28, 28, 1]`


batch size -1 means that it should be dynamic

all the layers in tensorflow get another layer as input some features and an activation function 
all the activation function in this implementation are Relu function

now we need two convolutional layer 
1. 32 filters with kernel size of 5*5
2. 64 filters with kernel size of 5*5

 ``` python 
 conv1 = tf.layers.conv2d( inputs=input_layer, filters=32, kernel_size=[5,  5], padding="same", activation=tf.nn.relu)  
```
each convolutional layer needs a pooling layer
``` python 
pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2,  2], strides=2)  
```

our second convolutional layer :
``` python 
conv2 = tf.layers.conv2d( inputs=pool1, filters=64, kernel_size=[5,  5], padding="same", activation=tf.nn.relu)  
```
and its pooling layer of
 ``` python 
 pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2,  2], strides=2)
 ``` 

the next step we give the outputs to a dense layer of 1024 neurons and as always Relu activation function
Before we connect the layer, however, we'll flatten our feature map
``` python 
pool2_flat = tf.reshape(pool2,  [-1,  7  *  7  *  64])  
```
Each example has 7 (pool2 height) * 7 (pool2 width) * 64 (pool2 channels) features, so we want the features dimension to have a value of 7 * 7 * 64 (3136 in total). The output tensor, pool2_flat, has shape [batch_size, 3136].

now we can pass it to the dense layer 
``` python 
dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)  
```
To help improve the results of our model, we also apply dropout regularization to our dense layer
tensor easily do that with 
``` python 
dropout = tf.layers.dropout( inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)  
```
The rate argument specifies the dropout rate; here, we use 0.4, which means 40% of the elements will be randomly dropped out during training.


**The final layer** in our neural network is the logits layer, which will return the raw values for our predictions 
it will return a vector with a size of 10 for each digit

``` python 
logits = tf.layers.dense(inputs=dropout, units=10)  
```
we don't really understand the following part but what we really know is the output vector contains many numbers in it if we normal the numbers and divide them by the max we can have the probability of each number of we can just select the maximum value and return it 
``` python 
tf.argmax(input=logits, axis=1)  

tf.nn.softmax(logits, name="softmax_tensor")  
```

the rest of the code is tensorflow syntax to communicate with the rest training part 
 **our CNN model is ready :)**
## Training :
we add other parts as the tutorial said but what is really important to know 
is this part

``` python 
train_input_fn = tf.estimator.inputs.numpy_input_fn( x={"x": train_data}, y=train_labels, batch_size=100, num_epochs=None, shuffle=True)  

mnist_classifier.train( input_fn=train_input_fn, steps=20000, hooks=[logging_hook])  
```
this code train our model 20000 times 

so from here to the end we just play with the parameters to understand and get to know their job in our CNN 

## Results :















