from User import User


class Table:

    def __init__(self, min_bet: int, table_id: int, user: User):
        self.table_id = table_id
        self.users = []
        self.users.append(user)
        self.min_bet = min_bet

    def send_format(self):
        return str(self.min_bet) + " " + str(self.table_id)
