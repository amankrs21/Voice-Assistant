# Note :- This Code is made for Python version 3

import os
import pyaudio
import datetime
import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia as wiki
from googletrans import Translator
from subprocess import call



listener = sr.Recognizer()

engine = pyttsx3.init()
voices= engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('voice',voices[1].id)    # We can use '0' for male voice and '1' for female voice
engine.setProperty('rate', 130)             # we can set speed/rate according to our need
engine.setProperty('volume',1.0)            # we can set volume 0 or 1

global translator
translator = Translator()
# translator = google_translator()

def speak(text):
    text1 = translator.translate(text, dest='hi').text
    # text1 = translator.translate(text,lang_tgt='gu')
    print(text1)
    engine.say(text1)
    engine.runAndWait()
    # call(['espeak', '-v', 'mb-us1', text])

def take_command():
    try:    
        with sr.Microphone() as source:
            print('listening...')
            listener.pause_threshold = 1
            listener.adjust_for_ambient_noise(source, duration=1)
            voice = listener.listen(source,timeout=5,phrase_time_limit=5)
            # command1 = listener.recognize_google(voice, language="en-IN")
            command1 = listener.recognize_google(voice, language="hi-IN")
            # command1 = listener.recognize_google(voice, language="gu-IN")
            command = translator.translate(command1,lang_tgt='en')
            command = command.lower()
            return command
    except:
        pass

def assistant_harry():
    command = take_command()
    print(command)
    try:
        if ('how are you' in command):
            speak('''I am fine, thanks for asking. This is Crucial time for everyone, Stay safe''')

        elif ('who are you' in command):
            speak('''My name is Harry.
            I'm a Digital Assistant Created by Aman Singh.
            I was created to be like Jarvis from Iron Man''')

        elif ('what can you do' in command):
            speak('''I can play songs, tell Jokes, tell time and weather, perform google searches,
            perform simple calculations, open mail, whatsapp, facebook, instagram, twitter etc''')
        
        elif ('current time' in command):
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current time is '+time)
            
        elif ('play' in command):
            song = command.replace('play','')
            speak('playing'+ song)
            pywhatkit.playonyt(song)

        elif ('joke' in command):
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)
        
        elif ('about' in command or 'who is' in command or 'what is' in command):
            person = command.replace('about', '')
            info = wiki.summary(person, 1)
            print(info)
            speak(info)
            webbrowser.open('https://google.com/search?q='+person)

        elif ('open mail' in command):
            speak('Opening Mail in the Browser')
            webbrowser.open('https://mail.google.com/')

        elif ('open whatsapp' in command):
            speak('Opening Whatsapp in the Browser')
            webbrowser.open('https://web.whatsapp.com/')

        elif ('open facebook' in command):
            speak('Opening Facebook in the Browser')
            webbrowser.open('https://www.facebook.com/')

        elif ('open twitter' in command):
            speak('Opening Twitter in the Browser')
            webbrowser.open('https://twitter.com/')

        elif ('open instagram' in command):
            speak('Opening Instagram in the Browser')
            webbrowser.open('https://www.instagram.com/')

        elif ('open youtube' in command):
            speak('Opening Youtube in the Browser')
            webbrowser.open('https://www.youtube.com/')
        
        elif ('love' in command):
            speak("I am in Realationship with wifi")
        
        # elif 'temperature' in command:
        #     pass
 
        # elif 'solve' or 'calculate' in command:
        #     pass
            

        
        elif ('thank you' in command):
            speak("You Welcome")
            exit()
        
        else:
            speak("Sorry I did not get it")

    except:
        # exit()
        pass
    
speak('hello, I am your personal assistant, how may i help you')
while True:
    assistant_harry()
