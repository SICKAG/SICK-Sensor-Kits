# SensorFusion

## Short Description

This challenge project shows how to use the Logic Editor of the SIG300 to visualize sensor results with green and red LEDs.

You can begin with a basic LED exercise and continue with a more advanced logic that combines measurements from all three sensors included in the IO-Link Connectivity Starter Kit.

## Project Information

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Project type</th>
      <th style="padding: 8px; text-align: left;">Required knowledge level</th>
      <th style="padding: 8px; text-align: left;">Estimated duration</th>
      <th style="padding: 8px; text-align: left;">Additional hardware and software requirements</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="project-badge challenge">Challenge Project</span></td>
      <td>Basic to Advanced</td>
      <td>30 minutes to 2 hours</td>
      <td>
        Test objects<br>
        Glass of water<br>
        Flat materials, such as pieces of paper
      </td>
    </tr>
  </tbody>
</table>


![Image](../images/)

## Challenge Goal

The goal of this project is to build a logic diagram in the Logic Editor of the SIG300 and visualize measurement results using the two colored LEDs from the Starter Kit.

The LEDs should react when a defined condition is met, for example:

- a measured value is within a specific range
- a measured value exceeds or falls below a defined value
- a sensor detects a specific material
- multiple sensor conditions are fulfilled at the same time

---

## Project Concept

The project uses the three sensors and the two colored LEDs included in the IO-Link Connectivity Starter Kit.

The required logic is created in the Logic Editor of the SIG300 WebUI.

The project is divided into two difficulty levels:

- **Basic:** Connect individual sensor results or conditions to an LED.
- **Advanced:** Combine the results of several sensors and control both LEDs with a more complex logic.

---

## Before You Start

Connect the SIG300, sensors and LEDs as described in the Getting Started guide.

[Getting started](../iolink/iolink_getting_started.md){.md-button .button-small}

Make sure that the required sensors and LEDs are connected to the SIG300 before creating the logic diagram.

---

## Basic Challenges

### Challenge 1: Continuous LED Output

Make an LED light up continuously.

??? info "Sample solution"

    Connect one LED to any port.

    In the Logic Editor, connect the **CON** block with the green arrow to the digital output of the selected port.

    Example:

    ```text
    S5DO4
    ```

    In this example:

    - `S5` refers to port 5
    - `DO4` refers to the digital output on pin 4 of the LED

---

### Challenge 2: Sensor-Controlled LED

Make an LED light up only when a sensor measures a specific value or a value within a defined range.

??? info "Sample solution"

    Connect one LED to any port and connect one sensor, for example the W10, to another port.

    Teach a specific value. This can be done either:

    - on the display of the W10
    - in the IODD Viewer of the device under **Detection settings** > **Qint.1 SP1 sensing range**

    In the Logic Editor, connect the digital input block of the sensor directly to the digital output block of the LED.

    Example sensor input:

    ```text
    S1DI2
    ```

    Example LED output:

    ```text
    S5DO4
    ```

    The LED should now light up when the taught value is exceeded or undercut.

---

## Advanced Challenge

Create a logic in which the green LED lights up only when all of the following conditions are fulfilled:

- The IMC30 detects an object within a specified range.
- The UC12 measures the distance to the surface of a glass of water.
- The W10 detects the distance to an object through a glass of water.

Also implement the following LED behavior:

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Fulfilled conditions</th>
      <th style="padding: 8px; text-align: left;">Required LED behavior</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>No condition is fulfilled</td>
      <td>The red LED lights up.</td>
    </tr>
    <tr>
      <td>One condition is fulfilled</td>
      <td>The red and green LEDs light up.</td>
    </tr>
    <tr>
      <td>Two conditions are fulfilled</td>
      <td>Both LEDs are switched off.</td>
    </tr>
    <tr>
      <td>All conditions are fulfilled</td>
      <td>The green LED lights up.</td>
    </tr>
  </tbody>
</table>

<br>

As part of the challenge, find out:

- which materials can be detected by the IMC30
- which measuring range can be used
- which settings are suitable for the individual sensors
- how the sensor results must be combined in the Logic Editor

??? info "Sample solution"

    Connect all sensors and LEDs to the SIG300.

    Try different settings in the IODD Viewer of the sensors and check which sensors can measure the selected materials.

    Build the logic diagram in the Logic Editor so that the LEDs are switched on or off according to the measured sensor values and the defined conditions.

---

## Possible Extensions

This project can be adapted in different ways.

Possible variations include:

- using different test objects
- selecting different measurement ranges
- changing the conditions for the LEDs
- combining fewer or more sensor values
- creating another LED behavior
- comparing the sensing technologies with different materials

---

## Expected Result

After completing the project, the connected LEDs should react according to the sensor measurements and the logic configured in the SIG300.

For the basic exercises, an LED should react to either a constant signal or the result of one sensor.

For the advanced challenge, the red and green LEDs should indicate how many of the three defined sensor conditions are fulfilled.

---

## Summary

In this challenge project, you used the Logic Editor of the SIG300 to connect sensor measurements with digital LED outputs.

You worked with:

- the W10 photoelectric sensor
- the UC12 ultrasonic distance sensor
- the IMC30 inductive proximity sensor
- the green and red LEDs
- the IODD Viewer
- the Logic Editor of the SIG300

The project can be adapted by changing the sensor settings, test materials and logical conditions.

## Next Steps

Return to the IO-Link project overview or continue with the Smart Train Loop project.

<div class="next-step-buttons" markdown>

[Example Projects](./iolink_example_projects.md){ .md-button }

[Smart Train Loop](./iolink_train.md){ .md-button }

</div>