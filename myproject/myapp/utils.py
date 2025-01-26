import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables


def get_text(genre):
  load_dotenv()

# Configure Google Generative AI
  genai.configure(api_key="AIzaSyC oCzMVva6GyGz0OIuaeDgEiyE7HnawjBE")

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
  prompt = f"Write a detailed {genre} short story in 100 words.response should only contain the story "
  response = chat_session.send_message(prompt)

  model_response = response.text.strip() 

  return model_response
