import json
import socket
from tkinter import messagebox, simpledialog
import threading
import tkinter


class Sender:
    def __init__(self, parent, window, senderName, senderPort):
        self.sender_name = senderName
        self.sender_port = senderPort
        print(self.sender_name)
        print(self.sender_port)
        self.sender_socket = None
        self.window = window

        window.update_status_bar("Sending Image")

        threading.Thread(target=self.listen, args=[self]).start()

        # b = Button(top, text="OK", command=self.ok)
        # b.pack(pady=5)

    @staticmethod
    def listen(self):
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sender_socket.bind((self.sender_name, self.sender_port))
        print(" Sender port open Name:" + self.sender_name + " Port:" + str(self.sender_port))
        self.sender_socket.listen(5)
        print("Listening ....")
        while True:
            client_socket, client_address = self.sender_socket.accept()
            print("Connection Received from", client_address, ". Do you want to accept connection .??")
            config = json.load(open("config.json", encoding='utf-8'))
            connection_choice = str(config["connection_choice"])
            print(connection_choice)
            if connection_choice == "True":
                client_socket.settimeout(60)
                tkinter.messagebox.showinfo("info", "message")
                print("Connected to - ", client_socket, client_address)
                print("Receiving")
                s = open('torecv.png', 'wb')
                size = 1024
                l = client_socket.recv(size)
                print(l)
                while l:
                    s.write(l)
                    l = client_socket.recv(size)
                    print(l)

                s.close()
                client_socket.close()

            elif connection_choice == "False":
                print("Connection rejected from ", client_address)
                client_socket.send(bytearray("Connection Rejected from server side " + str(self.sender_socket),
                                             encoding='utf-8'))
                client_socket.close()

        print("Disconnected")

    @staticmethod
    def send_image(self, master, image):
        dest_host = simpledialog.askstring("Destination Host", "Enter Destination Host name")
        dest_port = simpledialog.askinteger("Destination Port", "Enter Destination Port name")
        client_socket = socket.socket()
        client_socket.connect((dest_host, dest_port))
        print("Connected to" + str(dest_port))
        f = open(image, 'rb')
        print("Sending ... ")
        l = f.read(1024)
        while l:
            print("Sending ... ")
            client_socket.send(l)
            l = f.read(1024)

        f.close()
        print("Done Sending ... ")
        print(client_socket.recv(1024))
        client_socket.close()

