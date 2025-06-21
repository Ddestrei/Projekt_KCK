from Tool import percents, choice
from Deck import Deck
class Dealer():
    def __init__(self, screen):
        self.screen = screen
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

    def createDealerHand(self):
        for i in range(1, 3):
            self.addCard()

    def dealCard(self):
        return self.deck.getCard()

    def addCard(self):
        dealerCard = self.dealCard()
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
