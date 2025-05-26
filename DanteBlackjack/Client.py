import socket
import threading


class Client:
    def __init__(self):
        self.is_connected = False
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        self.conn = client_socket
        self.is_connected = True
        receiver_thread = threading.Thread(target=self.receiver)
        receiver_thread.start()
        self.sender("Ala ma kota")

        while self.is_connected:
            pass

        client_socket.close()  # close the connection

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            print(mess)
            # TODO procesing receivered messages
            # self.sender(mess)

    def sender(self, message):
        self.conn.send(message.encode())
