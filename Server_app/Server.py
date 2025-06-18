import socket

from DataBase import DataBase
from OneClientConnection import OneClientConnection
from Table import Table
from TableManager import TableManager


# client łączonc się z serverem nie dostaje imion graczy który tam są tylko ich ilosc
# imiona są przekazywane wtedy kiedy dolancza do danego stolu

class Server:
    def __init__(self):
        self.database = DataBase()
        self.tableManager = TableManager(self.add_table_info, self.add_user_to_table)
        host = socket.gethostname()
        port = 5000  # initiate port no above 1024
        self.clients = []
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((host, port))
            server_socket.listen()
            while True:
                conn, address = server_socket.accept()
                client = OneClientConnection(conn, address, dataBase=self.database, tableManager=self.tableManager)
                self.clients.append(client)

    def add_table_info(self, table: Table):
        for client in self.clients:
            client.sender("new_table" + " " + table.send_format())

    def add_user_to_table(self, table: Table):
        for client in self.clients:
            client.sender("user_join_table" + " " + str(table.table_id))
