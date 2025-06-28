from Dealer import Dealer
from Player import Player


class Table:

    def __init__(self, table_id: int, amount_users: int):
        self.table_id = table_id
        self.users_name = []
        self.amount_users = amount_users
        self.dealer = Dealer()

    def add_user_name(self, name, album_number, points):
        self.users_name.append(Player(name, album_number, points))
        self.amount_users += 1

    def find_player_by_album_number(self, album_number):
        for p in self.users_name:
            if p.album_number == album_number:
                return p
        return None
