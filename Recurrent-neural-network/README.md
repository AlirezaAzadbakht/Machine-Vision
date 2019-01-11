 # Recurrent Neural Networks (RNN)

![alt text](https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/C2nhDdwW8AIzf07.jpg)

In this page we share abstract of our study about Recurrent Neural Networks (RNN) and its applications

# Introduction

 ### what is RNN ?

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
  _ An unrolled recurrent neural network. _
  </p>
  <br>

  ### How does RNN work ?

  
  <p align="center">
    <img src="https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/rnn.jpg" >
      <br>_ A recurrent neural network and the unfolding in time of the computation involved in its forward computation _
  </p>
  <br>
  The above diagram shows a RNN being unrolled (or unfolded) into a full network. 
  By unrolling we simply mean that we write out the network for the complete sequence.
   For example, if the sequence we care about is a sentence of 5 words, the network would be unrolled into a 5-layer neural network, one layer for each word. 
   The formulas that govern the computation happening in a RNN are as follows:
  <br><br>
  - x_t is the input at time step t. For example, x_1 could be a one-hot vector corresponding to the second word of a sentence.
  <br>
  - s_t is the hidden state at time step t. It’s the “memory” of the network. s_t is calculated based on the previous hidden state and the input at the current step: s_t=f(Ux_t + Ws_{t-1}). 
  The function f usually is a nonlinearity such as tanh or ReLU.  s_{-1}, which is required to calculate the first hidden state, is typically initialized to all zeroes.
  <br>
  - o_t is the output at step t. For example, if we wanted to predict the next word in a sentence it would be a vector of probabilities across our vocabulary. o_t = \mathrm{softmax}(Vs_t).
   
  **Note**:  Unlike a traditional deep neural network, which uses different parameters at each layer, a RNN shares the same parameters (U, V, W above) across all steps. 
  This reflects the fact that we are performing the same task at each step, just with different inputs. 
  This greatly reduces the total number of parameters we need to learn.


  **Types Of RNN** 

