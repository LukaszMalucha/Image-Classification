# -*- coding: utf-8 -*-


## Model
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

## Dataset
from keras.datasets import mnist





######################################################  DATA PREPROCESSING ##################################################

## image dimensions (28x28px)
img_rows, img_cols = 28, 28

## Train Test Split
(x_train, y_train), (x_test, y_test) = mnist.load_data()

## Avoinding "only channel first is supported" error
if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)


## Reshape to float32
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

## Number of classes
num_classes = 10  ## 0-9 digits

## Convert to 0-1 class matrix
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)



###########################################################  BUILD MODEL ###################################################


model = Sequential()

## Convolutional layers
model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=input_shape))

model.add(Conv2D(64, (3, 3), activation='relu'))

model.add(MaxPooling2D(pool_size=(2, 2)))


## Dropout #1
model.add(Dropout(0.25))

# Flattening
model.add(Flatten())

# Fully connected layer
model.add(Dense(128, activation='relu'))

# Dropout #2
model.add(Dropout(0.5))

# Softmax to get probabilities
model.add(Dense(num_classes, activation='softmax'))

# Compile with AdaDelta and categorical crossentropy (for multiple classes)
model.compile(loss=keras.losses.categorical_crossentropy, 
              optimizer=keras.optimizers.Adadelta(), metrics=['accuracy'])

## Dataset dimensions
batch_size = 128
epochs = 15

# Train Dataset
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))


# Score
score = model.evaluate(x_test, y_test, verbose=0)
print('Loss:', score[0])
print('Acc:', score[1])

# Model serialize
model_json = model.to_json()
with open("digit_model.json", "w") as json_file:
    json_file.write(model_json)
    
# Save weights
model.save_weights("digit_model.h5")
print("Saved model to disk")