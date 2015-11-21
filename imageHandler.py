from tkinter.filedialog import askopenfilename
from tkinter import *

from PIL import Image, ImageTk


class ImageHandler:
    def __init__(self, window, filename, sizex=300, sizey=300):
        self.filename = filename
        self.window = window
        self.size = [sizex, sizey]

    def openImageDialog(self):
        self.filename = askopenfilename(filetypes=(("All files", "*.*"),
                                               ("JPEG Files", "*.jpg")))

        print("Opened File: " + self.filename)
        self.showImage()
        #mainWindow.MainWindow.enable_encryption(self.window)
        return self.filename

    def showImage(self):
        image = Image.open(self.filename)
        image.thumbnail(self.size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)

        img = Label(self.window, image=render)
        img.image = render
        img.place(x=10, y=10)
