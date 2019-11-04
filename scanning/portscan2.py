#!/usr/bin/python

import socket
from termcolor import colored

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.setdefaulttimeout(2)

host = input("[*] Enter The Host To Scan: ")

def portsscanner(port):
	if sock.connect_ex((host, port)):
		print(colored("Port %d is closed" % (port), 'red'))
	else:
		print(colored("Port %d is opened" % (port), 'green'))

# scanning multiple ports
for port in range(1, 1000):
	portsscanner(port)
