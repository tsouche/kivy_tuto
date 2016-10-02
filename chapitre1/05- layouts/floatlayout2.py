# File name: floatlayout.py
import kivy
kivy.require('1.7.0')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

class FloatLayout2App(App):
    def build(self):
        return FloatLayout()

if __name__=="__main__":
    FloatLayout2App().run()
