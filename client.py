from socket import *

host = "127.0.0.1"
port = 9999

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((host, port))
client_socket.sendall("hello".encode())

data = client_socket.recv(1024)
print("received from data", repr(data.decode()))

client_socket.close()
