#!/usr/bin/python

import crypt
from termcolor import colored

def crackPass(cryptWord):
	salt = cryptWord[0:2]
	dictionary = open('dictionary.txt', 'r')
	for word in dictionary.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word, salt)
		if cryptPass == cryptWord:
			print(colored("[+] Found Password: " + word, 'green'))
			return True
	return False

def main():
	passFile = open('pass1.txt', 'r')
	for line in passFile.readlines():
		if ":" in line:
			user, cryptWord = line.split(':')
			cryptWord = cryptWord.strip('\n')
			print(colored("[*] Cracking Password For: " + user, 'red'))
			if crackPass(cryptWord):
				exit(0)
	print('[-] Password Not Found')

main()
