# import warnings
# import pyttsx3 as p
# import speech_recognition as sr
# import os
import datetime
import calendar
import random
import wikipedia
# import webbrowser
# import subprocess
import pyjokes
# import traceback
# import time

# warnings.filterwarnings("ignore")

def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12: speak("Good Morning Sir !")
    elif hour >= 12 and hour <= 17: speak("Good Afternoon sir!"); speak(hour)
    else: speak("Good evening sir!")
    speak("I am Jarvis Version 0.2, How can i help you?")

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    ordinals = ["1st","2nd","3rd","4th","5th","6th","7th","8th","9th","10th","11th","12th","13th","14th","15th","16th","17th","18th","19th","20th","21st","22nd","23rd","24th","25th","26th","27th","28th","29th","30th","31st"]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def greet(text):
    response = ["hi","hello","greetings","Whats up","howdy","what's good","Hey there"]

    for word in text.split():
        if word.lower() in response:
            return random.choice(response) + ". I am jarvis. " + "What can i do for you sir?"

    return ""

def wiki_person(text):
    list_wiki = text.split()
    for i in range(0, len(list_wiki)):
        if i + 3 <= len(list_wiki) - 1 and list_wiki[i].lower() == "who" and list_wiki[i + 1].lower() == "is":
           return list_wiki[i + 2] + " " + list_wiki[i + 3]

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

welcome()
while True:
    try:
        text = listen().lower()
        reply = " "

        if "date" in text or "day" in text or "month" in text:
            get_today = today_date()
            reply = reply + " " + get_today

        elif "time" in text:
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

            reply = reply + " " + "It is " + str(hour) + ":" + minute + " " + meridiem + " ."

        elif "wikipedia" in text or "Wikipedia" in text:
            if "who is" in text:
                person = wiki_person(text)
                wiki = wikipedia.summary(person, sentences=2)
                reply = reply + " " + wiki

        elif "who are you" in text or "define yourself" in text:
            reply =reply + """Hello, I am an Assistant. Jarvis. I am here to make your life easier.  
            You can command me to perform various tasks such as solving mathematical questions or opening 
            applications etcetera."""

        elif "your name" in text:
            reply = reply + "My name is Jarvis."

        elif "who am i" in text:
            reply = reply + "You must probably be a human. i guess?"

        elif "why do you exist" in text or "why did you come" in text:
            reply = reply + "It is a secret sir."

        elif "how are you" in text:
            reply = reply + "I am fine, Thank you!"
            reply = reply + "\nHow are you?"

        elif "fine" in text or "good" in text:
            reply = reply + "Im happy to know that you are fine sir!"

        elif 'thank you' in text or 'thanks' in text:
            reply = reply + "You're Welcome"
            reply = reply + "\n Always here to help you out sir !"

        elif "note" in text or "remember this" in text:
            speak("What would you like me to write down sir?")
            note_text = listen()
            note(note_text)
            reply = reply + "Alright, i noted that down sir!."

        elif 'i love you' in text:
            reply = reply + "I love you too sir"

        elif 'joke' in text:
            reply = reply + pyjokes.get_joke()
            
        elif "don't listen" in text or "stop listening" in text or "do not listen" in text:
            speak("for how many seconds do you want me to sleep")
            duration = int(listen())
            time.sleep(duration)
            repply = reply + str(duration) + " seconds completed. I am Loaded again sir !"

        speak(reply)

    except:
        speak("I dont know, sorry")