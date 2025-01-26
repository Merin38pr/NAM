import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_text(genre):
    # Retrieve the API key securely from the environment variable
    api_key = os.getenv("API_KEY")  # Make sure you set this in your .env file
    
    # Configure Google Generative AI
    genai.configure(api_key=api_key)

    # Set up generation configuration with an increased token limit
    generation_config = {
        "temperature": 0.7,
        "top_p": 0.95,
        "top_k": 40,
        "max_output_tokens": 2048,  # Increased token limit for a longer story
        "response_mime_type": "text/plain",
    }

    # Initialize the generative model
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-exp",
        generation_config=generation_config,
        system_instruction="Assistant",
    )
    chat_session = model.start_chat(history=[])

    # Create the prompt with the genre, asking for a full story with a moral
    prompt = f"Please write a {genre} story for children that is at least 200 words long and ends with a moral."

    # Send the prompt to the model and get a response
    response = chat_session.send_message(prompt)

    # Retrieve and clean the response
    model_response = response.text.strip()

    # If the response is too short, keep asking for more until we get a complete story with a moral
    while len(model_response.split()) < 200 or "moral" not in model_response.lower():
        response = chat_session.send_message("Continue the story and include a moral at the end.")
        model_response += "\n" + response.text.strip()

    # Ensure proper line breaks in the generated story
    model_response = model_response.replace(". ", ".\n")  # Example for inserting line breaks after each sentence

    return model_response

