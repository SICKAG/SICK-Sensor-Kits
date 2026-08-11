# Erste Schritte mit dem LiDAR-Starter-Kit

Befolgen Sie diese Schritte, um Ihr LiDAR-Starter-Kit einzurichten und in Betrieb zu nehmen:

## Schritt 1: Hardware-Einrichtung
1. Schließen Sie den LiDAR-Sensor mithilfe des mitgelieferten Kabels und des Netzwerkadapters an Ihren Computer an.
2. Stellen Sie sicher, dass das Netzteil angeschlossen und eingeschaltet ist.
3. Konfigurieren Sie die IP-Adresse des Adapters.

??? sickinfo "Ausführliche Anleitung"

      - Tastenkombination unter Windows: „Win + R“: „ncpa.cpl“

      ![Win + R: ncpa.cpl](../images/Network_adapter_1.png)

      - Alternative: Öffnen Sie die Netzwerkeinstellungen Ihres Betriebssystems (z. B. **Systemsteuerung > Netzwerk und Internet** unter Windows 10/11 oder die entsprechende Option in Ihrem Betriebssystem).  
      Wählen Sie **Erweiterte Netzwerkeinstellungen**  

      - Suchen Sie den USB-Ethernet-Adapter (möglicherweise als **ASIX USB to Gigabit Ethernet Family Adapter** aufgeführt).

      ![Win + R: ncpa.cpl](../images/Network_adapter_2.png) 

      - Klicken Sie auf den Adapter und wählen Sie **Eigenschaften / Bearbeiten**.  

      - Geben Sie gegebenenfalls die Administrator-Anmeldedaten ein.  

      - Suchen Sie **Internetprotokoll Version 4 (TCP/IPv4)** und wählen Sie **Eigenschaften** oder klicken Sie mit der rechten Maustaste darauf.

      ![Win + R: ncpa.cpl](../images/Network_adapter_3.png)  

      - Von DHCP auf manuelle IP-Einstellungen umstellen:  
      Verwenden Sie die folgende IP-Adresse: `192.168.0.xxx`  
      Subnetzmaske: `255.255.0.0`

      ![Win + R: ncpa.cpl](../images/Network_adapter_4.png)  

      - Speichern Sie die Änderungen, indem Sie in beiden Fenstern auf **OK** klicken.

- Öffnen Sie einen Browser und geben Sie die Standard-IP-Adresse 192.168.0.1 ein. Nun sollte die Benutzeroberfläche des Sensors angezeigt werden.

![LiDAR-Anschlussplan](../images/lidarconnection.JPG)  
*Abbildung 1: Anschlusskonfiguration für das LiDAR-Starter-Kit.*

## Schritt 2: Softwareinstallation

Bei der Ersteinrichtung ist keine zusätzliche Softwareinstallation erforderlich, wenn Sie lediglich die Sensor-Benutzeroberfläche in Ihrem Browser öffnen möchten.

Für fortgeschrittenere Anwendungsfälle, wie beispielsweise das Auslesen von Messdaten mit Python-Skripten, können Sie die im Projekt-Repository bereitgestellten Beispielskripte verwenden.

Typische Werkzeuge, die Sie später möglicherweise benötigen:

- Python
- Visual Studio Code oder eine andere IDE
- Beispielskripte für die LiDAR-Kommunikation
- Optional: Projektdateien auf GitHub.com

!!! note "Software-Einrichtung"
    Die Grundeinrichtung kann über die Benutzeroberfläche des Sensors vorgenommen werden.  
    Python-Skripte werden hauptsächlich für fortgeschrittene Beispiele und benutzerdefinierte Anwendungen benötigt.

---

## Schritt 3: Erste Messung

Sobald der LiDAR-Sensor angeschlossen und erreichbar ist, können Sie mit Ihrer ersten Messung oder Ihrer ersten Demo beginnen.

Sie haben folgende Möglichkeiten:

- Überprüfen Sie über die Benutzeroberfläche des Sensors, ob der Sensor erreichbar ist.
- Weiter mit dem ersten LiDAR-Beispielprojekt
- Python-Skripte zum Auslesen von Geräte- oder Messdaten verwenden

---

## Nächste Schritte

**Starten Sie Ihr erstes LiDAR-Projekt:**

[Feldbewertung](./lidar_field_evaluation.md){ .md-button .button-small }

**Oder wählen Sie eine andere Option:**

<div class="next-step-buttons" markdown>

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[LiDAR-Code-Beispiele](./lidar_code_snippets.md){ .md-button }

[Fortgeschritten](./lidar_advanced.md){ .md-button }

</div>