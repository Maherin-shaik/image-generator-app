# 🖼️ AI Image Generator using Stable Diffusion
**Live Demo**
https://image-generator-app-87uvygnw6yzt8mcpyuse6m.streamlit.app/

This project was developed **during my Data Science training** as part of hands-on learning in **Generative AI and Deep Learning**.  
It demonstrates how state-of-the-art **Stable Diffusion models** can be integrated into a **Streamlit web application** for real-time text-to-image generation.

---

## 🎯 Project Objective

The goal of this project was to:
- Understand **text-to-image generation** using diffusion models
- Work with **Hugging Face models and APIs**
- Build and deploy an **interactive ML web application**
- Practice secure handling of **API tokens**
- Gain experience in **model deployment workflows**

---

## 🚀 Features

- Generate images from natural language prompts
- Uses Stable Diffusion model from Hugging Face
- Interactive and user-friendly Streamlit interface
- Image preview and download functionality
- Environment-variable based token management
- Suitable for local execution and cloud deployment

---

## 🧠 Model Used

- **Stable Diffusion v1.5**
- Model ID: `runwayml/stable-diffusion-v1-5`
- Platform: Hugging Face

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **PyTorch**
- **Hugging Face Diffusers**
- **Transformers**
- **Pillow**

---

## 📂 Project Structure

-image-generator-app/<br>
│<br>
├── app.py<br>
├── requirements.txt<br>
├── .gitignore<br>
└── README.md


---

## 🔑 Environment Variable Setup

This project requires a **Hugging Face Access Token**.

### Local Setup (Windows – PowerShell)

```powershell
setx HF_TOKEN "hf_your_token_here"
```
Restart the terminal after setting the variable.

### Streamlit Cloud Setup

Add the following under App Settings → Secrets:

HF_TOKEN = "hf_your_token_here"

### ▶️ How to Run the Project Locally
1️⃣ Clone the repository<br>
git clone https://github.com/YOUR_USERNAME/image-generator-app.git
cd image-generator-app

2️⃣ Install dependencies<br>
pip install -r requirements.txt

3️⃣ Run the Streamlit application<br>
python -m streamlit run app.py

### 📦 Dependencies
- streamlit
- torch
- diffusers
- transformers
- accelerate
- Pillow
- huggingface_hub

### ⚠️ Notes

- Image generation on CPU is slow, which is expected.
- The project can be extended to GPU-based deployment for faster performance.
- Hugging Face tokens should never be committed to version control.

### 🌱 Learnings from This Project

- Practical understanding of diffusion models
- Hands-on experience with Generative AI
- Using Hugging Face ecosystem for model access
- Building ML apps with Streamlit
- Deployment-ready project structuring

### 🔮 Future Enhancements

- Negative prompt support
- Image resolution and quality controls
- Multiple image generation
- GPU acceleration
- Deployment on Hugging Face Spaces

### 👤 Author

**Shaik Maherin**<br>
Computer Science Student<br>
Data Science & Full Stack Development


⭐ Acknowledgement

This project was completed as part of my Data Science training to strengthen practical skills in machine learning deployment and generative AI applications.
