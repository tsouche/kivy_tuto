from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import Image
 
class Example1(App):
 
    def build(self):
        #define the carousel
        carousel = Carousel(direction='right',loop='true')
        for i in range(1,7):
            #load pictures from images folder
            src = "images/%d.png" % i
            image = Image(source=src,pos=(400, 100), size=(200, 80))
            carousel.add_widget(image)
        return carousel
 
if __name__ == '__main__':
    Example1().run()