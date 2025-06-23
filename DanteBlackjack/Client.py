import socket
import string
import threading

from TableManager import TableManager
from User import User


# login_to_game nr_albumu password
# connect_to_table nr_albumu table_id
# disconnect nr_albumu
# start_game nr_albumu


# klient łącząc się z serwerem wysyła nr_albumu i hasło
# serwer jeżeli passy się zgadzają odsyła mu jego informacje
# serwer wysyłą informacje o istniejących stołach
# klient wysyła cheć stworzenia stołu
# server tworzy stów i wysyła kazedmu informacje o tym że jest nowy stół
# klient wysyła informacje że chce dołączyć do stołu
# server dołancza go stolu klienta i wysyła mu imiona graczy przy tym stole
# server odsyła każdemu informacje o tym że do stoły x dołączył gracz

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
        self.is_logged = False
        self.received_logging_answer = False
        self.tableManager = None
        self.receiver_thread = threading.Thread(target=self.receiver)
        self.receiver_thread.start()
        self.table = None

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            mess_parts = mess.split(" ")
            print("Client receiver a message: ")
            print(mess_parts)
            read_thread = threading.Thread(target=self.process_mess, args=(mess_parts,))
            read_thread.start()

    def process_mess(self, mess_parts: list[str]):
        if mess_parts[0] == "new_table":
            self.tableManager.add_new_table(mess_parts)
        elif mess_parts[0] == "user_info":
            self.add_user(mess_parts)
        elif mess_parts[0] == "send_table":
            self.tableManager.initialise(mess_parts)
        elif mess_parts[0] == "user_join_table":
            self.tableManager.increase_number_of_player(int(mess_parts[1]))
        elif mess_parts[0] == "players_in_table":
            self.tableManager.add_players_names_to_table(mess_parts, self.user.points)
        elif mess_parts[0] == "cannot_log_in":
            self.is_logged = False
            self.received_logging_answer = True
        elif mess_parts[0] == "YOU_CREAT_YOU_JOIN":
            mess_parts.append(self.user.name)
            mess_parts.append(self.user.album_number)
            self.tableManager.add_players_names_to_table(mess_parts, self.user.points)
            self.table = self.tableManager.find_table_by_id(int(mess_parts[1]))
        elif mess_parts[0] == "DEALER_GET_FIRST_CARD":
            self.table.dealer.add_card(mess_parts[1], mess_parts[2], mess_parts[3], mess_parts[4])
            self.table.dealer.get_first_card = True
        elif mess_parts[0] == "USER_GET_FIRST_CARD":
            player = self.table.find_player_by_album_number(mess_parts[1])
            player.add_card(mess_parts[2], mess_parts[3], mess_parts[4], mess_parts[5])
        elif mess_parts[0] == "DEALER_GET_SECOND_CARD":
            self.table.dealer.add_card(mess_parts[1], mess_parts[2], mess_parts[3], mess_parts[4])
            self.table.dealer.get_second_card = True
        elif mess_parts[0] == "USER_GET_SECOND_CARD":
            player = self.table.find_player_by_album_number(mess_parts[1])
            player.add_card(mess_parts[2], mess_parts[3], mess_parts[4], mess_parts[5])
            self.user.hit_stand_double = True
        elif mess_parts[0] == "PLACE_BET":
            self.user.placing_bets = True
        elif mess_parts[0] == "USER_USE_HIT_GET_NEXT_CARD":
            player = self.table.find_player_by_album_number(mess_parts[1])
            player.add_card(mess_parts[2], mess_parts[3], mess_parts[4], mess_parts[5])
            self.user.hit_stand_double = True
        elif mess_parts[0] == "USER_USE_DOUBLE":
            player = self.table.find_player_by_album_number(mess_parts[1])
            player.bet *= 2
        elif mess_parts[0] == "DEALER_SHOW_SECOND_CARD":
            self.table.dealer.hide_second_card = False
        elif mess_parts[0] == "WIN":
            self.user.points += float(mess_parts[1])
        elif mess_parts[0] == "LOSE":
            self.user.points -= float(mess_parts[1])
        elif mess_parts[0] == "DEALER_GET_ANOTHER_CARD":
            self.table.dealer.add_card(mess_parts[1], mess_parts[2], mess_parts[3], mess_parts[4])

    def sender(self, message: string):
        print("Client send " + message)
        self.conn.send(message.encode())

    def login_to_server(self, nr_album: string, password: string):
        self.sender("login_to_game" + " " + nr_album + " " + password)

    def add_user(self, mess_parts: list[str]):
        self.user = User(mess_parts[1], mess_parts[2], mess_parts[3], mess_parts[4], int(mess_parts[5]),
                         int(mess_parts[6]), int(mess_parts[7]), int(mess_parts[8]), int(mess_parts[9]))
        self.user.__str__()
        self.is_logged = True
        self.received_logging_answer = True

    def create_table(self, min_bet: int):
        self.sender("create_table" + " " + str(min_bet))

    def set_table_manager(self, tableManager: TableManager):
        self.tableManager = tableManager

    def join_to_table(self, table_id):
        self.sender("join_to_table" + " " + str(table_id))
