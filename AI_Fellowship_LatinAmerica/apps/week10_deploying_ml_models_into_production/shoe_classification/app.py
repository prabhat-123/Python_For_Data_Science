import os
import json
import uvicorn
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from tensorflow.keras.models import model_from_json


app = FastAPI()

def load_model(weights_file_path, json_file_path):
    # Load the model architecture from a JSON file
    with open(json_file_path, 'r') as json_file:
        loaded_model_json = json_file.read()
    loaded_model = model_from_json(loaded_model_json)
    # Load the weights into the model
    loaded_model.load_weights(weights_file_path)
    return loaded_model


def predict_image(img_path, loaded_model):
  labels = ["addidas", "nike"]
  img = image.load_img(img_path, target_size = (224, 224))
  img_arr = image.img_to_array(img)
  img_arr = np.expand_dims(img_arr, axis=0)
  img_arr = img_arr/255
  prediction = loaded_model.predict(img_arr)
  if prediction < 0.5:
    prediction = 0
    final_output = labels[prediction]
  else:
    prediction = 1
    final_output = labels[prediction]
  return final_output
    
@app.post("/predict")
async def predict_endpoint(img: UploadFile = File(...)):
    img_path = os.path.join(os.getcwd(),
                            'uploaded_images',
                            img.filename)
    # Make prediction using the loaded model
    weights_file_path = os.path.join(os.getcwd(), 
                                        'xception_model', 
                                        'shoe_brand_model_16-1.000000.h5')
    json_file_path = os.path.join(os.getcwd(), 
                                          'xception_model',
                                          'shoe_brand_model_xception.json')
    loaded_model = load_model(weights_file_path, json_file_path)
    result = predict_image(img_path, loaded_model)
    return JSONResponse(content=result)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
