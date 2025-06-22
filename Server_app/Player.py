class Player:
    def __init__(self, points: int):
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bank = points
        self.bet = -1
        self.roundsWon = 0
        self.x = 0
        self.y = 0

    def add_card(self, card):
        self.hand.append(card)
        self.count_cards()

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
