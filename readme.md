# Image Classifiers - Various Concepts

#### [Visit the App](https://imageclassifiers.herokuapp.com/)

<br>

## PROJECT OVERVIEW

Flask RESTful Application hosting three different approaches to image recognition APIs. First, Image Content Classifier, takes image url path as an input. Second model works with .jpg image upload. 
Third one, Digit Recognition, receives input via js. 

<br>

![1](https://user-images.githubusercontent.com/26208598/49669682-043e6a00-fa5a-11e8-8fe6-ea8d3846f829.PNG)


<br>


### Image Content Classification with Tensorflow

Application of Google-made image content classifier built with Tensorflow. Training this kind of model in home conditions would took an eternity, that's why it was downloaded from 
[official website](https://www.tensorflow.org/tutorials/images/image_recognition). Model accuracy is amazing.

<br>

![11](https://user-images.githubusercontent.com/26208598/49669686-06082d80-fa5a-11e8-95d5-65dd79adc156.PNG)


<br>


### Cat vs Dog Classifier with Keras & SK

Image classifier trained to distinct between cats and dogs images. Convolutional Neural Network was built with Keras & Tensorflow(GPU).

[Kaggle Dataset](https://www.kaggle.com/c/dogs-vs-cats/data)


#### CONVOLUTIONAL NEURAL NETWORK CHARACTERISTICS

1. Image Input Shape - 128,128,3, activation - relu
2. Three additional Convolutional Layers (batch size - respectively 32,64,128, dropout rate - 0.25,0.2,0.3)
3. Units in hidden layer - 128
4. Compiler - optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']
5. Acc - 89% Loss - 25% (approx 30min/epoch on GPU)
6. CNN Code Location: deep_learning/ConvolutionalNeuralNetwork.py

<br>

![22](https://user-images.githubusercontent.com/26208598/49669689-07395a80-fa5a-11e8-8df3-d13eb7c68153.PNG)


<br>


### Digit Recognition with Keras & Ajax.js

Hand-Written Digit Recognition based on MNIST Dataset. Convolutional Neural Network was built with Keras & Tensorflow(GPU). 
Heroku-hosted web application was built with Flask framework, Ajax & FileSaver. 

[MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

<br>

![33](https://user-images.githubusercontent.com/26208598/49669690-09031e00-fa5a-11e8-9d89-1d9e32faefb7.PNG)


<br>



## TOOLS, MODULES & TECHNIQUES:

##### Web Development:
Flask | Flask_Restful | Ajax | FileSaver.js | HTML | CSS | Bootstrap | Materialize

##### Python – CNN:
Keras | Tensorflow | Scipy | Numpy | h5py | Scikit-Image

<br>


## CREDITS & INSPIRATIONS

##### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ<br>
<br>
<br>

##### Thank you,

Lukasz Malucha