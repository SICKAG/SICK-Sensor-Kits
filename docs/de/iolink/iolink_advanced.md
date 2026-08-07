# Fortgeschritten

In diesem Abschnitt werden erweiterte Funktionen und Konfigurationen für das Vision Starter Kit behandelt.

Wenn Sie weitere Informationen zum SIG300 erhalten möchten, lesen Sie bitte die Bedienungsanleitung [Sensor Integration Gateway – SIG300 – REST-API](https://www.sick.com/ag/en/search?text=8029127)

Das IO-Link-Konnektivitäts-Starter-Kit lässt sich zudem mit zusätzlichem Zubehör kombinieren, um noch mehr Aufgaben und Anwendungen zu lösen. Hier finden Sie eine Liste nützlicher Zubehörteile:

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">#</th>
      <th style="padding: 8px; text-align: left;">Artikelbeschreibung</th>
      <th style="padding: 8px; text-align: left;">Artikelnummer</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>
        Signalturm <a href="https://www.sick.com/ag/en/catalog/products/accessories/signal-transmitters/optical-signal-transmitters/slt060-0b010j700/p/p663661?tab=detail" target="_blank">SLT</a> – optischer Signalsender zur Visualisierung von z. B. Füllstand oder Entfernung
      </td>
      <td>6075938</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        Farbsensor <a href="https://www.sick.com/ag/en/catalog/products/detection-sensors/color-sensors/csm/csm-wp1b7a2p/p/p672179?tab=detail" target="_blank">CSM</a> mit IO-Link für weitere Anwendungsbereiche
      </td>
      <td>1122739</td>
    </tr>
    <tr>
      <td>2</td>
      <td>
        Sensoren zur Zustandsüberwachung – Multiphysik-Box <a href="https://www.sick.com/ag/en/catalog/products/detection-sensors/condition-monitoring-sensors/multi-physics-box/mpb10-vs00vsiq00/p/p670770?tab=detail" target="_blank">MPB10</a> zur Erfassung zusätzlicher Daten
      </td>
      </tr>
  </tbody>
</table>
    

## Entwicklungswerkzeug SICK AppManager

Mit dem Engineering-Tool „SICK AppManager“ können Sie beispielsweise Ihre Firmware aktualisieren.

1. [SICK AppManager](https://www.sick.com/de/en/products/digital-services-and-software/engineering-tools/sick-appmanager/sick-appmanager/p/p532784)) herunterladen
2. SICK AppManager installieren und öffnen
3. Das Gerät sollte automatisch in der linken oberen Ecke angezeigt werden
![SICK AppManager1](../images/SICK AppManager1.png)
4. Falls nicht: Klicken Sie auf „Suchen“
5. Falls dies immer noch nicht funktioniert: Klicken Sie auf das Symbol „Einstellungen“, wählen Sie „USB“ aus und aktivieren Sie alle Kontrollkästchen unter „Ethernet“.
 ![SICK AppManager2](../images/SICK AppManager2.png)
6. Sie können die IP-Adresse des Geräts nur dann bearbeiten, wenn Sie über Ethernet verbunden sind.

**Firmware-Update:**

1. Gehen Sie zu [SIG300 – REST-Firmware](https://www.sick.com/ag/en/catalog/products/network-and-connection-technology/network-devices/sig300/sig300-0a0gaa100/p/p678107?category=g569793&tab=downloads) (Produktseite > Downloads > Software)) und laden Sie die neueste Firmware herunter.
2. Entpacken Sie die ZIP-Datei, um auf die SPK-Firmware-Datei zuzugreifen.
3. Wählen Sie in der oberen rechten Ecke des AppManagers „Firmware“ aus.
4. Klicken Sie auf das „+“
5. Wählen Sie die .spk-Datei aus
6. Stellen Sie sicher, dass das Gerät, das Sie aktualisieren möchten, ausgewählt ist, und klicken Sie unten rechts auf „Installieren“.
![SICK AppManager3](../images/SICK AppManager3.png)