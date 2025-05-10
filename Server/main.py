import socket
import threading

from OneClientConnection import OneClientConnection

if __name__ == "__main__":
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        while True:
            conn, address = server_socket.accept()
            client = OneClientConnection()
            client_thread = threading.Thread(target=client.run_client, args=(conn,address))
            client_thread.start()
            while client.is_connected is False:
                print("a")
                pass
