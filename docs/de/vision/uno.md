<!-- # UNO-Kartenspiel

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
      <td>Erkenne und klassifiziere UNO-Spielkarten und entwickle eine Strategie, um gegen den Computer zu spielen.</td>
      <td>Fortgeschrittene/Experten</td>
      <td>4–8 Stunden</td>
      <td>UNO-Spielkarten</td>
    </tr>
  </tbody>
</table>

![UNO](../images/Uno.jpg)

## Welches Problem muss gelöst werden?
Spielkarten sollen automatisch erkannt werden, damit ein klassisches Kartenspiel wie UNO oder Mau-Mau gegen den Computer gespielt werden kann. Kartenfarbe, Wert und Sonderkarten müssen zuverlässig erkannt werden.
<br>
<br>
Projektideen:

* Zuverlässige Kartenerkennung, selbst wenn die Karten leicht gedreht sind
* Regelbasierte Spielelogik für UNO oder Mau-Mau
* Spiele gegen den Computer
* Mehrspieler

## Beispiel für eine Konfigurationsdatei

[UNO-Konfiguration.zip](../files/configuration_nova_inspector_uno.ncfg)


-->


# UNO-Kartenspiel

## Kurzbeschreibung

Im Mittelpunkt dieses fortgeschrittenen Projekts steht die Erkennung und Klassifizierung von UNO-Spielkarten mithilfe des Vision Starter Kits.

Das Ziel besteht darin, Kartenfarben, Zahlen und Sonderkarten zu erkennen und anhand des Klassifizierungsergebnisses eine einfache Spiellogik zu entwickeln, um UNO oder ein ähnliches Kartenspiel gegen den Computer zu spielen.

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
      <td>Fortgeschrittenenprojekt</td>
      <td>Fortgeschritten bis Experte</td>
      <td>4 bis 8 Stunden</td>
      <td>UNO-Spielkarten</td>
    </tr>
  </tbody>
</table>

<br>

![Uno](../images/Uno.jpg)

## Ziel

Das Ziel dieses Projekts ist es, eine Anwendung zur Kartenerkennung zu entwickeln, die UNO-Spielkarten klassifizieren und die erkannten Karten in einer regelbasierten Spiellogik verwenden kann.

Nach Abschluss dieses Projekts sollten Sie wissen, wie Sie:

- UNO-Karten mit dem Vision Starter Kit sortieren
- Kartenfarben und -werte unterscheiden
- Spezialkarten erkennen
- Ergebnisse der Kartenklassifizierung der Spielelogik zuordnen
- die Grundlagen für ein computergestütztes UNO-Spiel schaffen

---

## Projektkonzept

In diesem Projekt wird das Vision Starter Kit zur Erkennung von UNO-Spielkarten eingesetzt.

Das Klassifizierungsergebnis kann dann von einer externen Anwendung oder der Spielelogik genutzt werden, um zu entscheiden, ob eine Karte ausgespielt werden kann, welche Wirkung eine Sonderkarte hat oder wie der Computer reagieren soll.

Das System sollte relevante Karteneigenschaften erkennen, wie zum Beispiel:

- Kartenfarbe
- Kartennummer
- besonderer Kartentyp
- Ungültige oder unbekannte Karte

Mögliche Spielvarianten:

- vereinfachte UNO-Logik
- Spielmechanik im Stil von „Mau-Mau“
- Einzelspieler-Modus gegen den Computer
- Multiplayer-Erweiterung

---

## Bevor Sie beginnen

Richten Sie das Vision Starter Kit wie in der Anleitung [Erste Schritte](./vision_getting_started.md) beschrieben ein.


!!! info "Fortgeschrittenenprojekt"
    Dieses Projekt erfordert eine zuverlässige Bildklassifizierung sowie zusätzliche Spielelogik.  
    Grundlegende Erfahrungen mit SICK Nova, KI-Klassifizierung und Programmierlogik sind von Vorteil.

---

## Aufgabe

Erstellen Sie eine Anwendung, die UNO-Spielkarten erkennt und die Informationen zu den erkannten Karten in der Spiellogik verwendet.

Ihre Lösung sollte Folgendes umfassen:

1. Einrichtung der Bildaufnahme für UNO-Karten
2. Einrichtung der KI-Klassifizierung für die Kartenerkennung
3. Definition der relevanten Kartenklassen
4. Trainingsbilder für jede Kartenklasse
5. Regeln zur Interpretation von Kartenfarbe, Zahl und Sonderkarten
6. Rückmeldung oder Darstellung der erkannten Karte
7. Optionale Spiellogik für das Spiel gegen den Computer

---

## Anforderungen

<div class="requirement-box">

<h3>Core Requirements</h3>

<ul>
  <li>Use the <strong>AI Classification</strong> tool in SICK Nova.</li>
  <li>Detect UNO cards reliably.</li>
  <li>Classify at least a selected subset of cards.</li>
  <li>Distinguish relevant card properties such as color, number or special card type.</li>
  <li>Provide a useful output for the detected card.</li>
  <li>Use the classification result in a simple game logic.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optional Extensions</h3>

<ul>
  <li>Implement the full UNO rule logic.</li>
  <li>Add a computer opponent.</li>
  <li>Add a multiplayer mode.</li>
  <li>Create a web-based interface.</li>
  <li>Add score tracking.</li>
  <li>Visualize playable cards.</li>
  <li>Add probability or strategy suggestions.</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem allgemeinen Ansatz:

