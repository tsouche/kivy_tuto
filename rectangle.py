from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.graphics import Color, Rectangle
from functools import partial
 
class CanvasApp(App):
 
    #function to add rectangle to screen
    def add_rects(self,wid,*largs):
        with wid.canvas:
                Color(1, 0, 0, .5, mode='rgba')
                wid.rect = Rectangle(pos=(200,200), size=(300,300))
                 
    #function to clear rectangle from screen
    def reset_rects(self,wid,*largs):
        wid.canvas.clear()
 
    def build(self):
        wid = Widget()
          
        #calling function with default arguments
        btn_add = Button(text='Draw rectangle',on_press=partial(self.add_rects,wid,'Adding a rectangle'))
        btn_clear = Button(text='Clear',on_press=partial(self.reset_rects,wid,'Clear the canvas'))
 
        layout = GridLayout(cols=1,rows=2)
        layout.add_widget(btn_add)
        layout.add_widget(btn_clear)
        root=GridLayout()
        root.add_widget(wid)
        root.add_widget(layout)
 
        return root
 
if __name__ == '__main__':
    CanvasApp().run()
    