# LiDAR-Code-Beispiele

## Kurzbeschreibung

Auf dieser Seite finden Sie kurze Python-Code-Beispiele für die Kommunikation mit dem LiDAR-Starter-Kit über TCP/IP.

Die Beispiele sollen als Ausgangspunkt für Ihre eigenen Anwendungen dienen.  
Es handelt sich dabei nicht um fertige Projekte, sondern um wiederverwendbare Bausteine zum Auslesen von Geräteinformationen, zum Anfordern von Scandaten und zum Empfangen von Auswertungsergebnissen vor Ort.

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
      <td>Gerätetyp auslesen</td>
      <td>Grundlegende Geräteinformationen vom LiDAR-Sensor abrufen.</td>
      <td>Grundlagen</td>
    </tr>
    <tr>
      <td>Scandaten einmal lesen</td>
      <td>Fordere eine Antwort mit den Scandaten vom Sensor an.</td>
      <td>Grundlagen</td>
    </tr>
    <tr>
      <td>Scandaten kontinuierlich lesen</td>
      <td>Aktivieren Sie die kontinuierliche Ausgabe von Scandaten und verarbeiten Sie eingehende Daten.</td>
      <td>Mittelstufe</td>
    </tr>
    <tr>
      <td>Ergebnis der Feldbewertung lesen</td>
      <td>Lesen Sie das Ergebnis der konfigurierten Erkennungsfelder aus.</td>
      <td>Mittelstufe</td>
    </tr>
    <tr>
      <td>Wiederverwendbare SOPAS-Hilfsfunktion</td>
      <td>Erstellen Sie eine Hilfsfunktion zum Senden von SOPAS-Befehlen.</td>
      <td>Mittelstufe</td>
    </tr>
  </tbody>
</table>

<br>

## Bevor Sie beginnen

Stellen Sie sicher, dass das LiDAR-Starter-Kit angeschlossen ist und von Ihrem Computer aus erreichbar ist.

Möglicherweise müssen Sie die folgenden Werte in den Code-Beispielen anpassen:

```python
HOST = "192.168.0.1"
PORT = 2111
```

!!! note "Netzwerkeinstellungen"
    Die IP-Adresse kann je nach Konfiguration Ihres Sensors variieren.  
    Überprüfen Sie die Netzwerkeinstellungen Ihres LiDAR-Starter-Kits, bevor Sie den Code ausführen.

!!! info "Code-Beispiele"
    Die folgenden Codeausschnitte sind für erste Tests und zu Lernzwecken gedacht.  
    Für vollständige Anwendungen verwenden Sie bitte die Projektdateien von GitHub.com oder passen Sie die Beispiele an Ihre eigenen Anforderungen an.

---

## Beispiel 1: Gerätetyp auslesen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

In diesem Beispiel wird der Gerätetyp vom LiDAR-Sensor abgefragt.

Dies kann als erster Verbindungstest dienen, um zu prüfen, ob der Sensor von Python aus erreichbar ist.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN DItype\x03"
    sock.sendall(telegram)

    data = sock.recv(1024)

print(f"Received: {data}")
```

<span class="example-label">Expected Result</span>

Wenn die Verbindung funktioniert, gibt das Skript eine Antwort des Sensors aus.

Beispiel:

```text
Received: b'\x02sRA DItype ... \x03'
```

Sollte keine Antwort eingehen, überprüfen Sie bitte Folgendes:

- Sensor-Stromversorgung
- Ethernet-Verbindung
- IP-Adresse des Sensors
- Netzwerkadapter-Einstellungen
- Firewall-Einstellungen

</div>

---

## Beispiel 2: Scandaten einmal lesen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

In diesem Beispiel wird ein Befehl gesendet, um einmalig Scandaten vom LiDAR-Sensor anzufordern.

Hier wird gezeigt, wie man einen SOPAS-Befehl sendet und die entsprechende Antwort empfängt.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN LMDscandata\x03"
    sock.sendall(telegram)

    data = sock.recv(4096)

print(f"Received: {data}")
```

<span class="example-label">Expected Result</span>

Das Terminal gibt eine Antwort mit den Scandaten des Sensors aus.

Die Antwort kann länger sein als die Antwort auf die Abfrage zum Gerätetyp.

!!! note "Puffergröße"
    Sollte die Antwort unvollständig sein, erhöhen Sie die Puffergröße in `recv()`, beispielsweise von `4096` auf einen größeren Wert.

</div>

---

## Beispiel 3: Scandaten kontinuierlich einlesen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

Dieses Beispiel ermöglicht die kontinuierliche Ausgabe von Scandaten vom LiDAR-Sensor.

Das Skript hält die TCP-Verbindung offen und gibt eingehende Scandaten wiederholt aus.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    # Enable continuous scan data output
    sock.sendall(b"\x02sEN LMDscandata 1\x03")

    while True:
        data = sock.recv(4096)
        print(data)
```

<span class="example-label">Expected Result</span>

Das Terminal gibt die vom Sensor empfangenen Scandaten fortlaufend aus.

Beenden Sie das Skript mit:

```text
CTRL + C
```

!!! warning "Kontinuierliche Ausgabe"
    Daten aus kontinuierlichen Scans können eine große Datenmenge erzeugen.  
    Verwenden Sie Filter-, Parsing- oder Protokollierungsfunktionen, wenn Sie die Daten in einer anderen Anwendung verarbeiten möchten.

</div>

---

## Beispiel 4: Ergebnis der Feldauswertung lesen

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

In diesem Beispiel wird das aktuelle Auswertungsergebnis des LiDAR-Sensors ausgelesen.

Es eignet sich für Anwendungen wie beispielsweise:

- Der Boden ist Lava
- Menschliches Klavier / Luftklavier
- Erkennung von Feldverletzungen
- Trigger- oder Rückkopplungslogik

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    telegram = b"\x02sRN FieldEvaluationResult\x03"
    sock.sendall(telegram)

    data = sock.recv(4096).decode("ascii")

print(f"Field evaluation result: {data}")
```

