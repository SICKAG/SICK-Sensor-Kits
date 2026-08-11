
# SICK-Sensor-Starter-Kits

Willkommen auf der GitHub-Seite für die SICK-Sensor-Starter-Kits!

Die Kits enthalten eine umfassende Auswahl an Sensoren, Zubehör und Anwendungsbeispielen, die Ihnen den schnellen Einstieg in die Arbeit mit SICK-Sensoren erleichtern. Diese Kits umfassen alles, was Sie benötigen, um Sensorlösungen zu erkunden, Prototypen zu entwickeln und in Ihre Projekte zu integrieren.



<style>
  .slideshow-container {
    position: relative;
    width: 600px; /* adjust as needed */
    margin: auto;
    overflow: hidden;
  }

  .slide {
    display: flex;
    transition: transform 1s ease-in-out;
    width: 100%;
  }

  .slide img {
    width: 100%;
    flex-shrink: 0;
  }

  /* Arrows */
  .arrow {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    font-size: 2rem;
    color: gray;
    background: none;
    border: none;
    cursor: pointer;
    z-index: 10;
  }

  .arrow-left {
    left: 10px;
  }

  .arrow-right {
    right: 10px;
  }
</style>

<div class="slideshow-container">
  <div class="slide" id="slide">
    <img src="images/A7406000.jpg" alt="Image 1">
    <img src="images/A7405998.jpg" alt="Image 2">
    <img src="images/A7405946.jpg" alt="Image 3">
    <img src="images/A7405872.jpg" alt="Image 4">
    <img src="images/A7405854.jpg" alt="Image 5">
  </div>
  <button class="arrow arrow-left" onclick="prevImage()">&lt;</button>
  <button class="arrow arrow-right" onclick="nextImage()">&gt;</button>
</div>

<script>
  const slide = document.getElementById('slide');
  const totalImages = slide.children.length;
  let index = 0;

  function updateSlide() {
    slide.style.transform = `translateX(-${index * 100}%)`;
  }

  function nextImage() {
    index = (index + 1) % totalImages;
    updateSlide();
  }

  function prevImage() {
    index = (index - 1 + totalImages) % totalImages;
    updateSlide();
  }

  // Auto-slide every 3 seconds
  setInterval(nextImage, 5000);
</script>


## Wählen Sie Ihr Starter-Kit aus

Wählen Sie das Starter-Kit aus, mit dem Sie arbeiten, um die Einrichtungsanleitung, die erste Demo und die Beispielprojekte zu öffnen.

<div class="grid cards kit-card-grid" markdown>

-    ![Vision-Starter-Kit](images/vision.jpg)

    **Vision-Starter-Kit**

    Machen Sie sich mit bildbasierten Sensoranwendungen und Beispielen für KI-gestützte Bildverarbeitung vertraut.

     [Vision](vision/vision_overview.md){.md-button}

-   ![LiDAR-Starter-Kit](images/lidar.jpg)

    **LiDAR-Starter-Kit**

    Entdecken Sie Entfernungsmessung, Geländebewertung und interaktive LiDAR-Demonstrationen

     [LiDAR](lidar/lidar_overview.md){.md-button}

-   ![IO-Link](images/iolink.jpg)

    **IO-Link-Konnektivitäts-Starter-Kit**

    IO-Link-Geräte anschließen und Prozessdaten auslesen.

    [IO-Link](iolink/iolink_overview.md){.md-button}

</div>

## Brauchst du ein Starter-Kit?

Sie haben noch kein Starter-Kit? Hier erfahren Sie mehr und können Ihr Exemplar kaufen!

[Starter-Sets](https://www.sick.com/s/sensor-starter-kits){:target="_blank".md-button}

!!! note "Nutzung zu Bildungszwecken"
    Bitte beachten Sie, dass die Starter-Kits ausschließlich für Schulungszwecke bestimmt sind und nicht in Produktionsumgebungen verwendet werden dürfen.