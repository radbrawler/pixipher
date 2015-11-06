import socket


class Server:
    serverName = "localhost"
    serverPort = 9215

    def open_connection(self):
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSocket.bind((self.serverName, self.serverPort))
        serverSocket.listen(5)