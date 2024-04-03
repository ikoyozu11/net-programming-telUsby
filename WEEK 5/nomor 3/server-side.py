import socket

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
sock.bind(server_address)

while True:
    print('Menunggu pesan dari client...')
    data, address = sock.recvfrom(4096)
    message = int(data.decode())
    print('Menerima pesan dari client:', message)
    
    # Mengecek apakah input merupakan bilangan prima
    if is_prime(message):
        response = 'Input adalah bilangan prima'
    else:
        response = 'Input bukan bilangan prima'
    
    # Mengirim balasan ke client
    sock.sendto(response.encode(), address)
