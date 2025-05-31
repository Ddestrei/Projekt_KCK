import random
from contextlib import nullcontext
import time
import pygame
from pygame.locals import *
import sys

resolutions = [(874, 620), (1166, 826), (1457, 1033)]
percents = [0.6, 0.8, 1]

print("Wybierz rozdzielczość aby rozpocząć:")
for i, res in enumerate(resolutions):
    print(f"{i + 1}. {res[0]}x{res[1]}")

choice = int(input("Twój wybór: ")) - 1

def scale_position(x, y, choice):
    if choice != 2:
        if choice == 0:
            x = 0.6 * x
            y = 0.6 * y
            return round(x), round(y)
        elif choice == 1:
            x = 0.8 * x
            y = 0.8 * y
            return round(x), round(y)
    return x, y


screenWidth, screenHeight = 1457, 1033
screenWidth,screenHeight = scale_position(screenWidth,screenHeight,choice)
screen = pygame.display.set_mode((screenWidth,screenHeight))

class Button:
    def __init__(self, x, y, image, scale=1, hover_image=None, enabled=True):
        width = image.get_width()
        height = image.get_height()
        self.base_image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.hover_image = pygame.transform.scale(hover_image, (int(width * scale), int(height * scale))) if hover_image else self.base_image
        self.image = self.base_image
        self.rect = self.image.get_rect(topleft=(x, y))
        self.clicked = False
        self.enabled = enabled

    def draw(self):
        action = False
        mouse_pos = pygame.mouse.get_pos()

        if self.enabled:
            self.image = self.hover_image if self.rect.collidepoint(mouse_pos) else self.base_image
        else:
            self.image = self._dim_image(self.base_image)

        screen.blit(self.image, (self.rect.x, self.rect.y))

        if self.enabled and pygame.mouse.get_pressed()[0] and self.rect.collidepoint(mouse_pos):
            if not self.clicked:
                self.clicked = True
                action = True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False

        return action

    def set_enabled(self, value: bool):
        self.enabled = value

    def _dim_image(self, image):
        dimmed = image.copy()
        dimmed.fill((180, 180, 180, 200), None, pygame.BLEND_RGBA_MULT)
        return dimmed

class Card:

    def __init__(self, suit, color, label, value,image):
        self.image = None
        self.suit = suit
        self.color = color
        self.label = label
        self.value = value

def brighten_surface(surface, brightness=40):
    hover = surface.copy()
    brighten_layer = pygame.Surface(surface.get_size()).convert_alpha()
    brighten_layer.fill((brightness, brightness, brightness, 0))  # RGB only
    hover.blit(brighten_layer, (0, 0), special_flags=pygame.BLEND_RGB_ADD)
    return hover

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
                if card_type ==1:
                    image = pygame.image.load(f"Grafika/Karty/Znak_Dante/{image_name}")
                if card_type==2:
                    image = pygame.image.load(f"Grafika/Karty/Znak_Mech/{image_name}")
                if card_type ==3:
                    image = pygame.image.load(f"Grafika/Karty/Znak_PL/{image_name}")
                if card_type ==4:
                    image = pygame.image.load(f"Grafika/Karty/Znak_WEEIA/{image_name}")
                card = Card(full_suit_name, color, label, value,image)
                card.image = pygame.transform.scale(image, (round(96*percents[choice]), round(144*percents[choice])))  # Resize if needed
                self.cards.append(card)
    def getCard(self):
        topCard = self.cards[0]
        self.cards.pop(0)
        return topCard

    def shuffleDeck(self):
        return random.shuffle(self.cards)
class player:
    def __init__(self,name):
        self.name = name
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.bank = 0
        self.bet = 0
        self.roundsWon = 0
        self.x = 0
        self.y = 0
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

class Dealer:
    def __init__(self):
        self.deck = Deck()
        self.deck.createDeck()
        self.deck.shuffleDeck()
        self.hand = []
        self.low_count = 0
        self.high_count = 0
        self.count = 0
        self.x = round(672*percents[choice])
        self.y = round(450*percents[choice])







