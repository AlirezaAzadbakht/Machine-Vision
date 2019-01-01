 # Recurrent Neural Networks (RNN)

![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/C2nhDdwW8AIzf07.jpg)

In this page we share abstract of our study about Recurrent Neural Networks (RNN) and its applications

# Introduction

 ### what are RNN ?

 In a traditional neural network we assume that all inputs (and outputs) are independent of each other.
  But for many tasks that’s a very bad idea. If you want to predict the next word in a sentence you better know which words came before it. 
  RNNs are called recurrent because they perform the same task for every element of a sequence, with the output being depended on the previous computations. 
  Another way to think about RNNs is that they have a “memory” which captures information about what has been calculated so far. 
  They are networks with loops in them, allowing information to persist.
  <br>
   ![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/RNN-rolled-loop.png)
   <br>
   _Recurrent Neural Networks have loops._
  
  In theory RNNs can make use of information in arbitrarily long sequences, but in practice they are limited to looking back only a few steps (more on this later). 

 




  <br>Here is what a typical RNN looks like: 
  <br><br>
 ![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/rnn.jpg)
  _A recurrent neural network and the unfolding in time of the computation involved in its forward computation_
  
  