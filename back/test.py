from json import load
import pickle
from keras.datasets import mnist
import PIL.Image
import numpy as np

model = pickle.load(open('./models/rfc_model_digits', 'rb'))
image = np.array(PIL.Image.open(
    "/home/administrateur/dev/tuto_ml_dl/dataset/im1.png"))
image = image.reshape(28*28)

print(model.predict(np.array([image])))
