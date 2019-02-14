"""
comp835
homework 2
Echo Server implementation from RealPython

Python version: 3.6.6
Required PIP Packages: no additional pip packages required

Lloyd Dagoc
University of New Hampshire
"""

import socket

HOST = "127.0.0.1"  # standard loopback interface address (localhost)
PORT = 65432        # port to listen on (non-privelege ports are >1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("Connected by...", addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
