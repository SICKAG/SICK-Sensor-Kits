# Code Snippets Vision
Below are some example code snippets to help you get started with the Vision Sensor Kit.

**Open your IDE (Visual Studio Code) and run the following demo.**

```python
1. import socket

# Function to initialize and connect the client socket
def run_client():
    global client
    # Create a socket object using IPv4 and TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Define the server's IP address and port number
    server_ip = "192.168.0.1"
    server_port = 34170

    # Connect to the server
    client.connect((server_ip, server_port))

# Function to continuously receive data from the server
def get_requests_continuously():
    global client
    try:
        while True:
            # Receive data from the server (buffer size: 1024 bytes)
            request = client.recv(1024)
            # Decode the received bytes to a string
            request = request.decode("utf-8")
            print("Received:", request)
    except KeyboardInterrupt:
        print("Stopping client...")
    finally:
        client.close()

# Initialize and run the client
run_client()
get_requests_continuously()

#trigger Commands: 

def trigger_img():
    global client

    client.sendall(b'\x02set job 2\x03')
    client.sendall(b'\x02trigger\x03')
    client.sendall(b'\x02RecordImages\x03')

 

2. Read Field Evaluation Results from Lidar: 

def fetch_data():
    import socket

    HOST = "192.168.0.153"
    PORT = 2111

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    s.sendall(b"\x02sRN FieldEvaluationResult\x03")

    data = s.recv(4048).decode('ascii')
    dataArray = data.split("\x20")

    s.close()
    
    return dataArray

```
