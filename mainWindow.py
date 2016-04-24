import json
import socket
from tkinter import *
import sys

import sender
import client
import imageHandler
import encryption
import decryption


class MainWindow(Frame):
    def __init__(self, master=None):

        self.init_config_json()

        print(sys.path)
        Frame.__init__(self, master)
        self.master = master
        self.filename = None
        self.s = None

        # print("Self Object is", self)
        # print("Master Object is", master)

        self.master.title("Pixipher v1.0")
        self.pack(fill=BOTH, expand=1)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        # # ***** Status Bar *****
        self.variable = StringVar()
        self.status = Label(self, bd=1, relief=SUNKEN, anchor=E,
                            textvariable=self.variable)
        self.variable.set('Status Bar')
        self.status.pack(side=BOTTOM, fill=X)

        print(type(self.master))
        # config = json.load(open("config.json", encoding='utf-8'))
        # host = str(config["server_host"])
        # port = int(str(config["server_port"]))
        # self.s = sender.Sender(self.master, self, host, port)
        # self.master.title("Pixipher running on " + str(port))

        # File Menu
        self.file = Menu(self.menu)
        self.file.add_command(label="Open", command=lambda: imageHandler.ImageHandler(app).openImageDialog(app))
        # file.add_command(label="Open", command=self.openImage)1
        # self.file.add_command(label="Image Properties", command=self.properties)
        self.file.add_command(label="Exit", command=self.master.destroy)
        self.menu.add_cascade(label="File", menu=self.file)

        # Edit Menu
        self.preferences = Menu(self.menu)
        self.preferences.add_command(label="Encrypt Image",
                                     command=lambda: encryption.Encryption(self.filename, window=app).encrypt_file())
        self.preferences.add_command(label="Decrypt Image",
                                     command=lambda: decryption.Decryption(self.filename, window=app).decrypt_file())
        self.menu.add_cascade(label="Preferences", menu=self.preferences)
        #self.disable_preferences()

        # Send Menu
        self.send = Menu(self.menu)
        self.send.add_command(label="Send Image", command=self.send_im)
        self.send.add_command(label="Receive Image", command=self.receive_im)
        # self.send.add_command(label="Receive Image", command=self.rec)
        self.menu.add_cascade(label="Send", menu=self.send)

        if self.filename is None:
            self.menu.entryconfig("Preferences", state="normal")
            print("Menu Disabled")
        else:
            self.menu.entryconfig("Preferences", state="normal")
            print("Menu Enabled")

        # ----------------------
        # Sockets Initialization
        # ----------------------
        # self.sock = sender.Sender()

    @staticmethod
    def init_config_json():
        file = open("config.json", "w")
        host = str(socket.gethostname())
        config = {
            "server_host": "192.168.43.50",
            "server_port": "18999",
            "connection_choice": "True",
            "parameter_arnold": "3.75",
            "parameter_temp_ki": "0.46",
            "parameter_u": "2",
            "parameter_v": "3",
        }
        file.write(json.dumps(config, indent=4))
        file.close()

    def update_filename(self, fname):
        print("Object in function is ", self, fname)
        self.filename = fname

    # This function will update the statusBar by changing the VarString
    # variable -> variable
    def update_status_bar(self, string):
        self.variable.set(string)

    @staticmethod
    def properties(self):
        top_level = Toplevel()
        img = Image.open(self.filename)
        print(img)
        display_text = "This is text \n" \
                    "with \n\n\n\nnewline chars" \
                    "inserted in between"
        label1 = Label(top_level, text=display_text, width=40)
        label1.pack()
        button = Button(top_level, text="OK", command=top_level.destroy)
        button.pack()

    @staticmethod
    def init_window():
        print(" Initialising Main Window")

    def send_im(self):
        print("In send")
        config = json.load(open("config.json", encoding='utf-8'))
        host = str(config["server_host"])
        port = int(str(config["server_port"]))
        w = sender.Sender(self.master, self, host, port)
        w.send_image(self, self.master, self.filename)

    def receive_im(self):
        print("In receive Image")
        config = json.load(open("config.json", encoding='utf-8'))
        host = str(config["server_host"])
        port = int(str(config["server_port"]))
        self.s = sender.Sender(self.master, self, host, port)

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


if __name__ == "__main__":
    root = Tk()

    logo = PhotoImage(file='icon4.png')
    root.tk.call('wm', 'iconphoto', root._w, logo)
    root.geometry("720x500")
    app = MainWindow(master=root)

    root.mainloop()
