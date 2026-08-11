<!-- # Entfernungsschätzung

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
      <td>Schätzen Sie die Entfernung zu einem Objekt und messen Sie diese mit einem LiDAR-Sensor.</td>
      <td>Grundlagen</td>
      <td>1–2 Stunden</td>
      <td>Beliebige Objekte</td>
    </tr>
  </tbody>
</table>

![Entfernungsschätzung](../images/distance_estimation.png)

## Welches Problem muss gelöst werden?
Die Einschätzung von Entfernungen durch Menschen und das räumliche Gedächtnis sollen anhand von 3D-Sensordaten in einem spielerischen Rahmen untersucht werden.

Projektideen:

* Präzise Entfernungsmessung mit 3D-Sensor
* Spiel-Dashboard, das zufällig einen bestimmten Entfernungswert generiert
* Abweichungsanalyse und Dashboard

## Beispiel-Projektdatei

[DistanceEstimation.Zip](../files/distance_estimation.zip)

-->


# Entfernungsschätzung

## Kurzbeschreibung

Im Mittelpunkt dieses Projektes steht das Schätzen und Messen von Entfernungen mit dem LiDAR-Starter-Kit.

Das Ziel ist es, eine spielerische Situation zu schaffen, in der die Nutzer die Entfernung zu einem Objekt schätzen und ihre Schätzung mit der gemessenen LiDAR-Entfernung vergleichen.

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
      <td><span class="project-badge challenge">Challenge-Projekt</span></td>
      <td>Grundlagen</td>
      <td>1 bis 2 Stunden</td>
      <td>Beliebige Objekte</td>
    </tr>
  </tbody>
</table>

<br>

![Entfernungsschätzung](../images/distance_estimation.png)

## Ziel der Herausforderung

Ziel dieses Projekts ist es, die Entfernungsschätzung durch Menschen anhand von LiDAR-Messdaten zu bewerten.

Die Benutzer sollen die Entfernung zu einem Objekt schätzen, während der LiDAR-Sensor die gemessene Entfernung liefert. Die Differenz zwischen Schätzung und Messwert kann dann angezeigt oder analysiert werden.

Im Gegensatz zu einem angeleiteten Projekt wird bei dieser Aufgabe keine vollständige Schritt-für-Schritt-Lösung bereitgestellt. Nutze dein Wissen aus früheren Projekten mit dem LiDAR-Starter-Kit, um deinen eigenen Ansatz zu entwickeln.

---

## Problemstellung

Die Einschätzung von Entfernungen durch Menschen kann ungenau sein, insbesondere wenn keine Bezugspunkte vorhanden sind.

Mit dem LiDAR-Starter-Kit lassen sich Entfernungen messen und mit dem vom Benutzer geschätzten Wert vergleichen.

Mögliche Ziele:

- die Entfernung zu einem Objekt messen
- geschätzte und gemessene Entfernung vergleichen
- die Abweichung berechnen
- das Ergebnis in einem Dashboard visualisieren
- Entwickle ein kleines Spiel, bei dem es um die Schätzung von Entfernungen geht

---

## Aufgabe

Entwickeln Sie eine Anwendung, die die Entfernung zu einem Objekt misst und diese mit der Schätzung des Benutzers vergleicht.

Ihre Lösung sollte Folgendes umfassen:

1. Ein festgelegter Messaufbau
2. Ein oder mehrere Testobjekte
3. Ein Verfahren zum Ablesen oder Anzeigen der gemessenen Entfernung
4. Eine Möglichkeit für Benutzer, ihre geschätzte Entfernung einzugeben oder auszuwählen
5. Berechnung der Abweichung zwischen Schätzung und Messwert
6. Optionale Darstellung des Ergebnisses

---

## Anforderungen

<div class="requirement-box">

<h3>Core Requirements</h3>

<ul>
  <li>Use the LiDAR Starter Kit to measure the distance to an object.</li>
  <li>Place a test object in front of the sensor.</li>
  <li>Read or display the measured distance value.</li>
  <li>Allow the user to estimate the distance.</li>
  <li>Compare the estimated distance with the measured distance.</li>
  <li>Calculate the deviation between estimation and measurement.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optional Extensions</h3>

<ul>
  <li>Create a dashboard for displaying the measured and estimated values.</li>
  <li>Generate random target distances for a game mode.</li>
  <li>Add a score based on estimation accuracy.</li>
  <li>Track multiple rounds or multiple players.</li>
  <li>Visualize the deviation as a bar, percentage or color indicator.</li>
  <li>Use different objects and compare measurement behavior.</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem Vorgehen:

