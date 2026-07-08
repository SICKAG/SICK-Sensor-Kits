# The Floor is Lava
<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Short description</th>
      <th style="padding: 8px; text-align: left;">Required knowledge level</th>
      <th style="padding: 8px; text-align: left;">Estimated duration</th>
      <th style="padding: 8px; text-align: left;">Additional hardware and software requirements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Play "The floor is lava" with a LiDAR scanner detecting infringed fields.</td>
      <td>Basic</td>
      <td>20-40 Minutes</td>
      <td>Several people or objects</td>
    </tr>
  </tbody>
</table>

![Lava](../images/lava.jpg)

In this project, the aim is to create a setup for the game "The floor is lava" with a LiDAR sensor. The LiDAR can distinguish static objects and moving objects moving through a parcours. A basic Python script reads out the sensor data and plays a sound once a person touching the floor is detected.

## Instruction

**Note:** The mentioned code snippets are just examples. Feel free to use your own code to run the project.

### Field evaluation

- Connect your device as mentioned in [Getting Started](./lidar_getting_started.md). The UI should now look something like this:

![LiDAR 1](../images/LiDAR_1.png)

- Log in as **Service**, password: **servicelevel** and press **Keep Default Password**.
- Select **Application** > **Field evaluation** and draw a field in a suitable size.

![LiDAR 3](../images/LiDAR_3.png)

- Perform a **Teach-in** to ignore all static objects. Stop the teach-in after around 10 seconds.

![LiDAR 2](../images/LiDAR_2.png)

- Define the field parameters, e.g. the max. blanking size which corresponds to the minimal oject size that infringes the field.

![LiDAR 4](../images/LiDAR_4.png)

- You can ignore **Output**

### Coding

- Open a coding environment with Python such as Visual Studio Code.
- Enter the following code:

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

def sopas(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        telegram = b"\x02" + cmd.encode("ascii") + b"\x03"
        s.sendall(telegram)
        return s.recv(1024).decode("ascii").strip("\x02\x03")

# Enable measurement
print(sopas("sMN SetAccessMode 03 F4724744"))
print(sopas("sMN LMCstartmeas"))

# Read field evaluation
response = sopas("sRN FieldEvaluationResult")
print("Field evaluation:", response)
```

- The result should look something like this: 

![LiDAR 5](../images/LiDAR_5.png)

- **2** = Field not infringed, **4** = Field infringed
- Now, read out a specific value (field infringed or not infringed, e.g. to play a sound or turn on a light)

??? sickinfo "Code"
    ```python
    output = response[38:39]
    print(output)
    ```

- **38:39** refers to the position in the result (first digit 2 or 4)
- Check if the result is giving out the right position (either 2 for "not infringed" or 4 for "infringed").
- Play a sound if the field is infringed; otherwise, display the text "error". Important: Type "import winsound" on the second line of the code (below the previous "import socket").

??? sickinfo "Code"
    ```python
    import winsound


    if output == '4':
        winsound.Beep(200, 1000)
    else:  print('error')
    ```

- To read out sensor data continuously, include the code in 'while True'
- **Complete code:**

??? sickinfo "Code"
    ```python
    import socket
    import winsound

    HOST = "192.168.0.1"
    PORT = 2111

    def sopas(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        telegram = b"\x02" + cmd.encode("ascii") + b"\x03"
        s.sendall(telegram)
        return s.recv(1024).decode("ascii").strip("\x02\x03")

    # Enable measurement
    print(sopas("sMN SetAccessMode 03 F4724744"))
    print(sopas("sMN LMCstartmeas"))

    while True:
    # Read field evaluation
    response = sopas("sRN FieldEvaluationResult")
    print("Field evaluation:", response)

    output= response[38:39]
    #print(output)

    if output == '4':
        winsound.Beep(200, 1000)
    else:  print('error')
    ```

- Now, you can walk through the parcours and check if the code is working correctly.
- If you like, you can use other sounds or variations of the game.






