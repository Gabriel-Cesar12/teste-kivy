from kivy.app import App
from kivy.uix.label import Label 

class MinhaApp(App):
    def build (self):
        return Label(
            text='Olá, SENAI',
            halign='left', # Alinha o texto à esquerda
            valign='top', #alinha o texto no topo
            size_hint=(None, None),
            size= (150, 50),
            text_size=(150, None)
            
        )

if __name__ == "__main__":
    MinhaApp().run()