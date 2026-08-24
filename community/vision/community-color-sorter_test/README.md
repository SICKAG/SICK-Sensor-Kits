# Project Name

Provide a short introduction to the project.

Explain what the project does, which problem it solves and how the SICK Sensor Starter Kit is used.

![Project Previewg

## Project Information

- **Starter Kit:** Vision / LiDAR / IO-Link
- **Project Type:** Community Project
- **Difficulty:** Beginner / Intermediate / Advanced
- **Estimated Duration:** e.g. 60 minutes
- **Programming Language:** e.g. Python
- **Author or Institution:** Optional
- **Tested Environment:** e.g. Windows 11, Python 3.12

Keep these values consistent with `project-info.yml`.

## Goal

Describe the goal of the project.

After completing the project, users should be able to:

- understand the main use case
- configure the required sensor functionality
- run the provided application
- reproduce the expected result

## Requirements

### Hardware

List all required hardware:

- SICK Sensor Starter Kit
- required sensor or device
- computer or laptop
- additional objects or hardware

Clearly indicate which components are not included in the Starter Kit.

### Software

List all required software:

- operating system
- programming language and tested version
- required SICK software
- additional applications
- external libraries

## Project Files

Briefly explain the contents of the project folder:

```text
project-name/
├── README.md
├── project-info.yml
├── requirements.txt
├── src/
└── images/
```

Example:

- `src/main.py`: Main application
- `requirements.txt`: Required Python packages
- `images/`: Preview image and screenshots
- `project-info.yml`: Structured project metadata

Add other folders to this list if the project uses configuration files or additional downloads.

## Hardware Setup

Explain how to assemble and connect the required hardware.

Include important information such as:

- sensor position
- cable connections
- power supply
- network connection
- position of test objects
- additional hardware

Add setup images when helpful:

```markdown
![Hardware Setup](images/hardware-setup.png)figuration

Explain how to configure the sensor.

Include where applicable:

1. Open the required SICK software or sensor interface.
2. Connect to the sensor.
3. Configure the required application or tools.
4. Import the provided configuration file.
5. Adjust values such as the IP address or detection fields.
6. Save or activate the configuration.

Document all values that users may need to adapt.

## Installation

Clone or download the repository and open the project folder.

For Python projects, install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

If additional installation steps are required, describe them here.

Remove this section if the project does not require an installation.

## Configuration

Explain which values users may need to change before running the project.

Example:

```python
HOST = "192.168.0.1"
PORT = 2111
```

Describe:

- what each value controls
- which default value is used
- when the value must be changed
- where the correct value can be found

Never add passwords, API keys or other credentials to the repository.

## Run the Project

Explain how to start the application.

Example:

```bash
python src/main.py
```

Then describe the expected interaction:

1. Start the sensor.
2. Open the required sensor application.
3. Run the provided source code.
4. Place an object in the monitored area.
5. Observe the application output.

## Expected Result

Describe what should happen when the project works correctly.

Include:

- expected sensor behavior
- terminal or application output
- visual, sound or signal feedback
- relevant measurement values
- screenshots where helpful

Example:

```text
When a configured field is infringed, the application displays the
field number and plays the corresponding sound.
```

images/result.png

## Configuration Options

Document useful configuration options.

Example:

```text
PLAY_MODE = "trigger"
```

Possible values:

- `trigger`: Run the action once when the state changes.
- `hold`: Keep the action active while the condition remains true.

Remove this section if the project has no configurable options.

## Troubleshooting

### The sensor cannot be reached

Check:

- power supply
- network connection
- sensor IP address
- computer network configuration
- firewall settings

### The application does not start

Check:

- programming language version
- installed dependencies
- file paths
- configuration values
- terminal error messages

### The result is not reliable

Check:

- sensor position
- lighting or environmental conditions
- configured detection areas
- object position
- application parameters

Add project-specific problems and solutions where necessary.

## Tested Environment

Document the environment in which the project was tested.

Example:

```text
Operating system: Windows 11
Python version: 3.12
Sensor: picoScan150
SICK software: Version used during testing
Additional library: pygame-ce 2.5
```

Do not claim support for platforms or devices that were not tested.

## Known Limitations

Describe known limitations honestly.

Examples:

- only tested on Windows
- field positions depend on the sensor configuration
- requires a specific software version
- performance depends on the computer
- additional hardware is required
- some object types may not be detected reliably

Write `No known limitations` if none are currently known.

## Possible Extensions

List optional ideas for extending the project:

- add additional sensor functions
- add more classes or detection fields
- create a dashboard
- add visual or sound feedback
- connect an external application
- support additional hardware
- add another game or operating mode

## Author and Affiliation

- **Author:** Name or GitHub username
- **Affiliation:** University, organization or community
- **Contact:** Optional public contact information

Only provide information that may be published publicly.

## Third-Party Content

List third-party libraries, images, audio files, datasets or other resources used by the project.

For each item, include where applicable:

- name
- source
- author
- license
- required attribution

Write `No third-party content included` if none is used.

## Educational Use

This project is intended for educational and demonstration purposes.

It must not be considered production-ready unless the required engineering, validation, security and product processes have been completed.

## Related Documentation

- https://sickag.github.io/SICK-Sensor-Starter-Kits/en/
- Add the related Starter Kit overview or Getting Started page here.