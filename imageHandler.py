from tkinter.filedialog import askopenfilename
from tkinter import *

from PIL import Image, ImageTk


class ImageHandler:
    def __init__(self, window, sizex=300, sizey=300):
        self.window = window
        # print("Window object is", window)
        self.size = [sizex, sizey]

    def openImageDialog(self, window):
        self.filename = askopenfilename(filetypes=(("All files", "*.*"),
                                               ("JPEG Files", "*.jpg")))

        print("Opened File: " + self.filename)
        self.showImage()
        # mainWindow.MainWindow.enable_encryption(self.window)

        # print("Window object in ImageDialog function is", window)
        # print("Filename in image handler is", window.filename)
        window.update_filename(self.filename)

    def showImage(self):
        image = Image.open(self.filename)
        image.thumbnail(self.size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)

        img = Label(self.window, image=render)
        img.image = render
        img.place(x=10, y=10)
