import audioop

import ctypes

from distutils.cmd import Command

from opcode import hasname

import shutil

import subprocess

import time

from tkinter.colorchooser import askcolor

from tkinter.filedialog import askdirectory

from urllib.request import urlopen

from xml.dom.minidom import NamedNodeMap

import pyttsx3

import speech_recognition as sr

import datetime

import os

import webbrowser

import webbrowser

import pyjokes

from time import ctime

from winsound import PlaySound

import speech_recognition as sr

import webbrowser

import time  

import os

 

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)

 

def there_exists(terms):

    for term in terms:

            return True

       

r = sr.Recognizer() # initialise a recogniser

# listen for audio and convert it to text:

def record_audio(ask=False):        

       

    with sr.Microphone() as source:

        r.energy_threshold=500            

        r.adjust_for_ambient_noise(source,1.2)

        r.pause_threshold= 1

        if askcolor:

            speak(askdirectory)

       

        voice_data = ''      

 

    try :

            voice_data = r.recognize_google(audioop)

       

    except sr.RequestError:

            speak('Sorry, the service is down')

    except sr.UnknownValueError:

            print('Recognizing..')

    print(f">> {voice_data.lower()}")

    return voice_data.lower()

 

def speak(audio):

    engine.say(audio)

    engine.runAndWait()

 

def wishMe():

    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<12:

        speak("Good Morning Sir !")

 

    elif hour>= 12 and hour<18:

        speak("Good Afternoon Sir !")

 

    else:

        speak("Good Evening Sir !")

 

    assname =("This is Bongo")

    speak("I am your Assistant")

    speak(assname)

   

def username():

    speak("What should i call you sir")

    uname = takeCommand()

    speak("Welcome Mister")

    speak(uname)

    columns = shutil.get_terminal_size().columns

   

    print("*********************".center(columns))

    print("Welcome Mr.", uname.center(columns))

    print("*********************".center(columns))

   

    speak("How can i Help you, Sir")

 

def takeCommand():

   

    r = sr.Recognizer()

   

    with sr.Microphone() as source:

       

        print("Listening...")

        r.pause_threshold = 1

        audio = r.listen(source)

 

    try:

        print("Recognizing...")

        query = r.recognize_google(audio, language ='en-in')

        print(f"User said: {query}\n")

 

    except Exception as e:

        print(e)

        print("Unable to Recognize your voice.")

        return "None"

   

    return query

 

if __name__ == '__main__':

    clear = lambda: os.system('cls')

    clear()

    wishMe()

    username()

   

 

while True:

             

        query = takeCommand().lower()

       

        if 'lock window' in query:

                speak("locking the device")

                ctypes.windll.user32.LockWorkStation()

 

        elif 'open youtube' in query:

            speak("Here you go to Youtube\n")

            webbrowser.open("youtube.com")

           

        elif 'lock window' in query:

                speak("locking the device")

                ctypes.windll.user32.LockWorkStation()  

 

        elif 'open google' in query:

            speak("Here you go to Google\n")

            webbrowser.open("google.com")

 

        elif 'open stackoverflow' in query:

            speak("Here you go to stackoverflow")

            webbrowser.open("stackoverflow.com")

           

        elif 'open facebook' in query:

            speak("Here you go to facebook")

            webbrowser.open("facebook.com")

           

        elif 'open dhaanish college' in query:

            speak("Here you go to dhaanish college")

            webbrowser.open("dhaanish.in")

           

        elif 'open anna university' in query:

            speak("Here you go to anna university")

            webbrowser.open("https://www.annauniv.edu")          

 

        elif 'my location' in query:

            speak("your location is")

            webbrowser.open("https://google.nl/maps/place/")

           

        elif 'open google' in query:

            speak("Here you go to google")

            webbrowser.open("https://www.google.com/")

 

        elif 'shutdown system' in query:

            speak("Hold On a Sec ! Your system is on its way to shut down")

            subprocess.call('shutdown / p /f')

       

        elif "don't listen" in query or "stop listening" in query:

            speak("for how much time you want to stop jarvis from listening commands")

            a = int(takeCommand())

            time.sleep(a)

            print(a)

       

        elif 'tell me a joke' in query:

            speak(pyjokes.get_joke())          

     

        elif "who am i" in query:

          speak("If you talk then definitely your human.")

         

        elif "why i came to world" in query:

          speak("Thanks to god. further It's a secret")

       

        elif "how are you" in query:

          speak("I'm fine, nice to meet you")

         

        elif "i love you" in query:

            speak("sorry, It's hard to understand")

       

        elif "wikipedia" in query:

            webbrowser.open("wikipedia.com")

           

        elif "bongo" in query:          

            wishMe()

            speak("bongos 1 point o in your service Mister")

            speak(NamedNodeMap)

       

        elif "are you single" in query:

            speak("no im comitted to my developer")

           

        elif "thank you" in query:

            speak("welcome")            

           

        elif "who is the prime minister of india " in query:

            speak("Narendra Modi")                  

       

        elif "stop listening" in query:

            listening = False

            speak('Listening stopped')

       

         

        day = datetime.date.date.today().weekday() + 1

        Day_dict = {1: 'Monday', 2: 'Tuesday',

                3: 'Wednesday', 4: 'Thursday',

                5: 'Friday', 6: 'Saturday',

                7: 'Sunday'}

     

        if day in Day_dict.keys():

           day_of_the_week = Day_dict[day]

           print(day_of_the_week)

           speak("The day is " + day_of_the_week)