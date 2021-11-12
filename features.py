## == REQUIRED KIVY MODULES == ##
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

## == REQUIRED MODULES == ##
import warnings
import webbrowser
from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import datetime
import subprocess
import pyjokes
import calendar
import random
import wikipedia
from time import sleep

warnings.filterwarnings("ignore")

## == APP ASPECT RATIO FUNCTION == ##
def window_aspect_ratio(width, height, factor):
	Window.size = ((40-factor)*width, (40-factor)*height)

## == ADDITIONAL GUI FEATURES == ##
class WrappedLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(
            width=lambda *x:
            self.setter('text_size')(self, (self.width, None)),
            texture_size=lambda *x: self.setter('height')(self, self.texture_size[1]))

## == FEATURES CLASS == ##
## ==== MAIN SCREEN ==== ##
class Features(Screen):

    # == GUI Variables == #
    response = StringProperty("Click the mic button below and start speaking.\n(Check 'Info' page for the commands.)")
    greeting = StringProperty("Good Evening")
    
    # == Mic Button on_release == #
    def start_listening(self):
        self.spoken = self.listen()
        self.lspoken = self.spoken.lower()

        self.features(self.lspoken)

    ## ==== TEXT-TO-SPEECH ==== ##
    # == Main TTS Conversion == #
    def tts(self, text, filename):
        tts = gTTS(text=text, lang="en", tld="ca")
        tts.save(filename)

    # == TTS For Fixed Sentences == #
    def speak(self, text):
        filename = f"{text.lower()[:20]}.mp3"
        if not os.path.exists(filename):
            self.tts(text, filename)
        playsound.playsound(filename)
    
    # == TTS For One Time Sentences == #
    def temp_speak(self, text):
        filename = f"{text.lower()[:20]}.mp3"
        self.tts(text, filename)
        playsound.playsound(filename)
        os.remove(filename)

    # ==== SPEECH-TO-TEXT ==== ##
    @staticmethod
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=5)
            print("Listening...")
            audio = r.listen(source)

        said = " "

        try:
            said = r.recognize_google(audio, language="en")
            print("You said: " + said)
        except sr.UnknownValueError:
            print("Sorry, couldn't understand that.")
        except sr.RequestError as ex:
            print("Request Error from Google Speech Recognition" + str(ex))
        except Exception as e:
            print("Exception: " + str(e))
        
        print("Done listening.")
        return said
    
    #### ======== FEATURES ======== ####

    ## ==== WELCOME GREETING ==== ##
    def welcome(self):
        self.hour = int(datetime.datetime.now().hour)
        
        if self.hour >= 0 and self.hour <= 12:
            self.speak("Good Morning!")
            return "Good Morning!"
        elif self.hour >= 12 and self.hour <= 17:
            self.speak("Good Afternoon!")
            return "Good Afternoon!"
        else:
            self.speak("Good Evening!")
            return "Good Evening!"
        
        # self.speak("I am Orator Version 14.63, How can I help you?")

    def today_date(self):
        now = datetime.datetime.now()
        date_now = datetime.datetime.today()
        week_now = calendar.day_name[date_now.weekday()]
        month_now = now.month
        day_now = now.day

        months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
        ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

        # return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."
        return f"{week_now}, {ordinals[date_now - 1]} {months[month_now - 1]}"
    
    def greet(text):
        greets = ["hi","hello","greetings","Whats up","howdy","what's good","Hey there"]

        for word in text.split():
            if word.lower() in greets:
                return random.choice(greets) + ". I am Orator. " + "What can I do for you sir?"

        return ""


    def wiki_person(self, text):
        list_wiki = text.split()
        for i in range(0, len(list_wiki)):
            if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
                return list_wiki[i + 2] + " " + list_wiki[i + 3]

    def note(self, text):
        date = datetime.datetime.now()
        file_name = str(date).replace(":", "-") + "-note.txt"
        with open(file_name, "w") as f:
            f.write(text)

        subprocess.Popen(["notepad.exe", file_name])

    ## ==== FEATURES ==== ##
    def features(self, lspoken):
        self.response = " "

        # ==== OPEN A WEBSITE (.com only) ==== #
        if "open" in lspoken:
            self.site = (lspoken.split("open")[1]).split()

            try:
                self.response = f"Opening {self.site[0] + self.site[1] + self.site[2]}.com in your browser."
                self.speak(self.response)
                webbrowser.open(f"https://www.{self.site[0] + self.site[1] + self.site[2]}.com/")
            except:
                try:
                    self.response = f"Opening {self.site[0] + self.site[1]}.com in your browser."
                    self.speak(self.response)
                    webbrowser.open(f"https://www.{self.site[0] + self.site[1]}.com/")
                except BaseException:
                    self.response = f"Opening {self.site[0]}.com in your browser."
                    self.speak(self.response)
                    webbrowser.open(f"https://www.{self.site[0]}.com/")
                except: print("Sorry, could not find that.")

        # ==== SEARCH ON WEB ==== #

        # == Search On YouTube == #
        if ("search" in lspoken or "play" in lspoken) and ("youtube" in lspoken):
            if "search" in lspoken: self.search = (lspoken.split("search")[1]).split("on youtube")[0]
            elif "play" in lspoken: self.search = (lspoken.split("play")[1]).split("on youtube")[0]

            self.response = f"Searching YouTube on your browser."
            self.speak(self.response)
            webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(self.search))

        # == Search On Google == #
        elif "search" in lspoken or "google" in lspoken:
            if "search" in lspoken: self.search = (lspoken.split("search")[1])
            elif "google" in lspoken: self.search = (lspoken.split("google")[1])

            self.response = f"Seaching on Google."
            self.speak(self.response)
            webbrowser.open("https://www.google.com/search?q=" + "+".join(self.search))
        
        # == Other Features == #
        
        if "date" in lspoken or "day" in lspoken or "month" in lspoken:
            get_today = self.today_date()
            self.response += " " + get_today
        
        elif "time" in lspoken:
            now = datetime.datetime.now()

            meridiem = " "
            if now.hour >= 12:
                meridiem = "p.m"
                hour = now.hour
            else:
                meridiem = "a.m"
                hour = now.hour

            if now.minute < 10:
                minute = "0" + str(now.minute)
            else:
                minute = str(now.minute)

            self.response += " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."
        
        elif "wikipedia" in lspoken or "Wikipedia" in lspoken:
            if "who is" in lspoken:
                person = self.wiki_person(lspoken)
                wiki = wikipedia.summary(person, sentences=2)
                self.response += " " + wiki
        
        elif "who are you" in lspoken or "define yourself" in lspoken:
            self.response += """Hello, I am an Assistant. Orator. I am here to make your life easier.  
            You can command me to perform various tasks such as solving mathematical questions or opening 
            applications etcetera."""
        
        elif "your name" in lspoken:
            self.response += "My name is Orator."

        elif "who am i" in lspoken:
            self.response += "You must probably be a human. I guess?"

        elif "why do you exist" in lspoken or "why did you come" in lspoken:
            self.response += "It is a secret sir."

        elif "how are you" in lspoken:
            self.response += "I am fine, Thank you!"
            self.response += "\nHow are you?"

        elif "fine" in lspoken or "good" in lspoken:
            self.response += "Im happy to know that you are fine sir!"

        elif 'thank you' in lspoken or 'thanks' in lspoken:
            self.response += "You're Welcome"
            self.response += "\n Always here to help you out sir !"

        elif "note" in lspoken or "remember this" in lspoken:
            self.speak("What would you like me to write down sir?")
            note_text = self.listen()
            self.note(note_text)
            
            self.response += "Alright, i noted that down sir!."

        elif 'i love you' in lspoken:
            self.response += "I love you too sir"

        elif 'joke' in lspoken:
            self.response += pyjokes.get_joke()

        elif "don't listen" in lspoken or "stop listening" in lspoken or "do not listen" in lspoken:
            self.speak("for how many seconds do you want me to sleep")
            duration = int(self.listen())
            sleep(duration)
            self.response += str(duration) + " seconds completed. I am Loaded again sir !"

        if self.response == " ":
            self.response = "No response."

        return self.response