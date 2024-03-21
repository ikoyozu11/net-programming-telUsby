import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = 'localhost'
PORT = 12345

client_socket.connect((HOST, PORT))

message = input("Masukkan pesan: ")
client_socket.sendall(message.encode())

response = client_socket.recv(1024)
print("Balasan dari server:", response.decode())

client_socket.close()