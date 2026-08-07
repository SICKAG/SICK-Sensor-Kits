# Sechskantmuttern und -schrauben klassifizieren

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
      <td>Probieren Sie das KI-Klassifizierungstool aus, indem Sie Bilder von verschiedenen Sechskantmuttern und/oder Schrauben aufnehmen, um Ihren ersten KI-Algorithmus zu erstellen.</td>
      <td>Grundlagen</td>
      <td>30 Minuten</td>
      <td>keine – alles ist im Starter-Kit enthalten</td>
    </tr>
  </tbody>
</table>

Richten Sie den Sensor wie im Abschnitt [Erste Schritte](./vision_getting_started.md) beschrieben ein.

![Sechskantmuttern klassifizieren 1](../images/Classify_hex_nuts_1.png)

1. Erstellen Sie einen **leeren Auftrag** und stellen Sie sicher, dass **Aufträge** und **Erfassung** ausgewählt sind
2. Bringen Sie die **Sechskantmutter** in das Sichtfeld des Sensors.
Es wird empfohlen, die Höhe der Halterung so einzustellen, dass sie näher am Objekt liegt (ca. 10 cm über dem Boden).
3. Wählen Sie **Konfigurieren**
4. Klicken Sie auf **Automatische Einrichtung ausführen**. Passen Sie den Fokus bei Bedarf mit dem Einstellwerkzeug an.
5. Klicken Sie auf **Empfohlen**. 
6. Klicken Sie auf **Ausführen**, um die Live-Bilder anzuzeigen
7. Passen Sie das **Sichtfeld (FOV)** an und führen Sie gegebenenfalls eine **Downsampling** durch.

![Sechskantmuttern klassifizieren 2](../images/Classify_hex_nuts_2.png)

8.	Klicken Sie im Abschnitt „Analyse“ auf **Tool hinzufügen** und wählen Sie **Klassifizieren > KI-Klassifizierung**
9.	Stellen Sie sicher, dass sich die **Sechskantmutter 1** im Sichtfeld des Sensors befindet. Passen Sie die Größe des roten Rechtecks so an, dass das Objekt vollständig darin enthalten ist.
10.	Öffne **Klasse 1**. 
11.	Klicken Sie auf **Aktives Bild hinzufügen**, wiederholen Sie diesen Schritt mehrmals mit einem neuen, identischen Objekt oder verschieben Sie das Objekt jedes Mal.
12.	Platzieren Sie eine **Sechskantmutter 2** im Sichtfeld des Sensors und öffnen Sie **Klasse 2**
13.	Klicken Sie auf **Aktives Bild hinzufügen**, wiederholen Sie diesen Schritt mehrmals mit einem neuen, identischen Objekt oder verschieben Sie das Objekt jedes Mal
14.	Klicken Sie auf **Trainieren** und warten Sie, bis der Job **erfolgreich trainiert** wurde.
15.	Prüfen Sie, ob das Objekt zuverlässig erkannt wird. Fügen Sie weitere Trainingsbilder hinzu, um die Ergebnisse zu verbessern.
