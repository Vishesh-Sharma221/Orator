## == REQUIRED KIVY MODULES == ##
from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock

## ==== FEATURES SCRIPT ==== ##
from features import *

## ==== APP VERSION ==== ##
__version__ = "14.53"

## == APP ASPECT RATIO == ##
window_aspect_ratio(9, 19.5, 0) # Width, Height, Scale

## == SCREENS == ##
#(Main Screen In features.py)#
class Info(Screen):
	pass

class Settings(Screen):
	pass

class WindowManager(ScreenManager):
	pass

## ==== GUI SCRIPT ==== ##
kvfile = Builder.load_file("mymain.kv")

## == MAIN APP BUILD == ##
class VAApp(App):
	def build(self):
		return kvfile

## == RUNNING APP == ##
if __name__ == "__main__":
	VAApp().run()