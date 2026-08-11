<div class="faq-page"markdown>

# FAQ - Vision Starter Kit

## Short Description

This FAQ answers common questions related to the Vision Starter Kit, SICK Nova, image acquisition and AI-based tools.

For general questions about the Starter Kits, support resources or additional training material, please visit the general [FAQ](../faq.md) section.

---

??? question "The device is running slowly. How can I improve the performance?"

    In the **Acquisition** section, you can adjust the **Downsample** slider to reduce the image resolution and increase the processing speed.

    This can improve performance, especially when using AI tools or multiple analysis tools in one job.

    !!! warning "Important"
        Adjust downsampling at the beginning of a project.  
        Regions that were already created, for example for Object Locator or AI tools, may not be adjusted automatically afterwards.

---

??? question "The image is too dark, too bright or blurry. What can I do?"

    Check the acquisition settings in SICK Nova.

    Useful actions include:

    - run **Auto setup**
    - adjust exposure settings
    - improve lighting conditions
    - adjust the focus manually using the focus adjustment tool
    - check the distance between object and sensor

    If the image quality is poor, AI Classification and Anomaly Detection may also become unreliable.

---

??? question "Where can I get more information about the available tools?"

    In SICK Nova, you can access tool-specific information directly through the **Help** section.

    This is useful if you want to understand what a specific tool does, which parameters are available and how the tool can be used in a workflow.

    A comprehensive online overview of the [SICK Nova](https://sicknova.documentation) tools is planned here:


    !!! note
        The online documentation link may not be available yet.

---

??? question "How can I use data from SICK Nova in an IDE such as Visual Studio Code or Python?"

    You can use the **Results** section in SICK Nova to configure and send result data.

    For first experiments, you can also use the [Vision Code Examples](./vision_code_snippets.md) page.

    Typical use cases include:

    - receiving sensor results in Python
    - triggering image acquisition
    - reading classification results
    - sending data to an external application

---

??? question "AI Classification does not work reliably. What can I improve?"

    Classification reliability strongly depends on the quality and variety of the training images.

    Try the following:

    - add more training images
    - use different object positions
    - use different rotations
    - keep lighting conditions stable
    - make sure the object is clearly visible
    - reduce reflections or shadows
    - check whether the classes are visually distinguishable

    If the classification is still unstable, start with fewer classes and add more classes later.

---

??? question "Anomaly Detection does not work reliably. What should I check?"

    Anomaly Detection depends on a stable image and, in many cases, on a reliable Object Locator.

    Check the following:

    - the object is positioned consistently
    - the image is sharp and well-lit
    - the Object Locator tracks the object reliably
    - the reference region is placed correctly
    - enough Good images were added
    - the training parameters are suitable for the object variation

    !!! warning "Dependency on Object Locator"
        If the Object Locator fails, Anomaly Detection may also fail.  
        Make sure the Object Locator works reliably before optimizing Anomaly Detection.

---

??? question "The Object Locator does not track the object reliably. What can I do?"

    The Object Locator needs a distinctive and stable reference area.

    Try the following:

    - select a part of the object with clear edges or contrast
    - avoid uniform or reflective areas
    - adjust edge strength
    - allow rotation if the object can rotate
    - adjust match score and angle settings
    - improve lighting and focus

    If tracking is still unstable, choose a different reference area.

---

??? question "Where can I find example projects for the Vision Starter Kit?"

    The Vision Starter Kit example projects are listed on the  [Example Projects](./vision_example_projects.md) page.

    Start with a guided project if you are new to the Vision Starter Kit.

---

??? question "Where can I find complete project files or source code?"

    The GitHub.io documentation provides explanations, setup guides and project overviews.

    Complete project files and source code should be provided through the [GitHub.com](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank"} project repository.

---

## Related Pages

<div class="next-step-buttons" markdown>

[Getting started](./vision_getting_started.md){ .md-button }

[Example Projects](./vision_example_projects.md){ .md-button }

[Vision Code Examples](./vision_code_snippets.md){ .md-button }

[FAQ](../faq.md){ .md-button }

</div>

</div>