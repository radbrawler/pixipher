from tkinter import *
from tkinter.filedialog import askopenfilename
from imread import imread
from matplotlib import pylab as plt
from PIL import Image, ImageTk


class Window(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.initWindow()

    def initWindow(self):
        # changing the title of our master widget
        self.master.title("Pixipher")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a menu instance
        menu = Menu(self.master)
        self.master.config(menu=menu)

        # create the file object)
        file = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        file.add_command(label="Exit", command=self.clientExit)

        #added "file" to our menu
        menu.add_cascade(label="File", menu=file)

        # create the file object
        edit = Menu(menu)

        # adds a command to the menu option, calling it exit, and the
        # command it runs on event is client_exit
        edit.add_command(label="Show Img", command=self.openImage)
        # edit.add_command(label="Show Text", command=self.showText)

        # added "file" to our menu
        menu.add_cascade(label="Edit", menu=edit)

        connect = Menu(menu)
        connect.add_command(label="Listen", command="")
        connect.add_command(label="Broadcast", command="")
        menu.add_cascade(label="Connect", menu=connect)

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
