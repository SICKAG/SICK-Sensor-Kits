# Entfernungsschätzung

## Kurzbeschreibung

Im Mittelpunkt dieses Projektes steht die Schätzung und Messung von Entfernungen mit dem LiDAR-Starter-Kit.

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

<h3>Grundlegende Anforderungen</h3>

<ul>
  <li>Verwenden Sie das LiDAR-Starter-Kit, um die Entfernung zu einem Objekt zu messen.</li>
  <li>Platzieren Sie ein Testobjekt vor dem Sensor.</li>
  <li>Lesen Sie den gemessenen Entfernungswert ab oder zeigen Sie ihn an.</li>
  <li>Geben Sie dem Benutzer die Möglichkeit, die Entfernung zu schätzen.</li>
  <li>Vergleichen Sie die geschätzte Entfernung mit der gemessenen Entfernung.</li>
  <li>Berechnen Sie die Abweichung zwischen Schätzung und Messung.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optionale Erweiterungen</h3>

<ul>
  <li>Erstellen Sie ein Dashboard zur Anzeige der gemessenen und geschätzten Werte.</li>
  <li>Generieren Sie zufällige Zielentfernungen für einen Spielmodus.</li>
  <li>Fügen Sie eine Wertung basierend auf der Schätzgenauigkeit hinzu.</li>
  <li>Verfolgen Sie mehrere Runden oder mehrere Spieler.</li>
  <li>Visualisieren Sie die Abweichung als Balken, Prozentangabe oder Farbindikator.</li>
  <li>Verwenden Sie verschiedene Objekte und vergleichen Sie das Messverhalten.</li>
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
    <h3>Einfache Messung</h3>
    <p>Platzieren Sie ein Objekt vor dem LiDAR-Sensor und lesen Sie die gemessene Entfernung ab.</p>
    <p>Dies ist die einfachste Variante und dient dazu, das grundlegende Messverhalten zu verstehen.</p>
  </div>

  <div class="strategy-card">
    <h3>Schätzspiel</h3>
    <p>Lassen Sie einen Benutzer die Entfernung zu einem Objekt schätzen, bevor der gemessene Wert angezeigt wird.</p>
    <p>Das Ergebnis kann je nachdem, wie nah die Schätzung am tatsächlichen Messwert lag, bewertet werden.</p>
  </div>

  <div class="strategy-card">
    <h3>Zufällige Zielentfernung</h3>
    <p>Generieren Sie eine zufällige Zielentfernung und bitten Sie den Nutzer, ein Objekt so nah wie möglich an dieser Entfernung zu platzieren.</p>
    <p>Der LiDAR-Sensor kann dann die tatsächliche Entfernung messen und die Abweichung berechnen.</p>
  </div>

  <div class="strategy-card">
    <h3>Visualisierung im Dashboard</h3>
    <p>Erstellen Sie ein einfaches Dashboard, das die geschätzte Entfernung, die gemessene Entfernung und die Abweichung anzeigt.</p>
    <p>Dadurch wird das Projekt interaktiver und bei Vorführungen leichter verständlich.</p>
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