# Black Jack

## Kurzbeschreibung

Im Mittelpunkt dieses fortgeschrittenen Projekts steht die Erkennung und Klassifizierung von Spielkarten mithilfe des Vision Starter Kits.

Das Ziel ist es, eine Blackjack-Anwendung zu entwickeln, die Spielkarten erkennt, den aktuellen Wert der Hand berechnet und eine Rückmeldung gibt, wenn der Wert 21 überschritten wird.

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
      <td><span class="project-badge advanced">Fortgeschrittenes Projekt</span></td>
      <td>Fortgeschritten bis Experte</td>
      <td>4 bis 8 Stunden</td>
      <td>Spielkarten</td>
    </tr>
  </tbody>
</table>

<br>

![Black Jack](../images/blackjack.jpg)

## Ziel

Das Ziel dieses Projekts ist es, eine „Vision Starter Kit“-Anwendung zu entwickeln, die Spielkarten erkennen und die ermittelten Werte in einer einfachen Blackjack-Spiellogik verwenden kann.

Nach Abschluss dieses Projekts sollten Sie wissen, wie man:

- Spielkarten erkennen und klassifizieren
- den erkannten Klassen Kartenwerte zuweisen
- den aktuellen Wert eines Kartenblatts berechnen
- eine Rückmeldung ausgeben, wenn der Wert 21 überschritten wird
- Erweiterung einer bildbasierten Klassifizierungsaufgabe um Anwendungslogik

---

## Projektkonzept

In diesem Projekt wird das Vision Starter Kit zur Klassifizierung von Spielkarten verwendet.

Das Klassifizierungsergebnis kann dann zur Berechnung des aktuellen Blattwerts in einem Blackjack-Spiel herangezogen werden. Auf Grundlage der Spiellogik kann das System anzeigen, ob der aktuelle Wert noch gültig ist oder ob der Wert 21 überschritten wurde.

Zu den möglichen Ausgabeoptionen gehören:

- Ein einfaches visuelles Ergebnis in SICK Nova
- ein Dashboard oder eine externe Anwendung
- eine Signalleuchte
- ein binäres Rückmeldesignal
- eine auf Wahrscheinlichkeiten basierende Empfehlung für die nächste Ziehung

---

## Bevor Sie beginnen

Richten Sie das Vision Starter Kit wie in der Anleitung [Erste Schritte](./vision_getting_started.md) beschrieben ein.


!!! info "Fortgeschrittenenprojekt"
    Dieses Projekt erfordert eine Kombination aus Bildklassifizierung und zusätzlicher Spielelogik.  
    Grundlegende Erfahrungen mit SICK Nova und der Programmierung von Steuerungslogik sind von Vorteil.

---

## Aufgabe

Erstellen Sie eine Anwendung, die Spielkarten erkennt und den aktuellen Wert der Blackjack-Hand berechnet.

Ihre Lösung sollte Folgendes umfassen:

1. Aufbau zur Bildaufnahme von Spielkarten
2. Einrichtung der KI-Klassifizierung für die Kartenerkennung
3. Definition der relevanten Kartenklassen
4. Trainingsbilder für jede Kartenklasse
5. Logik zur Berechnung des aktuellen Handwerts
6. Meldung bei Überschreitung des Wertes 21

---

## Anforderungen

<div class="requirement-box">

<h3>Grundlegende Anforderungen</h3>

<ul>
  <li>Verwenden Sie das <strong>KI</strong>-Klassifizierungstool in SICK Nova.</li>
  <li>Erkennen und klassifizieren Sie Spielkarten zuverlässig.</li>
  <li>Weisen Sie jeder erkannten Karte einen numerischen Wert zu.</li>
  <li>Berechnen Sie den aktuellen Wert des Blattes.</li>
  <li>Erkennen Sie, wenn der Wert 21 überschritten wird.</li>
  <li>Geben Sie je nach Ergebnis visuelles oder logisches Feedback.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optionale Erweiterungen</h3>

<ul>
  <li>Fügen Sie ein Dashboard zur Visualisierung hinzu.</li>
  <li>Verwenden Sie eine Signalleuchte für binäres Feedback.</li>
  <li>Berechnen Sie die Wahrscheinlichkeit, dass der Wert 21 bei der nächsten Ziehung überschritten wird.</li>
  <li>Fügen Sie einen Mehrspieler-Modus hinzu.</li>
  <li>Verfolgen Sie die Karten automatisch über mehrere Runden hinweg.</li>
  <li>Verbinden Sie das Klassifizierungsergebnis mit einer externen Anwendung.</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem allgemeinen Ansatz:

1. Richten Sie das Vision Starter Kit ein.
2. Bereiten Sie ein Kartenspiel vor.
3. Erstellen Sie einen leeren Auftrag in SICK Nova.
4. Bildaufnahme konfigurieren.
5. Fügen Sie das Tool **KI-Klassifizierung** hinzu.
6. Kartenklassen definieren.
7. Erfassen Sie Trainingsbilder für jede Kartenklasse.
8. Trainieren Sie das Klassifikationsmodell.
9. Prüfen Sie, ob die Karten zuverlässig erkannt werden.
10. Exportieren Sie das Klassifizierungsergebnis oder nutzen Sie es.
11. Erstellen Sie eine Logik zur Berechnung des aktuellen Handwerts.
12. Füge Rückmeldungen für gültige und ungültige Spielzustände hinzu.

