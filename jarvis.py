import pyttsx3 as tts
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
from googlesearch import search
import os



engine = tts.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(sound):
    '''Makes the assistant speak out stuff'''
    engine.say(sound)
    print(sound)
    engine.runAndWait()

def greetMe():
    '''greets the user according to the time of the day'''
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<12: speak("Good Morning")
    elif hour>=12 and hour<18: speak("Good Afternoon")
    else: speak("Good Evening")
    speak("I am your Desktop Assistant, how may I help you?")



def TakeCommand():
    '''Takes microphone input from the user and return string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        audio = r.listen(source)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio,language='en-in')
        print(f"Speech: {query}\n")
        return query
    except Exception as e:
        print(e)
        speak('An unknown error occured')
        speak("Say that again please.")
        query = "None"
        return query







if __name__ == '__main__':
    greetMe()
    while True:
        query = TakeCommand().lower()
        if 'wikipedia' in query:
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences = 3)
            speak('According to Wikipedia....')
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open(
                url ="https://www.youtube.com/")
        elif 'search google for' in query:
            query =  query.replace('search google for ','')
            speak(f'Searching Google for {query}')
            for i in search(query):
                site = i
                break
            webbrowser.open(site)
        elif 'take mock test' in query:
            webbrowser.open('https://www.onlinetestseries.in/allenkota/login')
        elif "check test schedule" in query:
            webbrowser.open('https://mypat.in/')
        elif "take custom test" in query:
            webbrowser.open('https://fiitjee-meerut.mypat.in/')
        elif "open bootstrap" in query:
            webbrowser.open('https://getbootstrap.com/')
        elif "open github" in query:
            webbrowser.open('https://github.com/')
        elif "open stackoverflow" in query:
            webbrowser.open('www.stackoverflow.com')
        elif "open google" in query:
            webbrowser.open('www.google.com')
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak("The time is :")
            speak(strTime)
        elif "open code" in query:
            codepath = 'C:\\Users\\hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk'
            os.startfile(codepath)
        elif "open sublime text" in query:
            sublimepath = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Sublime Text 3.lnk'
            os.startfile(sublimepath)
            