## Homework 9 Submission
## Updated for mac users with results
Setup a Python2 environment, download the PyPXE server and run it in DHCPProxy mode and download a file from it using the tftpy client.

### Pre-Requisites
1. You can use anaconda: https://docs.anaconda.com/anaconda/user-guide/tasks/switch-environment/
2. You can use pip and then install PyPXE and tftpy separately. Lloyd Dagoc did item2.

```
$ touch /tmp/lloyd.txt
$ vi /tmp/lloyd.txt
$ source activate py2
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ pip install PyPXE
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ pip install tftpy
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ python --version
Python 2.7.10
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ sudo python -m pypxe.server --dhcp-proxy --netboot-dir "/tmp"

2019-04-07 16:53:32,898 [INFO] PyPXE Starting TFTP server...
2019-04-07 16:53:32,898 [INFO] PyPXE Starting DHCP server in ProxyDHCP mode...
2019-04-07 16:53:32,898 [INFO] PyPXE PyPXE successfully initialized and running!
```

At another terminal, using the installed tftpy pip package, retrieve a file. Ensure you are running python2 virtualenv

```
$ source activate py2
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ python
Python 2.7.10 (default, Feb 22 2019, 21:17:52)
[GCC 4.2.1 Compatible Apple LLVM 10.0.1 (clang-1001.0.37.14)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import tftpy
>>> client = tftpy.TftpClient('127.0.0.1', 69)
>>> client.download('lloyd.txt', 'lloyddownload.txt')
>>> exit()
```

Verify downloaded file
```
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$ ls
PyPXE.md		lloyddownload.txt
(networkpy27) Lloyds-MB-Pro:homework9 lloydbrian$
```
