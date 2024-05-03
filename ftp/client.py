import socket
import os

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345
BUFFER_SIZE = 1024


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
            client_socket.send(command.encode())

            if command == 'byebye':
                print("[*] Disconnecting from server...")
                print(client_socket.recv(BUFFER_SIZE).decode())
                break

            data = client_socket.recv(BUFFER_SIZE).decode()
            if data == "Command not found":
                print("[!] Command not found. Please enter a valid command.")
            elif data.startswith("File with name"):
                print(data)
                new_filename = input("Please enter a different filename: ")
                client_socket.send(new_filename.encode())
            else:
                print(data)
                if command.startswith('upload'):
                    filename = command.split()[1]
                    print(client_socket.recv(BUFFER_SIZE).decode())
                    client_socket.send("start_upload".encode())
                    send_file(client_socket, filename)
                    print(client_socket.recv(BUFFER_SIZE).decode())


if __name__ == "__main__":
    main()
