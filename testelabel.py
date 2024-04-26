from kivy.app import App
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

class MinhaApp(App):
    def build(self):
        return Label(text='#GO LOUD', font_size=50, font_name='verdana',color=get_color_from_hex('#006400'))    
    
if __name__ == "__main__":
    MinhaApp().run()