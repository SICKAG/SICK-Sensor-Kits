<!-- # Tic Tac Toe

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
      <td>Analysiere ein Tic-Tac-Toe-Spielfeld und spiele gegen den Computer.</td>
      <td>Fortgeschritten</td>
      <td>4 Stunden</td>
      <td>Papier, Stift, Schere</td>
    </tr>
  </tbody>
</table>

![Tic Tac Toe](../images/tic_tac_toe.jpg)

## Welches Problem muss gelöst werden?
Ein physisches Spielbrett oder ein „Tic Tac Toe“-Spielfeld auf einem Blatt Papier muss vorhanden sein, um die Züge der Spieler zu erfassen und das Spiel gegen einen Computergegner zu ermöglichen.

Projektideen:

* Erkennung von Symbolen, Farben und leeren Feldern
* Rundenbasierte Spiellogik
* Verschiedene Schwierigkeitsgrade
* „Coach“, das die beste Position für das nächste Symbol vorschlägt
* Dashboard zur Visualisierung
* Roboterarm zum Zeichnen von Symbolen

## Beispielprojektdatei Python und Nova

[TicTacToe.zip](../files/tictactoe.zip)


-->


# Tic Tac Toe

## Kurzbeschreibung

Im Mittelpunkt dieses Challenge-Projekts steht die Analyse eines realen Tic-Tac-Toe-Spielbretts mithilfe des Vision Starter Kits.

Das Ziel besteht darin, die Züge der Spieler auf einem Spielbrett aus Papier zu erkennen und anhand des ermittelten Spielzustands gegen einen Computergegner zu spielen oder Vorschläge für den nächsten Zug zu unterbreiten.

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
      <td> <span class="project-badge challenge">Challenge-Projekt</span></td>
      <td>Fortgeschritten</td>
      <td>4 Stunden</td>
      <td>Papier, Stift, Schere</td>
    </tr>
  </tbody>
</table>

<br>

![Tic-Tac-Toe](../images/tic_tac_toe.jpg)

## Ziel der Herausforderung

Das Ziel dieses Projekts ist es, eine „Vision Starter Kit“-Anwendung zu entwickeln, die ein physisches Tic-Tac-Toe-Spielfeld beobachten und den aktuellen Spielstand erkennen kann.

Das System sollte erkennen, ob Felder leer oder belegt sind, und die von den Spielern platzierten Symbole identifizieren.

Im Gegensatz zu einem angeleiteten Projekt wird bei dieser Aufgabe keine vollständige Schritt-für-Schritt-Lösung bereitgestellt. Nutze dein Wissen aus früheren Vision Starter Kit-Projekten, um deinen eigenen Ansatz zu entwickeln.

---

## Problemstellung

Ein physisches Spielbrett oder ein „Tic Tac Toe“-Spielfeld auf einem Blatt Papier sollte mit dem Vision Starter Kit betrachtet werden.

Das System sollte die Züge der Spieler erkennen und es ermöglichen, gegen einen Computergegner zu spielen oder nützliche Spielinformationen anzuzeigen.

Mögliche Ziele:

- leere und belegte Felder erkennen
- zwischen verschiedenen Symbolen unterscheiden
- den aktuellen Spielstand auswerten
- gültige Züge ermitteln
- den besten nächsten Schritt vorschlagen
- Einen einfachen Computergegner erstellen

---

## Aufgabe

Erstellen Sie eine Anwendung, die ein Tic-Tac-Toe-Spielfeld analysiert und den aktuellen Spielstand auswertet.

Ihre Lösung sollte Folgendes umfassen:

1. Ein Tic-Tac-Toe-Spielbrett aus Holz oder ein Spielfeld auf Papier
2. Aufbau der Bildaufnahme
3. Erkennung von Leiterplattenfeldern
4. Erkennung von Symbolen oder Farben
5. Bewertung der Spielsituation
6. Optionaler Computergegner oder Zugvorschlag
7. Optionales Dashboard oder Visualisierung

---

## Anforderungen

<div class="requirement-box">

<h3>Core Requirements</h3>

<ul>
  <li>Use the Vision Starter Kit to observe the game board.</li>
  <li>Detect the individual fields of the Tic Tac Toe board.</li>
  <li>Identify whether a field is empty or occupied.</li>
  <li>Distinguish between the two player symbols.</li>
  <li>Evaluate the current board state.</li>
  <li>Provide useful feedback for the next move or game result.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optional Extensions</h3>

<ul>
  <li>Add a computer opponent with different difficulty levels.</li>
  <li>Add a move suggestion or coaching mode.</li>
  <li>Create a dashboard for visualization.</li>
  <li>Detect invalid moves.</li>
  <li>Add automatic win detection.</li>
  <li>Use a robot arm to draw symbols.</li>
  <li>Use color-based symbol detection instead of shape-based detection.</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem allgemeinen Ansatz:

