"""
comp835
homework 2
Echo Client implementation from RealPython

Python version: 3.6.6
Required PIP Packages: no additional pip packages required

Lloyd Dagoc
University of New Hampshire
"""

import socket

HOST = "127.0.0.1"  # the server's hostname or ip address
PORT = 65432        # the port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)

print("Received", repr(data))
