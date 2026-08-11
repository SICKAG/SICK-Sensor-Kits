<!-- # Darts

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
      <td>Analysiere die auf eine Dartscheibe geworfenen Darts und entwickle eine Logik für verschiedene Spiele.</td>
      <td>Fortgeschritten</td>
      <td>4 Stunden</td>
      <td>Klett-Dartscheibe mit Klettbällen</td>
    </tr>
  </tbody>
</table>

![Darts](../images/darts.jpg)

## Welches Problem muss gelöst werden?
Die Treffposition der „Darts“ (Klettbälle) auf der Dartscheibe muss automatisch erkannt werden, um die Punktestände zu berechnen und den Spielverlauf anzuzeigen.

Projektideen:

* Erkennung der Trefferposition des Darts
* Punkteberechnung nach den Regeln des Dartspiels
* Verschiedene Spielmodi
* Rundungs- und Beinarbeit
* Mehrspieler

-->

# Darts

## Kurzbeschreibung

Im Mittelpunkt dieses Challenge-Projekts steht die Erkennung der Treffposition von Klettbällen auf einer Dartscheibe mithilfe des Vision Starter Kits.

Das Ziel besteht darin, das Bild der Dartscheibe zu analysieren, festzustellen, wo die Kugel gelandet ist, und anhand dieser Informationen die Punktzahlen für verschiedene Dartspielmodi zu berechnen.

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
      <td>Fortgeschritten</td>
      <td>4 Stunden</td>
      <td>Klett-Dartscheibe mit Klett-Darts</td>
    </tr>
  </tbody>
</table>

<br>

![Darts](../images/darts.jpg)

## Ziel der Herausforderung

Das Ziel dieses Projekts ist die Entwicklung einer „Vision Starter Kit“-Anwendung, die automatisch die Trefferposition von Klettbällen auf einer Dartscheibe erkennt.

Die ermittelte Position sollte dann zur Berechnung der Punktestände und zur Anzeige des Spielverlaufs eines Dartspiels verwendet werden.

Im Gegensatz zu einem angeleiteten Projekt wird bei dieser Aufgabe keine vollständige Schritt-für-Schritt-Lösung bereitgestellt. Nutzen Sie Ihr Wissen aus früheren Vision Starter Kit-Projekten, um Ihren eigenen Ansatz zu entwickeln.

---

## Problemstellung

!!! tip 
    Die Treffposition eines Klettballs auf einer Dartscheibe sollte automatisch erkannt werden.

Auf der Grundlage der ermittelten Position sollte das System die entsprechende Punktzahl berechnen und Informationen zum aktuellen Spielstand bereitstellen.

Mögliche Ziele:

- Erkennen, ob ein Dart die Dartscheibe getroffen hat
- die Treffposition ermitteln
- die Trefferposition einem Punktfeld zuweisen
- die aktuelle Punktzahl berechnen
- Runden oder Etappen aufzeichnen
- verschiedene Spielmodi unterstützen
- mehrere Spieler unterstützen

---

## Aufgabe

Erstellen Sie eine Anwendung, die eine Dartscheibe analysiert und anhand der erkannten Trefferposition die Punktzahl berechnet.

Ihre Lösung sollte Folgendes umfassen:

1. Aufbau zur Bildaufnahme für die Dartscheibe
2. Stabile Positionierung der Dartscheibe im Kamerabild
3. Erkennung des Klettverschlussballs
4. Zuordnung der ermittelten Trefferposition zu einem Punktwert
5. Logik zur Punkteberechnung
6. Optionale Darstellung des Spielverlaufs

---

## Anforderungen

<div class="requirement-box">

<h3>Core Requirements</h3>

<ul>
  <li>Use the Vision Starter Kit to observe the dartboard.</li>
  <li>Detect the Velcro ball reliably.</li>
  <li>Identify the approximate hit position.</li>
  <li>Map the hit position to a score area.</li>
  <li>Calculate the score based on the dartboard logic.</li>
  <li>Provide feedback about the current score or game state.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optional Extensions</h3>

<ul>
  <li>Different game modes</li>
  <li>Round and leg calculation</li>
  <li>Multiplayer mode</li>
  <li>Score history</li>
  <li>Dashboard for visualization</li>
  <li>Automatic reset after each throw</li>
  <li>Difficulty levels or training mode</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem allgemeinen Ansatz:

