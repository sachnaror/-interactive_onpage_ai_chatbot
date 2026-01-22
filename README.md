# 🤖 On-page Interactive AI Chatbot (Demo)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.x-green?logo=django&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--powered-black?logo=openai)

An **AI-driven, read-only chatbot** built using **Django + ChatGPT API** to help logged-in users quickly find, view, and download their **documents** using natural language.

This project demonstrates **practical AI usage with strict guardrails** — no hallucinations, no data modification, no risk.

---

## ✨ What This Demo Shows

✅ Natural language understanding (AI-powered)

✅ Intent detection with confidence thresholds

✅ Profile-aware document lookup

✅ Human-friendly responses

✅ Strict read-only guardrails

✅ Clean, production-like UX


❌ No document creation

❌ No edits or deletes

❌ No legal or tax advice

❌ No access to other logged-in users’ data

---

## 🧠 How AI Is Used (Important)

AI is used **only** for:
- Understanding what the user is asking
- Extracting intent (view, download, status)
- Extracting context (bank offering, profile)
- Generating human-friendly responses

AI **does not**:
- Change backend data
- Invent dates or URLs
- Provide legal / tax advice

All actions are validated by backend guardrails.

---

## 🗂️ Profiles Explained

- **CG** → Individual / Personal investor profile
- **LLC** → Company / Entity investor profile

The same investor can have documents under multiple profiles.

---

## 🏗️ Architecture Overview

```
┌────────────────────┐
│   Investor (UI)    │
│  Bootstrap + HTML  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│  Django View/API   │
│  /chat endpoint   │
└─────────┬──────────┘
          │
          ▼
┌──────────────────────────┐
│ ChatGPT API (OpenAI)     │
│ Intent + Entity Parsing │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ Guardrails Layer         │
│ Allowed intents only    │
│ Confidence checks       │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ Django ORM (SQLite)      │
│ Downloadable Documents  │
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ Humanized Response       │
│ (No hallucination)       │
└──────────────────────────┘
```

Key principle: **AI understands language, backend controls behavior.**

---

## 🏗️ Tech Stack

- 🐍 Python 3.12
- 🌐 Django 4+
- 🧠 OpenAI / ChatGPT API (intent parsing only)
- 🎨 Bootstrap 5 (UI)
- 🗄️ SQLite (dummy data)

---

## 🚀 Getting Started

### 1️⃣ Create virtual environment
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Add OpenAI API key
Edit `.env` file:
```env
OPENAI_API_KEY=sk-your-api-key-here
```

### 4️⃣ Setup database
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Seed dummy data (20 records)
```bash
python manage.py seed_dummy_data
```

### 6️⃣ Run the server
```bash
python manage.py runserver
```

Open browser:
👉 http://127.0.0.1:8000/

---

## 💬 Example Questions to Try

- “Show my signed documents”
- “Download agreement for Bank offering”
- “Is my document complete for Offering 5?”
- “Do I have documents in my profile?”

---

## 🛡️ Guardrails (Non-Negotiable)

This chatbot **will refuse**:
- Editing or creating documents
- Bulk downloads
- Showing other logged-in users’ data
- Providing legal or tax advice
- Any unsupported action

This is **intentional and by design**.

---

## 🎯 Why This Matters

This approach:
- Reduces support tickets
- Improves investor experience
- Adds AI safely, not recklessly
- Scales across other modules (Reports, Updates)

It is **practical AI**, not gimmicky AI.

---

## 📌 Demo Disclaimer

This is a **demo application**:
- Uses dummy data only
- No real user's information
- No production credentials

---

## 📌 Directory Structure

```
├── ai_subscription_bot/
│   ├── requirements.txt
│   ├── db.sqlite3
│   ├── README.md
│   ├── .env
│   ├── manage.py
│   ├── ai_subscription_bot/
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── subscriptions/
│   │   ├── models.py
│   │   ├── apps.py
│   │   ├── admin.py
│   │   ├── urls.py
│   │   └── views.py
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   ├── seed_dummy_data.py
│   │   ├── templates/
│   │   │   ├── subscriptions/
│   │   │   │   └── documents.html
│   │   ├── services/
│   │   │   ├── gpt_intent_parser.py
│   │   │   ├── guardrails.py
│   │   │   └── response_builder.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── chatbot.js

```


## 👨‍💻 Author & Contact


## 📩 Contact

| Name              | Details                             |
|-------------------|-------------------------------------|
| **👨‍💻 Developer**  | Sachin Arora                      |
| **📧 Email**       | [sachnaror@gmail.com](mailto:sachnaror@gmail.com) |
| **📍 Location**    | Noida, India                       |
| **📂 GitHub**      | [github.com/sachinaror](https://github.com/sachinaror) |
| **🌐 Website**     | [https://about.me/sachin-arora](https://about.me/sachin-arora) |
| **📱 Phone**       | [+91 9560330483](tel:+919560330483) |

Happy coding! 🎯🔥

---

## 🧩 Next Possible Extensions

- Unified chatbot
- Confidence score visibility in UI
- Multi-language support
- Analytics on user intents
- Replace dummy data with GraphQL APIs

---



<!-- AI-driven Chatbot Demo
----------------------------------

Setup:
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

Run:
python manage.py migrate
python manage.py seed_dummy_data
python manage.py runserver

ai_subscription_bot
-->
