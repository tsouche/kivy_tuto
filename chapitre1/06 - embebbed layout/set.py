# File name: layouts2.py
import kivy
from gi.overrides.Gdk import Color
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.properties import BoundedNumericProperty
from kivy.properties import StringProperty
from random import randint



class Card(Button):

    i = BoundedNumericProperty(0, min=0, max=4)
    j = BoundedNumericProperty(0, min=0, max=3)
    c = BoundedNumericProperty(0, min=0, max=3)
    s = BoundedNumericProperty(0, min=0, max=3)
    f = BoundedNumericProperty(0, min=0, max=3)
    n = BoundedNumericProperty(0, min=0, max=3)
    code = StringProperty()
    
    def __init__(self, ic, jc, card_code):
        super(Card, self).__init__()
        self.i = ic
        self.j = jc
        self.code = card_code
        self.c = int(card_code[0])
        self.s = int(card_code[1])
        self.f = int(card_code[2])
        self.n = int(card_code[3])
            
    def build(self):
        return self

class PositionOnTable(RelativeLayout):
    
    def __init__(self, ic, jc, card_code):
        super(PositionOnTable, self).__init__()
        self.add_widget(Card(ic,jc,card_code))

    def build(self):
        return self

class Table(GridLayout):
    pass

class SetApp(App):
    def build(self):
        table = Table()
        for j in range(0,3):
            for i in range(0,4):
                code = str(randint(0,2))+str(randint(0,2))+str(randint(0,2))+str(randint(0,2))
                table.add_widget(PositionOnTable(i,j,code))
        return table

if __name__=="__main__":
    SetApp().run()
