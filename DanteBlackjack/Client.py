import socket
import string
import threading


# login_to_game nr_albumu password
# connect_to_table nr_albumu table_id
# disconnect nr_albumu
# start_game nr_albumu


class Client:
    def __init__(self):
        self.is_connected = False
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number

        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        self.conn = client_socket
        self.is_connected = True


    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            print(mess)
            # TODO procesing receivered messages
            # self.sender(mess)

    def sender(self, message):
        self.conn.send(message.encode())

    def login_to_server(self, nr_album: string, password: string):
        self.sender("login_to_game" + " " + nr_album + " " + password)
        mess = str(self.conn.recv(1024).decode())
        print(mess)
