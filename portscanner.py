import pyfiglet
import socket
import time
import threading
from datetime import datetime 
from queue import Queue

ascii_banner = pyfiglet.figlet_format("PORT SCANNER") 
print(ascii_banner)

socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = input('Enter the host to be scanned: ')
t_IP = socket.gethostbyname(target)

print("-" * 50)
print ('Starting scan on host: ', t_IP)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

def portscan(port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      con = s.connect((t_IP, port))
      with print_lock:
         print('Port', port, 'is open')
      con.close()
   except:
      pass

def threader():
   while True:
      worker = q.get()
      portscan(worker)
      q.task_done()
      
q = Queue()
startTime = time.time()
   
for x in range(100):
   t = threading.Thread(target = threader)
   t.daemon = True
   t.start()
   
for worker in range(1, 500):
   q.put(worker)
   
q.join()
print("-" * 50)
print('Time taken:', time.time() - startTime)
print("-" * 50)
