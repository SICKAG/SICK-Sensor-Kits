# LiDAR Code Examples

## Short Description

This page provides small Python code examples for communicating with the LiDAR Starter Kit over TCP/IP.

The examples are intended as starting points for your own applications.  
They are not complete projects, but reusable building blocks for reading device information, requesting scan data and receiving field evaluation results.

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
      <td>Read Device Type</td>
      <td>Request basic device information from the LiDAR sensor.</td>
      <td>Basic</td>
    </tr>
    <tr>
      <td>Read Scan Data Once</td>
      <td>Request one scan data response from the sensor.</td>
      <td>Basic</td>
    </tr>
    <tr>
      <td>Read Scan Data Continuously</td>
      <td>Enable continuous scan data output and process incoming data.</td>
      <td>Intermediate</td>
    </tr>
    <tr>
      <td>Read Field Evaluation Result</td>
      <td>Read the result of configured detection fields.</td>
      <td>Intermediate</td>
    </tr>
    <tr>
      <td>Reusable SOPAS Helper Function</td>
      <td>Create a helper function for sending SOPAS commands.</td>
      <td>Intermediate</td>
    </tr>
  </tbody>
</table>

<br>

## Before You Start

Make sure the LiDAR Starter Kit is connected and reachable from your computer.

You may need to adjust the following values in the code examples:

```python
HOST = "192.168.0.1"
PORT = 2111
```

!!! note "Network settings"
    The IP address may differ depending on your sensor configuration.  
    Check the network settings of your LiDAR Starter Kit before running the code.

!!! info "Code examples"
    The following snippets are intended for first tests and learning purposes.  
    For complete applications, use the project files from GitHub.com or adapt the examples to your own requirements.

---

## Example 1: Read Device Type

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example requests the device type from the LiDAR sensor.

It can be used as a first connection test to check whether the sensor can be reached from Python.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN DItype\x03"
    sock.sendall(telegram)

    data = sock.recv(1024)

print(f"Received: {data}")
```

<span class="example-label">Expected Result</span>

If the connection works, the script prints a response from the sensor.

Example:

```text
Received: b'\x02sRA DItype ... \x03'
```

If no response is received, check:

- sensor power supply
- Ethernet connection
- sensor IP address
- network adapter settings
- firewall settings

</div>

---

## Example 2: Read Scan Data Once

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example sends a command to request scan data from the LiDAR sensor once.

It demonstrates how to send a SOPAS command and receive the corresponding response.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN LMDscandata\x03"
    sock.sendall(telegram)

    data = sock.recv(4096)

print(f"Received: {data}")
```

<span class="example-label">Expected Result</span>

The terminal prints a scan data response from the sensor.

The response may be longer than the response from the device type request.

!!! note "Buffer size"
    If the response is incomplete, increase the buffer size in `recv()`, for example from `4096` to a larger value.

</div>

---

## Example 3: Read Scan Data Continuously

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example enables continuous scan data output from the LiDAR sensor.

The script keeps the TCP connection open and prints incoming scan data repeatedly.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    # Enable continuous scan data output
    sock.sendall(b"\x02sEN LMDscandata 1\x03")

    while True:
        data = sock.recv(4096)
        print(data)
```

<span class="example-label">Expected Result</span>

The terminal continuously prints scan data received from the sensor.

Stop the script with:

```text
CTRL + C
```

!!! warning "Continuous output"
    Continuous scan data can generate a large amount of output.  
    Use filtering, parsing or logging if you want to process the data in another application.

</div>

---

## Example 4: Read Field Evaluation Result

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

This example reads the current field evaluation result from the LiDAR sensor.

It is useful for applications such as:

- The Floor is Lava
- Human Piano / Air Piano
- field infringement detection
- trigger or feedback logic

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN FieldEvaluationResult\x03"
    sock.sendall(telegram)

    data = sock.recv(4096).decode("ascii")

print(f"Field evaluation result: {data}")
```

<span class="example-label">Expected Result</span>

The terminal prints the current field evaluation response.

Typical values in the response can indicate whether a field is infringed or not.

For example:

- `2` can indicate that a field is not infringed
- `4` can indicate that a field is infringed

!!! warning "Response format"
    The exact position of the field values depends on the field configuration.  
    Print the full response first and identify the relevant positions before parsing the result.

</div>

---

## Example 5: Reusable SOPAS Helper Function

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

For larger scripts, it can be useful to create a helper function for sending SOPAS commands.

This avoids repeating the socket setup and telegram formatting in every example.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

def send_sopas_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        sock.connect((HOST, PORT))

        telegram = b"\x02" + command.encode("ascii") + b"\x03"
        sock.sendall(telegram)

        response = sock.recv(4096).decode("ascii").strip("\x02\x03")

    return response

device_type = send_sopas_command("sRN DItype")
print("Device type:", device_type)

field_result = send_sopas_command("sRN FieldEvaluationResult")
print("Field evaluation:", field_result)
```

<span class="example-label">Expected Result</span>

The script prints the requested sensor responses.

Example:

```text
Device type: ...
Field evaluation: ...
```

!!! tip "When to use this helper"
    This helper is useful for simple request-response examples.  
    For continuous applications, consider keeping the socket connection open instead of reconnecting for every command.

</div>

---

<div class="faq-page"markdown>

## Troubleshooting

??? question "The script cannot connect to the sensor. What should I check?"

    Check the following points:

    - the LiDAR sensor is powered
    - the Ethernet cable is connected
    - the correct network adapter is configured
    - the computer IP address is in the same range as the sensor
    - the sensor IP address in the script is correct
    - no firewall blocks the connection

---

??? question "The script receives no data. What can I do?"

    Make sure the correct command is used and that the sensor supports the requested data.

    Also check:

    - the sensor is reachable in the browser
    - the command is written correctly
    - the start and end characters `\x02` and `\x03` are included
    - the receive buffer is large enough

---

??? question "The output is difficult to read. How can I process it?"

    SOPAS responses are often returned as text-based telegrams.

    You can decode and split the received data:

    ```python
    response = data.decode("ascii")
    parts = response.split(" ")
    print(parts)
    ```

    This can help you identify relevant values in the response.

---

??? question "The script stops during continuous scan data reading. What can I improve?"

    Continuous output can produce many messages.

    Try the following:

    - increase the receive buffer size
    - add error handling
    - process only relevant data
    - avoid printing every full response if the output is too large
    - keep the socket open instead of reconnecting repeatedly

</div>

---

## Summary

This page introduced basic Python code examples for the LiDAR Starter Kit.

You learned how to:

- connect to the LiDAR sensor with Python
- request the device type
- read scan data once
- receive scan data continuously
- read field evaluation results
- use a reusable SOPAS helper function

These examples can be used as building blocks for your own LiDAR applications and example projects.

---

## Next Steps

Continue with LiDAR example projects or advanced topics.

<div class="next-step-buttons" markdown>

[Example Projects](./lidar_example_projects.md){ .md-button }

[Field Evaluation](./lidar_field_evaluation.md){ .md-button }

[Advanced](./lidar_advanced.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>
