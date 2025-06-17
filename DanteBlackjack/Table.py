class Table:
    class User:
        def __init__(self, user_name, album_number):
            self.user_name = user_name
            self.album_number = album_number

    def __init__(self, min_bet: int, table_id: int, amount_users: int):
        self.table_id = table_id
        self.users_name = []
        self.min_bet = min_bet
        self.amount_users = amount_users

    def add_user_name(self, name, album_number):
        self.users_name.append(self.User(name, album_number))
