# SensorFusion

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
      <td>Erstellen Sie im Logik-Editor des SIG300 ein Logikdiagramm, um die Messergebnisse mithilfe von LEDs darzustellen.</td>
      <td>Grundlagen/Fortgeschrittene</td>
      <td>0,5–2 Stunden</td>
      <td>Testobjekte<br>Ein Glas Wasser<br>Flache Materialien (z. B. Papierstücke)</td>
    </tr>
  </tbody>
</table>

Ziel dieses Projekts ist es, LEDs zu aktivieren, sobald eine bestimmte Bedingung erfüllt ist, z. B. ein Messergebnis in einem bestimmten Bereich oder das Vorhandensein eines bestimmten Materials.

Dazu können wir die 3 Sensoren und die 2 farbigen LEDs aus dem Starter-Kit verwenden. Die Logik wird im Logik-Editor der WebUI des SIG300 definiert.

Hier findest du einige mögliche Ideen, wie du mit den Sensoren und LEDs arbeiten kannst.

**Grundlagen**

Lassen Sie eine LED dauerhaft leuchten.

??? sickinfo "Beispiellösung"
    Schließen Sie eine LED an einen beliebigen Port an und verbinden Sie den mit dem grünen Pfeil gekennzeichneten „CON“-Anschluss im Logik-Editor mit dem digitalen Ausgang des Ports (z. B. S5DO4 – Port 5, Pin 4 der LED).

Eine LED soll nur dann aufleuchten, wenn ein Sensor einen bestimmten Wert oder einen bestimmten Bereich misst

??? sickinfo "Beispiellösung"
    Schließen Sie eine LED an einen beliebigen Anschluss an und einen Sensor (z. B. W10) an einen anderen Anschluss.
    Stellen Sie einen bestimmten Wert ein (dies kann entweder auf dem Display des W10 oder im IODD-Viewer des Geräts erfolgen: Erkennungseinstellungen > Qint.1 SP1-Erfassungsbereich). 
    Verbinden Sie den Block für den digitalen Eingang des Sensors (z. B. S1DI2) im Logik-Editor direkt mit dem Block für den digitalen Ausgang der LED (z. B. S5DO4).
    Die LED sollte nun nur noch aufleuchten, wenn der eingestellte Wert unterschritten oder überschritten wird.

**Fortgeschritten**

Lassen Sie die grüne LED nur dann aufleuchten, wenn alle folgenden Bedingungen erfüllt sind:
* Der IMC30 erkennt Objekte innerhalb eines festgelegten Bereichs (erfahren Sie, welche Materialien gemessen werden können und wie groß der Messbereich ist)
* Der UC12 misst den Abstand zur Oberfläche eines Glases mit Wasser
* Das W10 ermittelt den Abstand zu einem Objekt durch ein Glas Wasser hindurch

Wenn keine der Bedingungen erfüllt ist, soll die rote LED aufleuchten.
Wenn nur eine Bedingung erfüllt ist, sollen die rote und die grüne LED aufleuchten.
Wenn zwei Bedingungen erfüllt sind, schalte beide LEDs aus.

Dieses Projekt lässt sich auf verschiedene Weise anpassen.

??? sickinfo "Beispiellösung"
    Schließen Sie alle Sensoren und LEDs an den SIG300 an. Probieren Sie im IODD-Viewer verschiedene Einstellungen der Sensoren aus und erstellen Sie im Logik-Editor ein Logikdiagramm, um die LEDs entsprechend den gemessenen Sensorwerten ein- und auszuschalten. Prüfen Sie, welche Sensoren welche Materialarten messen können.