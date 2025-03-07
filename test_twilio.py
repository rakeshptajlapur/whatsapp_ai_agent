import os
import subprocess
from twilio.rest import Client
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

def start_ngrok():
    print("🚀 Starting ngrok tunnel...")
    try:
        # Start ngrok using Windows command
        process = subprocess.Popen(
            ['cmd', '/c', 'ngrok.exe', 'http', '8000'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return process
    except Exception as e:
        print(f"❌ Error starting ngrok: {str(e)}")
        return None

# Start ngrok and get URL
ngrok_process = start_ngrok()
if ngrok_process:
    print("✅ Ngrok started successfully!")
    print("📝 Copy the HTTPS URL from the ngrok window")
    print("🌐 Use that URL + /webhook/ in Twilio console")

# Fetch Twilio credentials
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Use sandbox configuration
SANDBOX_NUMBER = "14155238886"
RECIPIENT_NUMBER = "918309537702"  # Your sandbox-approved number

FROM_WHATSAPP = f"whatsapp:+{SANDBOX_NUMBER}"
TO_WHATSAPP = f"whatsapp:+{RECIPIENT_NUMBER}"

print("🔷 Sandbox Configuration:")
print(f"→ Using Sandbox Number: +{SANDBOX_NUMBER}")
print(f"→ Sending to: +{RECIPIENT_NUMBER}")

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

try:
    # Test webhook configuration
    print("\n🔧 Webhook Setup Instructions:")
    print("1. Go to: https://console.twilio.com/")
    print("2. Click on Messaging → WhatsApp → Sandbox")
    print("3. Find 'WHEN A MESSAGE COMES IN'")
    print("4. Enter: http://localhost:8000/webhook/")
    print("5. Click Save")
    
    # Send test message
    message = client.messages.create(
        from_=FROM_WHATSAPP,
        body="Test message - reply 'hi' to test webhook",
        to=TO_WHATSAPP
    )
    
    print(f"\n✅ Message sent! SID: {message.sid}")
    
    # Track message status
    for i in range(5):
        message = client.messages(message.sid).fetch()
        status = message.status
        print(f"📋 Status: {status}")
        if status == 'delivered':
            print("✅ Message delivered!")
            break
        time.sleep(2)

except Exception as e:
    print(f"❌ Error: {str(e)}")
