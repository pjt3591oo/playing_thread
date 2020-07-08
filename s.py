from threading import Timer,Thread,Event
import time, socket

class perpetualTimer():
   cnt = 0
   def __init__(self,t,hFunction):
      perpetualTimer.cnt += 1
      self.cnt = perpetualTimer.cnt
      self.id = str(time.time()).split('.')[1]
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction(self.cnt, self.id)
      self.thread = Timer(self.t,self.handle_function)
      
      self.thread.start()

   def start(self):
      print('[%s] start try'%(self.id))
      self.thread.start()
      print('[%s] start success'%(self.id))

   def cancel(self):
      print('[%s] cancel try'%(self.id))
      self.thread.cancel()
      print('[%s] cancel success'%(self.id))

def printer(cnt, i):
    print ('[%d %7s] ipsem lorem'%(cnt, i))


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