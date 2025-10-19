# 🤖 Career Chatbot Backend

> The backend of my **AI-powered personal portfolio assistant**, built with **FastAPI**, **OpenAI**, and **Gemini**.  
> It powers the chatbot on my site — answering questions about my background, experience, and projects.

---

<div align="center">

[![Made with Python](https://img.shields.io/badge/Made%20with-Python%203.13-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/Framework-FastAPI-009688?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/AI-OpenAI%20GPT-412991?logo=openai&logoColor=white)](https://platform.openai.com/)
[![Gemini](https://img.shields.io/badge/AI-Gemini-4285F4?logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Mailjet](https://img.shields.io/badge/Email-Mailjet-FFB100?logo=maildotru&logoColor=white)](https://www.mailjet.com/)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)

</div>

---

## 🧠 Features

- 🤖 Connects to **OpenAI GPT** for natural language chat  
- 📄 Reads résumé from a local PDF (via `pypdf`)  
- 🧠 Uses **Gemini AI** to evaluate and improve email text  
- 📬 Sends follow-up emails via **Mailjet REST API**  
- ⚙️ Built with **FastAPI** + **Uvicorn**  
- 🔐 Uses `.env` for secure environment variables  
- 🧩 Runs in a containerized environment with **Docker**  

---

## ⚙️ Tech Stack

| Category | Tools |
|-----------|-------|
| **Language** | Python 3.13 |
| **Framework** | FastAPI |
| **AI Models** | OpenAI GPT, Google Gemini |
| **Email** | Mailjet REST API |
| **Environment Management** | `python-dotenv` |
| **Dependencies** | `pydantic`, `uvicorn`, `pypdf` |
| **Containerization** | Docker |

---

## 🚀 How to Run

### 1️⃣ Clone the repository

git clone https://github.com/yasamanforouzesh/career-chatbot.git
cd career-chatbot


2️⃣ Install dependencies

I use uv
 to manage Python environments and dependencies.

uv pip install -r requirements.txt

3️⃣ Run the app

uv run main.py

🔑 Environment Variables

Create a .env file in your project root:
```
OPENAI_API_KEY=sk-xxxx
FROM_EMAIL=example@example.com
TO_EMAIL=me@example.com
SMTP_USERNAME=<mailjet_api_key>
SMTP_PASSWORD=<mailjet_secret_key>
```

## 📄 Important Note: Résumé & Summary Files

⚠️ Your résumé (`resume.pdf`) and summary (`summary.json` or `summary.txt`) **are not included in the repository** because they are listed in `.gitignore`.

To make the chatbot work properly, you must add your own files manually:


🌐 Live Demo

🔗 https://portfolio.brightflowtools.com

👩‍💻 Author

Yasaman Forouzesh

📧 yasamanforouzesh93@gmail.com