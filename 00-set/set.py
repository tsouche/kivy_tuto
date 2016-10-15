# File name: layouts2.py
import kivy
from gi.overrides.Gdk import Color
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, BoundedNumericProperty
from kivy.properties import StringProperty
from random import randint

constant_card_height = 150
constant_card_width  = 100
constant_nb_cols = 4
constant_nb_rows = 3
constant_spacing = 10
constant_padding = 10
constant_table_width  =  constant_card_width *  constant_nb_cols      \
                      +     constant_spacing * (constant_nb_cols - 1) \
                      +     constant_padding * 2
constant_table_height = constant_card_height *  constant_nb_rows      \
                      +     constant_spacing * (constant_nb_rows - 1) \
                      +     constant_padding * 2

class Card(Button):

    card_width = NumericProperty()
    card_height = NumericProperty()
    i = BoundedNumericProperty(0, min=0, max=4)
    j = BoundedNumericProperty(0, min=0, max=3)
    c = BoundedNumericProperty(0, min=0, max=3)
    s = BoundedNumericProperty(0, min=0, max=3)
    f = BoundedNumericProperty(0, min=0, max=3)
    n = BoundedNumericProperty(0, min=0, max=3)
    code = StringProperty()
    filename = StringProperty()
    selected = False
    
    def __init__(self, ic, jc, card_code):
        # filepath = "/data/code/setgame/client/images/"
        filepath = "./../../setgame/client/images/"
        super(Card, self).__init__()
        self.card_width  = constant_card_width
        self.card_height = constant_card_height
        self.i = ic
        self.j = jc
        self.code = card_code
        self.c = int(card_code[0])
        self.s = int(card_code[1])
        self.f = int(card_code[2])
        self.n = int(card_code[3])
        self.filename = filepath + self.code + ".png"
        # print("BOGUS00: i=", ic, "- j=", jc, ":", self.filename)
        
    def select(self):
        self.selected = (self.selected == False)

    def build(self):
        return self

class CardOnTable(RelativeLayout):
    
    def __init__(self, ic, jc, card_code):
        super(CardOnTable, self).__init__()
        self.add_widget(Card(ic,jc,card_code))

    def build(self):
        return self

class Table(GridLayout):
    
    def index(self, i, j):
        return i + j*constant_nb_cols
    
    def __init__(self):
        super(Table, self).__init__()
        # self.size = (constant_table_width, constant_table_height)
        # self.cols = constant_nb_cols
        # self.rows = constant_nb_rows
        # self.col_default_width  = constant_card_width
        # self.row_default_height = constant_card_height
        self.positions = []
        for j in range(0,constant_nb_rows):
            for i in range(0,constant_nb_cols):
                code = str(randint(0,2))+str(randint(0,2))+str(randint(0,2))+str(randint(0,2))
                self.positions.append(CardOnTable(i,j,code))
        for j in range(0,constant_nb_rows):
            for i in range(0,constant_nb_cols):
                self.add_widget(self.positions[self.index(i,j)])


class SetApp(App):
    def build(self):
        table = Table()
        return table

if __name__=="__main__":
    SetApp().run()
