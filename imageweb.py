from kivy.app import App
from kivy.uix.image import Image, AsyncImage

class MinhaApp(App):
    def build(self):

        return AsyncImage(source='https://lh3.googleusercontent.com/V8vdLyruROpGL211Ucrzly_9ZagiG2lttAikhgnhPhy9cTs9THvPokb8O-Dv3tE4TUnDryphrnwA1ZwI_lB0MzYYSA=w640-h400-e365-rj-sc0x00ffffff')

if __name__ == "__main__":
    MinhaApp().run()