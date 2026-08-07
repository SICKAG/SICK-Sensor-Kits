<!-- # Simple Field Evaluation
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
      <td>Draw field(s) and infringe them with different sized objects</td>
      <td>Basic</td>
      <td>10-30 minutes</td>
      <td>Test objects</td>
    </tr>
  </tbody>
</table>

Connect your device as mentioned in [Getting Started](./lidar_getting_started.md).

Choose **Field Evaluation** on the left and draw a field in front of the device.

Set the parameters for a field infringement (object size and time inside the field).

Choose different test objects to test if the field is being infringed.

Possible tasks:

- Try to set the parameters so that the field is only infringed if you hold a DIN A4 paper horizontally but not vertically
- Try to set the parameters so that a hand doesn't infringe a field but an arm or body does. 

-->


# Simple Field Evaluation

## Short Description

This guided project introduces the **Field Evaluation** function of the LiDAR Starter Kit.

You will create one or more detection fields in front of the LiDAR sensor and test how different objects infringe these fields depending on their size, position and time inside the field.

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
      <td><span class="project-badge guided">Guided Project</span></td>
      <td>Basic</td>
      <td>10 to 30 minutes</td>
      <td>Test objects</td>
    </tr>
  </tbody>
</table>

## Goal

The goal of this project is to understand how field evaluation works with the LiDAR Starter Kit.

After completing this project, you should be able to:

- open the LiDAR sensor user interface
- create a detection field
- configure field infringement parameters
- test different objects inside the field
- understand how object size and time inside the field influence the result

---

## Before You Start

Connect your LiDAR Starter Kit as described in the [Getting Started](./lidar_getting_started.md) guide.

!!! tip "Recommended first LiDAR demo"
    Field Evaluation is a good first practical demo after completing the LiDAR Getting Started guide.  
    It helps you understand how the LiDAR sensor can monitor defined areas.

---

## Instructions

Follow the steps below to create and test your first field evaluation setup.

---

## 1. Open Field Evaluation

1. Open the LiDAR sensor user interface in your browser.
2. Make sure the sensor is connected and reachable.
3. Select **Field Evaluation** on the left side of the user interface.
4. Check whether the live measurement data is visible.

---

## 2. Draw a Detection Field

1. Draw a field in front of the device.
2. Position the field in an area where you want to detect objects.
3. Make sure the field is large enough for your first test object.
4. Save or apply the field configuration if required by the user interface.

!!! tip "Start simple"
    Start with one large field first.  
    After the basic field evaluation works, you can create smaller or more specific fields.

---

## 3. Configure Field Infringement Parameters

Set the parameters that define when a field is considered infringed.

Important parameters may include:

- object size
- time inside the field
- position inside the field
- field shape
- field sensitivity

The exact parameter names may depend on the sensor configuration and software version.

!!! note "Parameter behavior"
    A field infringement does not only depend on whether an object enters the field.  
    The configured object size and the time inside the field can also influence the result.

---

## 4. Test Different Objects

Use different test objects to check the field behavior.

Examples:

- sheet of paper
- hand
- arm
- body
- small box
- larger object

Place the objects in the field and observe whether the field is infringed.

---

## 5. Adjust the Field Settings

Adjust the field settings until the behavior matches your use case.

Possible test tasks:

- configure the parameters so that the field is only infringed if you hold a DIN A4 paper horizontally, but not vertically
- configure the parameters so that a hand does not infringe the field, but an arm or body does
- create a smaller field and test how precisely the sensor detects object positions
- create multiple fields and compare their behavior

---

## Expected Result

After completing this project, the LiDAR Starter Kit should detect when objects infringe a defined field.

A successful result means that:

- the detection field is configured correctly
- test objects can be detected inside the field
- object size and position influence the field result
- field parameters can be adjusted for different scenarios

---

## Summary

In this guided project, you learned how to create and test detection fields with the LiDAR Starter Kit.

You practiced how to:

- open the Field Evaluation function
- draw a detection field
- configure field infringement parameters
- test different objects
- adjust the field behavior for different use cases

This project is the recommended first practical demo for the LiDAR Starter Kit.

---

## Next Steps

Continue with another LiDAR project or open the complete project files on GitHub.com.

<div class="next-step-buttons" markdown>

[Example Projects](./lidar_example_projects.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>