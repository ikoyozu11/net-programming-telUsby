import socket

serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024

# Membuat koneksi socket
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    # Menerima input dari pengguna
    msgFromClient = input(
        "Masukkan pesan untuk dikirim ke server (ketik 'quit' untuk keluar): ")
    if msgFromClient.lower() == 'quit':
        break

    bytesToSend = str.encode(msgFromClient)

    # Kirim pesan
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message From Server:{}".format(msgFromServer[0])
    print(msg)

UDPClientSocket.close()
