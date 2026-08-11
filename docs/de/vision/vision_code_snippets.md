# Beispiele für Vision-Code

## Kurzbeschreibung

Auf dieser Seite finden Sie kurze Python-Code-Beispiele für die Kommunikation mit dem Vision Starter Kit über TCP/IP.

Die Beispiele sollen als Ausgangspunkt für Ihre eigenen Anwendungen dienen.  
Es handelt sich dabei nicht um fertige Projekte, sondern um wiederverwendbare Bausteine für die Anbindung an den Sensor, den Empfang von Daten und das Senden einfacher Befehle.

## Übersicht über die Code-Beispiele

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Beispiel</th>
      <th style="padding: 8px; text-align: left;">Zweck</th>
      <th style="padding: 8px; text-align: left;">Schwierigkeitsgrad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Mit dem Bildsensor verbinden</td>
      <td>Eine TCP-Verbindung zum Sensor herstellen</td>
      <td>Grundlagen</td>
    </tr>
    <tr>
      <td>Sensormeldungen empfangen</td>
      <td>Eingehende Nachrichten kontinuierlich lesen</td>
      <td>Grundlagen</td>
    </tr>
    <tr>
      <td>Bildaufnahme auslösen</td>
      <td>Triggerbefehle an den Sensor senden</td>
      <td>Mittelstufe</td>
    </tr>
  </tbody>
</table>

---

## Bevor Sie beginnen

Stellen Sie sicher, dass das Vision Starter Kit angeschlossen ist und von Ihrem Computer aus erreichbar ist.

Möglicherweise müssen Sie die folgenden Werte in den Code-Beispielen anpassen:

```python
server_ip = "192.168.0.1"
server_port = 34170
```

!!! note "Netzwerkeinstellungen"
    Die IP-Adresse und der Port können je nach Konfiguration Ihres Sensors variieren.  
    Überprüfen Sie die Netzwerkeinstellungen Ihres Vision Starter Kits, bevor Sie den Code ausführen.

---

## Beispiel 1: Verbindung zum Bildsensor herstellen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

Dieses Beispiel zeigt, wie man mit Python eine TCP-Verbindung zum Vision-Sensor herstellt.

Dies kann als erster Verbindungstest dienen, um zu überprüfen, ob Ihr Computer den Sensor über die konfigurierte IP-Adresse und den konfigurierten Port erreichen kann.

<span class="example-label">Code</span>

```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = "192.168.0.1"
server_port = 34170

client.connect((server_ip, server_port))

print("Connected to Vision Sensor")

client.close()
```

<span class="example-label">Expected Result</span>

Wenn die Verbindung erfolgreich hergestellt wurde, sollte auf dem Terminal Folgendes angezeigt werden:

```text
Connected to Vision Sensor
```

Sollte die Verbindung fehlschlagen, überprüfen Sie Folgendes:

- IP-Adresse des Sensors
- Sensoranschluss
- Netzwerkverbindung
- Firewall-Einstellungen
- Konfiguration des Netzwerkadapters

</div>

---

## Beispiel 2: Sensor-Meldungen kontinuierlich empfangen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

In diesem Beispiel wird eine Verbindung zum Sensor hergestellt und es werden kontinuierlich eingehende Nachrichten empfangen.

Damit lässt sich überprüfen, ob der Sensor Daten an Ihre Python-Anwendung sendet.

<span class="example-label">Code</span>

```python
import socket

def run_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.0.1"
    server_port = 34170

    client.connect((server_ip, server_port))

    try:
        while True:
            message = client.recv(1024)
            message = message.decode("utf-8")
            print("Received:", message)

    except KeyboardInterrupt:
        print("Stopping client...")

    finally:
        client.close()

run_client()
```

<span class="example-label">Expected Result</span>

Das Terminal gibt die vom Sensor empfangenen Meldungen aus.

Beispiel:

```text
Received: ...
```

Beenden Sie das Skript mit:

```text
CTRL + C
```

!!! note "Kontinuierlicher Empfang"
    In diesem Beispiel wird auf eingehende Daten vom Sensor gewartet.  
    Wenn nichts ausgedruckt wird, überprüfen Sie, ob der Sensor so konfiguriert ist, dass er Ergebnisdaten übermittelt.

</div>

---

## Beispiel 3: Bildaufnahme auslösen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

In diesem Beispiel werden einfache Auslösebefehle an den Sensor gesendet.

Damit lassen sich über ein Python-Skript ein Auftrag auswählen, die Bildaufnahme auslösen und die Bildaufzeichnung starten.

<span class="example-label">Code</span>

```python
import socket

def trigger_image():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "192.168.0.1"
    server_port = 34170

    client.connect((server_ip, server_port))

    client.sendall(b"\x02set job 2\x03")
    client.sendall(b"\x02trigger\x03")
    client.sendall(b"\x02RecordImages\x03")

    print("Trigger commands sent")

    client.close()

trigger_image()
```

<span class="example-label">Expected Result</span>

Der Sensor empfängt die Auslösebefehle und startet den konfigurierten Bildaufnahme-Workflow.

Auf dem Terminal sollte Folgendes angezeigt werden:

```text
Trigger commands sent
```

!!! warning "Auftragsnummer"
    Der Befehl `set job 2` wählt die Auftragsnummer 2 aus.  
    Ändern Sie diesen Wert, wenn Ihr entsprechender Auftrag eine andere Auftragsnummer hat.

!!! note "Befehlsformat"
    Die Zeichen `\x02` und `\x03` markieren den Anfang und das Ende des Befehlstelegramms.

</div>

## Erwartetes Ergebnis

Der Sensor empfängt die Auslösebefehle und startet den konfigurierten Bildaufnahme-Workflow.

!!! warning "Auftragsnummer"
    Der Befehl `set job 2` wählt die Auftragsnummer 2 aus.  
    Ändern Sie diesen Wert, wenn in Ihrem jeweiligen Auftrag eine andere Zahl verwendet wird.

---

## Fehlerbehebung

??? info "Fehlerbehebung"

    !!! failure "Verbindung abgelehnt"
        Überprüfen Sie, ob der Sensor erreichbar ist und ob der richtige Anschluss verwendet wird.

    !!! failure "Keine Rückmeldung vom Sensor"
        Überprüfen Sie die Ethernet-Verbindung und die Einstellungen des Sensornetzwerks.

    !!! failure "Unerwartetes Nachrichtenformat"
        Stellen Sie sicher, dass der Sensor so konfiguriert ist, dass er das erwartete Antwortformat übermittelt.

---

## Nächste Schritte

Nutzen Sie diese Beispiele als Bausteine für Ihre eigenen „Vision Starter Kit“-Projekte.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button }

[Fortgeschrittene Themen](./vision_advanced.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>