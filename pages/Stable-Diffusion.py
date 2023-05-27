# -*- coding: utf-8 -*-
"""text.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-arF_jX43gtR9du-eWWDriPTJaqzFuae
"""

import streamlit as st
import torch
import time
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler




#pipe = pipe.to("cuda")

@st.cache(allow_output_mutation=True)
def get_model():
    model_id = "CompVis/stable-diffusion-v1-4"
   # model_id = "stabilityai/stable-diffusion-2-1"
    # Use the DPMSolverMultistepScheduler (DPM-Solver++) scheduler here instead
    pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
   # pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    return pipe

pipe =get_model()


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