1. Richten Sie das Vision Starter Kit ein.
2. Platzieren Sie die Dartscheibe im Sichtfeld des Sensors.
3. Bildaufnahme konfigurieren.
4. Achte darauf, dass die Dartscheibe im Bild gut sichtbar und stabil steht.
5. Erkenne den Klettball nach einem Wurf.
6. Bestimmen Sie die Trefferposition relativ zur Dartscheibe.
7. Lege die Punktzonen für das Spielbrett fest.
8. Ordne die erfasste Position einem Punktwert zu.
9. Logik zur Punkteberechnung hinzufügen.
10. Erweitern Sie die Anwendung um Visualisierungs- oder Spielmodi.

---

## Mögliche Erkennungsstrategien

Es gibt verschiedene Möglichkeiten, diese Herausforderung zu meistern.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Object Detection</h3>
    <p>Detect the Velcro ball as an object in the camera image.</p>
    <p>Best suited if the ball has a clearly visible color or texture compared to the dartboard.</p>
  </div>

  <div class="strategy-card">
    <h3>Color-Based Detection</h3>
    <p>Use color differences between the Velcro ball and the dartboard.</p>
    <p>Useful if the ball has strong contrast and stable lighting.</p>
  </div>

  <div class="strategy-card">
    <h3>Position Mapping</h3>
    <p>Define fixed regions on the dartboard image and map the detected hit position to these regions.</p>
    <p>Works best if the dartboard remains in a fixed position.</p>
  </div>

</div>
---

## Ideen zur Spielelogik

Nachdem die Trefferposition ermittelt wurde, kann die Anwendung die Punktzahl berechnen und den Spielstand verfolgen.

Mögliche Logikelemente:

- Punktzahl für einen Wurf berechnen
- Punkte aus mehreren Würfen zusammenzählen
- Laufbahn-Spieler dreht sich
- Runden oder Etappen berechnen
- Ungültige Ausnahmen erkennen
- verschiedene Spielmodi unterstützen

Mögliche Rückmeldungen:

- Aktueller Wurfwert
- Aktuelle Gesamtpunktzahl
- aktiver Spieler
- verbleibende Punktzahl
- Rundenergebnis
- Gewinneranzeige

---

## Tipps

??? tip "Tipp 1: Halte die Dartscheibe fest"
    Versuchen Sie, die Dartscheibe in einer festen Position zu halten.  
    Eine stabile Brettposition erleichtert das Erstellen von Punktetabellen erheblich.

??? tip "Tipp 2: Beginnen Sie mit einfachen Zonen"
    Teilen Sie das Spielfeld zunächst in nur wenige größere Zonen auf.  
    Sobald dies zuverlässig funktioniert, erhöhen Sie den Detaillierungsgrad.

??? tip "Tipp 3: Verwenden Sie einen hohen Kontrast"
    Verwenden Sie einen Klettball, der sich deutlich vom Hintergrund der Dartscheibe abhebt.  
    Dies kann die Erkennung vereinfachen.

??? tip "Tipp 4: Erkennung und Bewertung voneinander trennen"
    Stellen Sie zunächst sicher, dass die Treffposition zuverlässig erkannt wird.  
    Fügen Sie anschließend die Logik zur Punkteberechnung hinzu.

??? tip "Tipp 5: Nutzen Sie frühere Klassifizierungsprojekte als Referenz"
    Wenn Sie sich nicht sicher sind, wie Sie das KI-Klassifizierungstool verwenden sollen, sehen Sie sich das [Beispielprojekt mit Anleitung](./classify_hex_nuts_screws.md) noch einmal an.

---

## Erwartetes Ergebnis

!!! success  
    Nach Abschluss dieser Aufgabe sollte das Vision Starter Kit in der Lage sein, die Treffposition eines Klettballs auf der Dartscheibe zu erkennen.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Die Dartscheibe ist im Kamerabild gut zu erkennen und steht stabil.
- Der Klettball wird zuverlässig erkannt
- Die Anschlagposition kann einem Notensystem zugewiesen werden
- Die Punktzahl kann automatisch berechnet werden
- Der Spielfortschritt kann angezeigt oder durch zusätzliche Logik erweitert werden

---

## Zusammenfassung

In diesem Projekt haben Sie die bildverarbeitungsbasierte Erkennung auf einen Anwendungsfall mit einer Dartscheibe angewendet.

Du hast geübt, wie man:

- Objektpositionen in einem Bild erkennen
- Positionen auf vordefinierte Regionen abbilden
- Punktestände auf der Grundlage der erkannten Positionen berechnen
- Bildanalyse mit Spielelogik kombinieren
- ein bildverarbeitungsbasiertes Projekt zu einer interaktiven Spielanwendung ausbauen

Dieses Projekt eignet sich gut als Übung, um die visuelle Erkennung mit einer regelbasierten Bewertungslogik zu verknüpfen.

---

## Nächste Schritte

Zurück zur Projektübersicht oder die vollständigen Projektdateien auf GitHub.com öffnen.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>
