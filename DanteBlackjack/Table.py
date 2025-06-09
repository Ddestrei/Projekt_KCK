class Table:

    def __init__(self, min_bet: int, table_id: int, amount_users:int):
        self.table_id = table_id
        self.users_name = []
        self.min_bet = min_bet
        self.amount_users = amount_users

    def send_format(self):
        return str(self.table_id) + " " + str(len(self.users)) + " " + str(self.min_bet)

    def add_user_name(self, name):
        self.users_name.append(name)
