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

HOST = "127.0.0.1"  # the server's hostname or ip address
# HOST = "10.21.128.219"  # the server's hostname or ip address
PORT = 65432        # the port used by the server

start_datetime = datetime.datetime.now()
print("Started: ", start_datetime)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Tell me time')
    data = s.recv(1024)
    unpacked_datetime = struct.unpack('ii', data)
    server_date = unpacked_datetime[0]
    server_time = unpacked_datetime[1]
    str_dt = str(server_date) + "." + str(server_time)
    fserver = float(str_dt)
    server_dt = datetime.datetime.fromtimestamp(fserver)
    print("CLIENT: ServerDT ", server_dt)

end_datetime = datetime.datetime.now()
total_duration = end_datetime - start_datetime

# print("Received", repr(data))

print("Ended: ", end_datetime, " at: ", total_duration, " milliseconds.")
