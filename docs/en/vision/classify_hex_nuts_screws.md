<!--# Classify Hex Nuts / Screws

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

-->

# Classify Hex Nuts / Screws

## Short Description

This guided project introduces the **AI Classification** tool in SICK Nova.  
You will train a simple AI model to distinguish between different hex nuts and screws using images captured with the Vision Starter Kit.

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
      <td><span class="project-badge guided">Guided Project</span> </td>
      <td>Basic</td>
      <td>30 Minutes</td>
      <td>None – everything is included in the Starter Kit</td>
    </tr>
  </tbody>
</table>


![Classify hex nuts 1](../images/Classify_hex_nuts_1.png){ width="850" }

## Goal

The goal of this project is to create a simple AI Classification task that can distinguish between different hex nuts and screws.

After completing this project, you should be able to:

- create an empty job in SICK Nova
- configure image acquisition settings
- add an AI Classification tool
- create image classes
- capture training images
- train an AI Classification model
- test and improve the classification result

---

## Before You Start

Set up the Vision Starter Kit as described in the [Getting started](./vision_getting_started.md) section.


!!! tip "Setup tip"
    Adjust the height of the mounting bracket if necessary.  
    For this project, a distance of approximately 10 cm between the object and the sensor can help to get a clearer image.

---

## Instructions

Follow the steps below to create your first AI Classification task.

---

## 1. Create an Empty Job and Configure Image Acquisition

1. Create an **Empty Job**.
2. Make sure that **Jobs** and **Acquisition** are selected.
3. Place the **Hex Nut** in the sensor's field of view.
4. Select **Configure**.
5. Click **Run auto setup**.
6. Adjust the focus with the focus adjustment tool if necessary.
7. Click **Recommended**.
8. Click **Run** to see the live images.
9. Adjust the **field of view (FOV)** and **Downsample** settings if useful.

![Classify hex nuts 1](../images/Classify_hex_nuts_1.png){ width="850" }

---

## 2. Add the AI Classification Tool

1. In the **Analysis** section, click **Add tool**.
2. Select **Classify** > **AI Classification**.

![Classify hex nuts 2](../images/Classify_hex_nuts_2.png){ width="850" }

---

## 3. Capture Images for the First Class

1. Make sure **Hex Nut 1** is in the sensor's field of view.
2. Adjust the size of the red rectangle so that it encloses the object.
3. Open **Class 1**.
4. Click **Add active image**.
5. Repeat this step several times.
6. Use a new identical object or move the object slightly each time.

!!! tip "Training tip"
    Try to capture small variations in object position and rotation.  
    This helps the AI model classify the object more reliably.

---

## 4. Capture Images for the Second Class

1. Place **Hex Nut 2** in the sensor's field of view.
2. Open **Class 2**.
3. Click **Add active image**.
4. Repeat this step several times.
5. Again, use different positions or rotations to improve the training data.

---

## 5. Train and Test the Classification

1. Click **Train**.
2. Wait until the job is **successfully trained**.
3. Test whether the objects are detected reliably.
4. Add more training images if the result is not stable enough.

!!! note "Improving the result"
    If the classification is unreliable, add more images with different positions, rotations and lighting conditions.  
    A higher variety of training images can improve the classification result.

---

## Expected Result

After completing this project, the Vision Starter Kit should be able to distinguish between the trained object classes.

The AI Classification tool should classify the selected hex nuts or screws based on the images captured during training.

---

## Summary

In this guided project, you created a basic AI Classification task with the Vision Starter Kit.

You learned how to:

- configure image acquisition
- create object classes
- capture training images
- train an AI Classification model
- test and improve the classification result

This project is a good next step after the Vision Starter Project and provides a simple introduction to AI-based image classification.

---

## Next Steps

Continue with another Vision project or open the complete project files on GitHub.com.

<div class="next-step-buttons" markdown>

[Example Projects](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>