---

## Mögliche Kurse

Je nach Umfang Ihrer Implementierung können Sie mit einem vereinfachten Kartensatz beginnen.

Verwenden Sie für eine erste Version eine reduzierte Auswahl an Klassen, zum Beispiel:

- Ass
- 2
- 3
- 4
- 5
- 10
- Jack
- Königin
- König

Für eine erweiterte Version können Sie die Klassifizierung auf alle Kartenwerte ausweiten.

!!! tip "Fang einfach an"
    Fangen Sie zunächst mit einem kleineren Kartensatz an.  
    Sobald die Klassifizierung zuverlässig funktioniert, können Sie weitere Kartenwerte hinzufügen.

---

## Spielmechanik

Nach dem Erkennen der Karten sollte die Blackjack-Logik den aktuellen Wert der Hand berechnen.

Zu beachtende Grundregeln:

- Zahlenkarten zählen mit ihrem Zahlenwert
- Bube, Dame und König zählen als 10
- Ein Ass kann je nach aktuellem Wert der Hand als 1 oder 11 gezählt werden.
- Wenn der Gesamtwert 21 übersteigt, ist das Blatt ungültig.

Mögliche Rückmeldungen:

- Der Wert liegt unter 21
- Der Wert beträgt genau 21
- Der Wert ist größer als 21
- Empfehlung, fortzufahren oder anzuhalten
- Wahrscheinlichkeit, dass bei der nächsten Ziehung 21 überschritten wird

---

## Tipps

??? tip "Tipp 1: Verwende zunächst einen reduzierten Kartensatz"
    Fang nicht mit einem vollständigen Kartenspiel an.  
    Wählen Sie einige Karten aus und prüfen Sie, ob die Klassifizierung zuverlässig ist.

??? tip "Tipp 2: Halte die Position der Karte einheitlich"
    Versuchen Sie, die Position der Karte, den Abstand und die Beleuchtung während des Trainings und der Tests so gleichmäßig wie möglich zu halten.

??? tip "Tipp 3: Fügen Sie bei Bedarf weitere Bilder hinzu"
    Sollte die Kartenerkennung unzuverlässig sein, fügen Sie weitere Trainingsbilder mit unterschiedlichen Positionen und Drehungen hinzu.

??? tip "Tipp 4: Trenne Erkennung und Spielelogik"
    Stellen Sie zunächst sicher, dass die Kartenerkennung zuverlässig funktioniert.  
    Fügen Sie anschließend die Berechnungslogik für Black Jack hinzu.

??? tip "Tipp 5: Nutzen Sie das Projekt zur geführten Klassifizierung"
    Wenn Sie sich nicht sicher sind, wie Sie das KI-Klassifizierungstool verwenden sollen, sehen Sie sich das [Beispielprojekt mit Anleitung](./classify_hex_nuts_screws.md) noch einmal an.


---

## Beispiel-Projektdatei

Eine vorgefertigte Beispielprojektdatei finden Sie hier:

[Blackjack.zip](../files/Blackjack.zip){ .md-button .button-small}

---

## Beispiel für eine Konfigurationsdatei

Eine vorgefertigte SICK-Nova-Konfigurationsdatei finden Sie hier:

[configuration_nova_inspector_blackjack.ncfg](../files/configuration_nova_inspector_blackjack.ncfg){ .md-button .button-small}

---

## Erwartetes Ergebnis

Nach Abschluss dieses Projekts sollte das Vision Starter Kit in der Lage sein, ausgewählte Spielkarten zu erkennen und die ermittelten Werte in einer Blackjack-Spielelogik zu verwenden.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Spielkarten werden zuverlässig erkannt
- Die erkannten Karten werden ihren korrekten Werten zugeordnet
- Der aktuelle Blattwert wird berechnet
- Das System zeigt an, ob der Wert 21 überschritten wurde.
- Das Konzept lässt sich durch Visualisierung oder externes Feedback erweitern.

---

## Zusammenfassung

In diesem Projekt für Fortgeschrittene hast du Bildklassifizierung mit Spielelogik kombiniert.

Du hast geübt, wie man:

- Spielkarten mit dem Vision Starter Kit sortieren
- Nützliche Kartenklassen definieren
- ein KI-Klassifikationsmodell trainieren und testen
- Ergebnisse der Kartenklassifizierung numerischen Werten zuordnen
- Implementiere die Logik für ein einfaches Blackjack-Spiel
- Überlegen Sie sich Möglichkeiten zur Visualisierung und Rückmeldung

Dieses Projekt veranschaulicht, wie das Vision Starter Kit über einfache Klassifizierungsaufgaben hinaus eingesetzt und mit anwendungsspezifischer Logik verknüpft werden kann.

---

## Nächste Schritte

Fahren Sie mit einem weiteren Vision-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>