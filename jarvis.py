import pyttsx3 as tts
import datetime


engine = tts.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(sound):
    engine.say(sound)
    print(sound)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12: speak("Good Morning")
    elif hour>=12 and hour<18: speak("Good Afternoon")
    else: speak("Good Evening")
    speak("I am your Desktop Assistant, how may I help you?")

if __name__ == '__main__':
    wishMe()