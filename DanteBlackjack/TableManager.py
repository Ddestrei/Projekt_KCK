import string

from Table import Table


class TableManager:

    def __init__(self):
        self.tables = []
        self.counter = 0
        self.no_tables = False

    def initialise(self, mess: string):
        mess_parts = mess.split(" ")
        amount_tables = int(mess_parts[1])
        for i in range(amount_tables):
            self.tables.append(Table(mess_parts[i + 2], mess_parts[i + 3]))
            amount_names = int(mess_parts[i + 4])
            for j in range(amount_names):
                self.tables[i].add_user_name(mess_parts[i + j + 5])

    def add_new_table(self, mess_parts: list[str]):
        table = Table(int(mess_parts[1]), int(mess_parts[2]))
        table.add_user_name(mess_parts[3])
        self.tables.append(table)
