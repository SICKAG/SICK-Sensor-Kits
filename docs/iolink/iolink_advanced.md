# Advanced

This section covers advanced features and configurations for the Vision Starter Kit.

If you want to get more information about the SIG300, check out the operating instructions [Sensor Integration Gateway - SIG300 - REST-API](https://www.sick.com/ag/en/search?text=8029127)

The IO-Link Connectivity Starter Kit can also be combined with additional accessories to solve even more tasks and applications. Here's a list of useful accessories:

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">#</th>
      <th style="padding: 8px; text-align: left;">Article Description</th>
      <th style="padding: 8px; text-align: left;">Part No.</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>
        Signal light tower <a href="https://www.sick.com/ag/en/catalog/products/accessories/signal-transmitters/optical-signal-transmitters/slt060-0b010j700/p/p663661?tab=detail" target="_blank">SLT</a> – optical signal transmitter to visualize e.g. fill level or distance
      </td>
      <td>6075938</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        Color sensor <a href="https://www.sick.com/ag/en/catalog/products/detection-sensors/color-sensors/csm/csm-wp1b7a2p/p/p672179?tab=detail" target="_blank">CSM</a> with IO-Link for additional applications
      </td>
      <td>1122739</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        Condition monitoring sensors – Multi physics box <a href="https://www.sick.com/ag/en/catalog/products/detection-sensors/condition-monitoring-sensors/multi-physics-box/mpb10-vs00vsiq00/p/p670770?tab=detail" target="_blank">MPB10</a> to measure additional data
      </td>

## Engineering Tool SICK AppManager

With the engineering tool "SICK AppManager", you can e.g. upgrade your firmware.

1. Download [SICK AppManager](https://www.sick.com/de/en/products/digital-services-and-software/engineering-tools/sick-appmanager/sick-appmanager/p/p532784)
2. Install and open SICK AppManager
3. Device should automatically show up in the left upper corner
![SICK AppManager1](../images/SICK AppManager1.png)
4. If not: Click "Search"
5. If still not: Click on Settings icon and select USB" and all cross boxes within "Ethernet""
 ![SICK AppManager2](../images/SICK AppManager2.png)
6. You can edit the IP address of the device if useful only if you are connected via Ethernet.

**Firmware Update:**

1. Go to [SIG300 - REST firmware](https://www.sick.com/ag/en/catalog/products/network-and-connection-technology/network-devices/sig300/sig300-0a0gaa100/p/p678107?category=g569793&tab=downloads) (product page > Downloads > Software) and download the latest firmware
2. Extract the .zip file to access the .spk firmware file
3. In the upper right corner of AppManager, select "Firmware"
4. Click on the "+"
5. Choose the .spk file
6. Make sure the device you want to update is selected and click on install in the bottom right corner
![SICK AppManager3](../images/SICK AppManager3.png)