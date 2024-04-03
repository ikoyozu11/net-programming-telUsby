import socket

def is_palindrome(string):
    return string == string[::-1]

# Inisialisasi socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5000)
sock.bind(server_address)

while True:
    print('Menunggu pesan dari client...')
    data, address = sock.recvfrom(4096)
    message = data.decode()
    print('Menerima pesan dari client:', message)
    
    # Mengecek apakah input merupakan palindrom
    if is_palindrome(message):
        response = 'Input adalah palindrom'
    else:
        response = 'Input bukan palindrom'
    
    # Mengirim balasan ke client
    sock.sendto(response.encode(), address)
