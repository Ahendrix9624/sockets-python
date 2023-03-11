"""
USAGE - This is a simple client-side socket program that establishes a connection to a server 
        running on the local machine.

        The program defines constants such as the header size, port, format, and message to be sent. 
        It creates a socket object, connects to the server, and defines a function to send a message 
        to the server.

       The send() function encodes the message, determines its length, and sends the message 
       length followed by the message to the server. It also prints the server's response. 
       The program then sends three different messages to the server and finally sends a disconnect 
       message to the server.

AUTHOR - https://github.com/Ahendrix9624/
"""
import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Drew!")

send(DISCONNECT_MESSAGE)
