import socket
import json
import argparse
import random
import time 
import argparse

athletes = ["Berber", "Martijn", "Quint", "Maarten", "Carmen"]
corners = ["Zamboni corner", "Long Track corner"]

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", type=str, default="127.0.0.1", help="host IP address")
    parser.add_argument("--port", type=int, default=5000, help="host port")
    parser.add_argument("--type", default="relay_exchange", help="start_recording|stop_recording|relay_exchange", type=str)

    
    args = parser.parse_args()

    host = args.host  # Server's IP address
    port = args.port  # Port used by the server

    # Create a socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Connect to the server
        client_socket.connect((host, port))
        
        if args.type == "relay_exchange":
            # Prepare a JSON message
            message = {
                "type": "relay_exchange",
                "pushing-athlete" : random.choice(athletes),
                "incoming-athlete" : random.choice(athletes),
                "corner" : random.choice(corners),
                "timestamp" : round(time.time()*1000),
                "metrics" : {
                    "acceleration-incoming-athlete" : random.randint(0,30)/10,
                    "desceleration-pushing-athlete" : random.randint(0,30)/10,
                    "speed-difference-before-push" : random.randint(0,30)/10
                }
            }
        elif args.type in ["start_recording", "stop_recording"]:
            message = {
                "type" : args.type
            }
        else:
            raise Exception(f"type {args.type} not supported")
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