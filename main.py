from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoEditTestApp(App):
    pass

class Display(Screen):
    def verify_image(self, text):
        if self.ids.name.text not in images:
            return image0
        else:
            if self.ids.name.text == images[0]:
                return images[0]
            elif self.ids.name.text == images[1]:
                return images[1]
            elif self.ids.name.text == images[2]:
                return images[2]
            elif self.ids.name.text == images[3]:
                return images[3]
    def display_image(self):
        if self.verify_image(self.ids.name.text) == image0:
            return image0
        elif self.verify_image(self.ids.name.text) == "dualvector.jpeg":
            return images[0]
        elif self.verify_image(self.ids.name.text) == "hypersphere.jpeg":
            return images[1]
        elif self.verify_image(self.ids.name.text) == "pyramid.jpeg":
            return images[2]
        elif self.verify_image(self.ids.name.text) == "venus.jpeg":
            return images[3]

images = ["dualvector.jpeg", "hypersphere.jpeg", "pyramid.jpeg", "venus.jpeg"]
image0 = "placeholder.png"


PhotoEditTestApp().run()