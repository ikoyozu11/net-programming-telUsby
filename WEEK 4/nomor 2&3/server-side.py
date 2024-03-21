import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345

server_socket.bind((HOST, PORT))

server_socket.listen(1)
print("Menunggu koneksi terhubung...")

client_socket, client_address = server_socket.accept()
print("Koneksi dibuat dengan", client_address)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    message = data.decode()
    character_count = len(message)
    response = "Jumlah karakter adalah " + str(character_count)
    client_socket.sendall(response.encode())

client_socket.close()
server_socket.close()