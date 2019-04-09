# coding: utf-8
import socket
from datetime import datetime
from multiprocessing.dummy import Pool as ThreadPool
 
remote_server = input("Enter a remote host to scan:")
remote_server_ip = socket.gethostbyname(remote_server)
ports = []
 

print ('Please wait, scanning remote host ', remote_server_ip)

 
socket.setdefaulttimeout(5)
 
def scan_port(port):
    try:
        s = socket.socket(2,1)
        res = s.connect_ex((remote_server_ip,port))
        if res == 0: 
            print( 'Port {}: OPEN'.format(port))
        s.close()
    except Exception as e:
        print( str(e.message))
 
 
 
for i in range(1,65535):
    ports.append(i)
 
t1 = datetime.now()
 
 
pool = ThreadPool(32)
results = pool.map(scan_port,ports)
pool.close()
pool.join()
 
print ('Multiprocess Scanning Completed in  ', datetime.now() - t1)
