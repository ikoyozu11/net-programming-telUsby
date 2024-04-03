import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024


def list_files():
    files = os.listdir('.')
    if files:
        return '\n'.join(files)
    else:
        return "Directory is empty"


def file_size(filename):
    if os.path.exists(filename):
        size = os.path.getsize(filename) / (1024 * 1024)
        return f'{filename}: {size:.2f} MB'
    else:
        return 'File not found'


def remove_file(filename):
    try:
        os.remove(filename)
        return f'{filename} removed successfully'
    except OSError as e:
        return f'Error: {e.strerror}'


def receive_file(client_socket, filename):
    with open(filename, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if not data:
                break
            file.write(data)


def send_file(client_socket, filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            while True:
                data = file.read(BUFFER_SIZE)
                if not data:
                    break
                client_socket.send(data)
        print(f"[*] File '{filename}' sent successfully")
    else:
        print(f"[!] File '{filename}' not found")
        client_socket.send("File not found".encode())


def main():
    print("[*] Starting server...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((SERVER_HOST, SERVER_PORT))
        server_socket.listen(1)
        print(f"[*] Server listening on {SERVER_HOST}:{SERVER_PORT}")

        while True:
            client_socket, client_address = server_socket.accept()
            print(
                f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")

            while True:
                data = client_socket.recv(BUFFER_SIZE).decode()

                if not data:
                    break

                if data == 'connme':
                    print("[*] Connection established.")
                    continue

                if data == 'ls':
                    files_list = list_files()
                    client_socket.send(files_list.encode())
                elif data.startswith('size'):
                    filename = data.split()[1]
                    file_info = file_size(filename)
                    client_socket.send(file_info.encode())
                elif data.startswith('rm'):
                    filename = data.split()[1]
                    removal_info = remove_file(filename)
                    client_socket.send(removal_info.encode())
                elif data.startswith('upload'):
                    filename = data.split()[1]
                    client_socket.send("Ready to receive file".encode())
                    receive_file(client_socket, filename)
                    client_socket.send(
                        f"{filename} uploaded successfully".encode())
                elif data.startswith('download'):
                    filename = data.split()[1]
                    send_file(client_socket, filename)
                elif data == 'byebye':
                    print(
                        f"[*] Closing connection from {client_address[0]}:{client_address[1]}")
                    client_socket.send("Connection closed".encode())
                    break
                else:
                    client_socket.send("Command not found".encode())

            client_socket.close()


if __name__ == "__main__":
    main()
