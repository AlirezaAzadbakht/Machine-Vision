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
  <br><br>
  <p align="center">
   <img src="https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/RNN-rolled-loop.png"  width="150" >
 _Recurrent Neural Networks have loops._
  </p>
   <br>
  
   
  
  These loops make recurrent neural networks seem kind of mysterious
  . However, if you think a bit more, it turns out that they aren’t all that different than a normal neural network. 
  A recurrent neural network can be thought of as multiple copies of the same network, each passing a message to a successor. 
  Consider what happens if we unroll the loop:
  <br>
  (In theory RNNs can make use of information in arbitrarily long sequences, but in practice they are limited to looking back only a few steps (more on this later). )
  <br><br>
  <p align="center">
    <img src="https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/RNN-unrolled.png" >
  _An unrolled recurrent neural network._
  </p>
  <br>

 



  <br><br>
 ![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/rnn.jpg)
  _A recurrent neural network and the unfolding in time of the computation involved in its forward computation_
  
  