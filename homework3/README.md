# COMP835: Networking Technologies
* Lloyd Dagoc
* Spring 2019
* University of New Hampshire

Python version: 3.6.6
Required PIP Packages: no additional pip packages required


### Homework Details
* Homework3
* Week3 February 7, 2019
* Implement RFC868: https://tools.ietf.org/html/rfc868.html
* Also implement this pseudo-code:
```
before_call  = datetime.now()
with socket as s
   s.connect
   data = s.receive
after_call = datetime.now()
milliseconds = after_call - before_call
print(f"it took {miliseconds} to fetch {data}")
```

### Project Pre-Requisites
* Python version: 3.6.6
* Requirements: None

### Program Logic
* In the echo server and client implementation, return server time

### Core Deliverables
* rfc868-server.py
* rfc868-client.py
