# COMP835: Networking Technologies
* Lloyd Dagoc
* Spring 2019
* University of New Hampshire

Python version: 3.6.6
Required PIP Packages: no additional pip packages required


### Homework Details
* Homework10
* Week10 April 11, 2019
* Compose a server using python which can respond to port 80 with the address of the connecting client. In the response, include HTTP Response 200 for all OK requests, and a 400 for all others.

### Project Pre-Requisites
* Python version: 3.6.6
* Requirements: None

### Program Logic
* Compose a server using python which can respond to port 80 \
with the address of the connecting client.
* On the same server, make it respond to an http request with a 200 successful response. Make it accessible via browser.

### Core Deliverables
* README.md
* MyTCPServerHandler.py - Stand-alone server that can run locally with a specified port. Defaults to port 80. Sample Usage: python MyTCPServerHandler.py 80 Sample Usage (use curl): curl -v MyTCPServerHandler
* TCPClient.py - Client socket python implementation.
** Sample Usage: python TCPClient.py localhost 80 Hello World
