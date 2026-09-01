# SensorFusion

## Kurzbeschreibung

Dieses Projekt im Rahmen der Challenge zeigt, wie man den Logik-Editor des SIG300 nutzt, um Sensordaten mithilfe von grünen und roten LEDs darzustellen.

Sie können mit einer einfachen LED-Übung beginnen und anschließend eine komplexere Logik entwickeln, bei der die Messwerte aller drei im IO-Link-Konnektivitäts-Starter-Kit enthaltenen Sensoren kombiniert werden.

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
      <td>30 Minuten bis 2 Stunden</td>
      <td>
        Testobjekte<br>
        Ein Glas Wasser<br>
        Flache Materialien, wie zum Beispiel Papierstücke
      </td>
    </tr>
  </tbody>
</table>


![Bild](../images/)

## Ziel der Herausforderung

Ziel dieses Projekts ist es, im Logik-Editor des SIG300 ein Logikdiagramm zu erstellen und die Messergebnisse mithilfe der beiden farbigen LEDs aus dem Starter-Kit zu visualisieren.

Die LEDs sollten reagieren, wenn eine bestimmte Bedingung erfüllt ist, zum Beispiel:

- Ein Messwert liegt innerhalb eines bestimmten Bereichs
- Ein Messwert liegt über oder unter einem festgelegten Wert
- Ein Sensor erkennt ein bestimmtes Material.
- Mehrere Sensorbedingungen sind gleichzeitig erfüllt

---

## Projektkonzept

Das Projekt nutzt die drei Sensoren und die zwei farbigen LEDs, die im IO-Link-Konnektivitäts-Starter-Kit enthalten sind.

Die erforderliche Logik wird im Logik-Editor der SIG300-WebUI erstellt.

Das Projekt ist in zwei Schwierigkeitsstufen unterteilt:

- **Grundlagen:** Verknüpfen Sie einzelne Sensordaten oder Zustände mit einer LED.
- **Fortgeschritten:** Kombinieren Sie die Ergebnisse mehrerer Sensoren und steuern Sie beide LEDs mit einer komplexeren Logik.

---

## Bevor Sie beginnen

Schließen Sie das SIG300, die Sensoren und die LEDs wie in der Anleitung „Erste Schritte“ beschrieben an.

[Erste Schritte](../iolink/iolink_getting_started.md){.md-button .button-small}

Stellen Sie sicher, dass die erforderlichen Sensoren und LEDs an den SIG300 angeschlossen sind, bevor Sie das Logikdiagramm erstellen.

---

## Grundlegende Herausforderungen

### Herausforderung 1: Kontinuierliche LED-Leistung

Lassen Sie eine LED dauerhaft leuchten.

??? info "Beispiellösung"

    Schließen Sie eine LED an einen beliebigen Anschluss an.

    Verbinden Sie im Logik-Editor den **CON**-Block mit dem grünen Pfeil mit dem digitalen Ausgang des ausgewählten Ports.

    Beispiel:

    ```text
    S5DO4
    ```

    In diesem Beispiel:

    - `S5` bezieht sich auf Port 5
    - `DO4` bezeichnet den digitalen Ausgang an Pin 4 der LED

---

### Aufgabe 2: Sensorgesteuerte LED

Sorgen Sie dafür, dass eine LED nur dann aufleuchtet, wenn ein Sensor einen bestimmten Wert oder einen Wert innerhalb eines definierten Bereichs misst.

??? info "Beispiellösung"

    Schließen Sie eine LED an einen beliebigen Anschluss an und einen Sensor, zum Beispiel den W10, an einen anderen Anschluss.

    Vermitteln Sie einen bestimmten Wert. Dies kann auf folgende Weise geschehen:

    - auf dem Display des W10
    - im IODD Viewer des Geräts unter **Erkennungseinstellungen** > **Qint.1 SP1-Erfassungsbereich**

    Verbinden Sie im Logik-Editor den digitalen Eingangsblock des Sensors direkt mit dem digitalen Ausgangsblock der LED.

    Beispiel für eine Sensoreingabe:

    ```text
    S1DI2
    ```

    Beispiel für die LED-Ausgabe:

    ```text
    S5DO4
    ```

    Die LED sollte nun aufleuchten, wenn der eingestellte Wert überschritten oder unterschritten wird.

