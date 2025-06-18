import random

from Server_app.Card import Card


class Deck:

    # this class contains an array that acts as our 52 card deck
    def __init__(self):
        self.cards = []

    # this method simply creates a deck using the Card class above
    def createDeck(self):
        suits = ["C", "S", "H", "D"]
        full_suits = {
            "C": "Clover",
            "S": "Spade",
            "H": "Heart",
            "D": "Diamond"
        }
        for suit in suits:
            for number in range(2, 15):
                full_suit_name = full_suits[suit]
                color = "Black" if suit in ["C", "S"] else "Red"
                label = str(number)
                value = number
                if number > 10:
                    value = 10
                if number == 14:
                    value = 1
                if number == 11:
                    label = "J"
                elif number == 12:
                    label = "Q"
                elif number == 13:
                    label = "K"
                elif number == 14:
                    label = "A"

                card = Card(full_suit_name, color, label, value)
                self.cards.append(card)

    def getCard(self):
        topCard = self.cards[0]
        self.cards.pop(0)
        return topCard

    def shuffleDeck(self):
        return random.shuffle(self.cards)
