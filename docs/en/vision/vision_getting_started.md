# Getting Started with the Vision Starter Kit

You are now ready to get started with the Vision Starter Kit. Follow along the instruction below to setup the sensor.

## Setup Vision Sensor

1. Mount the Inspector to the [Mounting Frame](../mounting_frame.md). Tilt the top bar about 10–15 degrees to avoid reflections.
2. Connect the Inspector with the network cable and power supply.
3. Connect the network cable to the USB network adapter.
4. Choose the correct plug adapter and plug the power supply into an outlet.
5. Connect the USB network adapter to the PC.
6. Configure the IP address of the adapter.

??? sickinfo "Detailed instructions"   

      - Shortcut in Windows: "Win + R": "ncpa.cpl"

      ![Win + R: ncpa.cpl](../images/Network_adapter_1.png)

      - Alternative: Open your operating system's network settings (e.g., **Control Panel > Network & Internet** in Windows 10/11, or the equivalent in your OS).  
      Choose **Advanced network settings**  

      - Identify the USB Ethernet adapter (might be listed as **ASIX USB to Gigabit Ethernet Family Adapter**).

      ![Win + R: ncpa.cpl](../images/Network_adapter_2.png) 

      - Click on the adapter and select **Properties / Edit**.  

      - Enter administrator credentials if necessary.  

      - Locate **Internet Protocol Version 4 (TCP/IPv4)** and select **Properties** or right-click.

      ![Win + R: ncpa.cpl](../images/Network_adapter_3.png)  

      - Change from DHCP to manual IP settings:  
      Use the following IP address: `192.168.0.210`  
      Subnet mask: `255.255.0.0`

      ![Win + R: ncpa.cpl](../images/Network_adapter_4.png)  

      - Save changes by clicking **Ok** in both windows.

- Open a browser and enter the default IP address 192.168.0.1.
You should now see the below UI. Create an Empty Job.

![Win + R: ncpa.cpl](../images/Vision_1.png)

---

## Next Steps

**Get started with your first project**: [Vision Starter Project](./vision_starter_project.md){.md-button .button-small}


**Or choose an [example project](./vision_example_projects.md) or [code snippets](./vision_code_snippets.md) or check out the [training materials](./vision_training_material.md).**

??? info "Troubleshooting"
    ## Troubleshooting

    Check out the [Operating instructions](https://www.sick.com/ag/en/catalog/products/machine-vision-and-identification/machine-vision/inspectorp61x/v2d611p-cmwbi4/p/p685672?tab=downloads) of the device for more information.

    1. Make sure you are disconnected from any VPN as this may block the connection to the network device. 
    2. If you can't connect to the sensor, check if the LED **"Ready"** is green.  
         If not, the power supply is not correctly established. Wait up to 2 minutes and check if the power supply is connected correctly.
    3. If you still can’t connect, look up the device IP address via **SICK AppManager**:  
         [SICK AppManager | SICK](https://www.sick.com/ag/en/catalog/products/digital-services-and-software/engineering-tools/sick-appmanager/sick-appmanager/p/p532784)  
         Go to the **Advanced section** for details.

    4. If you are already connected and using AI tools:  
       - The device has a trial license. After 2 hours, restart the device to reset the timer.  
       - Unplug and plug in again. Save configuration beforehand.

    5. Check the **FAQ section**: [FAQ](./vision_faq.md)

    6. If you still have issues with the device:  
         - Go to the **Support Portal**, register, and create a case to get assistance.





