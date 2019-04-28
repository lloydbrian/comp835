"""
comp835
homework 10
CheckIP Implementation - Client
Compose a server using python which can respond to port 80 \
with the address of the connecting client.

Python version: 3.6.6
Required PIP Packages: no additional pip packages required

Lloyd Dagoc
University of New Hampshire
"""


import socket
import sys


if len(sys.argv) < 3:
    print("Hostname and Port required as parameters. Defaulting to port 80")
    HOST = "localhost"
    PORT = 80
    data = "Your parameter count is incorrect but still, Hello World"
    # sys.exit
else:
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    data = " ".join(sys.argv[1:])  # join all args following the stqtement


sock_peername = ""

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    sock_peername = sock.getpeername()
    sock.sendall(bytes(data + "\n", "utf-8"))

    # Received data from the server and shutdown
    received = str(sock.recv(1024), "utf-8")

print("Sent:            {}".format(data))
print("Data sent to:    {}".format(sock_peername))
print("Reeived:         {}".format(received))