1. Richten Sie das Vision Starter Kit ein.
2. Bereite einen ausgewählten Satz UNO-Karten vor.
3. Erstellen Sie einen leeren Auftrag in SICK Nova.
4. Bildaufnahme konfigurieren.
5. Fügen Sie das Tool **KI-Klassifizierung** hinzu.
6. Kartenklassen definieren.
7. Erfassen Sie Trainingsbilder für jede Klasse.
8. Trainieren Sie das Klassifikationsmodell.
9. Prüfen Sie, ob die Karten zuverlässig erkannt werden.
10. Ordnen Sie die Klassifizierungsergebnisse den Kartenwerten und -farben zu.
11. Füge die grundlegende Spiellogik hinzu.
12. Erweitern Sie die Spiellogik, wenn die Klassifizierung zuverlässig funktioniert.

---

## Mögliche Kurse

Beginnen Sie bei einer ersten Version nicht mit dem kompletten UNO-Kartenspiel.  
Beginnen Sie mit einem reduzierten Kartenset und erweitern Sie das Projekt Schritt für Schritt.

Mögliche erste Klassen:

- rot 1
- rot 2
- blau 1
- blau 2
- grün 1
- gelb 1
- Karte überspringen
- Rückseite der Karte
- zwei Karten ziehen

Für eine fortgeschrittenere Variante können Sie folgende Kategorien unterscheiden:

- alle Farben
- alle Zahlen
- Sonderkarten
- Joker

!!! tip "Fang einfach an"
    Fang zunächst mit nur ein paar Karten an.  
    Sobald die Sortierung zuverlässig funktioniert, füge weitere Farben, Zahlen und Sonderkarten hinzu.

---

## Ideen zur Spielelogik

Nachdem eine Karte erkannt wurde, kann die Anwendung das Ergebnis in einer vereinfachten UNO-Spiellogik verwenden.

Mögliche Logikelemente:

- Prüfe, ob die erkannte Karte mit der aktuellen Farbe übereinstimmt
- Prüfe, ob die erkannte Karte mit der aktuellen Nummer übereinstimmt
- Effekte von Spezialkarten anwenden
- Der Computer soll eine zufällige oder gültige Karte auswählen
- Anzeigen, ob die gespielte Karte gültig ist
- Die aktuelle Karte auf dem Spielbrett aktualisieren

Mögliche Rückmeldungen:

- gültige Karte
- ungültige Karte
- Farbabstimmung
- Zahlenübereinstimmung
- besonderer Kartentrick
- Nächster Spieler ist am Zug

---

## Tipps

??? tip "Tipp 1: Reduzieren Sie die Anzahl der Klassen"
    Beginnen Sie mit einer kleinen Auswahl an Karten.  
    Zu viele Kurse können den ersten Trainingsversuch erschweren.

??? tip "Tipp 2: Farbe und Helligkeit voneinander trennen"
    Überlege dir, ob du vollständige Karten direkt klassifizieren möchtest oder die Logik in die Erkennung von Farbe und Wert aufteilen möchtest.

??? tip "Tipp 3: Achten Sie auf eine einheitliche Beleuchtung"
    UNO-Karten zeichnen sich durch kräftige Farben und glänzende Oberflächen aus.  
    Achten Sie auf eine gleichmäßige Beleuchtung und vermeiden Sie Reflexionen.

??? tip "Tipp 4: Variationen erfassen"
    Erfassungskarten mit geringen Abweichungen bei Position und Drehung.  
    Dadurch kann das Modell Karten zuverlässiger erkennen.

??? tip "Tipp 5: Zuerst die Erkennung lösen, dann die Spielelogik"
    Stellen Sie sicher, dass die Kartenerkennung zuverlässig funktioniert, bevor Sie komplexe Spielregeln hinzufügen.

---

## Beispiel für eine Konfigurationsdatei

Eine vorgefertigte SICK-Nova-Konfigurationsdatei finden Sie hier:

[configuration_nova_inspector_uno.ncfg](../files/configuration_nova_inspector_uno.ncfg){ .md-button .button-small}

---

## Erwartetes Ergebnis

Nach Abschluss dieses Projekts sollte das „Vision Starter Kit“ in der Lage sein, ausgewählte UNO-Spielkarten zu erkennen und deren Klassifizierungsergebnis für eine Spieleanwendung bereitzustellen.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Ausgewählte UNO-Karten werden zuverlässig erkannt
- Die Farben und Werte der Karten können interpretiert werden
- Das Klassifizierungsergebnis kann in der Spielelogik verwendet werden
- Gültige und ungültige Kartenzüge können ausgewertet werden
- Das Konzept lässt sich auf mehr Karten oder komplexere Regeln ausweiten.

---

## Zusammenfassung

In diesem Projekt für Fortgeschrittene haben Sie die KI-Klassifizierung auf einen Anwendungsfall im Bereich Kartenspiele angewendet.

Du hast geübt, wie man:

- UNO-Spielkarten klassifizieren
- Nützliche Kartenklassen definieren
- ein KI-Klassifikationsmodell trainieren und testen
- Klassifizierungsergebnisse auswerten
- Kartenerkennung mit regelbasierter Spielelogik verknüpfen
- ein bildverarbeitungsbasiertes Projekt zu einer interaktiven Anwendung ausbauen

Dieses Projekt veranschaulicht, wie sich das Vision Starter Kit nutzen lässt, um Objektklassifizierung mit anwendungsspezifischer Entscheidungslogik zu kombinieren.

---

## Nächste Schritte

Fahren Sie mit einem weiteren Vision-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>