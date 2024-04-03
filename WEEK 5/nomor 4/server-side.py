import socket

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
sock.bind(server_address)

while True:
    print('Menunggu pesan dari client...')
    data, address = sock.recvfrom(4096)
    numbers = data.decode().split(',')
    numbers = [int(num) for num in numbers]
    print('Menerima pesan dari client:', numbers)
    
    # Menghitung hasil penjumlahan dari semua bilangan yang diterima
    result = sum(numbers)
    
    # Mengirim balasan ke client berupa hasil penjumlahan
    response = f'Hasil penjumlahan: {result}'
    sock.sendto(response.encode(), address)
