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
