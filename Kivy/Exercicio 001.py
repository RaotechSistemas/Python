import kivy
kivy.require('2.0.0')
 
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.widget import Widget
 
class ShowImage(Image):
    pass
 
class MyApp(App):
    def build(self):
        return ShowImage(source='folhaGigante.jpg',pos=(0,0),size=(512,512))
 
if __name__ == '__main__':
    MyApp().run()