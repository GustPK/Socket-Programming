import socket

def main():
    username = input("Enter your username: ")
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    while True:
        message = input(f"{username}: ")
        if message.lower() == 'exit':
            break
        
        formatted_message = f"MESSAGE {username}: {message}"
        client_socket.send(formatted_message.encode())

        response = client_socket.recv(1024).decode()
        print(f"Server response: {response}")

    client_socket.close()

if __name__ == "__main__":
    main()
