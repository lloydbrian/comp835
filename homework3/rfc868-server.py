"""
comp835
homework 3
Client-Server datetime implementation
RFC868
https://tools.ietf.org/html/rfc868.html

Python version: 3.6.6
Required PIP Packages: no additional pip packages required

Lloyd Dagoc
University of New Hampshire
"""

import socket
import datetime
import struct

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
            server_datetime = datetime.datetime.now()
            server_timestamp = server_datetime.timestamp()

            # timestamp is in float format
            # next lines is to split the float so it can be passed as
            # 2 objects in the struck.pack
            str_stamp = str(server_timestamp)
            str_dtlist = str_stamp.split(".")
            int_dtlist = [int(dt) for dt in str_dtlist]

            print("SERVER: ServerDT: ",  datetime.datetime.fromtimestamp(server_timestamp))
            packed_data = struct.pack('ii', int_dtlist[0], int_dtlist[1])

            conn.sendall(packed_data)
