# Recycling

## Kurzbeschreibung

Im Mittelpunkt dieses Challenge-Projekts steht der Einsatz des Tools **KI-Klassifizierung** zur Klassifizierung verschiedener Abfallarten für Recyclingzwecke.

Sie entwickeln eine „Vision Starter Kit“-Anwendung, die zwischen verschiedenen Abfallklassen unterscheiden oder Fremdkörper in einer vordefinierten Abfallkategorie erkennen kann.

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
      <td>Von den Grundlagen bis zum Fortgeschrittenenniveau</td>
      <td>1 bis 4 Stunden</td>
      <td>
        Abfallgegenstände, zum Beispiel Papier, Kunststoffe oder Verpackungen<br>
        Optional: Förderband<br>
        Optional: Schieber oder Aussortierer zum Sortieren von Objekten<br>
        Alternative: LED- oder akustische Rückmeldung
      </td>
    </tr>
  </tbody>
</table>

<br>

![Recycling](../images/recycling.jpg)

## Ziel der Herausforderung

Ziel dieses Projekts ist es, mit dem Vision Starter Kit eine KI-basierte Recycling-Anwendung zu entwickeln.

Das System soll verschiedene Abfallgegenstände klassifizieren oder Fremdkörper in einem Abfallbehälter erkennen. So könnte die Anwendung beispielsweise Kunststoffgegenstände in einem Karton mit Papier erkennen oder Gegenstände in Kategorien wie Papier, Kunststoff und Verpackungen einordnen.

Im Gegensatz zu einem angeleiteten Projekt wird bei dieser Aufgabe keine vollständige Schritt-für-Schritt-Lösung bereitgestellt. Nutze dein Wissen aus früheren Vision Starter Kit-Projekten, um deinen eigenen Ansatz zu entwickeln.

---

## Problemstellung

Falsch sortierte Abfallgegenstände sollten automatisch erkannt werden, um die Recycling- und Abfalltrennungsprozesse zu unterstützen.

Mögliche Szenarien:

- Fremdkörper in einem Behälter erkennen
- Abfälle in verschiedene Materialkategorien einteilen
- falsch sortierte Objekte identifizieren
- auf der Grundlage des Klassifizierungsergebnisses visuelles oder akustisches Feedback geben

---

## Aufgabe

Erstellen Sie eine „Vision Starter Kit“-Anwendung, die Abfallgegenstände klassifiziert oder bewertet.

Ihre Lösung sollte Folgendes umfassen:

1. Definition von Objekt- oder Materialklassen
2. Aufbau der Bildaufnahme
3. Training zur KI-Klassifizierung
4. Tests mit verschiedenen Abfallgegenständen
5. Rückmeldung oder Ergebnisdarstellung

Mögliche Kurse könnten sein:

- Papier
- Kunststoff
- Pappe
- Verpackung
- Metall
- Fremdkörper
- leerer Hintergrund

Sie können auch eigene Klassen definieren, je nachdem, welche Objekte verfügbar sind.

---

## Anforderungen

<div class="requirement-box">

<h3>Grundlegende Anforderungen</h3>

<ul>
  <li>Verwenden Sie das <strong>KI</strong>-Klassifizierungstool in SICK Nova.</li>
  <li>Definieren Sie mindestens zwei Objekt- oder Materialklassen.</li>
  <li>Erfassen Sie für jede Klasse mehrere Trainingsbilder.</li>
  <li>Trainieren Sie das Klassifizierungsmodell.</li>
  <li>Testen Sie das Modell mit neuen Abfallobjekten.</li>
  <li>Beurteilen Sie, ob das Klassifizierungsergebnis zuverlässig ist.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Optionale Erweiterungen</h3>

<ul>
  <li>Fügen Sie eine LED- oder akustische Rückmeldung hinzu.</li>
  <li>Verwenden Sie ein Förderband.</li>
  <li>Lösen Sie die Bildaufnahme automatisch aus.</li>
  <li>Fügen Sie einen Schieber- oder Aussortiermechanismus hinzu.</li>
  <li>Vergleichen Sie einfache und schwierige Objektformen.</li>
  <li>Testen Sie verschiedene Lichtverhältnisse.</li>
</ul>

</div>

---

## Vorgeschlagene Vorgehensweise

Orientieren Sie sich an folgendem Vorgehen:

1. Richten Sie das Vision Starter Kit ein.
2. Wählen Sie die Abfallkategorien aus, die Sie zuordnen möchten.
3. Bereiten Sie für jede Kategorie mehrere Beispielobjekte vor.
4. Erstellen Sie einen leeren Auftrag in SICK Nova.
5. Bildaufnahme konfigurieren.
6. Fügen Sie das Tool **KI-Klassifizierung** hinzu.
7. Erstellen Sie für jede Abfallkategorie eine Klasse.
8. Nehmen Sie für jede Klasse mehrere Bilder auf.
9. Das Modell trainieren.
10. Testen Sie die Klassifizierung mit neuen Objekten.
11. Verbessern Sie den Datensatz, wenn das Ergebnis nicht zuverlässig ist.

