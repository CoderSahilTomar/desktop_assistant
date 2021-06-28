import pyttsx3 as tts
import datetime
import speech_recognition as sr


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
    except sr.WaitTimeoutError as e:
        speak("Wait Timeout Error\nNo input recieved")
        speak("Say that again please.")
    except Exception as e:
        speak('An unknown error occured')
        speak("Say that again please.")
    







if __name__ == '__main__':
    greetMe()
    TakeCommand()