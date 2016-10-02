from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.factory import Factory
from kivy.uix.image import Image
 
class Example1(App):
 
    def build(self):
        carousel = Carousel(direction='right',loop='true')
         
        for i in range(1,5):
            src = "http://placehold.it/480x270.png&text=slide-%d&.png" % i
            #load images asynchronously
            image = Factory.AsyncImage(source=src, allow_stretch=True)
            carousel.add_widget(image)
        return carousel
 
if __name__ == '__main__':
    Example1().run()
    