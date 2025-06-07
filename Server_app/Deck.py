from random import random


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

                image_name = f"{label}.png"
                card_type = random.randint(1, 4)
                image = None
                if card_type == 1:
                    image = pygame.image.load(f"Grafika/Karty/Znak_Dante/{image_name}")
                if card_type == 2:
                    image = pygame.image.load(f"Grafika/Karty/Znak_Mech/{image_name}")
                if card_type == 3:
                    image = pygame.image.load(f"Grafika/Karty/Znak_PL/{image_name}")
                if card_type == 4:
                    image = pygame.image.load(f"Grafika/Karty/Znak_WEEIA/{image_name}")
                card = Card(full_suit_name, color, label, value, image)
                card.image = pygame.transform.scale(image, (
                    round(96 * percents[choice]), round(144 * percents[choice])))  # Resize if needed
                self.cards.append(card)

    def getCard(self):
        topCard = self.cards[0]
        self.cards.pop(0)
        return topCard

    def shuffleDeck(self):
        return random.shuffle(self.cards)
