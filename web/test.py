import pyttsx3

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Ensure TTS engine is correctly initialized and set properties
tts_engine.setProperty('rate', 150)  # Speed of speech
tts_engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

def speak(text):
    tts_engine.say(text)
    tts_engine.runAndWait()

# Test the TTS functionality
speak("Hello, this is a test of the text to speech system.")
print("If you heard the spoken message, the TTS system is working correctly.")
