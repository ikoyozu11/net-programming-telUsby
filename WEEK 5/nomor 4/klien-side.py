import socket

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)

# Meminta input dari pengguna
numbers = input('Masukkan n buah bilangan bulat (pisahkan dengan koma): ')

# Mengirim pesan ke server
sock.sendto(numbers.encode(), server_address)

# Menerima balasan dari server
data, _ = sock.recvfrom(4096)
print('Menerima balasan dari server:', data.decode())
