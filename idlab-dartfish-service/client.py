import socket
import json

def main():
    host = '127.0.0.1'  # Server's IP address
    port = 5000         # Port used by the server

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Prepare a JSON message
        message = {
            "type": "greeting",
            "content": "Hello from Python!"
        }
        json_message = json.dumps(message)

        # Send the message
        client_socket.sendall(json_message.encode('utf-8'))
        print("Message sent!")

        # Receive a response
        response = client_socket.recv(1024)
        print("Received response:", response.decode('utf-8'))

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == '__main__':
    main()