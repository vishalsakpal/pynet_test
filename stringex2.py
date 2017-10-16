#!/usr/bin/env python
from __future__ import print_function

ip_addr = input("Enter IP Address:")

print (ip_addr)

ip_addr = ip_addr.split(".")

print (ip_addr)

print ("{:<12} {:<12} {:<12} {:<12}".format(*ip_addr))

