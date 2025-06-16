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
class Player:
    def __init__(self,name):
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

#Creating basic text itp
pygame.init()
pygame.font.init()
halfWidth, halfHeight = screenWidth / 2, screenHeight / 2
pokerBackgroundOriginal = pygame.image.load("grafika/tla/table.png")
pokerGreen = pygame.transform.scale(pokerBackgroundOriginal, (screenWidth, screenHeight))
black, blue, white, orange, red = (0, 0, 0), (51, 235, 255), (255, 255, 255), (255, 165, 0), (255, 0, 0)
fontType = 'Comic Sans MS'
text_Title = pygame.font.SysFont(fontType, 80)
text_Heading = pygame.font.SysFont(fontType, 60)
text_SubHeading = pygame.font.SysFont(fontType, 45)
text_Bold = pygame.font.SysFont(fontType, 30)
text_Normal = pygame.font.SysFont(fontType, 20)
text_Small = pygame.font.SysFont(fontType, 10)


bet15_img = pygame.image.load("Grafika/Obiekty/bet1,5p.png")
bet1_img = pygame.image.load("Grafika/Obiekty/bet1p.png")
bet05_img = pygame.image.load("Grafika/Obiekty/bet0.5.png")
hit_img = pygame.image.load("Grafika/Obiekty/hit.png")
stand_img = pygame.image.load("Grafika/Obiekty/STAND.png")
double_img = pygame.image.load("Grafika/Obiekty/double.png")
bet05_button = Button(halfWidth-round(300*percents[choice]),screenHeight-round(100*percents[choice]),bet05_img,percents[choice],hover_image=brighten_surface(bet05_img))
bet1_button = Button(halfWidth-round(100*percents[choice]),screenHeight-round(105*percents[choice]),bet1_img,percents[choice],hover_image=brighten_surface(bet1_img))
bet15_button = Button(halfWidth+round(100*percents[choice]),screenHeight-round(102*percents[choice]),bet15_img,percents[choice],hover_image=brighten_surface(bet15_img))
adjusted_center = halfWidth - 150 * percents[choice] + 50
button_spacing = 160 * percents[choice]
card_height = round(144*percents[choice])

hit_button = Button(adjusted_center - button_spacing, screenHeight - 70, hit_img,percents[choice],hover_image=brighten_surface(hit_img))
stand_button = Button(adjusted_center, screenHeight - 70, stand_img,percents[choice],hover_image=brighten_surface(stand_img))
double_button = Button(adjusted_center + button_spacing, screenHeight - 70, double_img, percents[choice],hover_image=brighten_surface(double_img))
card_back_img = pygame.image.load("Grafika/Karty/tyl_karty.png")
card_back_img = pygame.transform.scale(card_back_img, (round(96 * percents[choice]), round(144 * percents[choice])))
leave_img = pygame.image.load("Grafika/Obiekty/leave.png")
leave_button = Button(10, 10, leave_img, round(percents[choice]*1.5))
leave_button.set_enabled(True)
hit_button.set_enabled(True)
stand_button.set_enabled(True)
double_button.set_enabled(True)

