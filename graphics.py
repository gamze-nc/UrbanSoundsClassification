import seaborn as sns
import matplotlib.pyplot as plt


def graphics(model):

  plt.figure(figsize=(15,5))
  plt.subplot(1,2,1)
  sns.regplot(list(range(1)),model.history.history["accuracy"], label="accuracy")
  plt.ylabel("Accuracy")
  plt.xlabel("Epochs")
  plt.legend()
  plt.subplot(1,2,2)
  sns.regplot(list(range(1)),model.history.history["loss"], label="loss")
  plt.legend()
  plt.xlabel("Epochs")
  plt.ylabel("Loss")
  
  
  
graphics(model)