import threading


class OneClientConnection:

    def __init__(self, conn, address, dataBase):
        self.user = None
        self.is_connected = False
        self.client_id = ""
        self.conn = conn
        self.address = address
        print("Connection from: " + str(address))
        self.is_connected = True
        self.dataBase = dataBase
        receiver_thread = threading.Thread(target=self.receiver)
        receiver_thread.start()

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            self.read_mess(mess)

    def sender(self, message):
        self.conn.send(message.encode())

    def read_mess(self, message):
        mess_parts = message.split(" ")
        print(mess_parts)
        if mess_parts[0] == "login_to_game":
            nr_album = mess_parts[1]
            password = mess_parts[2]
            self.user = self.dataBase.get_user(nr_album)
            if self.user is None:
                self.sender("user_not_found")
            elif self.user.password != password:
                self.sender("password_incorrect")
            elif self.user.is_logged:
                self.sender("user_already_logged")
            else:
                self.sender(self.user.send_format())

        elif mess_parts[0] == "disconnect":
            pass
