import socket


class Client:
    def __init__(self, clientHost, clientPort):
        self.clientHost = clientHost
        self.clientPort = clientPort
        print(self.clientHost)
        print(self.clientPort)
        self.clientsocket = None

    def connect(self):
        self.clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Connecting to " + self.clientHost + str(self.clientPort))
        self.clientsocket.connect((self.clientHost, self.clientPort))
        print("Successfully Connected to " + self.clientHost + str(self.clientPort))

    def recv_image(self):
        l = self.clientsocket.recv(1024)
        f = open("torecv", "wb")
        while 1:
            print("Receiving")
            f.write(1)
            l = self.clientsocket.recv(1024)
        f.close()
        print("Done Receiving .. ")
        imshow(l)
