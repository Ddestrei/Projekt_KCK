from Table import Table


class TableManager:

    def __init__(self):
        self.tables = []
        self.counter = 0
        self.no_tables = False

    def initialise(self, mess_parts: list[str]):
        amount_tables = int(mess_parts[1])
        for i in range(2, amount_tables, 3):
            self.tables.append(Table(int(mess_parts[i + 0]), int(mess_parts[i + 1]), int(mess_parts[i + 2])))

    def add_new_table(self, mess_parts: list[str]):
        table = Table(int(mess_parts[1]), int(mess_parts[2]), 1)
        self.tables.append(table)

    def increase_number_of_player(self, table_id):
        table = self.find_table_by_id(table_id)
        table.amount_users += 1

    def find_table_by_id(self, table_id):
        for t in self.tables:
            if t.table_id == table_id:
                return t
        return None

    def add_players_names_to_table(self, mess_parts: list[str]):
        table = self.find_table_by_id(int(mess_parts[1]))
        for i in range(2, len(mess_parts), 2):
            table.users_names.append(mess_parts[i], mess_parts[i + 1])
