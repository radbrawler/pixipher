from tkinter import *
import sys

import sender
import client
import imageHandler
import encryption
import decryption


class MainWindow(Frame):
    def __init__(self, master=None):

        print(sys.path)
        Frame.__init__(self, master)
        self.master = master
        self.filename = None

        # print("Self Object is", self)
        # print("Master Object is", master)

        self.master.title("Pixipher v1.0")
        self.pack(fill=BOTH, expand=1)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # File Menu
        self.file = Menu(self.menu)
        self.file.add_command(label="Open", command=lambda: imageHandler.ImageHandler(app).openImageDialog(app))
        # file.add_command(label="Open", command=self.openImage)
        self.file.add_command(label="Save As", command=self.save_image)
        self.file.add_command(label="Exit", command=self.client_exit)
        self.menu.add_cascade(label="File", menu=self.file)

        self.preferences = Menu(self.menu)  # Edit Menu
        self.preferences.add_command(label="Encrypt Image",
                                     command=lambda: encryption.Encryption(self.filename, window=app).encrypt_file())
        self.preferences.add_command(label="Decrypt Image",
                                     command=lambda: decryption.Decryption(self.filename, window=app).decrypt_file())
        self.preferences.add_command(label="Set Parameters", command="")
        self.menu.add_cascade(label="Preferences", menu=self.preferences)
        #self.disable_preferences()

        self.send = Menu(self.menu)  # Send Menu
        self.send.add_command(label="Send Image", command=self.send())
        self.send.add_command(label="Receive Image", command=self.rec)
        self.menu.add_cascade(label="Send", menu=self.send)

        if self.filename is None:
            self.menu.entryconfig("Preferences", state="normal")
            print("Menu Disabled")
        else:
            self.menu.entryconfig("Preferences", state="normal")
            print("Menu Enabled")

        # # ***** Status Bar *****
        self.variable = StringVar()
        self.status = Label(self, bd=1, relief=SUNKEN, anchor=E,
                            textvariable=self.variable)
        self.variable.set('Status Bar')
        self.status.pack(side=BOTTOM, fill=X)

    def update_filename(self, fname):
        print("Object in function is ", self, fname)
        self.filename = fname

    # This function will update the statusBar by changing the VarString
    # variable -> variable
    def update_status_bar(self, string):
        self.variable.set(string)

    @staticmethod
    def init_window():
        print(" Initialising Main Window")

    @staticmethod
    def send(self):
        print("In send")
        sender.Sender(app, "localhost", 9999).send_image(self.filename)

    def rec(self):
        client.Client.recv_image()

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

    # def enable_encryption(self):

    # def disable_preferences(self):


if __name__ == "__main__":
    root = Tk()

    logo = PhotoImage(file='icon4.png')
    root.tk.call('wm', 'iconphoto', root._w, logo)
    root.geometry("720x500")
    print("In Main Loop")
    app = MainWindow(root)
    print("App object is ", app)
    app.update_filename("anmol")

    root.mainloop()
