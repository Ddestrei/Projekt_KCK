from Screen import *
from Dealer import Dealer
from Player import Player
import sys
from pygame.locals import *

screenWidth, screenHeight = resolutions[choice]
halfWidth, halfHeight = screenWidth / 2, screenHeight / 2
black, blue, white, orange, red = (0, 0, 0), (51, 235, 255), (255, 255, 255), (255, 165, 0), (255, 0, 0)
fontType = 'Comic Sans MS'
text_Title = pygame.font.SysFont(fontType, 80)
text_SubHeading = pygame.font.SysFont(fontType, 45)
text_Heading = pygame.font.SysFont(fontType, 60)
text_Bold = pygame.font.SysFont(fontType, 30)
text_Normal = pygame.font.SysFont(fontType, 20)
text_Small = pygame.font.SysFont(fontType, 10)


class GameScreen(Screen):
    def __init__(self):
        self.choice = None
        self.screen = None
        self.background = None

    def Start(self, window, choice):
        self.screen = window
        self.dealer = Dealer(self.screen)
        self.players = []
        self.num_of_players = 3
        self.turnOver = False
        self.players.append(Player("Kasia"))
        self.players.append(Player("Kacper"))
        self.players.append(Player("Oliwia"))
        self.choice = choice
        pygame.time.Clock().tick(60)
        self.background = pygame.image.load("grafika/tla/table.png")
        self.background = pygame.transform.scale(self.background, (resolutions[self.choice]))
        self.screen.blit(self.background, (0, 0))
        pygame.display.update()

    def BackgroudGetter(self):
        return self.background

    def fixCoordinates(self):
        if self.num_of_players == 1:
            self.players[0].x = round(669 * percents[choice])
            self.players[0].y = round(665 * percents[choice])
        elif self.num_of_players == 2:
            self.players[0].x = round(669 * percents[choice])
            self.players[0].y = round(665 * percents[choice])
            self.players[1].x = round(1020 * percents[choice])
            self.players[1].y = round(650 * percents[choice])
        elif self.num_of_players == 3:
            self.players[0].x = round(284 * percents[choice])
            self.players[0].y = round(646 * percents[choice])
            self.players[1].x = round(669 * percents[choice])
            self.players[1].y = round(665 * percents[choice])
            self.players[2].x = round(1020 * percents[choice])
            self.players[2].y = round(650 * percents[choice])
        elif self.num_of_players == 4:
            self.players[0].x = round(294 * percents[choice])
            self.players[0].y = round(413 * percents[choice])
            self.players[1].x = round(284 * percents[choice])
            self.players[1].y = round(646 * percents[choice])
            self.players[2].x = round(669 * percents[choice])
            self.players[2].y = round(665 * percents[choice])
            self.players[3].x = round(1020 * percents[choice])
            self.players[3].y = round(650 * percents[choice])
        elif self.num_of_players == 5:
            self.players[0].x = round(294 * percents[choice])
            self.players[0].y = round(413 * percents[choice])
            self.players[1].x = round(284 * percents[choice])
            self.players[1].y = round(646 * percents[choice])
            self.players[2].x = round(669 * percents[choice])
            self.players[2].y = round(665 * percents[choice])
            self.players[3].x = round(1020 * percents[choice])
            self.players[3].y = round(650 * percents[choice])
            self.players[4].x = round(1043 * percents[choice])
            self.players[4].y = round(410 * percents[choice])

    def add_text(self, text, font, surface, x, y, text_color):
        textObject = font.render(text, False, text_color)
        textWidth = textObject.get_rect().width
        textHeight = textObject.get_rect().height
        surface.blit(textObject, (x - (textWidth / 2), y - (textHeight / 2)))

    def delay_with_events(self, ms):
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
                self.screen.blit(self.BackgroudGetter(), (0, 0))
                self.add_text("Player " + str(i + 1 + number_of_deleted_players) + " hasn't enough points to play",
                              text_Bold, self.screen, halfWidth, 100, red)
                number_of_deleted_players += 1
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
                self.screen.blit(self.BackgroudGetter(), (0, 0))

                if leave_button.draw():
                    pygame.quit()
                    sys.exit()

                self.add_text("Player's " + str(i + 1) + " turn, place your bet", text_Bold, self.screen, halfWidth,
                              100, red)
                self.add_text("Your points: " + str(current_player.bank), text_Normal, self.screen,
                              round(150 * percents[choice]), round(100 * percents[choice]), orange)
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
        self.dealer = Dealer(self.screen)

    def draw_all_hands(self):
        # Drawing players hands
        for i, p in enumerate(self.players):
            x_offset = 0
            for card in p.hand:
                self.screen.blit(card.image, (p.x + x_offset, p.y))
                x_offset += 30
            # Adding text with number of points in cards
            if p.EndOfTurn == False:
                if p.low_count != p.high_count:
                    text = f"{p.low_count}/{p.high_count} pkt"
                else:
                    text = f"{p.low_count} pkt"
                self.add_text(text, text_Small, self.screen, p.x + 40, p.y - 10, white)
            else:
                self.add_text(str(p.result), text_Small, self.screen, p.x + 40, p.y - 10, white)

            self.add_text(p.name, text_Normal, self.screen, p.x + 40, p.y + card_height + 10, orange)

        # Draw dealers hand
        x_offset = 0
        for idx, card in enumerate(self.dealer.hand):
            if idx == 1 and self.dealer.hide_second_card:
                self.screen.blit(card_back_img, (self.dealer.x + x_offset, self.dealer.y))
            else:
                self.screen.blit(card.image, (self.dealer.x + x_offset, self.dealer.y))
            x_offset += 30

        # Show known dealers points
        if self.dealer.hide_second_card:
            visible_value = self.dealer.hand[0].value
            if self.dealer.hand[0].label == "A":
                visible_value = "1/11"
            self.add_text(f"{visible_value} pkt", text_Small, self.screen, self.dealer.x + 40, self.dealer.y - 10, red)
        else:
            if self.dealer.low_count != self.dealer.high_count:
                text = f"{self.dealer.low_count}/{self.dealer.high_count} pkt"
            else:
                text = f"{self.dealer.low_count} pkt"
            self.add_text(text, text_Small, self.screen, self.dealer.x + 40, self.dealer.y - 10, red)

    def redraw_game_screen(self):
        self.screen.blit(self.BackgroudGetter(), (0, 0))
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
                self.add_text("Dealing cards, please wait for your turn", text_Bold, self.screen, halfWidth, 40, white)
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
                self.screen.blit(self.BackgroudGetter(), (0, 0))
                self.draw_all_hands()
                self.add_text(f"Player's {self.players.index(player) + 1} turn", text_Bold, self.screen, halfWidth, 40,
                              orange)
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

                if player.count == 21 or player.high_count == 21:
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

        self.dealer.countAce()  # calculate points

        dealer_turn_over = False
        while not dealer_turn_over:
            self.screen.blit(self.BackgroudGetter(), (0, 0))
            self.draw_all_hands()
            self.add_text("Revealing cards...", text_Bold, self.screen, halfWidth, 40, red)

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
            self.screen.blit(self.BackgroudGetter(), (0, 0))
            self.add_text("End of this turn", text_Bold, self.screen, halfWidth, 40, red)
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
