class Player:
    def __init__(self):
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bank = 1
        self.bet = 0
        self.roundsWon = 0
        self.x = 0
        self.y = 0

    def add_card(self, card):
        self.hand.append(card)
        self.countCards()

    def count_cards(self):
        self.low_count = sum(card.value for card in self.hand)
        self.high_count = self.low_count
        has_ace = any(card.label == "A" for card in self.hand)
        if has_ace:
            self.high_count += 10
            if self.high_count > 21:
                self.high_count = self.low_count
        self.count = self.high_count if self.high_count <= 21 else self.low_count

    def reset_hand(self):
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bet = 0