---

## Fortgeschrittene Herausforderung

Erstellen Sie eine Logik, bei der die grüne LED nur dann aufleuchtet, wenn alle folgenden Bedingungen erfüllt sind:

- Der IMC30 erkennt Objekte innerhalb eines festgelegten Bereichs.
- Der UC12 misst den Abstand zur Oberfläche eines Glases mit Wasser.
- Das W10 ermittelt die Entfernung zu einem Objekt durch ein Glas Wasser hindurch.

Implementieren Sie außerdem das folgende LED-Verhalten:

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Erfüllte Bedingungen</th>
      <th style="padding: 8px; text-align: left;">Erforderliches LED-Verhalten</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Es ist keine Bedingung erfüllt</td>
      <td>Die rote LED leuchtet auf.</td>
    </tr>
    <tr>
      <td>Eine Bedingung ist erfüllt</td>
      <td>Die rote und die grüne LED leuchten auf.</td>
    </tr>
    <tr>
      <td>Zwei Bedingungen sind erfüllt</td>
      <td>Beide LEDs sind ausgeschaltet.</td>
    </tr>
    <tr>
      <td>Alle Bedingungen sind erfüllt</td>
      <td>Die grüne LED leuchtet auf.</td>
    </tr>
  </tbody>
</table>

<br>

Finden Sie im Rahmen dieser Herausforderung Folgendes heraus:

- Welche Materialien können mit dem IMC30 erkannt werden?
- Welcher Messbereich kann verwendet werden?
- Welche Einstellungen sind für die einzelnen Sensoren geeignet?
- wie die Sensordaten im Logik-Editor kombiniert werden müssen

??? info "Beispiellösung"

    Schließen Sie alle Sensoren und LEDs an den SIG300 an.

    Probieren Sie im IODD Viewer verschiedene Einstellungen für die Sensoren aus und prüfen Sie, welche Sensoren die ausgewählten Materialien messen können.

    Erstellen Sie im Logik-Editor das Logikdiagramm so, dass die LEDs entsprechend den gemessenen Sensorwerten und den definierten Bedingungen ein- oder ausgeschaltet werden.

---

## Mögliche Erweiterungen

Dieses Projekt lässt sich auf verschiedene Weise anpassen.

Mögliche Varianten sind unter anderem:

- unter Verwendung verschiedener Testobjekte
- Auswahl verschiedener Messbereiche
- Änderung der Betriebsbedingungen für die LEDs
- Kombination von mehr oder weniger Sensorwerten
- Ein weiteres LED-Verhalten erstellen
- Vergleich der Sensortechnologien mit unterschiedlichen Materialien

---

## Erwartetes Ergebnis

Nach Abschluss des Projekts sollten die angeschlossenen LEDs entsprechend den Sensormesswerten und der im SIG300 konfigurierten Logik reagieren.

Bei den Grundübungen sollte eine LED entweder auf ein konstantes Signal oder auf den Messwert eines Sensors reagieren.

Bei der fortgeschrittenen Aufgabe sollen die roten und grünen LEDs anzeigen, wie viele der drei definierten Sensorbedingungen erfüllt sind.

---

## Zusammenfassung

In diesem Projekt haben Sie den Logik-Editor des SIG300 verwendet, um Sensormesswerte mit digitalen LED-Ausgängen zu verknüpfen.

Du hast mit folgenden Personen zusammengearbeitet:

- der fotoelektrische Sensor W10
- der Ultraschall-Abstandssensor UC12
- der induktive Näherungssensor IMC30
- die grünen und roten LEDs
- der IODD-Viewer
- der Logik-Editor des SIG300

Das Projekt lässt sich durch Ändern der Sensoreinstellungen, der Testmaterialien und der logischen Bedingungen anpassen.

## Nächste Schritte

Zurück zur IO-Link-Projektübersicht oder weiter zum Projekt „Smart Train Loop“.

<div class="next-step-buttons" markdown>

[Beispielprojekte](./iolink_example_projects.md){ .md-button }

[Intelligente Zugsschleife](./iolink_train.md){ .md-button }

</div>