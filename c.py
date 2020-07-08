import socket, time

host = '127.0.0.1'
port = 9999

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((host, port))
client_socket.sendall('start'.encode())

time.sleep(3)

client_socket.sendall('stop'.encode())
# data = client_socket.recv(1024)
# print('receive data: %s'%(data.decode()))
# client_socket.close()