# Classify Hex Nuts / Screws

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
      <td>Try out the AI Classification tool by taking images of different hex nuts and/or screws to generate your first AI algorithm.</td>
      <td>Basic</td>
      <td>30 Minutes</td>
      <td>none – everything included in the Starter Kit</td>
    </tr>
  </tbody>
</table>

Setup the sensor as mentioned in the [Getting started](./vision_getting_started.md) section

![Classify hex nuts 1](../images/Classify_hex_nuts_1.png)

1. Create an **Empty Job** and make sure that **Jobs** and **Acquisition** is selected
2. Place the **Hex Nut** in the sensor’s field of view.
It is recommended to adjust the height of the mounting bracket to get closer to the object (~ 10 cm from the ground)
3. Select **Configure**
4. Click on **Run auto setup**. Adjust the focus with the adjustment tool if necessary
5. Click **Recommended**. 
6. Click **Run** to see the live images
7. Adjust the **field of view (FOV)** and **Downsample** if useful

![Classify hex nuts 2](../images/Classify_hex_nuts_2.png)

8.	Click **Add tool** under the Analysis section and choose **Classify > AI Classification**
9.	Make sure the **Hex Nut 1** is in the sensor’s FOV. Adjust the size of the red rectangle to enclose the object
10.	Open **Class 1**. 
11.	Click on **Add active image**, repeat this step several times with a new identical object or move the object each time
12.	Place a **Hex Nut 2** in the sensor’s field of view and open **Class 2**
13.	Click on **Add active image**, repeat this step several times with a new identical object or move the object each time
14.	Click **Train** and wait until the Job is **Successfully trained**
15.	Test if the object is detected reliably. Add more training images to improve the results

