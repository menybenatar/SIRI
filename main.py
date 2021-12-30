import pyaudio
import pyjokes
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import time

listener = sr.Recognizer()
engine =pyttsx3.init()

def siri_talking_with_you(str):
   engine.say(str)
   engine.runAndWait()

def get_talk():
    command = ""
    try:
        with sr.Microphone() as source:
            print("i am waiting...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'siri' in command:
                command = command.replace('siri ','')
                print(command)
    except:
        print("i can't understand you..")
    return command


def runing_siri():
    response = get_talk()
    print(response)
    if 'play' in response:
        song = response.replace('play ', '')
        siri_talking_with_you('playing' + song)
        print(song)
        pywhatkit.playonyt(song)
    elif 'time' in response:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        siri_talking_with_you('the time is ' + time)
    elif 'tell me about' in response:
        searching = response.replace('tell me about', '')
        info = wikipedia.summary(searching, 2)
        print(info)
        siri_talking_with_you(info)
    elif 'joke' in response:
        joke = pyjokes.get_joke()
        print(joke)
        siri_talking_with_you(joke)
    elif 'how are you' in response:
        siri_talking_with_you('Im fine, thanks.')

    else:
        siri_talking_with_you('please talking again')




for x in range(5):
    runing_siri()
    time.sleep(3)
