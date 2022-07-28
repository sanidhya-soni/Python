import datetime
import pyttsx3
import pyaudio
import speech_recognition as sr

# Making objects
var = sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


# Method to speak our message
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Initiating recognizer
r = sr.Recognizer()
heard = ''

# Accessing microphone
with sr.Microphone() as source:

    while heard != 'exit':
        try:
            print('Recording: ')
            record = r.listen(source)
            heard = r.recognize_google(record)
            print('I heard: ' + heard)
            speak(heard)

        except:
            print("Some Error!")
