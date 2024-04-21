from email import message
import socket

from threading import Thread

# Konfigurasi client dan server
connectionSocket = socket.socket()

serverIP = "127.0.0.1"
serverPort = 2222


def kirim_pesan(handlerSocket: socket.socket):
    while True:
        message = input()
        handlerSocket.send(message.encode())
        print("client : {}".format(message))


def terima_pesan(handlerSocket: socket.socket):
    while True:
        message = handlerSocket.recv(1024)
        print("server : {}".format(message.decode("utf-8")))


# Menghubungi server
connectionSocket.connect((serverIP, serverPort))
print("terhubung dengan server")

t1 = Thread(target=terima_pesan, args=(connectionSocket,))
t2 = Thread(target=kirim_pesan, args=(connectionSocket,))

t1.start()
t2.start()

t1.join()
t2.join()
