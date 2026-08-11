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

Das Ziel dieses Projekts ist die Entwicklung einer „Vision Starter Kit“-Anwendung, die automatisch die Treffposition von Klettbällen auf einer Dartscheibe erkennt.

Die ermittelte Position sollte dann zur Berechnung der Punktestände und zur Anzeige des Spielverlaufs eines Dartspiels verwendet werden.

Im Gegensatz zu einem angeleiteten Projekt wird bei dieser Aufgabe keine vollständige Schritt-für-Schritt-Lösung bereitgestellt. Nutze dein Wissen aus früheren Vision Starter Kit-Projekten, um deinen eigenen Ansatz zu entwickeln.

---

## Problemstellung

!!! tip 
    Die Treffposition eines Klettballs auf einer Dartscheibe sollte automatisch erkannt werden.

Auf der Grundlage der ermittelten Position sollte das System die entsprechende Punktzahl berechnen und Informationen zum aktuellen Spielstand bereitstellen.

Mögliche Ziele:

- Erkennen, ob ein Dart die Scheibe getroffen hat
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

<h3>Grundlegende Anforderungen</h3>

<ul>
  <li>Verwenden Sie das Vision Starter Kit, um die Dartscheibe zu beobachten.</li>
  <li>Erkennen Sie den Klettball zuverlässig.</li>
  <li>Ermitteln Sie die ungefähre Trefferposition.</li>
  <li>Ordnen Sie die Trefferposition einem Punktebereich zu.</li>
  <li>Berechnen Sie die Punktzahl anhand der Logik der Dartscheibe.</li>
  <li>Geben Sie Feedback zur aktuellen Punktzahl oder zum Spielstand.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optionale Erweiterungen</h3>

<ul>
  <li>Verschiedene Spielmodi</li>
  <li>Runden- und Leg-Berechnung</li>
  <li>Mehrspieler-Modus</li>
  <li>Punktestand-Verlauf</li>
  <li>Dashboard zur Visualisierung</li>
  <li>Automatischer Reset nach jedem Wurf</li>
  <li>Schwierigkeitsstufen oder Trainingsmodus</li>
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
    <h3>Objekterkennung</h3>
    <p>Erkennen Sie den Klettball als Objekt im Kamerabild.</p>
    <p>Am besten geeignet, wenn der Ball im Vergleich zur Dartscheibe eine deutlich erkennbare Farbe oder Struktur aufweist.</p>
  </div>

  <div class="strategy-card">
    <h3>Farbbasierte Erkennung</h3>
    <p>Nutzen Sie Farbunterschiede zwischen dem Klettball und der Dartscheibe.</p>
    <p>Nützlich, wenn der Ball einen starken Kontrast aufweist und die Beleuchtung stabil ist.</p>
  </div>

  <div class="strategy-card">
    <h3>Positionszuordnung</h3>
    <p>Definieren Sie feste Bereiche auf dem Bild der Dartscheibe und ordnen Sie die erkannte Trefferposition diesen Bereichen zu.</p>
    <p>Funktioniert am besten, wenn die Dartscheibe an einer festen Position bleibt.</p>
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
- Ungültige Auswürfe erkennen
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
