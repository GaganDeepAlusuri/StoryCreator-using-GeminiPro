from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()  # Loading the environment variables.

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##Function to load gemini pro model and get responses.
model = genai.GenerativeModel("gemini-pro")


def get_gemini_response(story_description, characters, theme):
    question = f"What is the story about? {story_description}\nWho are the characters? {characters}\nWhat is the theme? {theme}"
    response = model.generate_content(question)
    return response.text


## Initialize our streamlit app
st.set_page_config(page_title="Story Builder")
st.header("Gemini Story Building LLM Application")

story_description = st.text_input("What is the story about?")
characters = st.text_input("Who are the characters?")
theme = st.text_input("What is the theme?")

submit = st.button("Generate Story")

if submit:
    response = get_gemini_response(story_description, characters, theme)
    st.write(response)
