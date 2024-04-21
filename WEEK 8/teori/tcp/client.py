import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345
client_socket.connect((HOST, PORT))

while True:
    pesan = input("Masukkan angka (ketik 'exit' untuk keluar): ")
    if pesan.lower() == 'exit':
        break
    client_socket.sendall(pesan.encode())

    data = client_socket.recv(1024)
    print(data.decode())

client_socket.close()
