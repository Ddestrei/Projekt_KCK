class User:
    def __init__(self, name, album_number, email, password, points, help_points, wins, loses, is_admin):
        self.name = name
        self.album_number = album_number
        self.email = email
        self.password = password
        self.points = points
        self.help_points = help_points
        self.wins = wins
        self.loses = loses
        self.is_admin = is_admin

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
