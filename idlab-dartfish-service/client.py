import socket
import json
import argparse



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1", help="host IP address")
    parser.add_argument("--port", type=int, default=5000, help="host port")
    args = parser.parse_args()

    host = args.host  # Server's IP address
    port = args.port  # Port used by the server

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Prepare a JSON message
        message = {
            "type": "relay_exchange",
            "pushing-athlete" : "John Doe",
            "incoming-athlete" : "Jane Doe",
            "corner" : 1,
            #"relay-number" : "1:2",
            "timestamp" : 1733318347197,
            "metrics" : {
                "acceleration-incoming-athlete" : "2.3 m/s2",
                "desceleration-pushing-athlete" : "2.3 m/s2",
                "speed-difference-before-push" : "3 km/h"
            },
            "description" : "free text"
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