---

## Projektideen

Je nach verfügbarer Hardware können Sie die Aufgabe auf unterschiedliche Weise umsetzen.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Einfache Klassifizierung</h3>
    <p>Klassifizieren Sie einzelne Abfallgegenstände, die unter den Sensor gelegt werden.</p>
    <p>Mögliche Klassen könnten Papier, Kunststoff oder Verpackungen sein.</p>
    <p>Dies ist die einfachste Variante des Projekts und kann ausschließlich mit dem Starter-Kit umgesetzt werden.</p>
  </div>

  <div class="strategy-card">
    <h3>Fremdkörpererkennung</h3>
    <p>Erkennen Sie, ob ein Abfallbehälter einen Gegenstand enthält, der nicht zur erwarteten Kategorie gehört.</p>
    <p>Beispiel: Erkennen eines Kunststoffgegenstands in einem Papierbehälter.</p>
  </div>

  <div class="strategy-card">
    <h3>Visuelle Rückmeldung</h3>
    <p>Zeigen Sie das Prüfergebnis mithilfe einfacher Rückmeldungen an.</p>
    <p>Beispiele hierfür sind ein grünes Licht für korrekte Objekte, ein rotes Licht für falsche Objekte, akustisches Feedback oder eine Meldung auf einem angeschlossenen Gerät.</p>
  </div>

  <div class="strategy-card">
    <h3>Automatisierte Sortierung</h3>
    <p>Erweitern Sie das Projekt mit zusätzlicher Hardware.</p>
    <p>Mögliche Erweiterungen sind ein Förderband, ein Auslösesensor, ein Schieber, ein Aussortierer oder eine Signalleuchte.</p>
  </div>

</div>

---

## Tipps

??? tip "Tipp 1: Fangen Sie einfach an"
    Beginnen Sie mit nur zwei Klassen, zum Beispiel **Papier** und **Kunststoff**.  
    Sobald die Klassifizierung zuverlässig funktioniert, fügen Sie weitere Klassen hinzu.

??? tip "Tipp 2: Verwende verschiedene Varianten"
    Nehmen Sie Trainingsbilder mit unterschiedlichen Objektpositionen, Drehungen und Entfernungen auf.  
    Dies kann die Robustheit des Klassifizierungsergebnisses verbessern.

??? tip "Tipp 3: Achten Sie auf die Beleuchtung"
    Recyclinggegenstände können reflektierende oder transparente Oberflächen haben.  
    Achten Sie darauf, dass das Bild gut ausgeleuchtet ist und das Objekt deutlich zu erkennen ist.

??? tip "Tipp 4: Nutzen Sie das Projekt zur geführten Klassifizierung"
    Wenn Sie sich nicht sicher sind, wie Sie das KI-Klassifizierungstool verwenden sollen, sehen Sie sich das unten stehende [Beispielprojekt mit Anleitung](./classify_hex_nuts_screws.md) noch einmal an.


---

## Erwartetes Ergebnis

Nach Abschluss dieser Aufgabe sollte das Vision Starter Kit in der Lage sein, die ausgewählten Abfallgegenstände zu klassifizieren oder Fremdkörper in einem definierten Recycling-Szenario zu erkennen.

Ein erfolgreiches Ergebnis bedeutet, dass:

- Die trainierten Klassen werden korrekt erkannt
- Neue Testobjekte werden zuverlässig klassifiziert
- Falsch klassifizierte Objekte können durch zusätzliche Trainingsbilder identifiziert und verbessert werden.
- Die Projektidee lässt sich durch Feedback oder Sortierhardware erweitern.

---

## Beispiel-Projektdatei

Eine vorgefertigte Beispielprojektdatei finden Sie hier:

[Recycling-Papierkorb-Projekt](../files/RecyclingBinProject.zip){ .md-button .button-small}

---

## Zusammenfassung

In diesem Challenge-Projekt haben Sie die KI-Klassifizierung auf einen Anwendungsfall im Bereich Recycling angewendet.

Du hast geübt, wie man:

- Objekt- oder Materialklassen definieren
- Trainingsbilder sammeln
- ein KI-Klassifikationsmodell trainieren
- Klassifizierungsergebnisse auswerten
- den Datensatz verbessern
- Überlegen Sie sich mögliche Erweiterungen wie Feedback- oder Sortierfunktionen.

Dieses Projekt eignet sich gut als Übung, um den Workflow des Vision Starter Kits auf eine praxisnahe Anwendung zu übertragen.

---

## Nächste Schritte

Fahren Sie mit einem weiteren Vision-Projekt fort oder öffnen Sie die vollständigen Projektdateien auf GitHub.com.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./vision_example_projects.md){ .md-button .button-small }

[GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

</div>