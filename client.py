import socket
import threading
import sys

# Function to handle receiving messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"\n{message}")
            else:
                break
        except:
            print("Error receiving message")
            break

# Function to handle sending messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            client_socket.close()
            sys.exit()
        client_socket.send(message.encode('utf-8'))

# Main function to start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to server on localhost and port 12345

    # Start threads for receiving and sending messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    receive_thread.start()
    send_thread.start()

if __name__ == "__main__":
    start_client()
