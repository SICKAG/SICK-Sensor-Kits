# Smart Train Loop

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
      <td>Build a smart gate with different sensors that detect train waggons and load.</td>
      <td>Advanced</td>
      <td>1-2 Hours</td>
      <td>Mounting Kit<br>Battery-powered train with tracks<br>(Metallic) objects for train waggons<br>optional: SLT</td>
    </tr>
  </tbody>
</table>

![Train](../images/Train_1.jpg)

In this project, the aim is to analyze a train running on a track loop. This is done with different sensors for presence detection, distance measurement and detection of metal objects. The results can be visualized with LEDs. The logic is created in the logic editor of the SIG300 network device.

## Instruction

### Setup

- Connect the 3 sensors and the LEDs and/or SLT to the SIG300.

??? sickinfo "Example connection setup"
    - SIG300 connected to PC via USB-C
    - S1: W10
    - S2: UC12
    - S3: IMC30
    - S4: SLT or LED yellow
    - S5: LED green (initial status: blinking - as it's set to IO-Link)
    - S6: LED red (initial status: blinking - as it's set to IO-Link)

- Think of a useful task for each sensor and create the setup by mounting the sensors to the mounting frame of the mounting kit using the supplied mounting brackets and tools.

??? sickinfo "Sensor information"
    - [**W10**](https://www.sick.com/ag/en/catalog/products/detection-sensors/photoelectric-sensors/w10/wtm10l-241611d0a00zvzzzzzzzzz1/p/p678567): Photoelectric sensor, measures distance based on an optical functional principle, measuring range: 25-700 mm (depending on Mode)
    - [**UC12**](https://www.sick.com/ag/en/catalog/products/distance-sensors/ultrasonic-distance-sensors/uc12/uc12-1223e/p/p665120): Ultrasonic distance sensor, measuring range: 55-250 mm 
    - [**IMC30**](https://www.sick.com/ag/en/catalog/products/detection-sensors/inductive-proximity-sensors/imc/imc30-20nppvc0sa00/p/p483964?tab=detail): Inductive proximity sensor, detects metal objects, sensing range: 0-20 mm

??? sickinfo "Example setup and tasks"
   
    - **UC12** : On top of frame to detect the train - keep in mind the max. measuring range
    - **W10**: At the bottom of the other vertical bar to check if a waggon is loaded or not - keep in mind the minmum height of the objects on the waggon
    - **IMC30**: At the bottom of one vertical bar to detect metallic objects on the waggon - keep in mind the maximum measuring distance

    ![Train Setup](../images/train_setup.jpg)
    ![Setup W10](../images/train_w10.jpg)
    ![Setup IMC30](../images/train_imc30.jpg)

- Connect to the UI of the SIG300 as mentioned in [Getting Started](./iolink_getting_started.md).
- Log in as **Service**, password: **servicelevel** and press **Keep Default Password**

### IODD Files

- Select **Application** > **IODD File Management** and check if the IODDs for all sensors are uploaded.

![IODD](../images/iodd_1.png)

- If the IODDs are missing, you can download them via the SICK website of the product in the **Downloads** > **Software** tab or on [IODDfinder.com](https://ioddfinder.io-link.com/) by entering the article number (W10: WTM10x-xx1611xxA00xVxxxxxxxxxx, UC12: 6077702, IMC30: 1079301, SLT060: 6075938).
- Assign the IODDs to the ports if it hasn't worked automatically yet.

![IODD](../images/iodd_2.png)

### Port Configuration

#### Sensors (e.g., W10 at S1):

You can use the sensors either as Digital Input, e.g. to trigger a Digital Output such as an LED, OR use the sensor as IO-Link device to communicate with other IO-Link devices such as the SLT.

- Go to **Ports** > **Port 1**, choose the **Access rights** tab and set the check marks as in the picture (**Read process and service data** and **Sensor port configuration** are relevant)

![Access rights](../images/iolink_1.png)

- Switch to the tab **Port 1** for the configuration as in the image described below (Assigned IODD, IO-Link, Device Identification Check Yes, Version V1.1 is relevant).

- **Note:** Pin 4 is relevant for SLT (IO-Link); Pin 2 can be used for Digital Outputs only, e.g. LEDs (set sensor to Digital In)

![Port Configuraton 1](../images/iolink_2.png)


- Switch to the **IODD Viewer** tab and select the measurement type at the top center. You can already read the measurement value at the very bottom center. 
- To set a trigger at a specific measurement value, you can adjust the parameters. E.g. if you want the W10 to be triggered if the measurement value is bigger than 180 mm, find the **Detection settings** and set the **Qint.1 SP1 sensing range** to 180 mm and **High active**.

![Qint.1](../images/iolink_6.png)

- Repeat these steps for all sensors. 
**Note:** every sensor looks a bit different in the IODD Viewer tab depending on functional principle and integrated functions/parameters.

#### Lamps (e.g., LED at S5)

**Note:** the SLT works same as a sensor in terms of Port configuration. For simple Digital Outputs (e.g. LEDs), please follow the instructions below.

- Go to **Ports** > **Port 1**, choose the **Access rights** tab and set the check marks as in the picture (**Write process data** is relevant).

![Access rights](../images/iolink_4.png)

- Switch to the tab **Port 5** for the configuration. Set **Pin 4** to **Digital In**. Depending on the Sensor port configuration in the access rights, you can toggle HI/LO to see if the LED is working. 

![LED](../images/iolink_5.png)

- Repeat for all LEDs.

### Logic Editor

To combine the measurement data from the sensors (digital in) and the LEDs (digital out), we use the Logic Editor.
**Note:** You always need to click on **Apply** so that your changes in the Logic Editor take effect.

- Go to **Application** > **Logic editor**. Now create the logic for all sensors and LEDs according to the setup you defined in the beginning (e.g. make the green LED light up if a waggon is loaded).
In the following steps, there are some examples you can follow.

??? sickinfo "Light up green LED if waggon is loaded"
    First, try out a direct connection between SIDI2 (Pin 2 of W10) and S5DO4 (Pin 4 of LED) by dragging the arrow from the block on the left to the one on the right side. Depending on the measurement value of the W10, the LED should now light up.
    You can use logic blocks to negate the result, e.g. **Digital Logic** > **Gate** > **NOT** in between the two blocks

    ![Logic editor](../images/iolink_7.png)

??? sickinfo "Light up red LED if train is detected"
    - The UC12 can be used to detect any object in a specific area.
    - Mount the UC12 according to the measuring range and the height of the train that should be detected. Use the **IODD Viewer** to see the measurement result and test a good position for the UC12.
    - Adjust the trigger value by changing the value in **IODD Viewer** > **SSC1: switch signal channel 1** > **SP1** value and logic **Low active**
    **Note**: the value is not a milimeter value.

    ![UC12 config](../images/uc12_1.png)

    - Go the the **Logic editor** and connect S2I2 (Port 2 of UC12) and S6DO4 (Pin 4 of LED red). A NOT gate is not necessary as the logic is low active.

    ![UC12 logic](../images/uc12_2.png)

    - Click on **Apply** and test if it works.

??? sickinfo "Light up yellow LED if a metal object is detected"

    - The IMC30 can be used to detect metal objects in a specific area.
    - Mount the IMC30 according to the measuring range and the distance of the loaded metal objects to the gate. Use the **IODD Viewer** to see the measurement result and test a good position for the IMC30. There's no need to set a parameter.
    - Go the the **Logic editor** and connect S3I2 (Port 2 of UC12) and S4DO4 (Pin 4 of LED yellow). 

    ![IMC30 logic](../images/imc30_1.png)

    - Click on **Apply** and test if it works.

??? sickinfo "Make any LED light up for 3 seconds after the trigger"
    - Add a **Delay** block in the logic editor and set the **OffDelay** to 3000 (ms) to delay the lamp going out for 3 seconds

    ![Delay](../images/delay.png)

### Reset

When you are finished with your project, you can press **Clear** in the Logic Editor to remove all blocks and connections. Please note that a **Reset to factory settings** will also delete the uploaded IODD files.
