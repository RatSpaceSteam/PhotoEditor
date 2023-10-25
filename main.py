from PIL import Image
from kivy.app import App
from kivy.uix import image
from kivy.uix.screenmanager import Screen


class PhotoEditTestApp(App):
    pass

class Display(Screen):
    def oldtimey(self):
        pass
    def inverse(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                r = 255 - pixels[x, y][0]
                g = 255 - pixels[x, y][1]
                b = 255 - pixels[x, y][2]
                red = (pixels[x, y][0] * 0) + r
                green = (pixels[x, y][1] * 0) + g
                blue = (pixels[x, y][2] * 0) + b
                pixels[x, y] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_inverse.png")
        self.ids.pic.source = name + "_inverse.png"
    def linedrawing(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()

        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_linedrawing.png")
        self.ids.pic.source = name + "_linedrawing.png"
    def pointilism(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()

        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_pointilism.png")
        self.ids.pic.source = name + "_pointilism.png"
    def sepia(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                red = int(pixels[x, y][0] * 0.393) + int(pixels[x, y][1] * 0.769) + int(pixels[x, y][2] * 0.189)
                green = int(pixels[x, y][0] * 0.349) + int(pixels[x, y][1] * 0.686) + int(pixels[x, y][2] * 0.168)
                blue = int(pixels[x, y][0] * 0.272) + int(pixels[x, y][1] * 0.534) + int(pixels[x, y][2] * 0.131)
                pixels[x, y] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_sepia.png")
        self.ids.pic.source = name + "_sepia.png"
    def pixelate(self):
        img = Image.open(self.ids.pic.source)
        pixels = img.load()
        for i in range(0, img.size[1] - 20, 20):
            for j in range(0, img.size[0] - 20, 20):
                red = pixels[j, i][0]
                green = pixels[j, i][1]
                blue = pixels[j, i][2]
                for k in range(i, i + 20):
                    for l in range(j, j + 20):
                        pixels[k, l] = (red, green, blue)
        index = self.ids.pic.source.find(".")
        name = self.ids.pic.source[0:index]
        img.save(name + "_pixelate.png")
        self.ids.pic.source = name + "_pixelate.png"





PhotoEditTestApp().run()