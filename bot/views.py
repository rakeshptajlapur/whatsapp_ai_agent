from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from django.conf import settings
import logging
import json
from datetime import datetime

logger = logging.getLogger(__name__)

# Initialize Twilio client for outgoing messages
client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
SANDBOX_NUMBER = "14155238886"

# Load business services and responses
SERVICES = {
    "web_development": {
        "name": "Web Development",
        "description": "Custom web applications with modern technologies",
        "features": ["Full-stack development", "React/Angular/Vue.js", "API Integration"],
        "pricing": "Starting from ₹50,000"
    },
    "mobile_apps": {
        "name": "Mobile Apps",
        "description": "Native and cross-platform mobile applications",
        "features": ["iOS & Android", "Flutter/React Native", "Push notifications"],
        "pricing": "Starting from ₹75,000"
    },
    "ai_solutions": {
        "name": "AI Solutions",
        "description": "Custom AI and ML solutions for your business",
        "features": ["ChatBots", "Data Analysis", "Process Automation"],
        "pricing": "Custom quotes"
    }
}

def format_service_info(service_data):
    return f"""*{service_data['name']}*
Description: {service_data['description']}
Features:
{chr(10).join(['  • ' + f for f in service_data['features']])}
Price: {service_data['pricing']}"""

def home(request):
    return HttpResponse("WhatsApp AI is running! 🚀")

@csrf_exempt
def whatsapp_webhook(request):
    logger.info("==== WEBHOOK CALLED ====")
    
    if request.method == 'POST':
        try:
            # Get message details
            incoming_msg = request.POST.get('Body', '').lower().strip()
            sender = request.POST.get('From', '')
            
            logger.info(f"Message received: {incoming_msg} from {sender}")

            # Process message and get response
            if any(greeting in incoming_msg for greeting in ['hi', 'hello', 'hey']):
                response_text = """*Welcome to CodeSiddhi* 👋

Your Tech Innovation Partner!

How can I help you today?
1. Type *services* for our offerings
2. Type *pricing* for rates
3. Type *contact* for business inquiries
4. Type *about* to know more about us"""

            elif 'services' in incoming_msg:
                response_text = """*Our Services* 🚀

1. *Web Development* 💻
   • Custom websites and web apps
   • E-commerce solutions
   • API development

2. *Mobile Apps* 📱
   • iOS and Android apps
   • Cross-platform solutions
   • App maintenance

3. *AI Solutions* 🤖
   • Custom AI models
   • Chatbots
   • Process automation

Reply with service name for detailed information."""

            elif any(service in incoming_msg for service in SERVICES.keys()):
                for key, service in SERVICES.items():
                    if key in incoming_msg:
                        response_text = format_service_info(service)
                        break

            elif 'pricing' in incoming_msg:
                response_text = """*Pricing Overview* 💰

• Web Development: From ₹50,000
• Mobile Apps: From ₹75,000
• AI Solutions: Custom quotes

Type *contact* to discuss your project requirements."""

            elif 'contact' in incoming_msg:
                response_text = """*Contact Us* 📞

*Email:* contact@codesiddhi.com
*Phone:* +91-XXXXXXXXXX
*Website:* www.codesiddhi.com

Our team will get back to you within 24 hours!"""

            elif 'about' in incoming_msg:
                response_text = """*About CodeSiddhi* ✨

We're a tech innovation company specializing in:
• Custom Software Development
• Mobile App Solutions
• AI & ML Integration

With 5+ years of experience and 100+ successful projects.

Type *services* to explore our offerings!"""

            else:
                response_text = """Not sure what you're looking for? 

Try these commands:
• Type *services* for our offerings
• Type *pricing* for rates
• Type *contact* for business inquiries
• Type *about* to know more about us"""

            # Send response
            try:
                message = client.messages.create(
                    from_=f"whatsapp:+{SANDBOX_NUMBER}",
                    body=response_text,
                    to=sender
                )
                logger.info(f"Response sent! SID: {message.sid}")
                return HttpResponse("OK")
                
            except Exception as send_error:
                logger.error(f"Send Error: {str(send_error)}")
                return HttpResponse(str(send_error), status=500)

        except Exception as e:
            logger.error(f"Webhook Error: {str(e)}")
            return HttpResponse(str(e), status=500)

    return HttpResponse("Webhook is working", status=200)
