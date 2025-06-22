from Deck import Deck

class Player:
    def __init__(self, user_name: str, album_number: str):
        self.user_name = user_name
        self.album_number = album_number
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.deck = Deck()
        self.deck.createDeck()
        self.count = 0
        self.bank = 2
        self.bet = 0
        self.roundsWon = 0
        self.x = 0
        self.y = 0
        self.EndOfTurn = False
        self.result = ""
        self.bust = False

    def add_card(self, suit: str, color: str, label: str, value: str):
        dealerCard = self.deck.find_card(suit, color, label, value)
        self.hand.append(dealerCard)
        self.count += dealerCard.value
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