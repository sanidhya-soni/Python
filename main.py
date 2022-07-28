import datetime
from logging import exception

import speech_recognition as sr
var = sr
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
print(voices[0].id)


def speak(audio):
    """

    :rtype: object
    """
    engine.say(audio)
    engine.runAndWait()


def wishme():
  hour = int(datetime.datetime.now().hour)
  if 0 <= hour < 12:
      speak("Good Morning! sir")

  elif 12 <= hour < 18:
      speak("Good Afternoon sir")
  else:
    speak("Good Evening sir")
    def takecommand():
     r = var.recognizer
with var.microphone() as source:
    print("listening...")
    r.pause_threshold = 1
audio = r.listen(source)
try:
    print("recognizing...")
    query = r.recognizing_google(audio, language='en-in')
    print(f"user said: {query}\n")

except exception as e:

    print("say that again please...")



if __name__ == '__main__':
 speak("good evening sir")
speak("how may I help you sir ?")

wishme()
takecommand()