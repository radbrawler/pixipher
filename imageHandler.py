from tkinter.filedialog import askopenfilename
import tkinter as tk

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
        self.showImage(self.filename, erase=True)
        # mainWindow.MainWindow.enable_encryption(self.window)

        # print("Window object in ImageDialog function is", window)
        # print("Filename in image handler is", window.filename)
        window.update_filename(self.filename)

    def showImage(self, file_name, xi=40, yi=40, erase=False):
        image = Image.open(file_name)
        try:
            image.load()
        except IOError:
            pass # You can always log it to logger

        if erase:
            print("In erase func")
            im_blank = Image.open("blank.png")
            im_blank.load()

            im_blank.thumbnail([850, 800], Image.ANTIALIAS)
            render2 = ImageTk.PhotoImage(im_blank)

            img_2 = tk.Label(self.window, image=render2)
            img_2.image = render2
            img_2.place(x=0, y=0)

        image.thumbnail(self.size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)

        img = tk.Label(self.window, image=render)
        img.image = render
        img.place(x=xi, y=yi)
