import string
from time import sleep

from Dealer import Dealer
from Deck import Deck
from User import User
from Card import Card

class Table:

    def __init__(self, min_bet: int, table_id: int, user: User):
        self.table_id = table_id
        self.users = []
        self.users.append(user)
        self.min_bet = min_bet
        self.deck = Deck()
        self.dealer = Dealer()

    def send_format(self):
        return str(self.min_bet) + " " + str(self.table_id)

    def game(self):
        while self.users.__len__() != 0:
            self.send_to_all_users("START_ROUND")
            sleep(5)
            for u in self.users:
                u.sender("PLACE_BET")
                while u.player.bet == -1:
                    pass
            sleep(5)
            self.dealer.add_card()
            self.send_to_all_users(
                "DEALER_GET_FIRST_CARD" + " " + self.dealer.hand[0].send_format())
            sleep(5)
            for u in self.users:
                u.player.add_card(self.dealer.deal_card())
                self.send_to_all_users("USER_GET_FIRST_CARD" + " " + u.album_number + " " + u.player.hand[0].send_format())
            sleep(5)
            self.dealer.add_card()
            self.send_to_all_users(
                "DEALER_GET_SECOND_CARD" + " " + self.dealer.hand[0].send_format())
            sleep(5)
            for u in self.users:
                u.player.add_card(self.dealer.deal_card())
                self.send_to_all_users("USER_GET_SECOND_CARD" + " " + u.album_number + " " + u.player.hand[1].send_format())
                sleep(5)
                self.hit_stand_double(u)

        #TODO

    def send_to_all_users(self, mess: string):
        for u in self.users:
            u.sender(mess)

    def hit_stand_double(self, user: User):
        while user.hit_stand_double is False:
            pass
        if user.hit is True:
            self.send_to_all_users("USER_USE_HIT_GET_NEXT_CARD" + " " + user.album_number + " " + user.player.hand[
                user.player.hand.__len__() - 1].send_format())
            sleep(5)
            user.hit_stand_double = False
            user.hit = False
            self.hit_stand_double(user)
        elif user.double is True:
            sleep(5)
            self.send_to_all_users("USER_USE_DOUBLE" + " " + user.album_number)
            user.player.bet *= 2
        user.hit_stand_double = False
        user.hit = False
        user.stand = False
        user.double = False
