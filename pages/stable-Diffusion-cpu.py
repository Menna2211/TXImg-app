# -*- coding: utf-8 -*-
"""text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-arF_jX43gtR9du-eWWDriPTJaqzFuae
"""

import streamlit as st
import torch
import time
from optimum.onnxruntime import ORTStableDiffusionPipeline

model_id = "runwayml/stable-diffusion-v1-5"
pipe = ORTStableDiffusionPipeline.from_pretrained(model_id, export=True)

st.title("Stable Diffusion App")
# define the layout of your app

# Define the Streamlit app layout
prompt = st.text_input("Write your sentence:")
submit_button = st.button("Compute")

# Display the generated text
if submit_button:
    progress_text = "Operation in progress. Please wait."
    bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        generated_img=pipe(prompt).images[0]
        time.sleep(0.1)
        bar.progress(percent_complete + 1, text=progress_text)

    st.write("Generated Image:")
    st.image(generated_img)
    time.sleep(5)
    st.success('Congratulations task is done ', icon="✅")
    st.balloons()
