# from Server import Server
from time import sleep

from Table import Table
from User import User
import threading

class TableManager:

    def __init__(self, add_table_info, add_user_to_table):
        self.tables = []
        self.counter = 0
        self.add_table_info = add_table_info
        self.add_user_to_table = add_user_to_table

    def add_table(self, user: User):
        table = Table(table_id=self.counter, user=user)
        self.tables.append(table)
        self.counter += 1
        self.add_table_info(table)
        sleep(1)
        user.sender("YOU_CREAT_YOU_JOIN" + " " + str(table.table_id))
        game_thread = threading.Thread(target=table.game, args=())
        game_thread.start()

    # Dodaje użytkowniak do stołu jeżeli stół o takim_id nie istnieje zwrazany jest False
    def add_player_to_table(self, table_id: int, user: User):
        table = self.find_table_by_id(table_id)
        if table is None:
            return False
        table.users.append(user)
        self.add_user_to_table(table)
        return True

    def send_tables(self):
        mess = "send_table"
        mess += " "
        mess += str(len(self.tables))
        for table in self.tables:
            mess += " "
            mess += str(table.min_bet)
            mess += " "
            mess += str(table.table_id)
            mess += " "
            mess += str(len(table.users))
        return mess

    def return_players_names_in_table(self, table_id: int):
        table = self.find_table_by_id(table_id=table_id)
        for user in table.users:
            names = " "
            names += user.name
            names += " "
            names += user.album_number
        return names

    def find_table_by_id(self, table_id):
        for t in self.tables:
            if t.table_id == table_id:
                return t
        return None
