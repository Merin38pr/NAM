from gtts import gTTS
import pygame
import time
from pathlib import Path


def text_to_speech(text):
    try:
        # Define the path for the audio file
        speech_file_path = Path(__file__).parent / "speech.mp3"

        # Generate the audio file using gTTS
        tts = gTTS(text)
        tts.save(speech_file_path)

        # Initialize pygame mixer and play the audio
        pygame.mixer.init()
        pygame.mixer.music.load(str(speech_file_path))
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

    except Exception as e:
        print(f"Error in text_to_speech: {e}")
    finally:
        # Ensure the mixer is properly quit
        if pygame.mixer.get_init():
            pygame.mixer.quit()
