from socket import *

host = "127.0.0.1"
port = 9999

server_soket = socket(AF_INET, SOCK_STREAM)
server_soket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
server_soket.bind((host, port))

print("listening...")
server_soket.listen()

client_socket, addr = server_soket.accept()
print("connected by", addr)

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print("received from data", addr, data.decode())
    client_socket.sendall(data)
client_socket.close()
server_soket.close()