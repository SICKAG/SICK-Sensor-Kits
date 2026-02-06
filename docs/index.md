# SICK Sensor Starter Kits

Welcome to the GitHub for the SICK Sensor Starter Kits!

The Kits provide a comprehensive set of sensors, accessories and examples to help you quickly get started with SICK sensors. These kits include everything you need to explore, prototype, and integrate sensor solutions into your projects.

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

<br>
Don’t have a Starter Kit yet? Find out more and purchase yours here!

[Starter Kits](https://www.sick.com/s/sensor-starter-kits){:target="_blank".md-button}


Please note that the starter kits are intended for educational purposes only and must not be used in production environments.

Got your Starter Kit(s)? Start exploring now!

- [LIDAR Starter Kit](lidar/lidar_overview.md)
- [Vision Starter Kit](vision/vision_overview.md)
- [IO Link Connectivity Starter Kit](iolink/iolink_overview.md)
