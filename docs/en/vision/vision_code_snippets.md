<!-- # Code Snippets Vision
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


-->

# Vision Code Examples

## Short Description

This page provides small Python code examples for communicating with the Vision Starter Kit over TCP/IP.

The examples are intended as starting points for your own applications.  
They are not complete projects, but reusable building blocks for connecting to the sensor, receiving data and sending simple commands.

## Code Example Overview

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Example</th>
      <th style="padding: 8px; text-align: left;">Purpose</th>
      <th style="padding: 8px; text-align: left;">Difficulty</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Connect to the Vision Sensor</td>
      <td>Establish a TCP connection to the sensor</td>
      <td>Basic</td>
    </tr>
    <tr>
      <td>Receive Sensor Messages</td>
      <td>Continuously read incoming messages</td>
      <td>Basic</td>
    </tr>
    <tr>
      <td>Trigger Image Acquisition</td>
      <td>Send trigger commands to the sensor</td>
      <td>Intermediate</td>
    </tr>
  </tbody>
</table>

---

## Before You Start

Make sure the Vision Starter Kit is connected and reachable from your computer.

You may need to adjust the following values in the code examples:

```python
server_ip = "192.168.0.1"
server_port = 34170
```

!!! note "Network settings"
    The IP address and port may differ depending on your sensor configuration.  
    Check the network settings of your Vision Starter Kit before running the code.

---

## Example 1: Connect to the Vision Sensor

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example shows how to create a TCP connection to the Vision Sensor using Python.

It can be used as a first connection test to check whether your computer can reach the sensor over the configured IP address and port.

<span class="example-label">Code</span>

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "192.168.0.1"
server_port = 34170

client.connect((server_ip, server_port))

print("Connected to Vision Sensor")

client.close()
```

<span class="example-label">Expected Result</span>

If the connection is successful, the terminal should display:

```text
Connected to Vision Sensor
```

If the connection fails, check:

- sensor IP address
- sensor port
- network connection
- firewall settings
- network adapter configuration

</div>

---

## Example 2: Receive Sensor Messages Continuously

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example connects to the sensor and continuously receives incoming messages.

It can be used to test whether the sensor sends data to your Python application.

<span class="example-label">Code</span>

```python
import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.0.1"
    server_port = 34170

    client.connect((server_ip, server_port))

    try:
        while True:
            message = client.recv(1024)
            message = message.decode("utf-8")
            print("Received:", message)

    except KeyboardInterrupt:
        print("Stopping client...")

    finally:
        client.close()

run_client()
```

<span class="example-label">Expected Result</span>

The terminal prints incoming messages from the sensor.

Example:

```text
Received: ...
```

Stop the script with:

```text
CTRL + C
```

!!! note "Continuous receiving"
    This example waits for incoming data from the sensor.  
    If nothing is printed, check whether the sensor is configured to send result data.

</div>

---

## Example 3: Trigger Image Acquisition

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example sends simple trigger commands to the sensor.

It can be used to select a job, trigger image acquisition and start image recording from a Python script.

<span class="example-label">Code</span>

```python
import socket

def trigger_image():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.0.1"
    server_port = 34170

    client.connect((server_ip, server_port))

    client.sendall(b"\x02set job 2\x03")
    client.sendall(b"\x02trigger\x03")
    client.sendall(b"\x02RecordImages\x03")

    print("Trigger commands sent")

    client.close()

trigger_image()
```

<span class="example-label">Expected Result</span>

The sensor receives the trigger commands and starts the configured image acquisition workflow.

The terminal should display:

```text
Trigger commands sent
```

!!! warning "Job number"
    The command `set job 2` selects job number 2.  
    Change this value if your relevant job uses a different job number.

!!! note "Command format"
    The characters `\x02` and `\x03` mark the start and end of the command telegram.

</div>

## Expected Result

The sensor receives the trigger commands and starts the configured image acquisition workflow.

!!! warning "Job number"
    The command `set job 2` selects job number 2.  
    Change this value if your relevant job uses a different number.

---

## Troubleshooting

??? info "Troubleshooting"

    !!! failure "Connection refused"
        Check whether the sensor is reachable and whether the correct port is used.

    !!! failure "No response from sensor"
        Check the Ethernet connection and sensor network settings.

    !!! failure "Unexpected message format"
        Make sure the sensor is configured to send the expected response format.

---

## Next Steps

Use these examples as building blocks for your own Vision Starter Kit projects.

<div class="next-step-buttons" markdown>

[Example Projects](./vision_example_projects.md){ .md-button }

[Advanced Topics](./vision_advanced.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>