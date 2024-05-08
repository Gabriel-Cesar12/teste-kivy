from kivy.app import App
from kivy.uix.carousel import Carousel
from kivy.uix.label import Label
from kivy.uix.image import  AsyncImage

class CarouselApp(App):
    def build(self):

        carousel = Carousel(direction='right', loop=True)

        imagens = ['https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKfVFYL7lWtCkJCeCPqIKCXhqdHj0fQ5x3Dfr590q5-A&s', 'https://scc10.com.br/wp-content/uploads/2024/04/obito-2.jpg.webp', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/8a771de5-7203-4197-a993-247cc3907855/dfw7s12-6bf57907-27b1-45b6-a038-10f276aab1be.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzhhNzcxZGU1LTcyMDMtNDE5Ny1hOTkzLTI0N2NjMzkwNzg1NVwvZGZ3N3MxMi02YmY1NzkwNy0yN2IxLTQ1YjYtYTAzOC0xMGYyNzZhYWIxYmUuanBnIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.kwFeVmUT2-bh1JEhG_rVO5COMKITXlu5Dt8ZS2kgWK0']
        for imagem in imagens:
            imagem_widget = AsyncImage(source=imagem)
            carousel.add_widget(imagem_widget)

        return carousel
    
if __name__ == "__main__":
    CarouselApp().run()
