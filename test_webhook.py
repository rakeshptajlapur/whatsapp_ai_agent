import requests
import json
import time
import re

def validate_ngrok_url(url):
    """Validate ngrok URL format"""
    pattern = r'https://[a-zA-Z0-9-]+\.ngrok-free\.app'
    return bool(re.match(pattern, url))

def test_webhook():
    # Use provided ngrok URL
    ngrok_url = "https://6259-122-171-20-54.ngrok-free.app"
    
    if not validate_ngrok_url(ngrok_url):
        print("❌ Invalid ngrok URL format")
        return
    
    # Ensure URL ends with /webhook/
    url = f"{ngrok_url}/webhook/" if not ngrok_url.endswith('/') else f"{ngrok_url}webhook/"
    
    # Test data
    data = {
        'Body': 'hi',
        'From': 'whatsapp:+14155238886',
        'To': 'whatsapp:+918309537702'
    }
    
    try:
        print("\n========== WEBHOOK TEST ==========")
        print(f"🎯 Testing webhook at: {url}")
        print(f"📤 Sending data: {json.dumps(data, indent=2)}")
        
        response = requests.post(url, data=data, timeout=10)
        
        print("\n📥 Response Details:")
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print("✅ Webhook is working!")
        else:
            print("⚠️ Non-200 status code received")
        print(f"Content: {response.text[:200]}...")  # Show first 200 chars
        
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Request Failed: {str(e)}")
    
    print("\n================================")

if __name__ == "__main__":
    # Check if Django is running
    try:
        requests.get('http://localhost:8000', timeout=2)
    except requests.exceptions.ConnectionError:
        print("⚠️ Django server not running!")
        print("Please run: python manage.py runserver")
        exit(1)
    
    test_webhook()