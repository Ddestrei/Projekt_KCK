import string
from time import sleep

from Dealer import Dealer
from User import User


class Table:

    def __init__(self, min_bet: int, table_id: int, user: User):
        self.table_id = table_id
        self.users = []
        self.users.append(user)
        self.min_bet = min_bet
        self.dealer = Dealer()

    def send_format(self):
        return str(self.min_bet) + " " + str(self.table_id)

    def game(self):
        while self.users.__len__() != 0:
            self.send_to_all_users("START_ROUND")
            sleep(5)
            for u in self.users:
                u.player.bet = -1
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
                self.send_to_all_users(
                    "USER_GET_FIRST_CARD" + " " + u.album_number + " " + u.player.hand[0].send_format())
            sleep(5)
            self.dealer.add_card()
            self.send_to_all_users(
                "DEALER_GET_SECOND_CARD" + " " + self.dealer.hand[1].send_format())
            sleep(5)
            for u in self.users:
                u.player.add_card(self.dealer.deal_card())
                self.send_to_all_users(
                    "USER_GET_SECOND_CARD" + " " + u.album_number + " " + u.player.hand[1].send_format())
                sleep(5)
                self.hit_stand_double(u)
            sleep(5)
            self.send_to_all_users("DEALER_SHOW_SECOND_CARD")
            while self.dealer.low_count < 17:
                self.dealer.add_card()
                self.send_to_all_users(
                    "DEALER_GET_ANOTHER_CARD" + " " + self.dealer.hand[self.dealer.hand.__len__()-1].send_format())
                sleep(5)

            for u in self.users:
                self.dealer.count_ace()
                u.player.count_cards()
                if self.dealer.count > 21 >= u.player.count:
                    u.sender("WIN" + " " + str(u.player.bet * 2))
                elif self.dealer.count == u.player.count:
                    u.sender("DROW")
                elif self.dealer.count <= 21 and 21 >= u.player.count > self.dealer.count:
                    u.sender("WIN" + " " + str(u.player.bet * 2))
                elif u.player.count > 21:
                    u.sender("LOSE" + " " + str(u.player.bet))
                elif 21 >= u.player.count and u.player.count < self.dealer.count:
                    u.sender("LOSE" + " " + str(u.player.bet))
            for u in self.users:
                u.player.reset_hand()
            self.dealer.reset_hand()
            sleep(5)


    def send_to_all_users(self, mess: string):
        for u in self.users:
            u.sender(mess)

    def hit_stand_double(self, user: User):
        while user.hit_stand_double is False:
            pass
        if user.hit is True:
            user.hit = False
            if user.player.count < 21:
                user.player.add_card(self.dealer.deal_card())
                self.send_to_all_users("USER_USE_HIT_GET_NEXT_CARD" + " " + user.album_number + " " + user.player.hand[
                    user.player.hand.__len__() - 1].send_format())
                sleep(5)
                self.hit_stand_double(user)

        elif user.double is True:
            sleep(5)
            self.send_to_all_users("USER_USE_DOUBLE" + " " + user.album_number)
            user.player.bet *= 2
            user.double = False