<span class="example-label">Expected Result</span>

Das Terminal gibt die aktuelle Antwort auf die Feldauswertung aus.

Typische Werte in der Antwort können Aufschluss darüber geben, ob ein Feld verletzt ist oder nicht.

Zum Beispiel:

- `2` kann darauf hinweisen, dass ein Feld nicht verletzt wird
- `4` kann darauf hinweisen, dass ein Feld verletzt wird

!!! warning "Antwortformat"
    Die genaue Position der Feldwerte hängt von der Feldkonfiguration ab.  
    Drucken Sie zunächst die vollständige Antwort aus und ermitteln Sie die relevanten Stellen, bevor Sie das Ergebnis analysieren.

</div>

---

## Beispiel 5: Wiederverwendbare SOPAS-Hilfsfunktion

<div class="code-example-box" markdown>

<span class="example-label">Purpose</span>

Bei umfangreicheren Skripten kann es sinnvoll sein, eine Hilfsfunktion zum Senden von SOPAS-Befehlen zu erstellen.

Dadurch wird vermieden, dass die Einrichtung der Socket-Verbindung und die Formatierung der Telegramme in jedem Beispiel wiederholt werden müssen.

<span class="example-label">Code</span>

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

def send_sopas_command(command):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(2)
        sock.connect((HOST, PORT))

        telegram = b"\x02" + command.encode("ascii") + b"\x03"
        sock.sendall(telegram)

        response = sock.recv(4096).decode("ascii").strip("\x02\x03")

    return response

device_type = send_sopas_command("sRN DItype")
print("Device type:", device_type)

field_result = send_sopas_command("sRN FieldEvaluationResult")
print("Field evaluation:", field_result)
```

<span class="example-label">Expected Result</span>

Das Skript gibt die angeforderten Sensorwerte aus.

Beispiel:

```text
Device type: ...
Field evaluation: ...
```

!!! tip "Wann sollte dieser Helfer verwendet werden?"
    Dieser Helfer eignet sich für einfache Request-Response-Beispiele.  
    Bei kontinuierlichen Anwendungen sollten Sie in Erwägung ziehen, die Socket-Verbindung offen zu halten, anstatt für jeden Befehl eine neue Verbindung herzustellen.

</div>

---

<div class="faq-page"markdown>

## Fehlerbehebung

??? question "Das Skript kann keine Verbindung zum Sensor herstellen. Was sollte ich überprüfen?"

    Bitte überprüfen Sie die folgenden Punkte:

    - Der LiDAR-Sensor wird mit Strom versorgt
    - Das Ethernet-Kabel ist angeschlossen.
    - Der richtige Netzwerkadapter ist konfiguriert.
    - Die IP-Adresse des Computers liegt im gleichen Bereich wie die des Sensors.
    - Die IP-Adresse des Sensors im Skript ist korrekt.
    - Keine Firewall blockiert die Verbindung

---

??? question "Das Skript erhält keine Daten. Was kann ich tun?"

    Stellen Sie sicher, dass der richtige Befehl verwendet wird und dass der Sensor die angeforderten Daten unterstützt.

    Siehe auch:

    - Der Sensor ist im Browser erreichbar.
    - Der Befehl ist korrekt geschrieben.
    - Die Start- und Endzeichen `\x02` und `\x03` sind enthalten
    - Der Empfangspuffer ist groß genug

---

??? question "Die Ausgabe ist schwer zu lesen. Wie kann ich sie aufbereiten?"

    SOPAS-Antworten werden häufig als textbasierte Telegramme zurückgesendet.

    Sie können die empfangenen Daten dekodieren und aufteilen:

    ```python
    response = data.decode("ascii")
    parts = response.split(" ")
    print(parts)
    ```

    Dies kann Ihnen dabei helfen, relevante Werte in der Antwort zu identifizieren.

---

??? question "Das Skript bricht beim kontinuierlichen Einlesen von Scandaten ab. Was kann ich verbessern?"

    Bei einer kontinuierlichen Ausgabe können viele Meldungen entstehen.

    Versuchen Sie Folgendes:

    - die Größe des Empfangspuffers erhöhen
    - Fehlerbehandlung hinzufügen
    - nur relevante Daten verarbeiten
    - Vermeiden Sie es, jede vollständige Antwort auszugeben, wenn die Ausgabe zu umfangreich ist.
    - Den Socket offen halten, anstatt immer wieder eine neue Verbindung herzustellen

</div>

---

## Zusammenfassung

Auf dieser Seite wurden grundlegende Python-Code-Beispiele für das LiDAR-Starter-Kit vorgestellt.

Sie haben gelernt, wie man:

- Mit Python eine Verbindung zum LiDAR-Sensor herstellen
- Gerätetyp abfragen
- Scandaten einmal lesen
- Scandaten kontinuierlich empfangen
- Ergebnisse der Feldauswertung lesen
- Verwenden Sie eine wiederverwendbare SOPAS-Hilfsfunktion

Diese Beispiele können als Bausteine für Ihre eigenen LiDAR-Anwendungen und Beispielprojekte dienen.

---

## Nächste Schritte

Fahren Sie mit den LiDAR-Beispielprojekten oder fortgeschrittenen Themen fort.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[Feldbewertung](./lidar_field_evaluation.md){ .md-button }

[Fortgeschritten](./lidar_advanced.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>