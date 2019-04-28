"""
comp835
homework 10
CheckIP Implementation - Server
Compose a server using python which can respond to port 80 \
with the address of the connecting client.

Python version: 3.6.6
Required PIP Packages: no additional pip packages required

Lloyd Dagoc
University of New Hampshire
"""

import socketserver
import sys


class MyTCPServerHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{}:{} wrote: ".format(self.client_address[0], self.client_address[1]))
        print(self.data)
        # just send back the same data, but upper-cased
        # self.request.sendall(self.data.upper())

        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        resp_body = "<html><body><center><h3>Status 200: Hello World from Lloyd</h3><p>Python HTTP Server</p></center></body></html>"

        resp_headers = {
            "Content-Type": "text/html; encoding=utf8",
            "Content-Length": len(resp_body),
            "Connection": "Active - Wohooo",
        }

        resp_headers_raw = ''.join('%s: %s\n' % (x, y) for x, y in resp_headers.items())
        print(resp_headers)

        resp_protocol = "HTTP/1.1"
        resp_status = "200"
        respo_status_text = "OK - You got this!"

        self.request.send("{} {} {}".format(resp_protocol, resp_status, respo_status_text).encode("utf-8"))
        self.request.send(bytes("\n", "utf-8"))
        self.request.send(bytes(resp_headers_raw, "utf-8"))
        # to separate headers from body
        self.request.send(bytes("\n", "utf-8"))
        self.request.send(bytes(resp_body, "utf-8"))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Hostname and Port required as parameters. Defaulting.")
        HOST = "localhost"
        PORT = 80
        # sys.exit
    else:
        HOST = sys.argv[1]
        PORT = int(sys.argv[2])

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPServerHandler) as server:
        # Activate the server; this will keep running until interrupted
        print("Server running at {}:{}".format(HOST, PORT))
        server.serve_forever()
