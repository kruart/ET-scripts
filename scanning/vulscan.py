#!/usr/bin/python

import socket
import os
import sys

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except:
		return

def checkVulns(banner, filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip("\n") in banner:
			print("[+] Server is vulnerable: " + banner.strip("\n"))

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print("[-] File Doesn't Exist!")
			exit(0)
		if not os.access(filename, os.R_OK):
			print('[-] Access Denied!')
			exit(0)
	else:
		print('[-] Usage: ' + str(sys.argv[0]) + ' <vuln filename>')
		exit(0)
	portlist = [21,22,25,80,110,443,445]
	for x in range(35, 36):	#35 is port of my metasploittable machine
		ip = "192.168.1." + str(x)
		for port in portlist:
			banner = str(retBanner(ip, port))
			if banner:
				print('[+] ' + ip + '/' + str(port) + ' : ' + banner)
				checkVulns(banner, filename)

main()
