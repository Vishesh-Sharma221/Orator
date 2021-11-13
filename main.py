## == REQUIRED KIVY MODULES == ##
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

## ==== FEATURES SCRIPT ==== ##
from features import *

## ==== THEME FILE ==== ##
with open("theme.txt", "a+") as f:
	if f.read() == "":
		f.write("cyan")

## ==== APP VERSION ==== ##
__version__ = "14.67"

## == APP ASPECT RATIO == ##

window_aspect_ratio(9, 16, -5.8) # Width, Height, Scale

## == SCREENS == ##
#(Main Screen In features.py)#
class Info(Screen):
	pass

class Setting(Screen):
	pass

class WindowManager(ScreenManager):

	maintheme = StringProperty("#00D1FF")
	background = StringProperty("#202124")
	card = StringProperty("#E1DADA")
	micdown = StringProperty("#282F42")
	micnormal = StringProperty("#2F384F")

	def change_theme_cyan(self):
		self.maintheme = "#00D1FF"
		self.background = "#202124"
		self.micdown = "#282F42"
		self.micnormal = "#2F384F"
		with open("theme.txt","w+") as f:
			f.write("cyan")
	
	def change_theme_matrix(self):
		self.maintheme = "#00FF00"
		self.background = "#000000"
		self.micdown = "#00FF00"
		self.micnormal = "#000000"
		with open("theme.txt","w+") as f:
			f.write("matrix")

	def change_theme_pinkanta(self):
		self.maintheme = "#E415DC"
		self.background = "#202124"
		self.micdown = "#282F42"
		self.micnormal = "#2F384F"
		with open("theme.txt","w+") as f:
			f.write("pinkanta")

	f = open("theme.txt", "r")
	theme = f.read()
	f.close()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		if self.theme == "cyan": self.change_theme_cyan()
		elif self.theme == "matrix": self.change_theme_matrix()
		elif self.theme == "pinkanta": self.change_theme_pinkanta()
	
	examples = StringProperty('''1. Telling the current date,time,month or year.
    eg: Orator what is the time/month/date/year ?
2. Opening a website in your default web browser.
    eg: Orator search on google github.com
3. Searching anything you say on the wikipedia.
    eg: Orator search on wikipedia Who is rick astley
4. Searching anything you say on YouTube.
    eg: Orator search on youtube Sidemen
5. Opening any application on your desktop.
    eg: Orator open Spotify
6. Writing down anything you say on the notepad.
    eg: Orator note down today is my birthday
7. Can tell you some good jokes and even facts!
    eg: Orator tell me a joke/fact''')

## ==== GUI SCRIPT ==== ##
kvfile = Builder.load_file("mymain.kv")

## == MAIN APP BUILD == ##
class VAApp(App):
	def build(self):
		return kvfile

## == RUNNING APP == ##
if __name__ == "__main__":
	VAApp().run()