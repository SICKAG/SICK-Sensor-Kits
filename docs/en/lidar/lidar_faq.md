<!-- # FAQ - LiDAR Starter Kit

## Short Description

This FAQ answers common questions related to the LiDAR Starter Kit, field evaluation and sensor communication.

For general questions about the Starter Kits, please visit the general FAQ section.

../faq.md{ .md-button .button-small }

---

??? question "The LiDAR sensor is not reachable. What should I check?"

    Check the power supply, Ethernet connection and IP address of the sensor.

---

??? question "Field Evaluation does not return the expected result. What can I do?"

    Check whether the detection fields are configured correctly and whether the object is inside the defined area.

---

??? question "Where can I find example projects for the LiDAR Starter Kit?"

    The LiDAR example projects are listed on the Example Projects page.

    ./lidar_example_projects.md{ .md-button .button-small }

-->

<div class="faq-page" markdown>

# FAQ - LiDAR Starter Kit

## Short Description

This FAQ answers common questions related to the LiDAR Starter Kit, field evaluation, sensor communication and basic troubleshooting.

For general questions about the Starter Kits, support resources or additional training material, please visit the general FAQ section.

[FAQ](../faq.md){ .md-button .button-small }

---

??? question "The LiDAR sensor is not reachable. What should I check?"

    Check the following points:

    - the power supply is connected
    - the Ethernet cable is connected correctly
    - the correct network adapter is configured
    - your computer IP address is in the same range as the sensor
    - the sensor IP address is correct
    - no other device uses the same IP address
    - firewall settings do not block the connection

    The default IP address used in the documentation is usually:

    ```text
    192.168.0.1
    ```

    If the sensor user interface does not open in the browser, revisit the Getting Started guide.

    [Getting Started Guide](./lidar_getting_started.md){.md-button .button-small}

---

??? question "The sensor user interface does not open in the browser. What can I do?"

    First, check whether the computer and the sensor are in the same IP range.

    Example configuration:

    ```text
    Sensor IP:    192.168.0.1
    Computer IP:  192.168.0.100
    Subnet mask:  255.255.0.0
    ```

    Also check:

    - the correct Ethernet adapter is selected
    - DHCP is disabled for this adapter
    - the manual IP address was saved correctly
    - the sensor has completed its startup process
    - the browser URL starts with `http://`

    Example:

    ```text
    http://192.168.0.1
    ```

---

??? question "Field Evaluation does not return the expected result. What can I do?"

    Check whether the detection fields are configured correctly and whether the object is inside the defined field area.

    Also verify:

    - the field is placed in the correct position
    - the field size matches the object or person to be detected
    - the object size parameters are configured correctly
    - the object remains inside the field long enough
    - static objects were handled correctly with teach-in if needed

    If the field behavior is still unexpected, start with one large field and one clearly visible test object.

---

??? question "What do the field evaluation values mean?"

    In the example projects, the field evaluation response is used to determine whether a field is infringed.

    Typical values can be:

    - `2`: field is not infringed
    - `4`: field is infringed

    !!! warning "Response format"
        The exact position of these values in the response depends on the sensor configuration and the number of fields.  
        Print the full response first and identify the relevant positions before parsing the result in code.

---

??? question "My Python script cannot connect to the LiDAR sensor. What should I check?"

    Check the following points:

    - the sensor is reachable in the browser
    - the IP address in the script is correct
    - the port is correct
    - the Ethernet connection is stable
    - the network adapter is configured correctly

    Example values used in the code examples:

    ```python
    HOST = "192.168.0.1"
    PORT = 2111
    ```

    If your sensor uses a different IP address, adapt the `HOST` value in the script.

---

??? question "The Python script receives no data. What can I do?"

    Make sure that the sent SOPAS command is correct and that the sensor supports the requested data.

    Also check:

    - the start character `\x02` is included
    - the end character `\x03` is included
    - the receive buffer is large enough
    - the sensor is in the correct state
    - the requested data is available

    For first tests, use the LiDAR Code Examples page.

    [LiDAR Code Examples](./lidar_code_snippets.md){ .md-button .button-small}

---

??? question "The script stops after some time with a socket error. What can I do?"

    This can happen if a new socket connection is opened too often.

    A typical error message is:

    ```text
    Only one usage of each socket address, protocol, network address or port is normally permitted.
    ```

    To reduce this problem:

    - keep one socket connection open
    - avoid reconnecting in every loop iteration
    - close sockets properly when the script stops
    - add a small delay in loops
    - add error handling and reconnect logic if required

    The Human Piano / Air Piano project contains an improved example using a persistent socket connection.

    [Human Air Piano](./lidar_human_piano_air_piano.md){ .md-button .button-small }

---

??? question "Where can I find example projects for the LiDAR Starter Kit?"

    The LiDAR example projects are listed on the Example Projects page.

    [Example Projects](./lidar_example_projects.md){ .md-button .button-small}

    If you are new to the LiDAR Starter Kit, start with the Field Evaluation project.

    [Field Evaluation](./lidar_field_evaluation.md){ .md-button .button-small}

---

??? question "Which project should I start with?"

    If you are new to the LiDAR Starter Kit, start with this order:

    1. Getting Started
    2. Field Evaluation
    3. Distance Estimation
    4. The Floor is Lava
    5. Human Piano / Air Piano

    Field Evaluation is the recommended first demo because it introduces the basic concept of detection fields.

---

??? question "Where can I find code examples for the LiDAR Starter Kit?"

    Basic Python examples are available on the LiDAR Code Examples page.

    [LiDAR Code Examples](./lidar_code_snippets.md){ .md-button .button-small}

    The page includes examples for:

    - reading the device type
    - reading scan data
    - reading scan data continuously
    - reading field evaluation results
    - using a reusable SOPAS helper function

---

??? question "Where can I find advanced integration information?"

    Advanced integration topics are covered on the Advanced Topics page.

    [Advanced](./lidar_advanced.md){ .md-button .button-small}

    This includes information about:

    - protocol-based integration
    - SDK usage
    - scan data processing
    - external system integration
    - SICK Perception SDK

---

??? question "Where can I find complete project files or source code?"

    The GitHub.io documentation provides explanations, setup guides and project overviews.

    Complete project files and source code should be provided through the GitHub.com project repository.

    [GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

    !!! note
        The final GitHub.com project repository link may need to be adjusted once the official repository structure is defined.

---

## Related Pages

<div class="next-step-buttons" markdown>

[Getting Started Guide](./lidar_getting_started.md){.md-button }

[Field Evaluation](./lidar_field_evaluation.md){ .md-button }

[Example Projects](./lidar_example_projects.md){ .md-button }

[LiDAR Code Examples](./lidar_code_snippets.md){ .md-button }

[Advanced](./lidar_advanced.md){ .md-button }

[FAQ](../faq.md){ .md-button }

</div>

</div>