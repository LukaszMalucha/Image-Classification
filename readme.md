# Image Classifiers - Various Concepts

#### [Visit the App](http://www.unflasked.com/)

<br>

![1](https://user-images.githubusercontent.com/26208598/56462832-c49d6c80-63c1-11e9-9108-fad52b36eb03.JPG)

<br>

## PROJECT OVERVIEW

Flask RESTful Application hosting three different approaches to image recognition APIs. First, Image Content Classifier, takes image url path as an input. Second model works with .jpg image upload. 
Third one, Digit Recognition, receives input via js. 

<br>


### Image Content Classification with Tensorflow

Application of Google-made image content classifier built with Tensorflow. Training this kind of model in home conditions would took an eternity, that's why it was downloaded from 
[official website](https://www.tensorflow.org/tutorials/images/image_recognition). Model accuracy is amazing.

*(Heroku-hosted app works only with small photos with white background due to limited memory, works perfect on local hosts)*

<br>

![2](https://user-images.githubusercontent.com/26208598/56462833-c49d6c80-63c1-11e9-97d0-5aac4af81aea.JPG)


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

![3](https://user-images.githubusercontent.com/26208598/56462834-c49d6c80-63c1-11e9-9234-6c322ab1fb30.JPG)


<br>


### Digit Recognition with Keras & Ajax.js

Hand-Written Digit Recognition based on MNIST Dataset. Convolutional Neural Network was built with Keras & Tensorflow(GPU). 
Heroku-hosted web application was built with Flask framework, Ajax & FileSaver. 

[MNIST Dataset](http://yann.lecun.com/exdb/mnist/)

<br>

![1](https://user-images.githubusercontent.com/26208598/56584552-dd7d6c00-65d3-11e9-9de9-378c02bac71f.JPG)


<br>


### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/Image-Classification.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Image-Classification)

### Test Files:

##### /tests



## TOOLS, MODULES & TECHNIQUES:

##### Web Development:
Flask | Flask_Restful | Ajax | FileSaver.js | HTML | CSS | Bootstrap | Materialize | Docker 

##### Python – CNN:
Keras | Tensorflow | Scipy | Numpy | h5py | Scikit-Image

##### Database Development:
SQLite

##### Testing
selenium | unittest

<br>


## CREDITS & INSPIRATIONS

##### Error 404 template:

Robin Selmer:

https://codepen.io/robinselmer/pen/vJjbOZ<br>
<br>
<br>

##### Thank you,

Lukasz Malucha
