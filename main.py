from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoEditTestApp(App):
    pass

class Display(Screen):
    pass

images = ["dualvector.jpeg", "hypersphere.jpeg", "pyramid.jpeg", "venus.jpeg"]
image0 = "placeholder.png"


PhotoEditTestApp().run()