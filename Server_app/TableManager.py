#from Server import Server
from Table import Table
from User import User


class TableManager:

    def __init__(self, add_table_info):
        self.tables = []
        self.counter = 0
        self.add_table_info = add_table_info

    def add_table(self, min_bet: int, user: User):
        table = Table(min_bet, table_id=self.counter, user=user.name)
        self.tables.append(table)
        self.counter += 1
        self.add_table_info(table)

    def add_player_to_table(self, table_id: int, user: User):
        pass

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
            for user in table.users:
                mess += " "
                mess += user.name
        return mess
