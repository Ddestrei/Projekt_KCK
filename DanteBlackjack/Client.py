import socket
import string

from TableManager import TableManager
from User import User


# login_to_game nr_albumu password
# connect_to_table nr_albumu table_id
# disconnect nr_albumu
# start_game nr_albumu


class Client:
    def __init__(self):
        self.is_connected = False
        host = socket.gethostname()  # as both code is running on same pc
        port = 5000  # socket server port number
        self.user = None
        client_socket = socket.socket()  # instantiate
        client_socket.connect((host, port))  # connect to the server
        self.conn = client_socket
        self.is_connected = True
        self.tableManager = None

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            mess_parts = mess.split(" ")
            if mess_parts[0] == "new_table":
                self.tableManager.add_new_table(mess_parts)

    def sender(self, message: string):
        self.conn.send(message.encode())

    def login_to_server(self, nr_album: string, password: string):
        self.sender("login_to_game" + " " + nr_album + " " + password)
        mess = str(self.conn.recv(1024).decode())
        self.add_user(mess)
        self.sender("received")
        mess = str(self.conn.recv(1024).decode())
        self.tableManager.initialise(mess)

    def add_user(self, mess: string):
        mess_parts = mess.split(" ")
        self.user = User(mess_parts[1], mess_parts[2], mess_parts[3], mess_parts[4], int(mess_parts[5]),
                         int(mess_parts[6]), int(mess_parts[7]), int(mess_parts[8]), int(mess_parts[9]))
        self.user.__str__()

    def create_table(self, min_bet: int):
        self.sender("create_table" + " " + str(min_bet))
        pass

    def set_table_manager(self, tableManager: TableManager):
        self.tableManager = tableManager
