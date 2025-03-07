# WhatsApp AI Agent

A WhatsApp business chatbot built with Django and Twilio that handles customer inquiries automatically.

## Features
- WhatsApp integration via Twilio
- Automated responses for services, pricing, and inquiries
- Rule-based message handling
- OpenAI integration for business intelligence and smart response
- Detailed logging

## Setup
1. Clone the repository
```bash
git clone https://github.com/rakeshptajlapur/whatsapp_ai_agent.git
cd whatsapp_ai_agent
```

2. Create and activate virtual environment
```bash
python -m venv venv
.\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create `.env` file with:
```plaintext
DJANGO_SECRET_KEY=your_secret_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_token
DEBUG=True
SANDBOX_NUMBER=14155238886
```

5. Run migrations
```bash
python manage.py migrate
```

6. Start development server
```bash
python manage.py runserver
```

## Configuration
Update `.env` with your Twilio credentials from [Twilio Console](https://console.twilio.com/)