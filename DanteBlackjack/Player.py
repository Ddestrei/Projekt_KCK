

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bank = 1
        self.bet = 0
        self.roundsWon = 0
        self.x = 0
        self.y = 0
        self.EndOfTurn = False
        self.result = ""
        self.bust = False

    def addCard(self, card):
        self.hand.append(card)
        self.countCards()

    def countCards(self):
        self.low_count = sum(card.value for card in self.hand)
        self.high_count = self.low_count
        has_ace = any(card.label == "A" for card in self.hand)
        if has_ace:
            self.high_count += 10
            if self.high_count > 21:
                self.high_count = self.low_count
        self.count = self.high_count if self.high_count <= 21 else self.low_count

    def ResetHand(self):
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bet = 0