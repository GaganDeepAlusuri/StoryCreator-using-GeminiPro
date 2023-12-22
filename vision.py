from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()  # Loading the environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# Function to load gemini pro-vision model and get responses
def get_gemini_response(theme, image):
    model = genai.GenerativeModel("gemini-pro-vision")
    if theme != "":
        question = f"Created a story based on the image in approximately 200 words with a theme of {theme}."
        response = model.generate_content([question, image])
    else:
        question = f"Tell a story about the image in approximately 200 words."
        response = model.generate_content(image)

    return response.text


# Initialize our streamlit application
st.set_page_config(page_title="Gemini Image to Story Demo")
st.header("Gemini Image to Story Application")

uploaded_file = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])
theme = st.text_input("Theme or question (optional):")

image = None

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

submit = st.button("Generate Story")

# If the Generate Story button is clicked
if submit:
    response = get_gemini_response(theme, image)
    st.subheader("Generated story:")
    st.write(response)
