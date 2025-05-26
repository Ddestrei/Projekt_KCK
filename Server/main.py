import socket
import threading

from OneClientConnection import OneClientConnection

if __name__ == "__main__":
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    clients = []
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        while True:
            conn, address = server_socket.accept()
            client = OneClientConnection(conn, address)
            clients.append(client)
