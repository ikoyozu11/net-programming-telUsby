import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024


def main():
    print("\n------------------------------------")
    print("FTP with Socket Programming on Python")
    print("-------------------------------------")
    print("Choose Command:")
    print("connme                : Connect to server (run this first to continue other commands)")
    print("ls                    : List files")
    print("size <file_name>      : View size files")
    print("upload <file_name>    : Upload file")
    print("download <file_name>  : Download file")
    print("rm <file_name>        : Delete file")
    print("byebye                : Exit program and Disconnect from server")
    print("-------------------------------------")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        while True:
            command = input("\nEnter Command : ").strip()
            if command == 'connme':
                client_socket.connect((SERVER_HOST, SERVER_PORT))
                print(f"[*] Connected to server {SERVER_HOST}:{SERVER_PORT}")
                client_socket.send(command.encode())
                print("[*] Connection established.")
                break

        while True:
            command = input("\nEnter Command : ").strip()
            client_socket.send(command.encode())

            if command == 'byebye':
                print("[*] Disconnecting from server...")
                print(client_socket.recv(BUFFER_SIZE).decode())
                break

            data = client_socket.recv(BUFFER_SIZE).decode()
            if data == "Command not found":
                print("[!] Command not found. Please enter a valid command.")
            else:
                print(data)


if __name__ == "__main__":
    main()
