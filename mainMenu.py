from tkinter import *
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

import sender
import client


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.initWindow()

    def initWindow(self):
        self.master.title("Pixipher")
        self.pack(fill=BOTH, expand=1)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)  # File Menu
        file.add_command(label="Exit", command=self.clientExit)
        menu.add_cascade(label="File", menu=file)

        edit = Menu(menu)  # Edit Menu
        edit.add_command(label="Show Img", command=self.openImage)
        menu.add_cascade(label="Edit", menu=edit)

        connect = Menu(menu)  # Connect Menu
        connect.add_command(label="Open Connection", command=self.ope)
        connect.add_command(label="Establish Connection", command=self.con)
        menu.add_cascade(label="Connect", menu=connect)

    @staticmethod
    def ope():
        sender.Sender("127.0.0.1", 9125).open_connection()

    @staticmethod
    def con():
        client.Client("127.0.0.1", 9125).connect()

    def openImage(self):
        print("Opening File")
        filename1 = askopenfilename(filetypes=(("All files", "*.*"),
                                               ("JPEG Files", "*.jpg")))

        size =300, 300
        print("Opened File: " + filename1)
        image = Image.open(filename1)
        image.thumbnail(size, Image.ANTIALIAS)
        render = ImageTk.PhotoImage(image)

        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=10)

    def saveImage(self):
        print("Saving Image")

    def clientExit(self):
        exit()


if __name__ == "__main__":
    root = Tk()
    root.geometry("800x400")
    print("In Main Loop")
    app = Window(root)
    root.mainloop()
