## == REQUIRED KIVY MODULES == ##
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock, mainthread

## ==== FEATURES SCRIPT ==== ##
from features import *

## ==== THEME FILE ==== ##
with open("theme.txt", "r+") as f:
	if f.read() == "":
		f.write("cyan")


## ==== APP VERSION ==== ##
__version__ = "14.63"

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

	def change_theme_cyan(self):
		self.maintheme = "#00D1FF"

		with open("theme.txt","w+") as f:
			f.write("cyan")
	
	def change_theme_matrix(self):
		self.maintheme = "#00FF00"

		with open("theme.txt","w+") as f:
			f.write("matrix")

	def change_theme_pinkanta(self):
		self.maintheme = "#E415DC"

		with open("theme.txt","w+") as f:
			f.write("pinkanta")

	f = open("theme.txt", "r")
	theme = f.read()
	
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		if self.theme == "cyan": self.change_theme_cyan()
		elif self.theme == "matrix": self.change_theme_matrix()
		elif self.theme == "pinkanta": self.change_theme_pinkanta()
	

## ==== GUI SCRIPT ==== ##
kvfile = Builder.load_file("mymain.kv")

## == MAIN APP BUILD == ##
class VAApp(App):
	def build(self):
		return kvfile

## == RUNNING APP == ##
if __name__ == "__main__":
	VAApp().run()