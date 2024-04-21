import socket
import threading

HOST = 'localhost'
PORT = 12345


def handle_client(client_socket, client_address):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        angka = int(data.decode())
        print("Request dari client: ", angka, "IP client: ", client_address)
        if angka % 2 == 0:
            response = "angka " + str(angka) + " merupakan genap"
        else:
            response = "angka " + str(angka) + " merupakan ganjil"
        client_socket.sendall(response.encode())
    client_socket.close()


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(5)

print("Waiting for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connected to:", client_address)
    client_thread = threading.Thread(
        target=handle_client, args=(client_socket, client_address))
    client_thread.start()
