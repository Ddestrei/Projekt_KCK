import sqlite3

from User import User

DATABASE_NAME = "Project_KCK.db"

USERS = [("Adrian", "123456", "123456@edu.p.lodz.pl", "password", 10, 3, 5, 5, 0, 0),
         ("Maciej", "654321", "654321@edu.p.lodz.pl", "password", 11, 2, 3, 0, 1, 0),
         ("Dorota", "135790", "135790@edu.p.lodz.pl", "password", 18, 6, 2, 5, 0, 0),
         ("Andrzej", "323223", "323223@edu.p.lodz.pl", "password", 18, 6, 2, 5, 0, 0),
         ("Marek", "543255", "543255@edu.p.lodz.pl", "password", 18, 6, 2, 5, 0, 0),
         ("Filip", "098765", "098765@edu.p.lodz.pl", "password", 0, 0, 0, 0, 0, 0),]


class DataBase:

    def __init__(self):
        self.cursor = None
        self.connection = None
        self.connect_to_database()

    def connect_to_database(self):
        self.connection = sqlite3.connect(DATABASE_NAME, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
            SELECT name FROM sqlite_master where type='table' AND name = 'users';
        """)
        if self.cursor.fetchall().__len__() == 0:
            self.cursor.execute("""
                CREATE TABLE 'users' (
                    name VARCHAR(100) NOT NULL,
                    album_number VARCHAR(6) PRIMARY KEY,
                    email VARCHAR(100) NOT NULL,
                    password VARCHAR(50) NOT NULL,
                    points INT NOT NULL,
                    help_points INT NOT NULL,
                    wins INT NOT NULL,
                    loses INT NOT NULL,
                    admin INT NOT NULL,
                    is_login INT NOT NULL
                );
            """)
            self.cursor.executemany("""
                INSERT INTO users(name,album_number,email,password,points,help_points,wins,loses,admin,is_login )
                VALUES(?,?,?,?,?,?,?,?,?,?);
            """, USERS)
            self.connection.commit()

    def add_user(self, user):
        self.cursor.executemany("""
            INSERT INTO users(name,album_number,email,password,points,help_points,wins,loses,admin,is_login)
                VALUES(?,?,?,?,?,?,?,?,?,?);
        """, [(user.name, user.album_number, user.email, user.password, user.points, user.help_points, user.wins,
               user.loses, user.is_admin, 0)])
        self.connection.commit()

    def disconnect(self):
        self.connection.close()

    def get_user(self, album_number):
        self.cursor.execute("""
            SELECT * FROM users WHERE users.album_number = ?;
        """, [album_number])
        fetch = self.cursor.fetchall()
        if fetch[0][9] == 1:
            return None
        self.set_login(fetch[0][1], 0)
        return User(fetch[0][0], fetch[0][1], fetch[0][2], fetch[0][3], fetch[0][4], fetch[0][5], fetch[0][6],
                    fetch[0][7], fetch[0][8], self.change_points)

    def change_points(self, album_number, points):
        self.cursor.executemany("""
            UPDATE users
            SET points = ?
            WHERE album_number = ?
        """, [(points, album_number)])
        self.connection.commit()
        pass

    def set_login(self, album_number, value):
        self.cursor.executemany("""
                    UPDATE users
                    SET is_login = ?
                    WHERE album_number = ?
                """, [(value, album_number)])
        self.connection.commit()
