# from Server import Server
from Table import Table
from User import User


class TableManager:

    def __init__(self, add_table_info, add_user_to_table):
        self.tables = []
        self.counter = 0
        self.add_table_info = add_table_info
        self.add_user_to_table = add_user_to_table

    def add_table(self, min_bet: int, user: User):
        table = Table(min_bet, table_id=self.counter, user=user)
        self.tables.append(table)
        self.counter += 1
        self.add_table_info(table)

    # Dodaje użytkowniak do stołu jeżeli stół o takim_id nie istnieje zwrazany jest False
    def add_player_to_table(self, table_id: int, user: User):
        table = self.find_table_by_id(table_id)
        if table is None:
            return False
        table.users.append(user)
        self.add_user_to_table(table)
        return True

    def start_table(self, table_id: int):
        pass

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
        names = " "
        for user in table.users:
            names += user.name
            names += " "
        return names

    def find_table_by_id(self, table_id):
        for t in self.tables:
            if t.table_id == table_id:
                return t
        return None

