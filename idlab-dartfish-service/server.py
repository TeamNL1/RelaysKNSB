import socket

def main():
    host = '127.0.0.1'  # IP address to bind the server
    port = 5000         # Port to listen on

    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)  # Listen for incoming connections (max 1 in queue)
    print(f"Server started on {host}:{port}")

    while True:
        # Accept a connection from a client
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        try:
            # Receive data from the client
            data = client_socket.recv(1024)
            if not data:
                break

            # Decode and print the received data
            received_message = data.decode('utf-8')
            print(f"Received: {received_message}")

            # Echo the message back to the client
            client_socket.sendall(data)
            print(f"Sent back: {received_message}")

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            # Close the connection with the client
            client_socket.close()
            print(f"Connection closed with {client_address}")

if __name__ == '__main__':
    main()