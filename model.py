import pylab as pl
import tensorflow as tf
from tensorflow import keras
from keras import backend as K
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras import layers, activations


model = Sequential()

model.add(layers.Conv2D(filters=4, activation="relu", kernel_size=(5,5), input_shape=(28,28,1)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(filters=8, activation="relu", kernel_size=(3,3)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(filters=16, activation="relu", kernel_size=(2,2)))
model.add(layers.MaxPooling2D(2,2))
model.add(layers.Conv2D(filters=32, activation="relu", kernel_size=(2,2)))

model.add(layers.Flatten())

model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(128, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))


#model.summary()


optimizer = tf.keras.optimizers.RMSprop(learning_rate=0.001)
loss = tf.keras.losses.CategoricalCrossentropy()

model.compile(optimizer=optimizer, loss=loss, metrics=["accuracy"])

result = model.fit(x_train, y_train, epochs=100, verbose=1, validation_data=(x_val, y_val), batch_size=128)


#result.history

model.evaluate(x_test)
