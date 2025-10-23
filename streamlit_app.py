import streamlit as st
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
from PIL import Image

st.title("🚀 My Streamlit App")
st.write("Hello, world! This is a simple Streamlit app running via LocalTunnel.")
st.text_input("BAASANSUREN")

# Load the image from a file
# Make sure 'my_picture.jpg' is in the same directory or provide the full path
try:
    image = Image.open("my_picture.jpg")
    # Display it in Streamlit
    st.image(image, caption="My Picture", use_column_width=True)
except FileNotFoundError:
    st.error("https://lh3.googleusercontent.com/gps-cs-s/AG0ilSwiYD-0C1fNgW9Gk8C36r_gXkI3H7vMR2wyz3CJWIgXam7LoMOx89_E9XrDxnsOlmRBdj2eID8DE3ZvJBiw0NT06QmJBp64NXxo5ew2_ZJLQcuhyNygXEDPuxpxTZTA5nBlcRXa2KM32mea=s680-w680-h510-rw.")
