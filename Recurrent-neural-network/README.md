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
  Recurrent Neural Networks have loops.
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
    An unrolled recurrent neural network.
  </p>
  <br>

  ### How does RNN work ?

  
  <p align="center">
    <img src="https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/rnn.jpg" >
      <br>A recurrent neural network and the unfolding in time of the computation involved in its forward computation
  </p>
  <br>
  The above diagram shows a RNN being unrolled (or unfolded) into a full network. 
  By unrolling we simply mean that we write out the network for the complete sequence.
   For example, if the sequence we care about is a sentence of 5 words, the network would be unrolled into a 5-layer neural network, one layer for each word. 
   The formulas that govern the computation happening in a RNN are as follows:
  
  
  - x_t is the input at time step t. For example, x_1 could be a one-hot vector corresponding to the second word of a sentence.
  
  - s_t is the hidden state at time step t. It’s the “memory” of the network. s_t is calculated based on the previous hidden state and the input at the current step: s_t=f(Ux_t + Ws_{t-1}). 
  The function f usually is a nonlinearity such as tanh or ReLU.  s_{-1}, which is required to calculate the first hidden state, is typically initialized to all zeroes.
 
  - o_t is the output at step t. For example, if we wanted to predict the next word in a sentence it would be a vector of probabilities across our vocabulary. o_t = \mathrm{softmax}(Vs_t).
   
  **Note**:  Unlike a traditional deep neural network, which uses different parameters at each layer, a RNN shares the same parameters (U, V, W above) across all steps. 
  This reflects the fact that we are performing the same task at each step, just with different inputs. 
  This greatly reduces the total number of parameters we need to learn.


  **Types Of RNN** 
  
  
   <p align="center">
    <img src="https://raw.githubusercontent.com/AlirezaAzadbakht/Machine-Vision/master/Recurrent-neural-network/images/typeOfRNN.png">
    <br>
    types of RNN

  </p>
  
  Each rectangle is a vector and arrows represent functions (e.g. matrix multiply).
   Input vectors are in red, output vectors are in blue and green vectors hold the RNN’s state (more on this soon). 
   From left to right:
   
   1.   without RNN , from fixed size-input to fixed-sized output (e.g. image classification) . 
   2.   Sequence output (e.g. image captioning takes an image and outputs a sentence of words).
   3.   Sequence input (e.g. sentiment analysis where a given sentence is classified as expressing positive or negative sentiment).
   4.   Sequence input and sequence output (e.g. Machine Translation: an RNN reads a sentence in English and then outputs a sentence in French).   
   5.   Synced sequence input and output (e.g. video classification where we wish to label each frame of the video).
   
   ### what can RNN do ?
   
   **Language Modelling and Prediction:**
   
   In this method, the likelihood of a word in a sentence is considered. The probability of the output of a particular time-step is used to sample the words in the next iteration(memory). 
   In Language Modelling, input is usually a sequence of words from the data and output will be a sequence of predicted word by the model.
   
   **Speech Recognition:**
   
   A set of inputs containing phoneme(acoustic signals) from an audio is used as an input. 
   This network will compute the phonemes and produce a phonetic segments with the likelihood of output.
   
   **Machine Translation:**
   
   In Machine Translation, the input is will be the source language(e.g. Hindi) and the output will be in the target language(e.g. English). 
   The main difference between Machine Translation and Language modelling is that the output starts only after the complete input has been fed into the network.
   
   **Image recognition and characterization:**
   
   
  Recurrent Neural Network along with a ConvNet work together to recognize an image and give a description about it if it is unnamed. This combination of neural network works in a beautiful and it produces fascinating results.
  Here is a visual description about how it goes on doing this, the combined model even aligns the generated words with features found in the images.
  
  
 ## SPEECH RECOGNITION WITH DEEP RECURRENT NEURAL NETWORKS
 
 Neural networks have a long history in speech recognition,usually in combination with hidden Markov models.
 Instead of combining RNNs with HMMs, it is possible to train RNNs ‘end-to-end’ for speech recognition.
This approach exploits the larger state-space and richer dynamics of RNNs compared to HMMs, and avoids the problem of using potentially incorrect alignments as training targets.

### RNN Network

Given an input x = (x<sub>1</sub>)
  
 

