#!/usr/bin/python

import scapy.all as scapy
import argparse


def get_args():
        parser = argparse.ArgumentParser()
        parser.add_argument("-t", "--target", dest="target", help="Target IP / IP range.")
        options = parser.parse_args()
        return options


def scan(ip):
        # scapy.arping(ip)
        # our own impl
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        clients = []
        for elem in answered_list:
                client_dict = {"ip": elem[1].psrc, "mac": elem[1].hwsrc}
                clients.append(client_dict)
        return clients


def print_result(results_list):
        print("IP\t\t\tMAC Address\n-----------------------------------------")
        for client in results_list:
                print(client["ip"] + "\t\t" + client["mac"])

# run comman: python network_scanner.py  -t 192.168.1.1/24
options = get_args()
# scan_result = scan("192.168.1.1/24")
scan_result = scan(options.target)
print_result(scan_result)
