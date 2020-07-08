import socket, time
import asyncio, random

async def start():
  host = '127.0.0.1'
  port = 9999

  client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  client_socket.connect((host, port))
  await asyncio.sleep(random.randint(1, 4))
  client_socket.sendall('start'.encode())

async def main():
  await asyncio.wait([ 
    start(),
    start(),
    start()
  ])

asyncio.run(main())

# client_socket.sendall('stop'.encode())
# data = client_socket.recv(1024)
# print('receive data: %s'%(data.decode()))
# client_socket.close()