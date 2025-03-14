import socket


HOST = '0.0.0.0'
PORT = 3423
format = "utf-8"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()
print(f"listening on {HOST}")


client_socket, client_address = server.accept()
print(f"Connected to {client_address}")


username = client_socket.recv(1024).decode(format)


while True:
    data = client_socket.recv(1024).decode(format)
    data = str(data)
    if not data:
        break
    print(f"{username}: {data}")
