# Projekt „Vision Starter“

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
      <td>Machen Sie sich mit den ersten Einstellungen zur Bilderfassung und einer einfachen Aufgabe zur KI-Klassifizierung und Anomalieerkennung vertraut.</td>
      <td>Grundlagen</td>
      <td>90 Minuten</td>
      <td>keine – alles ist im Starter-Kit enthalten</td>
    </tr>
  </tbody>
</table>

![Vision_2](../images/Vision_2.png)

## Anleitung

### 1. Bildaufnahme

- Richten Sie den Inspector wie unter [Erste Schritte](./vision_getting_started.md) beschrieben ein.
- Wählen Sie oben **Live** aus und drücken Sie unten die **Play**-Taste, um Bilder im Serienmodus aufzunehmen.
-  Platzieren Sie die GitHub-Infokarte im Sichtfeld der Kamera.
- Wählen Sie **Aufträge** > **Erfassung** und probieren Sie die verschiedenen **Einstellungen** aus, um ein gut belichtetes Bild zu erhalten. Alternativ können Sie auch direkt auf **Automatische Einrichtung ausführen** klicken.

![Vision_2](../images/Vision_2.png)

- Passen Sie den Fokus der Kamera bei Bedarf manuell mit dem Fokus-Einstellwerkzeug (im Lieferumfang enthalten) an.

### 2. KI-Klassifizierung

- Wählen Sie **Analyse** > **Tool hinzufügen** > **Klassifizieren** > **KI-Klassifizierung** (ohne dStudio)

![Vision_3](../images/Vision_3.png)

- Passen Sie die Größe des Rahmens so an, dass er das gesamte Objekt sowie einen Puffer zur Berücksichtigung von Abweichungen oder unterschiedlichen Positionen umfasst.

![Vision_4](../images/Vision_4.png)

- Erstellen Sie Klassen unter **Dataset** auf der rechten Seite
- Klicken Sie auf das Wiedergabesymbol unten in der Mitte, um Serienfotos aufzunehmen
- Erweitern Sie die erste Klasse und nehmen Sie Bilder mit **Aktives Bild hinzufügen** auf
- Probieren Sie verschiedene Varianten aus (Position / Drehung)

![Vision_5](../images/Vision_5.png)

- Wiederholen Sie den Vorgang für die zweite Klasse, nehmen Sie jeweils mindestens 5 Bilder auf und klicken Sie auf **Train**.

![Vision_6](../images/Vision_6.png)

- Nach einigen Sekunden ist das Training beendet und Sie können die Ergebnisse überprüfen.

![Vision_7](../images/Vision_7.png)

- Fügen Sie gegebenenfalls weitere Bilder hinzu oder nehmen Sie zusätzliche Klassen (z. B. „Leer“) auf, um die Ergebnisse zu optimieren.

### 3. Objekt-Locator

Der Object Locator dient dazu, die Position eines Objekts zu ermitteln und Analysen in Bezug auf diese Position durchzuführen (z. B. zur Erkennung von Anomalien).

- Wählen Sie links **Jobs** > **Analyse** > **Tool hinzufügen** > **Suchen** > **Objekt-Locator**
- Füge ein Objekt in das Bild ein
- Klicken Sie unten in der Mitte auf **Referenz aktualisieren** und wechseln Sie zur Registerkarte **Referenz**.
- Ziehen Sie den Rahmen über einen markanten Teil des Objekts.

![Vision_8](../images/Vision_8.png)

- Passen Sie gegebenenfalls die Parameter auf der rechten Seite an:
  - Kantenstärke für Kontrastkanten
  - Drehung zur möglichen Drehung des Objekts
  - Skalierung, Übereinstimmungswert und Winkel für die Sensitivität
- Klicken Sie in der Mitte auf **Live** und **Play**, um zu testen, ob der betreffende Teil des Objekts verfolgt wird, wenn das Objekt bewegt wird.

![Vision_9](../images/Vision_9.png)

**Wichtig**: Der Object Locator muss zuverlässig funktionieren, bevor andere Tools verwendet werden.
Fügen Sie weitere Werkzeuge direkt unterhalb des Objekt-Locators hinzu.

![Vision_10](../images/Vision_10.png)

### 4. Erkennung von Anomalien

- Wählen Sie links **Jobs** > **Analyse** > **Tool hinzufügen** > **Überprüfen** > **KI-Anomalieerkennung** (ggf. unter „Object Locator“)

![Vision_11](../images/Vision_11.png)

- Wählen Sie oben in der Mitte die Registerkarte **„Referenz“** aus und ziehen Sie einen Rahmen über das Objekt (machen Sie ihn nur geringfügig größer, da der Objekt-Locator mitverfolgt wird).

![Vision_12](../images/Vision_12.png)


- Gehen Sie zurück zu **Live** und **Play** und suchen Sie unten rechts nach **Dataset**. Fügen Sie „gute“ Bilder mit verschiedenen Variationen hinzu. Beginnen Sie vorerst mit nur wenigen „guten“ Bildern.
- Klicken Sie auf **Zug**.

![Vision_13](../images/Vision_13.png)

Passen Sie die Trainingsparameter bei Bedarf an:

- **Anzahl der Trainingsbilder** (der Rest dient der Auswertung)
- **Schnell vs. präzise** – je nach Anzahl der Bilder und Zeitaufwand
- Lassen Sie **„Strikte Übereinstimmung“** aktiviert, wenn die Objektvariation sehr gering ist bzw. nur ein Objekt vorhanden ist.

![Vision_14](../images/Vision_14.png)

- Stellen Sie die Optionen auf **Live** und **Play** ein und probieren Sie verschiedene Positionen und Fremdkörper aus.
- **Hinweis**: Die Anomalieerkennung hängt immer vom Objekt-Locator ab. Wenn dieser fehlschlägt, schlägt auch die Anomalieerkennung fehl.
- Passen Sie unten rechts unter **Ergebnisse** bei Bedarf den **Anomalie-Score** und den **Visualisierungsbereich** an. Dies beeinflusst die Empfindlichkeit bei der Erkennung von Anomalien und deren Darstellung in einer Heatmap.

![Vision_15](../images/Vision_15.png)

Falls erforderlich, nehmen Sie weitere Bilder auf und fügen Sie auch schlechte Bilder hinzu, um die Ergebnisse zu optimieren.

### 5. Zurücksetzen

Klicken Sie oben rechts auf die **3 Punkte** > **Anwendungsstandards**

![Vision_16](../images/Vision_16.png)


