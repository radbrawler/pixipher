import socket


class Client:
    def __init__(self, clientName, clientPort):
        self.clientName = clientName
        self.clientPort = clientPort
        print(self.clientName)
        print(self.clientPort)

    def connect(self):
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting to " + self.clientName + str(self.clientPort))
        clientSocket.connect((self.clientName, self.clientPort))
        print("Successfully Connected to " + self.clientName + str(self.clientPort))
