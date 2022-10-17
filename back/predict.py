from json import load
import pickle
from io import BytesIO
from PIL import Image, ImageDraw

import numpy as np
import torch


class Inference():

    def __init__(self):
        # self.model = pickle.load(open('./models/rfc_model_digits', 'rb'))
        self.model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
        self.model.classes=[0]

    def processImg(self, image):
        image = BytesIO(image)
        # image = np.array(PIL.Image.open(image))
        # nx1, ny1 = image.shape
        # image = image.reshape(28*28)
        # self.image = np.array(image)
        self.image = Image.open(image)

    def predict(self):
        # return self.model.predict(self.image)[0]
        results = self.model(self.image)
        xmin=results.pandas().xyxy[0].xmin.values
        xmax=results.pandas().xyxy[0].xmax.values
        ymin=results.pandas().xyxy[0].ymin.values
        ymax=results.pandas().xyxy[0].ymax.values


        #-----------------------------------------#


        draw = ImageDraw.Draw(self.image, "RGBA")
        for i in range(len(xmin)):
            shape = [(xmin[i],ymin[i]), (xmax[i],ymax[i])]
            draw.rectangle(shape, fill=(200, 100, 0, 127))
            draw.rectangle(shape, outline=(0, 0, 0, 127), width=2)

        self.image.save('../front/src/components/res.png')

