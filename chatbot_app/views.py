from django.shortcuts import render
import os
from django.shortcuts import render
from .forms import ChatForm
from .models import ChatMessage
from dotenv import load_dotenv
import time
import google.generativeai as genai

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-pro')


def get_gemini_response(user_message):
    try:
        response = model.generate_content(user_message)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I encountered an error."

def chatbot_view(request):
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            bot_response = get_gemini_response(user_message)
            ChatMessage.objects.create(user_message=user_message, bot_response=bot_response)

            chat_messages = ChatMessage.objects.all()
            return render(request, 'chatbot.html', {'form': ChatForm(), 'chat_messages': chat_messages})
    else:
        chat_messages = ChatMessage.objects.all()
        form = ChatForm()
    return render(request, 'chatbot.html', {'form': form, 'chat_messages': chat_messages})
# Create your views here.
