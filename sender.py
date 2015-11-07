import socket


class Sender:
    def __init__(self, senderName, senderPort):
        self.senderName = senderName
        self.senderPort = senderPort

    def open_connection(self):
        senderSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        senderSocket.bind((self.senderName, self.senderPort))
        senderSocket.listen(5)
