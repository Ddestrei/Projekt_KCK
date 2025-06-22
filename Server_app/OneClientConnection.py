import threading

from DataBase import DataBase
from TableManager import TableManager


class OneClientConnection:

    def __init__(self, conn, address, dataBase: DataBase, tableManager: TableManager):
        self.user = None
        self.is_connected = False
        self.client_id = ""
        self.conn = conn
        self.address = address
        print("Connection from: " + str(address))
        self.is_connected = True
        self.dataBase = dataBase
        self.tableManager = tableManager
        receiver_thread = threading.Thread(target=self.receiver)
        receiver_thread.start()

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            print("Server receiver a message: ")
            read_thread = threading.Thread(target=self.read_mess, args=(mess,))
            read_thread.start()

    def sender(self, message):
        self.conn.send(message.encode())
        print("Server send: " + message)

    def read_mess(self, message):
        mess_parts = message.split(" ")
        print(mess_parts)
        if mess_parts[0] == "login_to_game":
            nr_album = mess_parts[1]
            password = mess_parts[2]
            self.user = self.dataBase.get_user(nr_album)
            self.user.add_sender_and_receiver(self.sender, self.receiver)
            if self.user is None or self.user.password != password or self.user.is_logged:
                self.sender("cannot_log_in")
            else:
                self.sender(self.user.send_format())
                self.sender(self.tableManager.send_tables())
        elif mess_parts[0] == "create_table":
            min_bet = int(mess_parts[1])
            self.tableManager.add_table(min_bet, self.user)
            pass
        elif mess_parts[0] == "join_to_table":
            self.tableManager.add_player_to_table(int(mess_parts[1]), self.user)
            self.sender("players_in_table" + self.tableManager.return_players_names_in_table((int(mess_parts[1]))))
        elif mess_parts[0] == "PLACE_BET":
            self.user.player.bet = float(mess_parts[1])
        elif mess_parts[0] == "HIT":
            self.user.hit_stand_double = True
            self.user.hit = True
        elif mess_parts[0] == "STAND":
            self.user.hit_stand_double = True
            self.user.stand = True
        elif mess_parts[0] == "DOUBLE":
            self.user.hit_stand_double = True
            self.user.double = True
