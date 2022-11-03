import numpy as np
import os
import cv2
import tensorflow as tf
from tensorflow import keras
from keras.layers import Rescaling


dataset = []

def prepro():
  global data
  scale = tf.keras.layers.Rescaling(scale=1./255)
  for j in range(10):
    os.chdir(f"/content/drive/MyDrive/global ai hub/spectrograms/{j}")
    liste = os.listdir()

    for i in range(len(liste)):
      path = f"/content/drive/MyDrive/global ai hub/spectrograms/{j}/"+liste[i]
      resim = cv2.imread(path)
      sb = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
      sb = cv2.resize(resim, (28,28))
      sb = np.array(sb)
      sb = scale(sb)
      dataset.append([sb,j]) #[görüntü, etiket]
      

prepro()


