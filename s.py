from threading import Timer,Thread,Event
import time, socket

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      print('start try')
      self.thread.start()
      print('start success')

   def cancel(self):
      print('cancel try')
      self.thread.cancel()
      print('cancel success')

def printer():
    print ('ipsem lorem')


class Server():
  
  def __init__(self):
    self.HOST = '127.0.0.1'
    self.PORT = 9999
    self.threads = []

    self.s = self.bind(self.HOST, self.PORT)
    print('bind complete')
    while True:
      client_socket, addr = self.s.accept()
      self.run(client_socket, addr)

  def bind(self, host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((host, port))
    s.listen()
    return s

  def run(self, client_socket, addr):
    while True:
      data = client_socket.recv(1024)
      if not data:
         break
      else:
         data = data.decode()
         print('receive data: %s'%(data))

         if data == 'start':
            t = perpetualTimer(1,printer)
            self.threads.append(t)
            t.start()  
            print('생성된 쓰레드 갯수: %d'%(len(self.threads)))

         elif data == 'stop':
            if len(self.threads):
               t = self.threads.pop()
               t.cancel()
            else: print('Threads empty')
            
s = Server()