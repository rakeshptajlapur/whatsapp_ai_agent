import openai
from django.conf import settings
import json

# Load business context from JSON
with open('bot/data/business_context.json', 'r') as f:
    BUSINESS_CONTEXT = json.load(f)

def process_business_query(user_message):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"""You are CodeSiddhi's AI assistant. Here's your context:
                    - You only answer questions about CodeSiddhi's products and services
                    - You're friendly but professional
                    - If asked about non-business topics, politely redirect to business matters
                    - Use these product details: {BUSINESS_CONTEXT['products']}
                    - Follow these response guidelines: {BUSINESS_CONTEXT['guidelines']}"""
                },
                {"role": "user", "content": user_message}
            ],
            max_tokens=150,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return "I apologize, but I'm having trouble processing your request. Please try again."