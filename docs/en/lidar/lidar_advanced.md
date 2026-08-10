<!-- # Advanced Usage of the LiDAR Starter Kit
The LiDAR Starter Kit is a powerful tool for developers and researchers looking to integrate advanced sensing capabilities into their projects. This guide provides detailed instructions and code examples to help you make the most of its features.

For more detailed information and resources on working with SICK devices and their integration, refer to the [picoScan100: Protocols and Integration article](https://support.sick.com/sick-knowledgebase/article/?code=KA-09481).


## SICK driver sick_scan_xd
For additional functionality and advanced integration, you can explore the [sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk) driver. This driver provides extended support for SICK LiDAR devices and can be a valuable resource for your projects.

In the world of LiDAR, precise measurement data is only as powerful as the software that unlocks it. A C++ SDK acts as the essential digital accessory giving developers direct, high‑performance access to raw sensor data and configuration options for real‑time applications.

**Features**

- Receive scan, IMU, and encoder data in SICK data format Compact over UDP or TCP and perform sensor configuration via REST API
- Thread-safe and event-driven data acquisition from multiple sensors.
- Cross-platform build system using CMake for Linux and Windows and dependency management via Conan 2 possible.
- Compatible with x86_64 and ARM64 architectures (e.g., Raspberry Pi).
- Multiple ready-to-use examples for fast prototyping.
- Built-in diagnostic and logging capabilities.
- Comprehensive unit and CI tests with included real-world test data.
- Designed to meet the requirements of the EU Cyber Resilience Act.

-->

# Advanced Usage of the LiDAR Starter Kit

## Short Description

This page provides advanced information for working with the LiDAR Starter Kit.

It focuses on protocol-based integration, software development kits, advanced data access and possible integration scenarios for custom LiDAR applications.

## Advanced Topic Overview

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Topic</th>
      <th style="padding: 8px; text-align: left;">Purpose</th>
      <th style="padding: 8px; text-align: left;">Recommended for</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Protocols and Integration</td>
      <td>Understand how LiDAR data can be accessed and integrated into external applications.</td>
      <td>Users who want to build custom software around the LiDAR sensor.</td>
    </tr>
    <tr>
      <td>SICK Perception SDK</td>
      <td>Use a software development kit for advanced access to SICK sensor data.</td>
      <td>Developers working on larger or performance-oriented applications.</td>
    </tr>
    <tr>
      <td>Scan Data Processing</td>
      <td>Receive and process LiDAR scan data for custom applications.</td>
      <td>Users who want to analyze raw or processed sensor data.</td>
    </tr>
    <tr>
      <td>External Integration</td>
      <td>Connect LiDAR results to other software systems, dashboards or automation logic.</td>
      <td>Advanced users and system integrators.</td>
    </tr>
  </tbody>
</table>

<br>

## Further Product and Protocol Information

For more detailed information about working with SICK LiDAR devices, protocols and integration options, refer to the SICK Knowledge Base article below.

[Knowledgebase](https://support.sick.com/sick-knowledgebase/article/?code=KA-09481){ .md-button .button-small }

!!! note "Advanced documentation"
    The linked article provides additional background information about protocols and integration options.  
    It is especially useful if you want to go beyond the basic Starter Kit examples.

---

## SICK Perception SDK

For additional functionality and advanced integration, you can explore the SICK Perception SDK.

[Sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk){ .md-button .button-small }

The SDK provides extended support for SICK LiDAR devices and can be a valuable resource for advanced projects.

In LiDAR applications, precise measurement data is only useful if software can reliably access, process and integrate this data.  
A software development kit can help developers access sensor data, configure devices and build real-time applications.

---

## What the SDK Can Be Used For

The SICK Perception SDK can be useful for applications that require more than basic browser-based configuration or simple code snippets.

Typical use cases include:

- receiving scan data
- working with compact SICK data formats
- configuring sensors programmatically
- integrating LiDAR data into custom applications
- building real-time applications
- using LiDAR data on platforms such as PCs or embedded systems

---

## Key Features

<div class="requirement-box">

<h3>Core Capabilities</h3>

<ul>
  <li>Receive scan, IMU and encoder data in SICK data format Compact over UDP or TCP.</li>
  <li>Perform sensor configuration via REST API.</li>
  <li>Acquire data from multiple sensors in an event-driven and thread-safe way.</li>
  <li>Use a cross-platform build system based on CMake for Linux and Windows.</li>
  <li>Use dependency management via Conan 2.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Additional Features</h3>

<ul>
  <li>Compatible with x86_64 and ARM64 architectures, for example Raspberry Pi.</li>
  <li>Includes ready-to-use examples for fast prototyping.</li>
  <li>Provides diagnostic and logging capabilities.</li>
  <li>Includes unit and CI tests with real-world test data.</li>
  <li>Designed to support cybersecurity-related requirements such as the EU Cyber Resilience Act.</li>
</ul>

</div>

---

## When Should You Use the SDK?

Use the SDK if you want to build applications that require more advanced access to LiDAR data.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Use the Starter Kit UI</h3>
    <p>Use the browser-based user interface if you want to configure the sensor, create fields or test basic functionality.</p>
    <p>This is the best option for first demos and educational exercises.</p>
  </div>

  <div class="strategy-card">
    <h3>Use Code Examples</h3>
    <p>Use the LiDAR code examples if you want to send simple SOPAS commands or read basic measurement data with Python.</p>
    <p>This is useful for small scripts and first software experiments.</p>
  </div>

  <div class="strategy-card">
    <h3>Use the SDK</h3>
    <p>Use the SDK if you want to build more robust, scalable or performance-oriented applications.</p>
    <p>This is useful for advanced integration, sensor data processing and larger software projects.</p>
  </div>

</div>

---

## Typical Advanced Workflow

A possible workflow for advanced LiDAR integration could look like this:

1. Complete the LiDAR Getting Started guide.
2. Run a simple Field Evaluation demo.
3. Test the basic LiDAR Code Examples.
4. Read scan or field evaluation data with Python.
5. Decide whether simple scripts are sufficient.
6. If more robust integration is required, explore the SICK Perception SDK.
7. Build a custom application that processes or visualizes LiDAR data.

---

## Integration Ideas

The LiDAR Starter Kit can be extended in different ways depending on the use case.

Possible advanced integration ideas:

- create a dashboard for live LiDAR data
- visualize scan data in an external application
- combine field evaluation results with sound or light feedback
- use LiDAR data for interactive installations
- connect LiDAR data to a robot, PLC or control system
- process distance values for measurement or monitoring tasks
- combine multiple sensors in one application

---

## Relation to Code Examples

The LiDAR Code Examples page provides smaller Python snippets for basic communication.

Use the Code Examples page if you want to:

- test a TCP connection
- read the device type
- request scan data
- read field evaluation results
- understand basic SOPAS command handling

[LiDAR Code Examples](./lidar_code_snippets.md){ .md-button .button-small }

For larger software projects, the SDK may be a better starting point.

---

## Raw Sensor Data

If you want to access the raw data of the sensor, have a look at the following page:

[ScanSegmentAPI](https://github.com/SICKAG/ScanSegmentAPI/blob/public/README.md){ .md-button .button-small }

It describes how to receive and decode the raw scan segment data streamed by the sensor.  

---

## Summary

This page introduced advanced usage options for the LiDAR Starter Kit.

You learned where to find additional protocol and integration information, when the SICK Perception SDK may be useful and how advanced users can move from simple code examples to more robust LiDAR software applications.

The advanced topics are especially useful if you want to go beyond the basic Starter Kit demos and integrate LiDAR data into your own software or system environment.

## Next Steps

Continue with Training materials, example projects or the SICK Perception SDK.

<div class="next-step-buttons" markdown>

[Training material](./lidar_training_material.md){ .md-button }

[Example Projects](./lidar_example_projects.md){ .md-button }

[Sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk){ .md-button }

</div>