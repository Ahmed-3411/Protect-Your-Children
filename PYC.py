import streamlit as st
from PIL import Image
from ultralytics import YOLO
import numpy as np

model = YOLO("model/yolov8n.pt")  # أو سلام وجود تحميل تلقائي

st.set_page_config(page_title="Protect Your Children", layout="centered")
st.title("🛡 Protect Your Children Demo")

uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)

    results = model(np.array(img))
    annotated = results[0].plot()
    st.image(annotated, caption="Detection Result", use_column_width=True)
