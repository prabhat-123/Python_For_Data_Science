import os
import requests
import streamlit as st
from PIL import Image



st.title("Image Upload and Prediction App")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # Display the uploaded image
    st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)
    # Create a new folder for storing uploaded images
    upload_folder = "uploaded_images"
    os.makedirs(upload_folder, exist_ok=True)
    # Save the uploaded image to the new folder
    uploaded_image_path = os.path.join(upload_folder, uploaded_file.name)
    with open(uploaded_image_path, "wb") as f:
        f.write(uploaded_file.getvalue())
    # Modify the parameter name to match the FastAPI server
    fastapi_url = "http://localhost:8000/predict"  
    files = {"img": open(uploaded_image_path, "rb")}  
    response = requests.post(fastapi_url, files=files)
    # Display the prediction result
    if response.status_code == 200:
        result = response.json()
        st.write(f"Prediction: {result}")
    else:
        st.write(f"Error predicting image. Status code: {response.status_code}")

