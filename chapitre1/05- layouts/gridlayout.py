# File name: gridlayout.py
import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class Card(Button):
    def __init__(self, i, j):
        super(Card).__init__()
        self.i = i
        self.j = j
        
    def build(self, i, j):
        return self

class TableApp(App):
    def build(self):
        table = GridLayout(cols=4, rows=3)
        for i in range(0,4):
            for j in range(0,3):
                table.add_widget(Card(i,j))
        return table

if __name__=="__main__":
    TableApp().run()
