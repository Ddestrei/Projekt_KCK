import string
from Player import Player

class User:
    def __init__(self, name: string, album_number: string, email: string, password: string, points: int,
                 help_points: int, wins: int, loses: int, is_admin: int):
        self.name = name
        self.album_number = album_number
        self.email = email
        self.password = password
        self.points = points
        self.help_points = help_points
        self.wins = wins
        self.loses = loses
        self.is_admin = is_admin
        self.is_logged = False
        self.player = Player()
        self.sender = None
        self.hit_stand_double = False
        self.hit = False
        self.hit_stand_double = False
        self.double = False

    def add_sender(self, sender):
        self.sender = sender

    def __str__(self):
        print("Name: ", self.name)
        print("Album number: ", self.album_number)
        print("Email: ", self.email)
        print("Password: ", self.password)
        print("Points: ", self.points)
        print("Help_points: ", self.help_points)
        print("Wins: ", self.wins)
        print("Loses: ", self.loses)
        print("Is admin: ", self.is_admin)

    def send_format(self):
        return ("user_info" + " " + self.name + " " + self.album_number + " " + self.email + " " + self.password + " " +
                self.points.__str__() + " " + self.help_points.__str__() + " " + self.wins.__str__() + " " +
                self.loses.__str__() + " " + self.is_admin.__str__())

