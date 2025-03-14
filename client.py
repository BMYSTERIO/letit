import socket
from addtional.file_handler import *


SERVER_IP = socket.gethostbyname(socket.gethostname())  
SERVER_PORT = 3423
format = "utf-8"      


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_IP, SERVER_PORT))
print("Connected to the server.")

username = get_username()
if username == "empty":
    username = input("Enter your username: ")
    save_usrname(username)
else:
    pass


client_socket.send(username.encode(format))



while True:
    message = input(f"{username}: ") 
    if message.lower() == 'exit':  
        break
    client_socket.send(message.encode(format)) 

client_socket.close()
