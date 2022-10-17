import torch
from PIL import Image, ImageDraw

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # or yolov5n - yolov5x6, custom
model.classes=[0]

img = './rue.jpg'  # or file, Path, PIL, OpenCV, numpy, list
img = Image.open(img)

# Inference
results = model(img)
xmin=results.pandas().xyxy[0].xmin.values
xmax=results.pandas().xyxy[0].xmax.values
ymin=results.pandas().xyxy[0].ymin.values
ymax=results.pandas().xyxy[0].ymax.values


#-----------------------------------------#


draw = ImageDraw.Draw(img, "RGBA")
for i in range(len(xmin)):
    shape = [(xmin[i],ymin[i]), (xmax[i],ymax[i])]
    draw.rectangle(shape, fill=(200, 100, 0, 127))
    draw.rectangle(shape, outline=(0, 0, 0, 127), width=2)

img.save('../front/src/components/res.png')