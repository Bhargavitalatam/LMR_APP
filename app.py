import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load model
model = tf.keras.models.load_model("landmark_model.keras")

st.title("🌍 Landmark Classification App")
st.write("Upload an image and get predicted Landmark ID")

file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if file is not None:
    img = Image.open(file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # preprocess
    img = img.resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # prediction
    pred = model.predict(img)
    class_id = int(np.argmax(pred))

    st.success(f"Predicted Landmark ID: {class_id}")