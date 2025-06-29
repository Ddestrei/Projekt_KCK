import sys

from pygame.locals import *

from Client import Client
from Screen import *
from Table import Table

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
    def __init__(self, client: Client):
        self.choice = None
        self.screen = None
        self.background = None
        self.table = None
        self.client = client

    def Start(self, window, choice):
        self.screen = window
        self.choice = choice
        pygame.time.Clock().tick(60)
        self.background = pygame.image.load(Game_background_path)
        self.background = pygame.transform.scale(self.background, (resolutions[self.choice]))
        self.screen.blit(self.background, (0, 0))
        self.fixCoordinates()
        if self.client.user.placing_bets:
            for p in self.table.users_name:
                p.reset_hand()
                self.table.dealer.reset_hand()
            self.placing_bets()
        self.redraw_game_screen()
        pygame.display.update()

    def set_table(self, table: Table):
        self.table = table

    def BackgroudGetter(self):
        return self.background

    def fixCoordinates(self):
        if self.table.amount_users == 1:
            self.table.users_name[0].x = round(669 * percents[choice])
            self.table.users_name[0].y = round(665 * percents[choice])
        elif self.table.amount_users == 2:
            self.table.users_name[0].x = round(669 * percents[choice])
            self.table.users_name[0].y = round(665 * percents[choice])
            self.table.users_name[1].x = round(1020 * percents[choice])
            self.table.users_name[1].y = round(650 * percents[choice])
        elif self.table.amount_users == 3:
            self.table.users_name[0].x = round(284 * percents[choice])
            self.table.users_name[0].y = round(646 * percents[choice])
            self.table.users_name[1].x = round(669 * percents[choice])
            self.table.users_name[1].y = round(665 * percents[choice])
            self.table.users_name[2].x = round(1020 * percents[choice])
            self.table.users_name[2].y = round(650 * percents[choice])
        elif self.table.amount_users == 4:
            self.table.users_name[0].x = round(294 * percents[choice])
            self.table.users_name[0].y = round(413 * percents[choice])
            self.table.users_name[1].x = round(284 * percents[choice])
            self.table.users_name[1].y = round(646 * percents[choice])
            self.table.users_name[2].x = round(669 * percents[choice])
            self.table.users_name[2].y = round(665 * percents[choice])
            self.table.users_name[3].x = round(1020 * percents[choice])
            self.table.users_name[3].y = round(650 * percents[choice])
        elif self.table.amount_users == 5:
            self.table.users_name[0].x = round(294 * percents[choice])
            self.table.users_name[0].y = round(413 * percents[choice])
            self.table.users_name[1].x = round(284 * percents[choice])
            self.table.users_name[1].y = round(646 * percents[choice])
            self.table.users_name[2].x = round(669 * percents[choice])
            self.table.users_name[2].y = round(665 * percents[choice])
            self.table.users_name[3].x = round(1020 * percents[choice])
            self.table.users_name[3].y = round(650 * percents[choice])
            self.table.users_name[4].x = round(1043 * percents[choice])
            self.table.users_name[4].y = round(410 * percents[choice])

    def add_text(self, text, font, surface, x, y, text_color):
        textObject = font.render(text, False, text_color)
        textWidth = textObject.get_rect().width
        textHeight = textObject.get_rect().height
        surface.blit(textObject, (x - (textWidth / 2), y - (textHeight / 2)))

    def placing_bets(self):
        i = 0
        number_of_deleted_players = 0
        while i < len(self.table.users_name):
            current_player = self.table.users_name[i]

            if current_player.bank < 0.5:
                self.screen.blit(self.BackgroudGetter(), (0, 0))
                self.add_text("Player " + str(i + 1 + number_of_deleted_players) + " hasn't enough points to play",
                              text_Bold, self.screen, halfWidth, 100, red)
                number_of_deleted_players += 1
                if leave_button.draw(self.screen):
                    pygame.quit()
                    sys.exit()
                pygame.display.update()
                # self.delay_with_events(1000)
                self.players.pop(i)
                self.num_of_players -= 1
                if self.num_of_players == 0:
                    self.turnOver = True
                    return
                continue

            bet_placed = False
            while not bet_placed:
                self.screen.blit(self.BackgroudGetter(), (0, 0))
                if leave_button.draw(self.screen):
                    pygame.quit()
                    sys.exit()
                self.add_text("Player's " + str(i + 1) + " turn, place your bet", text_Bold, self.screen, halfWidth,
                              100, red)
                self.add_text("Your points: " + str(self.client.user.points), text_Normal, self.screen,
                              round(150 * percents[choice]), round(100 * percents[choice]), orange)
                bet05_button.set_enabled(current_player.bank >= 0.5)
                bet1_button.set_enabled(current_player.bank >= 1)
                bet15_button.set_enabled(current_player.bank >= 1.5)

                if bet05_button.draw(self.screen):
                    current_player.bet = 0.5
                    current_player.ready = True
                    bet_placed = True
                    self.client.sender("PLACE_BET" + " " + str(0.5))
                    self.client.user.placing_bets = False

                if bet1_button.draw(self.screen):
                    current_player.bet = 1
                    current_player.ready = True
                    bet_placed = True
                    self.client.sender("PLACE_BET" + " " + str(1))
                    self.client.user.placing_bets = False

                if bet15_button.draw(self.screen):
                    current_player.bet = 1.5
                    current_player.ready = True
                    bet_placed = True
                    self.client.sender("PLACE_BET" + " " + str(1.5))
                    self.client.user.placing_bets = False

                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.client.sender("LEAVE")

                pygame.display.update()

            i += 1

    def draw_all_hands(self):
        # Drawing players hands
        for i, p in enumerate(self.table.users_name):
            x_offset = 0
            for card in p.hand:
                self.screen.blit(card.image, (p.x + x_offset, p.y))
                x_offset += 30
            # Adding text with number of points in cards
            if not p.EndOfTurn:
                if p.low_count != p.high_count:
                    text = f"{p.low_count}/{p.high_count} pkt"
                else:
                    text = f"{p.low_count} pkt"
                self.add_text(text, text_Small, self.screen, p.x + 40, p.y - 10, white)
            else:
                self.add_text(str(p.result), text_Small, self.screen, p.x + 40, p.y - 10, white)

            self.add_text(p.user_name, text_Normal, self.screen, p.x + 40, p.y + card_height + 10, orange)

        # Draw dealers hand
        x_offset = 0
        for idx, card in enumerate(self.table.dealer.hand):
            if idx == 1 and self.table.dealer.hide_second_card:
                self.screen.blit(card_back_img, (self.table.dealer.x + x_offset, self.table.dealer.y))
            else:
                self.screen.blit(card.image, (self.table.dealer.x + x_offset, self.table.dealer.y))
            x_offset += 30

        # Show known dealers points
        if self.table.dealer.hide_second_card:
            if self.table.dealer.get_first_card:
                visible_value = self.table.dealer.hand[0].value
                if self.table.dealer.hand[0].label == "A":
                    visible_value = "1/11"
                self.add_text(f"{visible_value} pkt", text_Small, self.screen, self.table.dealer.x + 40,
                              self.table.dealer.y - 10, red)
        else:
            if self.table.dealer.low_count != self.table.dealer.high_count:
                text = f"{self.table.dealer.low_count}/{self.table.dealer.high_count} pkt"
            else:
                text = f"{self.table.dealer.low_count} pkt"
            self.add_text(text, text_Small, self.screen, self.table.dealer.x + 40, self.table.dealer.y - 10, red)

    def redraw_game_screen(self):
        self.screen.blit(self.BackgroudGetter(), (0, 0))
        self.draw_all_hands()
        if self.client.user.hit_stand_double:
            self.add_text("Choose!!! HIT, STAND or DOUBLE", text_Bold, self.screen, halfWidth, 100, red)
            if hit_button.draw(self.screen):
                self.client.sender("HIT")
                self.client.user.hit_stand_double = False
            if stand_button.draw(self.screen):
                self.client.sender("STAND")
                self.client.user.hit_stand_double = False
            if double_button.draw(self.screen):
                self.client.sender("DOUBLE")
                self.client.user.hit_stand_double = False
        else:
            if self.client.drow is True:
                self.add_text("Drow", text_Bold, self.screen, halfWidth, 100, red)
            elif self.client.win is True:
                self.add_text("Win", text_Bold, self.screen, halfWidth, 100, red)
            elif self.client.lose is True:
                self.add_text("Lose", text_Bold, self.screen, halfWidth, 100, red)
            else:
                self.add_text("Dealing cards", text_Bold, self.screen, halfWidth, 100, red)
        if leave_button.draw(self.screen):
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
