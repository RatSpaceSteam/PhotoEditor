from PIL.Image import Image
from kivy.app import App
from kivy.uix.screenmanager import Screen


class PhotoEditTestApp(App):
    pass

class Display(Screen):
    def oldtimey(self, text):
        pass
    def inverse(self, text):
        pass
    def linedrawing(self, text):
        pass
    def pointilism(self, text):
        pass
    def sepia(self, text, format):
        img = Image(self.ids.name.text)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = int(pixels[x, y][0] * 0.393) + int(pixels[x, y][1] * 0.769) + int(pixels[x, y][2] * 0.189)
                green = int(pixels[x, y][0] * 0.349) + int(pixels[x, y][1] * 0.686) + int(pixels[x, y][2] * 0.168)
                blue = int(pixels[x, y][0] * 0.272) + int(pixels[x, y][1] * 0.534) + int(pixels[x, y][2] * 0.131)
                pixels[x, y] = (red, green, blue)
        img.save(self.ids.name.text[0:-5] + "_sepia.png")
        return img
    def pixelate(self, text):
        pass

images = ["dualvector.jpeg", "hypersphere.jpeg", "pyramid.jpeg", "venus.jpeg"]
image0 = "placeholder.png"


PhotoEditTestApp().run()