1. Richten Sie das LiDAR-Starter-Kit ein.
2. Platzieren Sie einen Gegenstand in sichtbarer Entfernung vor dem Sensor.
3. Öffnen Sie die Benutzeroberfläche des Sensors oder verwenden Sie ein Skript, um die Messdaten auszulesen.
4. Der Benutzer soll die Entfernung zum Objekt schätzen.
5. Lesen Sie die vom Sensor gemessene Entfernung ab.
6. Berechne die Differenz zwischen der geschätzten und der gemessenen Entfernung.
7. Zeige das Ergebnis an.
8. Wiederholen Sie den Vorgang mit unterschiedlichen Abständen oder Objekten.

---

## Projektideen

Je nach den vorhandenen Voraussetzungen und Ihren Programmierkenntnissen können Sie die Aufgabe auf unterschiedliche Weise umsetzen.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Simple Measurement</h3>
    <p>Place an object in front of the LiDAR sensor and read the measured distance.</p>
    <p>This is the easiest version and can be used to understand the basic measurement behavior.</p>
  </div>

  <div class="strategy-card">
    <h3>Estimation Game</h3>
    <p>Let a user estimate the distance to an object before revealing the measured value.</p>
    <p>The result can be scored based on how close the estimation was to the real measurement.</p>
  </div>

  <div class="strategy-card">
    <h3>Random Target Distance</h3>
    <p>Generate a random target distance and ask the user to place an object as close as possible to that distance.</p>
    <p>The LiDAR sensor can then measure the actual distance and calculate the deviation.</p>
  </div>

  <div class="strategy-card">
    <h3>Dashboard Visualization</h3>
    <p>Create a simple dashboard that shows estimated distance, measured distance and deviation.</p>
    <p>This can make the project more interactive and easier to understand during demonstrations.</p>
  </div>

</div>

---

## Tipps

??? tip "Tipp 1: Beginne mit einem Objekt"
    Beginnen Sie mit einem einzelnen Objekt und einer festen Sensorposition.  
    Sobald die Messung zuverlässig funktioniert, testen Sie verschiedene Objekte und Entfernungen.

??? tip "Tipp 2: Verwenden Sie klare Messbedingungen"
    Stellen Sie sicher, dass das Objekt für den LiDAR-Sensor sichtbar ist und sich nicht zu nahe am Sensor befindet.

??? tip "Tipp 3: Trenne die Messung von der Spielelogik"
    Vergewissern Sie sich zunächst, dass die Entfernungsmessung funktioniert.  
    Fügen Sie anschließend Schätz-, Bewertungs- oder Dashboard-Logik hinzu.

??? tip "Tipp 4: Mehrere Runden vergleichen"
    Lassen Sie die Benutzer die Schätzung mehrmals wiederholen und eine durchschnittliche Abweichung berechnen.

??? tip "Tipp 5: Verwenden Sie bei Bedarf Code-Beispiele"
    Wenn Sie Messdaten mit Python auslesen möchten, sehen Sie sich die LiDAR-Code-Beispiele an.

    [LiDAR-Beispielcodes](./lidar_code_snippets.md){ .md-button .button-small }

---

## Beispiel-Projektdatei

Eine vorgefertigte Beispielprojektdatei finden Sie hier:

[Entfernungsschätzung](../files/distance_estimation.zip){ .md-button .button-small }

---

## Erwartetes Ergebnis

Nach Abschluss dieser Aufgabe sollte das LiDAR-Starter-Kit in der Lage sein, die Entfernung zu einem Objekt zu messen und diese mit der vom Benutzer geschätzten Entfernung zu vergleichen.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Das Objekt wird vom LiDAR-Sensor erkannt.
- Die gemessene Entfernung kann abgelesen oder angezeigt werden
- Die vom Benutzer geschätzte Größe kann mit dem Messwert verglichen werden.
- Die Abweichung lässt sich berechnen
- Das Projekt lässt sich zu einem kleinen interaktiven Spiel oder einem Dashboard ausbauen.

---

## Zusammenfassung

In diesem Challenge-Projekt haben Sie das LiDAR-Starter-Kit verwendet, um Entfernungen zu messen und diese mit den Schätzungen von Menschen zu vergleichen.

Du hast geübt, wie man:

- Objektabstand mit LiDAR messen
- Messergebnisse auswerten
- Abweichungen berechnen
- eine spielerische Vorrichtung zur Entfernungsmessung bauen
- Sensordaten in eine einfache interaktive Anwendung integrieren

Dieses Projekt eignet sich gut, um das Messverhalten von LiDAR zu verstehen und Sensordaten in eine interaktive Demo umzusetzen.

---

## Nächste Schritte

Fahren Sie mit einem weiteren LiDAR-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button}

</div>