# Fortgeschrittene Anwendung des Vision Starter Kits

## Kurzbeschreibung

Diese Seite enthält detaillierte Informationen zur Arbeit mit dem Vision Starter Kit.

Es umfasst nützliches Zubehör, den SICK AppManager, Firmware- und SICK Nova-Updates, individuelle Bildverarbeitungsoptionen sowie Integrationsmöglichkeiten mit externen Systemen.

## Übersicht über fortgeschrittene Themen

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Thema</th>
      <th style="padding: 8px; text-align: left;">Zweck</th>
      <th style="padding: 8px; text-align: left;">Empfohlen für</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zubehör</td>
      <td>Erweitern Sie das Vision Starter Kit um zusätzliche Hardware.</td>
      <td>Benutzer, die komplexere Konfigurationen erstellen möchten.</td>
    </tr>
    <tr>
      <td>SICK AppManager</td>
      <td>Geräte suchen, IP-Adressen ändern und installierte Apps verwalten.</td>
      <td>Benutzer, die das Gerät konfigurieren oder warten müssen.</td>
    </tr>
    <tr>
      <td>Firmware- und SICK Nova-Updates</td>
      <td>Aktualisieren Sie die Geräte-Firmware oder installieren Sie eine neuere Version von SICK Nova.</td>
      <td>Fortgeschrittene Benutzer und Betreuer.</td>
    </tr>
    <tr>
      <td>Individuelle Bildverarbeitung</td>
      <td>Erstellen und exportieren Sie benutzerdefinierte Konfigurationen für weitere Projekte.</td>
      <td>Nutzer, die ihre eigenen Anwendungen entwickeln möchten.</td>
    </tr>
    <tr>
      <td>Externe Integration</td>
      <td>Schließen Sie das Vision Starter Kit an externe Systeme an.</td>
      <td>Anwender, die an Automatisierungs- oder Systemintegrationsaufgaben arbeiten.</td>
    </tr>
  </tbody>
</table>

<br>

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

---

## Zusammenfassung

Auf dieser Seite wurden erweiterte Optionen für die Arbeit mit dem Vision Starter Kit vorgestellt.

Sie haben erfahren, wo Sie weitere Produktinformationen finden, wie Sie den SICK AppManager nutzen, wie Firmware- und SICK Nova-Updates installiert werden können und wie sich das Starter-Kit mit Zubehör, externen Systemen und benutzerdefinierten Bildverarbeitungsabläufen erweitern lässt.

Diese Themen sind besonders hilfreich, wenn Sie von den grundlegenden Starter-Kit-Demos zu fortgeschritteneren Anwendungen übergehen möchten.

---

## Nächste Schritte

Fahren Sie mit den Beispielprojekten, den grundlegenden Code-Beispielen oder den Schulungsunterlagen fort.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button }

[Beispiele für Vision-Code](./vision_code_snippets.md){ .md-button }

[Schulungsunterlagen](./vision_training_material.md){ .md-button }

</div>