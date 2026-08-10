<!-- # Einfache Feldauswertung
<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Kurzbeschreibung</th>
      <th style="padding: 8px; text-align: left;">Erforderliches Wissensniveau</th>
      <th style="padding: 8px; text-align: left;">Voraussichtliche Dauer</th>
      <th style="padding: 8px; text-align: left;">Zusätzliche Hardware- und Softwareanforderungen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Zeichne ein oder mehrere Felder und übergreife sie mit Objekten unterschiedlicher Größe</td>
      <td>Grundlagen</td>
      <td>10–30 Minuten</td>
      <td>Testobjekte</td>
    </tr>
  </tbody>
</table>

Schließen Sie Ihr Gerät wie unter [Erste Schritte](./lidar_getting_started.md) beschrieben an.

Wählen Sie links **Feldauswertung** aus und zeichnen Sie ein Feld vor dem Gerät ein.

Legen Sie die Parameter für einen Feldverstoß fest (Objektgröße und Verweildauer im Feld).

Wählen Sie verschiedene Testobjekte aus, um zu prüfen, ob das Feld verletzt wird.

Mögliche Aufgaben:

- Versuchen Sie, die Parameter so einzustellen, dass der Bereich nur dann überschritten wird, wenn Sie ein DIN-A4-Blatt horizontal, nicht jedoch vertikal halten.
- Versuchen Sie, die Parameter so einzustellen, dass eine Hand ein Feld nicht verletzt, ein Arm oder der Körper jedoch schon. 

-->


# Einfache Feldauswertung

## Kurzbeschreibung

Dieses angeleitete Projekt bietet eine Einführung in die Funktion **Feldauswertung** des LiDAR-Starter-Kits.

Sie werden ein oder mehrere Erfassungsfelder vor dem LiDAR-Sensor anlegen und untersuchen, wie verschiedene Objekte diese Felder je nach ihrer Größe, Position und Verweildauer im Feld durchdringen.

## Projektinformationen

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Projektart</th>
      <th style="padding: 8px; text-align: left;">Erforderliches Wissensniveau</th>
      <th style="padding: 8px; text-align: left;">Voraussichtliche Dauer</th>
      <th style="padding: 8px; text-align: left;">Zusätzliche Hardware- und Softwareanforderungen</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><span class="project-badge guided">Betreutes Projekt</span></td>
      <td>Grundlagen</td>
      <td>10 bis 30 Minuten</td>
      <td>Testobjekte</td>
    </tr>
  </tbody>
</table>

## Ziel

Ziel dieses Projekts ist es, zu verstehen, wie die Feldauswertung mit dem LiDAR-Starter-Kit funktioniert.

Nach Abschluss dieses Projekts sollten Sie in der Lage sein:

- Öffnen Sie die Benutzeroberfläche des LiDAR-Sensors
- Ein Erkennungsfeld erstellen
- Parameter für Feldverletzungen konfigurieren
- verschiedene Objekte auf dem Spielfeld testen
- verstehen, wie die Größe des Objekts und die Verweildauer im Feld das Ergebnis beeinflussen

---

## Bevor Sie beginnen

Schließen Sie Ihr LiDAR-Starter-Kit wie in der Anleitung [Erste Schritte](./lidar_getting_started.md) beschrieben an.

!!! tip "Empfohlene erste LiDAR-Demo"
    „Field Evaluation“ ist eine gute erste praktische Übung nach Abschluss des LiDAR-Einführungsleitfadens.  
    So können Sie besser verstehen, wie der LiDAR-Sensor bestimmte Bereiche überwachen kann.

---

## Anleitung

Befolgen Sie die folgenden Schritte, um Ihre erste Feldauswertungskonfiguration zu erstellen und zu testen.

---

## 1. Bewertung im Freiland

