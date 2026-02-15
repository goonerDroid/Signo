# Signo 📸🌎  
### AI-Powered Signboard Translation & Context Agent

---

## 🚀 Overview

Signo is an AI-powered mobile-first system that:

1. Accepts a photo of a public sign  
2. Extracts text using OCR  
3. Detects the language  
4. Translates the text to English  
5. Explains cultural and legal context (Quebec-specialized)

---

## 🎯 Vision

Build an intelligent cultural interpreter — not just a translator.

Unlike standard translation apps, Signo:
- Explains meaning
- Adds cultural context
- Identifies legal significance
- Dynamically adapts its reasoning workflow

---

## 🏗️ Architecture

**System Flow**

Mobile App (React Native)  
↓  
FastAPI Backend  
↓  
Autonomous Agent Loop  
↓  
Tools:
- OCR  
- Language Detection  
- Translation  
- Quebec Context Explainer  

---

## 📁 Project Structure

    signo-backend/
        app/
            main.py
            agent/
            services/
            schemas/
        requirements.txt
        .env
        README.md

---

## ⚙️ Setup Instructions

### Clone the repository

    git clone <your-repo-url>
    cd signo-backend

### Create virtual environment

    python3 -m venv venv
    source venv/bin/activate

Windows:

    venv\Scripts\activate

### Install dependencies

    pip install -r requirements.txt

### Run the server

    uvicorn app.main:app --reload

Open in browser:

    http://127.0.0.1:8000

Swagger docs:

    http://127.0.0.1:8000/docs

---

## 🛣️ Roadmap

- [x] Backend skeleton
- [ ] Image upload endpoint
- [ ] OCR integration
- [ ] Language detection
- [ ] Translation tool
- [ ] Quebec context reasoning
- [ ] Autonomous agent loop
- [ ] Mobile application

---

## 🧠 Tech Stack

- Python  
- FastAPI  
- OpenAI API  
- Modular tool-based agent architecture  
- React Native (planned mobile client)

---

## 📌 Future Enhancements

- Confidence scoring  
- Sign classification  
- Structured reasoning trace  
- Caching  
- Multi-region support  

---

## 👨‍💻 Author

Built to combine AI reasoning with real-world cultural intelligence.
