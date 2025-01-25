import os
from django.shortcuts import render, redirect
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
        prompt_instructions = f"Respond to the following message as if you are a friendly chatbot interacting with a kid. Keep your responses concise, clear, fun, and avoid using complex words or jargons. Use simple and positive language. If the user is asking a question, answer it directly and to the point, in a manner suitable for a young audience. If you don't have an answer, just say 'I'm not sure about that, let's learn together!'. Here is the user message: {user_message}"
        response = model.generate_content(prompt_instructions)
        return response.text
    except Exception as e:
        print(f"Gemini API Error: {e}")
        return "Sorry, I encountered an error."

def chatbot_view(request):
    if request.method == 'POST':
        if 'new_chat' in request.POST:
            ChatMessage.objects.all().delete()
            return redirect('chatbot')
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
