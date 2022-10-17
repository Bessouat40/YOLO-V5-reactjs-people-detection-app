from fastapi import FastAPI, UploadFile, File
from PIL import Image
from predict import Inference
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

inf = Inference()

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# @app.post('/prediction')
# async def add_lieux(image: UploadFile = File(...),):
#     image_bytes = image.file.read()
#     inf.processImg(image_bytes)
#     pred = "Prédiction : " + str(inf.predict())
#     return pred

@app.post('/prediction')
async def add_lieux(image: UploadFile = File(...),):
    image_bytes = image.file.read()
    inf.processImg(image_bytes)
    inf.predict()
    return './res.png'