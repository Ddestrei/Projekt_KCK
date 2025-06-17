class Card:

    def __init__(self, suit, color, label, value):
        self.suit = suit
        self.color = color
        self.label = label
        self.value = value

    def send_format(self):
        return self.suit + " " + self.color + " " + self.label + " " + str(self.value)
