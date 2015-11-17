from tkinter import *

import sender
import client
import imageHandler
import encryption


class MainWindow(Frame):
    def __init__(self, master=None):

        Frame.__init__(self, master)
        self.master = master
        self.filename = None

        self.master.title("Pixipher")
        self.pack(fill=BOTH, expand=1)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.file = Menu(self.menu)  # File Menu
        self.file.add_command(label="Open", command=imageHandler.ImageHandler(root, self.filename).openImageDialog)
        # file.add_command(label="Open", command=self.openImage)
        self.file.add_command(label="Save As", command=self.save_image())
        self.file.add_command(label="Exit", command=self.client_exit)
        self.menu.add_cascade(label="File", menu=self.file)

        self.preferences = Menu(self.menu)  # Edit Menu
        self.preferences.add_command(label="Encrypt Document", command=encryption.Encryption)
        self.preferences.add_command(label="Decrypt Document", command="")
        self.preferences.add_command(label="Set Parameters", command="")
        self.menu.add_cascade(label="Preferences", menu=self.preferences)
        self.disable_preferences()

        self.connect = Menu(self.menu)  # Connect Menu
        self.connect.add_command(label="Open Connection", command=self.open)
        self.connect.add_command(label="Establish Connection", command=self.con)
        self.menu.add_cascade(label="Connect", menu=self.connect)

    @staticmethod
    def init_window():
        print(" Initialising Main Window")

    @staticmethod
    def open():
        sender.Sender("127.0.0.1", 9125).open_connection()

    @staticmethod
    def con():
        client.Client("127.0.0.1", 9125).connect()

    @staticmethod
    def save_image():
        print("Saving Image not done yet")

    @staticmethod
    def client_exit():
        exit()

    def enable_encryption(self):
        self.menu.entryconfig("Preferences", state="normal")

    def disable_preferences(self):
        self.menu.entryconfig("Preferences", state="disabled")

if __name__ == "__main__":
    root = Tk()
    root.geometry("800x400")
    print("In Main Loop")
    app = MainWindow(root)
    root.mainloop()
