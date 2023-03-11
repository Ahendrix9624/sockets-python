"""
USAGE - The code creates a server that listens on a specific IP address and port. 
        It uses sockets and threading modules to handle incoming connections from clients. 
        The server binds to the IP address and port, and starts listening for incoming connections. 
        When a client connects, it creates a new thread to handle the client's connection. 
        The handle_client() function receives messages from the client, prints the message along with the 
        client's address, and sends a confirmation message back to the client. If the client sends 
        the DISCONNECT_MESSAGE, the connection is closed. The start() function listens for incoming 
        connections and starts a new thread for each incoming connection.

AUTHOR - https://github.com/Ahendrix9624/
"""
import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())  # Get the Ip address of this computer
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
# print((SERVER))
# print(socket.gethostname())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        
        
print("[STARTING] server is starting...")
start()
