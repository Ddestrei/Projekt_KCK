class OneClientConnection:
    def __init__(self):
        self.is_connected = False

    def run_client(self, conn, address):
        # accept new connection
        print("Connection from: " + str(address))
        self.is_connected = True
        while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("from connected user: " + str(data))
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

        conn.close()  # close the connection
