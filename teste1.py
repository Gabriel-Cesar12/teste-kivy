from kivy.app import App
from kivy.uix.button import Button

class MyApp (App):
    def build(self):
        return Button(text='Helo world! This is my firts progam in kivy \n I m a Sesiano student, and I love my teacher')
if __name__ == '__main__':
    MyApp().run()