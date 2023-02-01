import socket
import datetime
import random
server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 20001))
server_socket.listen()
print("Server is up and running")
(client_socket, client_address) = server_socket.accept()
print("Client connected")
data = client_socket.recv(1024).decode()
print("Client sent: " + data)
if data == "TIME":  
    reply = str(datetime.datetime.now().hour) + " " + data
if data == "WHORU":
    reply = "test server nameXX" + " " + data
if data == "RAND":
    reply = str(random.randint(1,11))
if data == "EXIT":
    client_socket.close()
    server_socket.close()
client_socket.send(reply.encode())
client_socket.close()
server_socket.close()