1. Richten Sie das Vision Starter Kit ein.
2. Bereite ein Tic-Tac-Toe-Spielfeld auf Papier vor.
3. Bringen Sie die Platine in das Sichtfeld des Sensors.
4. Bildaufnahme konfigurieren.
5. Legen Sie fest, wie die einzelnen Felder auf der Platine erkannt werden sollen.
6. Entscheiden Sie, ob Symbole anhand ihrer Form, Farbe oder Position erkannt werden sollen.
7. Schulen Sie die Mitarbeiter im Umgang mit den erforderlichen Werkzeugen oder konfigurieren Sie diese in SICK Nova.
8. Prüfen Sie, ob der Spielstand zuverlässig erkannt wird.
9. Füge eine Spiellogik hinzu, um das Spielfeld auszuwerten.
10. Fügen Sie Feedback, Visualisierung oder eine Logik für den Computergegner hinzu.

---

## Mögliche Erkennungsstrategien

Es gibt verschiedene Möglichkeiten, diese Herausforderung zu meistern.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Symbol Classification</h3>
    <p>Classify the symbols in each field of the Tic Tac Toe board.</p>
    <p>Possible classes could be empty field, circle and cross.</p>
    <p>This approach is useful if the symbols are clearly visible and placed consistently inside the board fields.</p>
  </div>

  <div class="strategy-card">
    <h3>Color Detection</h3>
    <p>Use different colors for the two players and detect the color inside each field.</p>
    <p>Possible classes could be empty field, player 1 color and player 2 color.</p>
    <p>This can simplify the first version of the project, especially if symbol recognition is difficult.</p>
  </div>

  <div class="strategy-card">
    <h3>Fixed Field Analysis</h3>
    <p>Divide the camera image into nine fixed board areas and evaluate each area separately.</p>
    <p>This can be helpful if the board position is stable and does not move during the game.</p>
    <p>It also makes it easier to connect the detected field states with the Tic Tac Toe game logic.</p>
  </div>

</div>

---

## Ideen zur Spielelogik

Nachdem der Spielstand ermittelt wurde, kann die Anwendung die Partie auswerten.

Mögliche Logikelemente:

- Prüfen, ob ein Spieler drei Symbole in einer Reihe hat
- Prüfe, ob das Spiel unentschieden ausgeht
- ungültige Züge erkennen
- den bestmöglichen nächsten Schritt vorschlagen
- Einen einfachen Computergegner programmieren
- verschiedene Schwierigkeitsgrade hinzufügen

Mögliche Rückmeldungen:

- Zug des aktuellen Spielers
- zulässiger oder unzulässiger Zug
- Sieger
- ziehen
- Vorschlag für den nächsten Schritt

---

## Tipps

??? tip "Tipp 1: Die Brettstellung festlegen"
    Versuche, das Tic-Tac-Toe-Spielfeld in einer festen Position zu halten.  
    Eine stabile Lage der Platine erleichtert die Erkennung von Feldern erheblich.

??? tip "Tipp 2: Beginnen Sie mit der Farberkennung"
    Wenn das Erkennen von Symbolen Schwierigkeiten bereitet, beginnen Sie mit farbigen Symbolen oder farbigen Papierstücken.  
    Dies kann die erste Version des Projekts vereinfachen.

??? tip "Tipp 3: Verwende eine verkürzte erste Fassung"
    Ermitteln Sie zunächst nur, ob die Felder leer oder ausgefüllt sind.  
    Fügen Sie anschließend die Symbolunterscheidung und die Spielelogik hinzu.

??? tip "Tipp 4: Trenne die Erkennung von der Spielelogik"
    Stellen Sie zunächst sicher, dass der Board-Zustand zuverlässig erkannt wird.  
    Füge anschließend die Spiellogik für „Tic Tac Toe“ hinzu.

??? tip "Tipp 5: Nutzen Sie frühere Projekte als Vorlage"
    Wenn Sie sich nicht sicher sind, wie Sie Objekte oder Symbole klassifizieren sollen, schauen Sie sich noch einmal das Projekt [Geführte Klassifizierung](./classify_hex_nuts_screws.md) an.


---

## Beispiel-Projektdatei

Eine vorgefertigte Beispielprojektdatei finden Sie hier:

[tictactoe.zip](../files/tictactoe.zip){ .md-button .button-small}

---

## Erwartetes Ergebnis

Nach Abschluss dieser Aufgabe sollte das Vision Starter Kit in der Lage sein, ein physisches Tic-Tac-Toe-Spielbrett zu analysieren und den aktuellen Spielstand zu ermitteln.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Die Platine wird zuverlässig erkannt.
- Leere und belegte Felder werden erkannt
- Spielersymbole lassen sich unterscheiden
- Der aktuelle Spielstand kann ausgewertet werden
- Ein Spielergebnis oder der nächste Zug kann angezeigt werden
- Das Konzept lässt sich um einen computergesteuerten Gegner oder einen Trainingsmodus erweitern.

---

## Zusammenfassung

In diesem Projekt haben Sie bildverarbeitungsgestützte Erkennung auf ein physisches Brettspiel angewendet.

Du hast geübt, wie man:

- ein strukturiertes Spielfeld analysieren
- Symbole oder Farben erkennen
- eine Spielstellung auswerten
- Bildanalyse mit Spielelogik kombinieren
- Entwickeln Sie eine interaktivere Anwendung auf Basis des Vision Starter Kits

Dieses Projekt ist eine gute Übung, um Klassifizierung, Logik und Visualisierung in einem spielerischen Anwendungsfall zu kombinieren.

---

## Nächste Schritte

Fahren Sie mit einem weiteren Vision-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>