import socket


class Sender:
    def __init__(self, senderName, senderPort):
        self.senderName = senderName
        self.senderPort = senderPort
        print(self.senderName)
        print(self.senderPort)

    def open_connection(self):
        senderSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        senderSocket.bind((self.senderName, self.senderPort))
        print(" Sender port open Name:" + self.senderName + " Port:" + str(self.senderPort))
        senderSocket.listen(5)
        print("Listening ....")
        clientSocket, clientAddress = senderSocket.accept()
        print("Connected to - ", clientSocket, clientAddress)

    def send_image(self, image):
