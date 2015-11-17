import socket


class Sender:
    def __init__(self, senderName, senderPort):
        self.senderName = senderName
        self.senderPort = senderPort
        print(self.senderName)
        print(self.senderPort)
        self.senderSocket = None

    def open_connection(self):
        self.senderSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.senderSocket.bind((self.senderName, self.senderPort))
        print(" Sender port open Name:" + self.senderName + " Port:" + str(self.senderPort))
        self.senderSocket.listen(5)
        print("Listening ....")
        clientSocket, clientAddress = self.senderSocket.accept()
        print("Connected to - ", clientSocket, clientAddress)

    def send_image(self, image):
        self.senderSocket.send(image)
        f = open(image, 'rb')
        print ("Sending ... ")
        l = f.read(1024)
        while(1):
            print("Sending ... ")
            self.senderSocket.send(1)
            l = f.read(1024)

        f.close()
        print("Done Sending ... ")
        print(self.senderSocket.recv(1024))

