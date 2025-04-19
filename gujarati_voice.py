# This Program is Plateform dependent and it will only run on Windows Plateform
# Note :- This Code is made for Python version 3
# In this program System will just understnd hindi and it will speaks in hindi

import datetime
import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit
import pyjokes
import wikipedia as wiki
from google_trans_new import google_translator


listen = sr.Recognizer()

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
rate = engine.getProperty('rate')
volume = engine.getProperty('volume')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate', 140)
engine.setProperty('volume',1.0)

global translator
translator = google_translator()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Speak Now...')
            listen.pause_threshold = 1
            listen.adjust_for_ambient_noise(source, duration=1)
            voice = listen.listen(source,timeout=5,phrase_time_limit=5)
            print("Recognising...")
            command1 = listen.recognize_google(voice, language='gu-IN')
            command = translator.translate(command1,lang_tgt='en')
            command = command.lower()
            return command

    except sr.RequestError as e:
        print("Could not request error",e)
    except:
        pass


def assistant_harry():
    command = take_command()
    print(command)
    try:
        if ('how are you' in command):
            speak('''Huṁ pūchavā māṭē ābhāra chuṁ. Tē badhā māṭē mahatvapūrṇa samaya chē, surakṣita rahō''')

        elif ('who are you' in command):
            speak('''Māruṁ nāma hērī chē.
            Huṁ amanasinhē banāvēlō ḍijiṭala sahāyaka chuṁ.
            Ā'ī ēma mēḍa ṭu bāya barō jarvisa phrōma āyarna ma.Na''')

        elif ('what can you do' in command):
            speak('''Huṁ gītōnī sāthē viḍi'ōjha calāvī śakuṁ chuṁ, jōksa kahī śakuṁ chuṁ, samaya anē havāmāna kahī śakuṁ chuṁ, gūgala sarca karī śakuṁ chuṁ,
             mē'ila, vōṭsa'ēpa, phēsabuka, insṭāgrāma, ṭviṭara vagērē khōlī śakē chē.''')
        
        elif ('time' in command):
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Vartamāna samaya chē '+time)
            
        elif ('play' in command):
            song1 = command.replace('play','')
            song = translator.translate(song1,lang_tgt='hi')
            speak(song+'Saṅgīta vagāḍavuṁ chē')
            pywhatkit.playonyt(song)

        elif ('joke' in command):
            joke1 = pyjokes.get_joke()
            joke = translator.translate(joke1,lang_tgt='hi')
            speak(joke)
        
        elif ('who is' in command or 'what is' in command):
            info1 = wiki.summary(command, 1)
            info = translator.translate(info1,lang_tgt='hi')
            speak(info)

        elif ('open mail' in command):
            speak("Brā'ujharamāṁ mē'ila khōlīnē")
            webbrowser.open('https://mail.google.com/')

        elif ("open what'sp" in command or 'open whatsapp' in command):
            speak('ब्राउज़र में व्हाट्सएप खुल रहा है')
            webbrowser.open('https://web.whatsapp.com/')

        elif ('open facebook' in command):
            speak('ब्राउज़र में फेसबुक खुल रहा है')
            webbrowser.open('https://www.facebook.com/')

        elif ('open twitter' in command):
            speak('ब्राउज़र में ट्विटर खुल रहा है')
            webbrowser.open('https://twitter.com/')

        elif ('open instagram' in command):
            speak('ब्राउज़र में इंस्टाग्राम खुल रहा है')
            webbrowser.open('https://www.instagram.com/')

        elif ('open youtube' in command):
            speak('ब्राउज़र में यूट्यूब खुल रहा है')
            webbrowser.open('https://www.youtube.com/')

        elif ('open flipkart' in command):
            speak('ब्राउज़र में फ्लिपकार्ट खुल रहा है')
            webbrowser.open('https://www.flipkart.com/')

        elif ('open amazon' in command):
            speak('ब्राउज़र में अमेज़न खुल रहा है')
            webbrowser.open('https://amazon.com/')
        
        elif ('google' in command):
            things = command.replace('search', '')
            things = things.replace('google', '')
            things = things.replace('on', '')
            things = things.replace('about', '')
            speak(things+'के बारे में गूगल पे ढूंढा जा रहा है')
            webbrowser.open('https://google.com/search?q='+things)
        
        elif ('love' in command):
            speak("मैं वाईफाई के साथ रिलेशनशिप में हूं")
        
        # elif 'temperature' in command:
        #     pass
 
        # elif 'solve' or 'calculate' in command:
        #     pass
            

        
        elif ('thank you' in command or 'thanks' in command):
            speak("आप का स्वागत है")
            exit()
        
        else:
            speak("क्षमा करें मुझे यह समझ में नहीं आया")

    except:
        pass

speak('नमस्ते मैं आपका निजी सहायक हूँ मैं आपकी कैसे मदद कर सकता हूँ?')

while True:
    assistant_harry()
