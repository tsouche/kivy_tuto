from kivy.app import App
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.uix.scatter import Scatter
from kivy.animation import Animation
from kivy.graphics import Color, Rectangle

class ExampleWidget(Widget):
    def __init__(self, **kwargs):
        super(ExampleWidget, self).__init__(**kwargs)
        self.size = (100,100)
        self.pos = (100,100)
        with self.canvas:
            Color(1,0,0)
            self.texture = Rectangle(size=self.size, pos=self.pos)

    def on_pos(self, obj, value):
        try: self.texture.pos = value
        except: pass

class ExampleScatterTexture(Widget):
    def __init__(self, **kwargs):
        super(ExampleScatterTexture, self).__init__(**kwargs)
        with self.canvas:
            Color(0,1,0)
            texture = Rectangle(size=self.size, pos=self.pos)

class ExampleScatter(Scatter):
    def __init__(self, **kwargs):
        super(ExampleScatter, self).__init__(**kwargs)
        self.do_rotation = False
        self.do_scale = False
        self.do_translation = False
        self.size = (100,100)
        self.pos = (100,300)
        texture = ExampleScatterTexture(size=self.size)
        self.add_widget(texture)

class ExampleScreen(Widget):
    def __init__(self, **kwargs):
        super(ExampleScreen, self).__init__(**kwargs)
        self.size = Window.size

        example_widget = ExampleWidget()
        self.add_widget(example_widget)

        example_scatter = ExampleScatter()
        self.add_widget(example_scatter)

        #SCATTER IS GREEN, WIDGET IS RED
        example_widget_animation = Animation(pos=(300,100), duration=2., t='out_elastic') + Animation(pos=(100,100), duration=2., t='in_bounce')
        example_scatter_animation = Animation(pos=(300,300), duration=2., t='in_bounce') + Animation(pos=(100,300), duration=2., t='in_bounce')
        example_widget_animation.repeat = True
        example_scatter_animation.repeat = True
        example_widget_animation.start(example_widget)
        example_scatter_animation.start(example_scatter)

class BadAnimationExample(App):
    def build(self):
        root = ExampleScreen()
        return root

if __name__ == "__main__":
    BadAnimationExample().run()
