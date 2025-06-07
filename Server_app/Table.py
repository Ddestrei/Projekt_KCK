from User import User


class Table:

    def __init__(self, min_bet, table_id, user: User):
        self.table_id = table_id
        self.users = []
        self.users.append(user)
        self.min_bet = min_bet

    def send_format(self):
        return str(str(self.min_bet) + " " + str(self.table_id) + " " + self.users[0].name)
