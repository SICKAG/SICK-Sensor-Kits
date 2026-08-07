# Fortgeschrittene Anwendung des Vision Starter Kits

In diesem Abschnitt werden erweiterte Funktionen und Konfigurationen für das Vision Starter Kit behandelt.

Wenn Sie weitere Informationen zum InspectorP61x oder zu SICK Nova erhalten möchten, lesen Sie bitte die Bedienungsanleitung [V2D611P-CMWBI4 – InspectorP61x | SICK](https://www.sick.com/ag/en/catalog/produkte/industrielle-bildverarbeitung-und-identifikation/industrielle-bildverarbeitung/inspectorp61x/v2d611p-cmwbi4/p/p685672?tab=downloads)

Das Vision Starter Kit lässt sich zudem mit zusätzlichem Zubehör kombinieren, um noch mehr Aufgaben und Anwendungsfälle zu bewältigen. Hier finden Sie eine Liste nützlicher Zubehörteile:

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
      <td>T-Verteiler – Schließen Sie ein zusätzliches Gerät für einen Ausgang (z. B. eine Signalleuchte) zwischen Stromversorgung und InspectorP61x an<br>Bitte beachten Sie, dass Sie zum Anschluss der Geräte ein zusätzliches Netzteil M12 5-polig (6075718) sowie ein Adapterkabel für das Netzteil (5 m, 2087577) benötigen.</td>
      <td>6030664</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Signalleiste – Optischer Signalsender zur Anzeige eines Sensorausgangs</td>
      <td>1114219</td>
    </tr>
    <tr>
      <td>3</td>
      <td>Lichtschranke – Auslösesensor für Inspector61x<br>Bitte beachten Sie, dass Sie ein zusätzliches IO-Link-Kabel (2096000) benötigen.</td>
      <td>1133545</td>
    </tr>
    <tr>
      <td>4</td>
      <td>3D-Druckdateien für Schokolade: <a href="https://sick.com/de/en/downloads/media/swp682086">sick.com/de/en/downloads/media/swp682086</a></td>
      <td>-</td>
    </tr>
  </tbody>
</table>

## Entwicklungswerkzeug SICK AppManager

Mit dem Engineering-Tool „SICK AppManager“ können Sie die IP-Adresse Ihres Geräts ermitteln, diese ändern oder die Firmware aktualisieren.

1. [SICK AppManager](https://www.sick.com/de/en/products/digital-services-and-software/engineering-tools/sick-appmanager/sick-appmanager/p/p532784)) herunterladen
2. SICK AppManager installieren und öffnen
3. Das Gerät sollte automatisch in der linken oberen Ecke angezeigt werden
![SICK AppManager1](../images/SICK AppManager1.png)
4. Falls nicht: Klicken Sie auf „Suchen“
5. Falls dies immer noch nicht funktioniert: Klicken Sie auf das Symbol „Einstellungen“ und aktivieren Sie alle Kontrollkästchen unter „Ethernet“.
 ![SICK AppManager2](../images/SICK AppManager2.png)
6. Sie können die IP-Adresse des Geräts bearbeiten, falls dies erforderlich ist.
7. Klicken Sie auf das Gerät, um die installierten Apps anzuzeigen. Standardmäßig sollten die Tools von SICK Nova als einzelne Apps vorinstalliert sein.

## Firmware-Update 

**Gerät:**

Wenn Sie ein Upgrade auf eine neuere Firmware-Version durchführen möchten, gehen Sie wie folgt vor:

1. Gehen Sie zu [V2D611P-CMWBI4 – InspectorP61x | SICK](https://www.sick.com/in/en/catalog/products/machine-vision-and-identification/machine-vision/inspectorp61x/v2d611p-cmwbi4/p/p685672?category=g569793&tab=downloads) (Produktseite > Downloads > Software) und laden Sie die neueste Firmware herunter
2. Entpacken Sie die ZIP-Datei, um auf die SPK-Firmware-Datei zuzugreifen.
3. Wählen Sie in der oberen rechten Ecke des AppManagers „Firmware“ aus.
4. Klicken Sie auf das „+“
5. Wählen Sie die .spk-Datei aus
6. Stellen Sie sicher, dass das Gerät, das Sie aktualisieren möchten, ausgewählt ist, und klicken Sie unten rechts auf „Installieren“.
![SICK AppManager3](../images/SICK AppManager3.png)

**SICK Nova:**

Wenn Sie auf eine neuere Version von SICK Nova aktualisieren möchten, haben Sie zwei Möglichkeiten:

1. Gehe zu [Nova Inspector im SICK AppPool](https://apppool.cloud.sick.com/publications/b027d4a7-9952-4651-acac-291a3929d3ad)
2. Gehen Sie zu „Versionen“ und laden Sie die neueste Version herunter.
3. Wählen Sie in der oberen rechten Ecke des AppManagers „Lokale Pakete“ aus.
4. Klicken Sie auf das „+“
5. Wählen Sie die .sapk-Datei aus
6. Stellen Sie sicher, dass das Gerät, das Sie aktualisieren möchten, ausgewählt ist, und klicken Sie unten rechts auf „Installieren“.
![SICK AppManager3](../images/SICK AppManager3.png)

## Individuelle Bildverarbeitung
- Verwenden Sie Nova, um benutzerdefinierte Bildverarbeitungsaufgaben zu erstellen.
- Konfigurationen für die Verwendung in anderen Projekten exportieren.

## Integration mit externen Systemen
- Schließen Sie das Vision Starter Kit an eine SPS oder ein anderes Steuerungssystem an.
- Nutzen Sie die bereitgestellte API für komplexe Automatisierungsaufgaben.

## Generator für benutzerdefinierte Werkzeuge
- Mit dem Generator für benutzerdefinierte Tools können Sie vorhandene Tools anpassen, z. B. wenn Sie eine große Anzahl von Blobs zählen möchten.
Laden Sie diese ZIP-Datei herunter und öffnen Sie die Datei „search.html“.
[Nova-API-2.9.0-.zip](../files/Nova API 2.9.0.zip)