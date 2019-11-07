#!/usr/bin/python

from termcolor import colored
import hashlib


def tryOpen(wordlist):
	try:
		pass_file = open(wordlist, 'r')
		return pass_file
	except:
		print("[!!] No Such File At That Path!")
		quit()


pass_hash = input("[*] Enter MD5 Hash Value: ")
wordlist = input("[*] Enter Path To The Password File: ")
pass_file = tryOpen(wordlist)

for word in pass_file:
	print(colored("[-] Trying: " + word.strip('\n'), 'yellow'))
	enc_wrd = word.encode('utf-8')
	md5digest = hashlib.md5(enc_wrd.strip()).hexdigest()

	if md5digest == pass_hash:
		print(colored("[+] Password Found: " + word, 'green'))
		exit(0)

print("[!!] Password Not In List!")
