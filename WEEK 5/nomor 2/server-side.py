import socket

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
sock.bind(server_address)

while True:
    print('Menunggu pesan dari client...')
    data, address = sock.recvfrom(4096)
    message = data.decode()
    print('Menerima pesan dari client:', message)
    
    # Menghitung jumlah karakter pada pesan
    num_chars = len(message)
    response = f'Jumlah karakter: {num_chars}'
    
    # Mengirim balasan ke client
    sock.sendto(response.encode(), address)
