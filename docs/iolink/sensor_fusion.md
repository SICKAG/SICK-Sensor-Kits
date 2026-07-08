# SensorFusion

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
      <td>Build a logic diagram in the logic editor of the SIG300 to visualize measurement results with LEDs.</td>
      <td>Basic/Advanced</td>
      <td>0,5-2 Hours</td>
      <td>Test objects<br>Glass of Water<br>Flat materials (e.g. pieces of paper)</td>
    </tr>
  </tbody>
</table>

In this project, the aim is to visualize LEDs if a specific condition is reached, e.g. a  measurement result in a specific range or the presence of a specific material.

For this, we can use the 3 sensors and the 2 colored LEDs from the Starter Kit. The logic is defined in the logic editor of the WebUI of the SIG300.

Here you can find some possible ideas how to work with the sensors and LEDs.

**Basic**

Make an LED light up continuously.

??? sickinfo "Sample solution"
    Connect one LED to any port and connect the "CON" wih the green arrow in the logic editor with the Digital Output of the port (e.g. S5DO4 - port 5, pin 4 of the LED)

Make an LED light up only if a sensor measures a specific value or range

??? sickinfo "Sample solution"
    Connect one LED to any port and connect one sensor (e.g. W10) to another port.
    Teach a specific value (can be done either on the display of the W10 or in the IODD-Viewer of the device: Detection settings > Qint.1 SP1 sensing range). 
    Connect the block for the digital input of the sensor (e.g. S1DI2) in the logic editor directly with the block for the digital output of the LED (e.g. S5DO4).
    The LED should now light up only if the teached value is underperformed or exceeded.

**Advanced**

Make the green LED light up only if all following conditions are fulfilled:
* The IMC30 detects an object within a specified range (find out which materials can be measured and what's the measuring range)
* The UC12 measures the distance to the surface of a glass of water
* The W10 detects the distance to an object through a glass of water

If no condition is fulfilled, make the red LED light up.
If only one condition is fulfilled, make the red and green LED light up.
If two conditions are fulfilled, turn off both LEDs.

This project can be adapted in various ways.

??? sickinfo "Sample solution"
    Connect all sensors and LEDs to the SIG300. Try out different settings in the IODD-Viewer of the sensors and build the logic diagram in the logic editor to light up and turn off the LEDs according to the measured sensor values. Check which sensors can measure which types of materials.