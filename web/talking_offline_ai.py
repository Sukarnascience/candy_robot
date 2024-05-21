import speech_recognition as sr
from gtts import gTTS
import pygame
import time
import aiml
import os

import presidencyRelatedAi as pai


def update_expression_ai(new_expression):
    try:
        with open('expression.txt', 'w') as file:
            file.write(new_expression)
        print("Expression updated successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Initialize recognizer
recognizer = sr.Recognizer()

# Chatbot class
class Chatbot:
    def __init__(self):
        print("""Hi! This is Sukarna Jana, the creator of this code.
Its a offline Mode which was trained long back.
Thank you!
================= Happy Chatting =================""")
        
        self.kernel = aiml.Kernel()
        self.kernel.learn("std-startup.xml")
        self.kernel.respond("LOAD AIML B")

    def get_response(self, input_text):
        """
        Get response based on the input text.
        
        Parameters:
        - input_text (str): The input text.
        
        Returns:
        - str: The response from the chatbot.
        """
        return self.kernel.respond(input_text)

# Function to convert text to speech and play it
def speak(text):
    tts = gTTS(text=text, lang='en', slow=False)
    tts.save("response.mp3")
    
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("response.mp3")
    pygame.mixer.music.play()
    
    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        time.sleep(1)
    
    # Stop the mixer and clean up
    pygame.mixer.music.unload()
    pygame.mixer.quit()
    os.remove("response.mp3")

# Function to listen for the hotword "Candy"
def listen_for_hotword():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for hotword 'Candy'...")
        audio = recognizer.listen(source)
        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio).lower()
            print(f"Recognized: {text}")
            if "candy" in text:
                return True
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
    return False

# Function to get user input and respond using the AI chatbot
def ai_conversation(chatbot):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("You can speak now...")
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")

            # Get AI response
            ai_response = pai.presiAnswer(user_input)
            if(ai_response == "sorry"):
                ai_response = chatbot.get_response(user_input)
            update_expression_ai("talking")
            print(f"AI: {ai_response}")
            speak(ai_response)
            update_expression_ai("neutral")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            speak("Sorry, I did not understand that.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            speak("There was an error with the speech recognition service.")

# Main loop to listen for hotword and trigger AI conversation
def main():
    chatbot = Chatbot()
    while True:
        if listen_for_hotword():
            ai_conversation(chatbot)
            print("Returning to hotword listening mode...")
            time.sleep(2)  # Pause briefly before listening again

if __name__ == "__main__":
    main()

