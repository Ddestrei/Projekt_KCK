from Deck import Deck

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.deck.createDeck()
        self.deck.shuffleDeck()
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0

    def create_dealer_hand(self):
        for i in range(1, 3):
            self.addCard()

    def deal_card(self):
        return self.deck.getCard()

    def add_card(self):
        dealerCard = self.dealCard()
        self.hand.append(dealerCard)
        self.count += dealerCard.value
        self.countAce()

    def count_ace(self):
        self.low_count = sum(card.value for card in self.hand)
        self.high_count = self.low_count
        has_ace = any(card.label == "A" for card in self.hand)

        if has_ace:
            self.high_count += 10
            if self.high_count > 21:
                self.high_count = self.low_count

        self.count = self.high_count if self.high_count <= 21 else self.low_count
