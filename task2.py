import speech_recognition as sr
import pyttsx3
import random
from datetime import datetime
import os


engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Now listening")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Deciphering")   
        query = r.recognize_google(audio, language ='en-in')
        print("You Said: " + query)
  
    except Exception as e:
        print(e)
        print("Did not hear anything") 
        return "None"
     
    return query


while True:
    command = takeCommand()
    #Conversational
    if 'how are you' in command:
        speak("I'm doing well")
    if 'thank you' in command:
        speak("Anytime")

    #Tasks
    if 'time' in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak("The Current Time is " + current_time)  
    if 'random number' in command:
        randInt = random.randint(0, 10) 
        speak("A random number between 0 and 10 is " + str(randInt))
    if 'open slack' in command:
        os.system('open /Applications/Slack.app')
        speak("Opening Slack")
    if 'close slack' in command:
        os.system('open /Applications/Slack.app')
        speak("Closing Slack")


        # Voice Assistant Code explanation:
#
# 1. Imports:
#    - `speech_recognition`: Voice input.
#    - `pyttsx3`: Text-to-speech.
#    - `random`: Random numbers.
#    - `datetime`: Current time.
#    - `os`: System commands.
#
# 2. Functions:
#    - **speak(audio):** Text to speech.
#    - **takeCommand():** Listens and recognizes speech.
#
# 3. Commands:
#    - **"how are you"** → "I'm doing well."
#    - **"thank you"** → "Anytime."
#    - **"time"** → Current time.
#    - **"random number"** → Random number (0-10).
#    - **"open slack"** → Opens Slack.
#    - **"close slack"** → Closes Slack.
#
# Summary: A simple voice assistant responding to commands.
