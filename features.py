import webbrowser
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.properties import ObjectProperty, NumericProperty, StringProperty

from gtts import gTTS
import playsound
import os
import speech_recognition as sr
import datetime
from time import sleep

def window_aspect_ratio(width, height, factor):
	Window.size = (dp((40-factor)*width), dp((40-factor)*height))

class Features(Screen):

    response = StringProperty("Hola!")

    def start_listening(self):
        self.spoken = self.listen()
        self.lspoken = self.spoken.lower()

        self.features(self.lspoken)

    ## ==== TEXT-TO-SPEECH ==== ##

    def tts(self, text, filename):
        tts = gTTS(text=text, lang="en", tld="ca")
        tts.save(filename)

    def speak(self, text):
        filename = f"{text.lower()[:20]}.mp3"
        if not os.path.exists(filename):
            self.tts(text, filename)
        playsound.playsound(filename)

    def temp_speak(self, text):
        filename = f"{text.lower()[:20]}.mp3"
        self.tts(text, filename)
        playsound.playsound(filename)
        os.remove(filename)

    ## ==== SPEECH-TO-TEXT ==== ##

    @staticmethod
    def listen():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            # r.adjust_for_ambient_noise(source, duration=1)
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

    ## ==== FEATURES ==== ##

    def features(self, lspoken):
        self.response = " "

        # ==== OPEN A WEBSITE (.com only)==== #
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

        # == YOUTUBE == #
        if ("search" in lspoken or "play" in lspoken) and ("youtube" in lspoken):
            if "search" in lspoken: self.search = (lspoken.split("search")[1]).split("on youtube")[0]
            elif "play" in lspoken: self.search = (lspoken.split("play")[1]).split("on youtube")[0]

            self.response = f"Searching YouTube on your browser."
            webbrowser.open("http://www.youtube.com/results?search_query=" + "+".join(self.search))

        # == GOOGLE == #
        elif "search" in lspoken or "google" in lspoken:
            if "search" in lspoken: self.search = (lspoken.split("search")[1])
            elif "google" in lspoken: self.search = (lspoken.split("google")[1])

            self.response = f"Seaching on Google."
            webbrowser.open("https://www.google.com/search?q=" + "+".join(self.search))

        if self.response == " ":
            self.response = "No response."

        return self.response