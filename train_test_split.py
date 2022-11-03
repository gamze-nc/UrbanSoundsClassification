import random

x_train = []
y_train = []
x_test = []
y_test = []
x_val = []
y_val = []

def train_test(data):

  global x_train, x_test, x_val, y_test, y_train, y_val

  random.shuffle(data)

  for i in range(len(data)):

    if i<=len(data)*0.8:
      # data %80 --> train
      x_train.append(data[i][0])
      y_train.append(data[i][1])

    elif i>=len(data)*0.8 and i<=len(data)*0.9:
      # data %10 --> validation
      x_val.append(data[i][0])
      y_val.append(data[i][1])

    else:
      # data %10 --> test
      x_test.append(data[i][0])
      y_test.append(data[i][1])
      
train_test(dataset)