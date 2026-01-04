import os
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(page_title="AI Image Generator", layout="centered")

st.title("🖼️ AI Image Generator (Stable Diffusion XL)")
st.write("Generate images using Hugging Face SDXL")

# Get token from (Streamlit Secrets)
hf_token = st.secrets["HF_TOKEN"]

if not hf_token:
    st.error("HF_TOKEN not found. Please set it in Streamlit Secrets.")
    st.stop()

model_id = "stabilityai/stable-diffusion-xl-base-1.0"
client = InferenceClient(model=model_id, token=hf_token)

prompt = st.text_input(
    "Enter image prompt",
    "Professional product photo of wireless headphones"
)

generate = st.button("Generate Image")

if generate:
    with st.spinner("Generating image..."):
        try:
            image = client.text_to_image(prompt)
            st.image(image, caption="Generated Image", use_container_width=True)

            image.save("output.png")
            st.success("Image generated successfully!")

            with open("output.png", "rb") as f:
                st.download_button(
                    "Download Image",
                    f,
                    file_name="generated_image.png",
                    mime="image/png"
                )

        except Exception as e:
            st.error(f"Error: {e}")
