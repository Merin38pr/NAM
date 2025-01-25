import os
import google.generativeai as genai
from dotenv import load_dotenv
from main import text_to_speech

# Load environment variables
load_dotenv()

# Configure Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Set up generation configuration
generation_config = {
    "temperature": 0.7,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 256,
    "response_mime_type": "text/plain",
}

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash-exp",
    generation_config=generation_config,
    system_instruction="Assistant",
)
chat_session = model.start_chat(history=[])

# Welcome message
print("Bot: select a genre")
text_to_speech("select a genre")

# Main chatbot loop
while True:
    user_input = input("You:  ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        text_to_speech("Goodbye!")
        break

    try:
        # Send user input to the Gemini API
        response = chat_session.send_message(user_input)
        model_response = response.text

        print(f"Bot: {model_response}")
        text_to_speech(model_response)

    except Exception as e:
        print(f"Error: {e}")