class Game:
    def __init__(self):
        self.dealer = Dealer()
        self.players = []
        self.num_of_players = 3
        self.turnOver= False
        self.players.append(Player("Kasia"))
        self.players.append(Player("Kacper"))
        self.players.append(Player("Oliwia"))
    def fixCoordinates(self):
        if self.num_of_players == 1:
            self.players[0].x = round(669*percents[choice])
            self.players[0].y = round(665*percents[choice])
        elif self.num_of_players == 2:
            self.players[0].x = round(669*percents[choice])
            self.players[0].y = round(665*percents[choice])
            self.players[1].x = round(1020*percents[choice])
            self.players[1].y = round(650*percents[choice])
        elif self.num_of_players == 3:
            self.players[0].x = round(284*percents[choice])
            self.players[0].y = round(646*percents[choice])
            self.players[1].x = round(669*percents[choice])
            self.players[1].y = round(665*percents[choice])
            self.players[2].x = round(1020*percents[choice])
            self.players[2].y = round(650*percents[choice])
        elif self.num_of_players == 4:
            self.players[0].x = round(294*percents[choice])
            self.players[0].y = round(413*percents[choice])
            self.players[1].x = round(284*percents[choice])
            self.players[1].y = round(646*percents[choice])
            self.players[2].x = round(669*percents[choice])
            self.players[2].y = round(665*percents[choice])
            self.players[3].x =  round(1020*percents[choice])
            self.players[3].y = round(650*percents[choice])
        elif self.num_of_players == 5:
            self.players[0].x = round(294*percents[choice])
            self.players[0].y = round(413*percents[choice])
            self.players[1].x = round(284*percents[choice])
            self.players[1].y = round(646*percents[choice])
            self.players[2].x = round(669*percents[choice])
            self.players[2].y = round(665*percents[choice])
            self.players[3].x =  round(1020*percents[choice])
            self.players[3].y = round(650*percents[choice])
            self.players[4].x = round(1043*percents[choice])
            self.players[4].y = round(410*percents[choice])

    def add_text(self,text, font, surface, x, y, text_color):
        textObject = font.render(text, False, text_color)
        textWidth = textObject.get_rect().width
        textHeight = textObject.get_rect().height
        surface.blit(textObject, (x - (textWidth / 2), y - (textHeight / 2)))

    def delay_with_events(self,ms):
        start_time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start_time < ms:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            if leave_button.draw():
                pygame.quit()
                sys.exit()
    def placing_bets(self):

        i = 0
        number_of_deleted_players = 0
        while i < len(self.players):
            current_player = self.players[i]

            if current_player.bank < 0.5:
                screen.blit(pokerGreen, (0, 0))
                self.add_text("Player "+ str(i+1+number_of_deleted_players) +" hasn't enough points to play", text_Bold, screen, halfWidth, 100, red)
                number_of_deleted_players+=1
                if leave_button.draw():
                    pygame.quit()
                    sys.exit()
                pygame.display.update()
                self.delay_with_events(1000)
                self.players.pop(i)
                self.num_of_players -= 1
                if self.num_of_players == 0:
                    self.turnOver = True
                    return
                continue

            bet_placed = False
            while not bet_placed:
                screen.blit(pokerGreen, (0, 0))

                if leave_button.draw():
                    pygame.quit()
                    sys.exit()

                self.add_text("Player's "+ str(i+1) +" turn, place your bet", text_Bold, screen, halfWidth, 100, red)
                self.add_text("Your points: "+ str(current_player.bank), text_Normal, screen, round(150*percents[choice]), round(100*percents[choice]), orange)
                bet05_button.set_enabled(current_player.bank >= 0.5)
                bet1_button.set_enabled(current_player.bank >= 1)
                bet15_button.set_enabled(current_player.bank >= 1.5)

                if bet05_button.draw():
                    current_player.bet = 0.5
                    current_player.ready = True
                    bet_placed = True

                if bet1_button.draw():
                    current_player.bet = 1
                    current_player.ready = True
                    bet_placed = True

                if bet15_button.draw():
                    current_player.bet = 1.5
                    current_player.ready = True
                    bet_placed = True

                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()

                pygame.display.update()

            i += 1
    def newDeck(self):
        self.dealer = Dealer()
    def draw_all_hands(self):
        # Drawing players hands
        for i, p in enumerate(self.players):
            x_offset = 0
            for card in p.hand:
                screen.blit(card.image, (p.x + x_offset, p.y))
                x_offset += 30
            # Adding text with number of points in cards
            if p.EndOfTurn == False:
                if p.low_count != p.high_count:
                    text = f"{p.low_count}/{p.high_count} pkt"
                else:
                    text = f"{p.low_count} pkt"
                self.add_text(text, text_Small, screen, p.x + 40, p.y - 10, white)
            else:
                self.add_text(str(p.result), text_Small, screen, p.x + 40, p.y - 10, white)

            self.add_text(p.name, text_Normal, screen, p.x + 40, p.y + card_height+ 10, orange)

        # Draw dealers hand
        x_offset = 0
        for idx, card in enumerate(self.dealer.hand):
            if idx == 1 and self.dealer.hide_second_card:
                screen.blit(card_back_img, (self.dealer.x + x_offset, self.dealer.y))
            else:
                screen.blit(card.image, (self.dealer.x + x_offset, self.dealer.y))
            x_offset += 30

        # Show known dealers points
        if self.dealer.hide_second_card:
            visible_value = self.dealer.hand[0].value
            if self.dealer.hand[0].label == "A":
                visible_value = "1/11"
            self.add_text(f"{visible_value} pkt", text_Small, screen, self.dealer.x + 40, self.dealer.y - 10, red)
        else:
            if self.dealer.low_count != self.dealer.high_count:
                text = f"{self.dealer.low_count}/{self.dealer.high_count} pkt"
            else:
                text = f"{self.dealer.low_count} pkt"
            self.add_text(text, text_Small, screen, self.dealer.x + 40, self.dealer.y - 10, red)
    def redraw_game_screen(self):
        screen.blit(pokerGreen, (0, 0))
        self.draw_all_hands()
        hit_button.draw()
        stand_button.draw()
        double_button.draw()
        if leave_button.draw():
            pygame.quit()
            sys.exit()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    def createHands(self):
        dealing_stage = 0
        last_deal_time = pygame.time.get_ticks()
        deal_delay = 500
        dealing_done = False

        total_players = len(self.players)

        while not dealing_done:
            current_time = pygame.time.get_ticks()
            if current_time - last_deal_time >= deal_delay:
                last_deal_time = current_time

                if dealing_stage == 0:
                    # first card for dealer
                    self.dealer.addCard()

                elif 1 <= dealing_stage <= total_players:
                    # first card for i player
                    self.players[dealing_stage - 1].addCard(self.dealer.dealCard())

                elif dealing_stage == total_players + 1:
                    # second card for dealer
                    self.dealer.addCard()

                elif (total_players + 2) <= dealing_stage <= (2 * total_players + 1):
                    # second card for i player
                    player_index = dealing_stage - (total_players + 2)
                    self.players[player_index].addCard(self.dealer.dealCard())

                else:
                    dealing_done = True

                dealing_stage += 1
                self.redraw_game_screen()
                self.add_text("Dealing cards, please wait for your turn", text_Bold, screen, halfWidth, 40, white)
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if leave_button.draw():
                    pygame.quit()
                    sys.exit()
    def playTurn(self):
        for player in self.players:
            turn_active = True
            can_double = True
            hit_button.set_enabled(True)
            stand_button.set_enabled(True)
            double_button.set_enabled(True)
            while turn_active:
                screen.blit(pokerGreen, (0, 0))
                self.draw_all_hands()
                self.add_text(f"Player's {self.players.index(player) + 1} turn", text_Bold, screen, halfWidth, 40, orange)
                hit_button.draw()
                stand_button.draw()
                double_button.draw()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

                if leave_button.draw():
                    pygame.quit()
                    sys.exit()

                if player.count==21 or player.high_count==21:
                    turn_active = False

                if stand_button.draw():
                    turn_active = False

                elif hit_button.draw():
                    player.addCard(self.dealer.dealCard())
                    self.draw_all_hands()
                    can_double = False
                    double_button.set_enabled(False)

                    if player.high_count > 21:
                        player.bust = True
                        turn_active = False

                elif double_button.draw() and can_double:
                    player.bet *= 2
                    player.addCard(self.dealer.dealCard())
                    if player.high_count > 21:
                        player.bust = True
                    turn_active = False
                    can_double = False

                pygame.display.update()
    def dealers_turn(self):
        self.dealer.hide_second_card = False  # Reveal dealer's card

        self.dealer.countAce()  #  calculate points

        dealer_turn_over = False
        while not dealer_turn_over:
            screen.blit(pokerGreen, (0, 0))
            self.draw_all_hands()
            self.add_text("Revealing cards...", text_Bold, screen, halfWidth, 40, red)


            if leave_button.draw():
                pygame.quit()
                sys.exit()

            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.delay_with_events(500)

            # drawing cards by dealer when < 17 points
            if self.dealer.count < 17:
                pygame.time.wait(500)
                self.dealer.addCard()
            else:
                dealer_turn_over = True
    def calculateResults(self):
        result_display_time = 5000
        start_time = pygame.time.get_ticks()

        while pygame.time.get_ticks() - start_time < result_display_time:
            screen.blit(pokerGreen, (0, 0))
            self.add_text("End of this turn", text_Bold, screen, halfWidth, 40, red)
            self.draw_all_hands()


            for i, p in enumerate(self.players):
                if p.EndOfTurn == False:
                    if p.bust:
                        p.result = "Bust!"
                        p.bank -= p.bet
                    elif self.dealer.count > 21:
                        p.result = f"Win! (Dealer bust)"
                        p.roundsWon += 1
                        p.bank += p.bet
                    elif p.count > self.dealer.count:
                        p.result = f"Win! ({p.count} > {self.dealer.count})"
                        p.roundsWon += 1
                        p.bank += p.bet
                    elif p.count == self.dealer.count:
                        p.result = f"Draw ({p.count} = {self.dealer.count})"
                    else:
                        p.result = f"Lose ({p.count} < {self.dealer.count})"
                        p.bank -= p.bet
                    p.EndOfTurn = True



            if leave_button.draw():
                pygame.quit()
                sys.exit()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    def ResetStats(self):
        for p in self.players:
            p.ResetHand()




#main game loop starts here

gameOver = False
while gameOver is False:
    game = Game()
    screen.blit(pokerGreen, (0, 0))
    game.fixCoordinates()
    roundOver = False
    pygame.display.update()
    while game.turnOver == False:
        game.placing_bets()
        if game.num_of_players==0:
            gameOver = True
        if game.turnOver ==True:
            break
        game.newDeck()
        game.createHands()
        game.playTurn()
        game.dealers_turn()
        game.calculateResults()
        game.ResetStats()


