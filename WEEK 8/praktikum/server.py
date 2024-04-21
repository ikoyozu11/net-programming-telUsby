# Import library
import socket
from threading import Thread

# Konfigurasi server
listenerSocket = socket.socket()
serverIP = "0.0.0.0"
serverPort = 2222

# Fungsi kirim pesan


def kirim_pesan(handlerSocket: socket.socket):
    while True:
        message = input()
        handlerSocket.send(message.encode())
        print("server : {}".format(message))

# Fungsi terima pesan


def terima_pesan(handlerSocket: socket.socket):
    while True:
        message = handlerSocket.recv(1024)
        print("client : {}".format(message.decode('utf-8')))


# Binding socket dengan IP dan Port
listenerSocket.bind((serverIP, serverPort))

# Listener socket siap menerima koneksi
listenerSocket.listen(0)
print("server menunggu koneksi dari client...")

# listener socket menunggu koneksi dari client, line di bawah ini bersifat 'blocking'
# artinya, programmnya terhenti di sini sampai ada koneksi ke listenerSocket
handler, addr = listenerSocket.accept()

# jika sudah ada koneksi dari client, maka program akan jalan ke line ini
print("sebuah client terkoneksi dengan alamat : {}".format(addr))

t1 = Thread(target=kirim_pesan, args=(handler,))
t2 = Thread(target=terima_pesan, args=(handler,))

t1.start()
t2.start()

t1.join()
t2.join()
