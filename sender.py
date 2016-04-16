import json
import socket
from tkinter import messagebox
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
                    if str(l) == "request_connection":
                        print("Connection Accepted")
                        self.connection_request()
                    elif str(l) == "sending file":
                        print("Remote sending Files")
                        pass
                    l = client_socket.recv(size)
                    print(l)
                s.close()
                client_socket.send(bytearray("Thanks for Connecting !!", 'utf-8'))

            elif connection_choice == "False":
                print("Connection rejected from ", client_address)
                client_socket.send(bytearray("Connection Rejected from server side " + str(self.sender_socket),
                                             encoding='utf-8'))
                client_socket.close()

        print("Disconnected")

    def send_image(self, image):
        self.sender_socket.send(image)
        f = open(image, 'rb')
        print("Sending ... ")
        l = f.read(1024)
        while(1):
            print("Sending ... ")
            self.sender_socket.send(1)
            l = f.read(1024)

        f.close()
        print("Done Sending ... ")
        print(self.sender_socket.recv(1024))

