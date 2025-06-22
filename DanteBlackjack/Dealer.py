from Deck import Deck
from Tool import percents, choice
from Card import Card

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.deck.createDeck()
        self.deck.shuffleDeck()
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.x = round(672 * percents[choice])
        self.y = round(450 * percents[choice])
        self.hide_second_card = True
        self.get_first_card = False
        self.get_second_card = False

    def createDealerHand(self):
        for i in range(1, 3):
            self.addCard()

    def add_card(self, suit: str, color: str, label: str, value: str):
        dealerCard = self.deck.find_card(suit, color, label, value)
        self.hand.append(dealerCard)
        self.count += dealerCard.value
        self.countAce()

    def countAce(self):
        self.low_count = sum(card.value for card in self.hand)
        self.high_count = self.low_count
        has_ace = any(card.label == "A" for card in self.hand)

        if has_ace:
            self.high_count += 10
            if self.high_count > 21:
                self.high_count = self.low_count

        self.count = self.high_count if self.high_count <= 21 else self.low_count
