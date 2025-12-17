# Code Snippets LiDAR

Below are some example code snippets to help you get started with the LiDAR Sensor Kit:

## Read Device Type
The LiDAR Starter Kit provides advanced features for developers to customize and optimize their applications. This guide covers how to interact with the device programmatically and configure it for specific use cases.
```python
import socket
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"\x02sRN DItype\x03")
    data = s.recv(1024)
 
print(f"Received {data}")
```

## Read scan data
To retrieve scan data from the LiDAR Starter Kit, you can use the following Python script. This script demonstrates how to send a command to the device and receive the corresponding scan data response.
```python
import socket
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"\x02sRN LMDscandata\x03")
    data = s.recv(1024)
 
print(f"Received {data}")
```

## Read scan data continous
To continuously read scan data from the LiDAR Starter Kit, you can use the following Python script. This script enables the device to send scan data in real-time, which can be processed as needed for your application.
```python
import socket
import time
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"\x02sEN LMDscandata 1\x03")
         
    while True:
        data = s.recv(2048)
        print(data)
```