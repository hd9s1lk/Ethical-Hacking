#!/bin/python3

import sys
import socket
from datetime import datetime as dt

#define our target

if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1])
else:
	print("Invalido")
	sys.exit()
	
print("-" * 50)
print("Scanning target" +target)
print("Time Started: " +str(dt.now()))
print("-" * 50)

try:
	for port in range(50,85):
		s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		print("A ver porta: " +str(port))
		if result == 0:
			print("Port: " +port)
		s.close()
		
except KeyboardInterrupt:
	print("\n A Sair...")
	sys.exit()
except socket.gaierror:
	print("Hostname can't be resolved")
	sys.exit()
except socket.error:
	print("O Sv esta down")
	sys.exit()