1. Öffnen Sie die Benutzeroberfläche des LiDAR-Sensors in Ihrem Browser.
2. Stellen Sie sicher, dass der Sensor angeschlossen und erreichbar ist.
3. Wählen Sie auf der linken Seite der Benutzeroberfläche die Option **Feldauswertung** aus.
4. Überprüfen Sie, ob die Live-Messdaten angezeigt werden.

---

## 2. Zeichnen Sie ein Erkennungsfeld

1. Zeichnen Sie vor dem Gerät ein Feld ein.
2. Platzieren Sie das Feld an einer Stelle, an der Sie Objekte erkennen möchten.
3. Stellen Sie sicher, dass das Feld groß genug für Ihr erstes Testobjekt ist.
4. Speichern oder übernehmen Sie die Feldkonfiguration, falls dies von der Benutzeroberfläche verlangt wird.

!!! tip "Fang einfach an"
    Fang zunächst mit einem großen Feld an.  
    Nach den grundlegenden Feldauswertungsarbeiten können Sie kleinere oder spezifischere Felder anlegen.

---

## 3. Parameter für Feldverstöße konfigurieren

Legen Sie die Parameter fest, anhand derer bestimmt wird, wann ein Feld als verletzt gilt.

Zu den wichtigen Parametern können gehören:

- Objektgröße
- Zeit auf dem Spielfeld
- Position innerhalb des Feldes
- Feldform
- Feldempfindlichkeit

Die genauen Parameternamen können je nach Sensorkonfiguration und Softwareversion variieren.

!!! note "Verhalten der Parameter"
    Ein Feldverstoß hängt nicht nur davon ab, ob ein Objekt in das Feld eindringt.  
    Die eingestellte Objektgröße und die im Feld angegebene Zeit können ebenfalls das Ergebnis beeinflussen.

---

## 4. Testen Sie verschiedene Objekte

Verwenden Sie verschiedene Testobjekte, um das Verhalten im Feld zu überprüfen.

Beispiele:

- Blatt Papier
- Hand
- Arm
- Körper
- kleine Schachtel
- größeres Objekt

Platzieren Sie die Objekte auf dem Feld und beobachten Sie, ob das Feld verletzt wird.

---

## 5. Passen Sie die Feldeinstellungen an

Passen Sie die Feldeinstellungen so lange an, bis das Verhalten Ihrem Anwendungsfall entspricht.

Mögliche Testaufgaben:

- Stellen Sie die Parameter so ein, dass der Bereich nur dann überschritten wird, wenn Sie ein DIN-A4-Blatt quer, nicht aber längs halten.
- Stellen Sie die Parameter so ein, dass eine Hand das Feld nicht verletzt, ein Arm oder der Körper jedoch schon
- Erstellen Sie ein kleineres Feld und testen Sie, wie genau der Sensor die Positionen von Objekten erfasst.
- Mehrere Felder erstellen und deren Verhalten vergleichen

---

## Erwartetes Ergebnis

Nach Abschluss dieses Projekts sollte das LiDAR-Starter-Kit erkennen, wenn Objekte in einen definierten Bereich eindringen.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Das Erfassungsfeld ist korrekt konfiguriert.
- Testobjekte können innerhalb des Feldes erkannt werden
- Die Größe und Position des Objekts beeinflussen das Messergebnis
- Die Feldparameter können an verschiedene Szenarien angepasst werden

---

## Zusammenfassung

In diesem angeleiteten Projekt haben Sie gelernt, wie Sie mit dem LiDAR-Starter-Kit Erkennungsfelder erstellen und testen können.

Du hast geübt, wie man:

- Öffnen Sie die Funktion „Feldauswertung“
- Ein Erkennungsfeld zeichnen
- Parameter für Feldverletzungen konfigurieren
- verschiedene Objekte testen
- das Verhalten des Feldes an verschiedene Anwendungsfälle anpassen

Dieses Projekt ist die empfohlene erste praktische Demo für das LiDAR-Starter-Kit.

---

## Nächste Schritte

Fahren Sie mit einem weiteren LiDAR-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>