import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.sendto('poggerd'.encode(),('127.0.0.1',8821))
(data, remote_address) = my_socket.recvfrom(1024)
print('server sent: ' + data.decode())
my_socket.close()