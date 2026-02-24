# Advanced Usage of the LiDAR Starter Kit
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