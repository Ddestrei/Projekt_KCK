import threading


class OneClientConnection:

    def __init__(self, conn, address):
        self.is_connected = False
        self.client_id = ""
        self.conn = conn
        self.address = address
        print("Connection from: " + str(address))
        self.is_connected = True
        receiver_thread = threading.Thread(target=self.receiver)
        receiver_thread.start()

    def receiver(self):
        while self.is_connected:
            mess = str(self.conn.recv(1024).decode())
            print(mess)
            self.sender(mess)

    def sender(self, message):
        self.conn.send(message.encode())
