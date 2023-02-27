import streamlit as st
from PIL import Image
image = Image.open('final_canvas.jpg')
st.image(image, caption='final_canvas')