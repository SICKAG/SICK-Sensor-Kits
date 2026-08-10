<!-- # FAQ – LiDAR-Starter-Kit

## Kurzbeschreibung

Diese FAQ beantwortet häufig gestellte Fragen zum LiDAR-Starter-Kit, zur Praxistestphase und zur Sensorkommunikation.

Bei allgemeinen Fragen zu den Starter-Kits besuchen Sie bitte den Bereich „Allgemeine FAQ“.

../faq.md{ .md-button .button-small }

---

??? question "Der LiDAR-Sensor ist nicht erreichbar. Was sollte ich überprüfen?"

    Überprüfen Sie die Stromversorgung, die Ethernet-Verbindung und die IP-Adresse des Sensors.

---

??? question "Die Feldauswertung liefert nicht das erwartete Ergebnis. Was kann ich tun?"

    Überprüfen Sie, ob die Erfassungsfelder korrekt konfiguriert sind und ob sich das Objekt innerhalb des definierten Bereichs befindet.

---

??? question "Wo finde ich Beispielprojekte für das LiDAR-Starter-Kit?"

    Die LiDAR-Beispielprojekte sind auf der Seite „Beispielprojekte“ aufgeführt.

    ./lidar_example_projects.md{ .md-button .button-small }

-->

<div class="faq-page" markdown>

# FAQ – LiDAR-Starter-Kit

## Kurzbeschreibung

Diese FAQ beantwortet häufig gestellte Fragen zum LiDAR-Starter-Kit, zur Praxistestphase, zur Sensorkommunikation und zur grundlegenden Fehlerbehebung.

Bei allgemeinen Fragen zu den Starter-Kits, Support-Ressourcen oder zusätzlichem Schulungsmaterial besuchen Sie bitte den Bereich „Allgemeine FAQ“.

[Häufig gestellte Fragen](../faq.md){ .md-button .button-small }

---

??? question "Der LiDAR-Sensor ist nicht erreichbar. Was sollte ich überprüfen?"

    Bitte überprüfen Sie die folgenden Punkte:

    - Das Netzteil ist angeschlossen
    - Das Ethernet-Kabel ist korrekt angeschlossen.
    - Der richtige Netzwerkadapter ist konfiguriert.
    - Die IP-Adresse Ihres Computers liegt im gleichen Bereich wie die des Sensors.
    - Die IP-Adresse des Sensors ist korrekt.
    - Kein anderes Gerät verwendet dieselbe IP-Adresse.
    - Die Firewall-Einstellungen blockieren die Verbindung nicht.

    Die in der Dokumentation verwendete Standard-IP-Adresse lautet in der Regel:

    ```text
    192.168.0.1
    ```

    Falls sich die Benutzeroberfläche des Sensors nicht im Browser öffnet, lesen Sie bitte noch einmal die Anleitung „Erste Schritte“.

    [Leitfaden für den Einstieg](./lidar_getting_started.md){.md-button .button-small}

---

??? question "Die Benutzeroberfläche des Sensors lässt sich im Browser nicht öffnen. Was kann ich tun?"

    Überprüfen Sie zunächst, ob sich der Computer und der Sensor im selben IP-Bereich befinden.

    Beispielkonfiguration:

    ```text
    Sensor IP:    192.168.0.1
    Computer IP:  192.168.0.100
    Subnet mask:  255.255.0.0
    ```

    Siehe auch:

    - der richtige Ethernet-Adapter ist ausgewählt
    - DHCP ist für diesen Adapter deaktiviert.
    - Die manuell eingegebene IP-Adresse wurde korrekt gespeichert.
    - Der Sensor hat seinen Startvorgang abgeschlossen.
    - Die Browser-URL beginnt mit `http://`

    Beispiel:

    ```text
    http://192.168.0.1
    ```

---

??? question "Die Feldauswertung liefert nicht das erwartete Ergebnis. Was kann ich tun?"

    Überprüfen Sie, ob die Erfassungsfelder korrekt konfiguriert sind und ob sich das Objekt innerhalb des definierten Erfassungsbereichs befindet.

    Überprüfen Sie außerdem:

    - Das Feld wird an der richtigen Stelle platziert.
    - Die Feldgröße entspricht dem zu erkennenden Objekt oder der zu erkennenden Person.
    - Die Parameter für die Objektgröße sind korrekt konfiguriert.
    - Das Objekt verbleibt lange genug innerhalb des Feldes
    - Statische Objekte wurden bei Bedarf korrekt per Teach-In verarbeitet

    Sollte das Verhalten des Feldes weiterhin unerwartet sein, beginnen Sie mit einem großen Feld und einem gut sichtbaren Testobjekt.

---

??? question "Was bedeuten die Werte der Feldauswertung?"

    In den Beispielprojekten wird die Feldauswertungsantwort herangezogen, um festzustellen, ob ein Feld verletzt wird.

    Typische Werte können sein:

    - `2`: Das Feld wird nicht verletzt
    - `4`: Feld wurde verletzt

    !!! warning "Antwortformat"
        Die genaue Position dieser Werte in der Antwort hängt von der Sensorkonfiguration und der Anzahl der Felder ab.  
        Drucken Sie zunächst die vollständige Antwort aus und ermitteln Sie die relevanten Stellen, bevor Sie das Ergebnis im Code auswerten.

---

??? question "Mein Python-Skript kann keine Verbindung zum LiDAR-Sensor herstellen. Was sollte ich überprüfen?"

    Bitte überprüfen Sie die folgenden Punkte:

    - Der Sensor ist im Browser erreichbar.
    - Die IP-Adresse im Skript ist korrekt.
    - Der Port ist korrekt.
    - Die Ethernet-Verbindung ist stabil.
    - Der Netzwerkadapter ist korrekt konfiguriert.

    Beispielwerte, die in den Code-Beispielen verwendet werden:

    ```python
    HOST = "192.168.0.1"
    PORT = 2111
    ```

    Falls Ihr Sensor eine andere IP-Adresse verwendet, passen Sie den Wert `HOST` im Skript entsprechend an.

---

??? question "Das Python-Skript erhält keine Daten. Was kann ich tun?"

    Stellen Sie sicher, dass der gesendete SOPAS-Befehl korrekt ist und dass der Sensor die angeforderten Daten unterstützt.

    Siehe auch:

    - Das Startzeichen `\x02` ist enthalten
    - Das Endzeichen `\x03` ist enthalten
    - Der Empfangspuffer ist groß genug
    - Der Sensor befindet sich im korrekten Zustand.
    - Die angeforderten Daten sind verfügbar

    Für erste Tests nutzen Sie die Seite „LiDAR-Code-Beispiele“.

    [LiDAR-Code-Beispiele](./lidar_code_snippets.md){ .md-button .button-small}

---

??? question "Das Skript bricht nach einer Weile mit einem Socket-Fehler ab. Was kann ich tun?"

    Dies kann passieren, wenn zu oft eine neue Socket-Verbindung geöffnet wird.

    Eine typische Fehlermeldung lautet:

    ```text
    Only one usage of each socket address, protocol, network address or port is normally permitted.
    ```

    Um dieses Problem zu verringern:

    - Eine Socket-Verbindung offen halten
    - Vermeiden Sie es, in jeder Schleifeniteration erneut eine Verbindung herzustellen
    - Sockets ordnungsgemäß schließen, wenn das Skript beendet wird
    - In Schleifen eine kurze Verzögerung einfügen
    - Fügen Sie bei Bedarf eine Fehlerbehandlung und eine Logik zur Wiederherstellung der Verbindung hinzu

    Das Projekt „Human Piano / Air Piano“ enthält ein verbessertes Beispiel, bei dem eine dauerhafte Socket-Verbindung verwendet wird.

    [Human Air Piano](./lidar_human_piano_air_piano.md){ .md-button .button-small }

---

??? question "Wo finde ich Beispielprojekte für das LiDAR-Starter-Kit?"

    Die LiDAR-Beispielprojekte sind auf der Seite „Beispielprojekte“ aufgeführt.

    [Beispielprojekte](./lidar_example_projects.md){ .md-button .button-small}

    Wenn Sie noch keine Erfahrung mit dem LiDAR-Starter-Kit haben, beginnen Sie mit dem Projekt „Feldtest“.

    [Feldbewertung](./lidar_field_evaluation.md){ .md-button .button-small}

---

??? question "Mit welchem Projekt soll ich anfangen?"

    Wenn Sie noch keine Erfahrung mit dem LiDAR-Starter-Kit haben, beginnen Sie mit dieser Reihenfolge:

    1. Erste Schritte
    2. Feldbewertung
    3. Entfernungsschätzung
    4. Der Boden ist Lava
    5. Menschliches Klavier / Luftklavier

    „Feldbewertung“ ist die empfohlene erste Demo, da sie das Grundkonzept der Erkennungsfelder vorstellt.

---

??? question "Wo finde ich Code-Beispiele für das LiDAR-Starter-Kit?"

    Einfache Python-Beispiele finden Sie auf der Seite „LiDAR-Code-Beispiele“.

    [LiDAR-Code-Beispiele](./lidar_code_snippets.md){ .md-button .button-small}

    Die Seite enthält Beispiele für:

    - Gerätetyp auslesen
    - Scandaten einlesen
    - kontinuierliches Einlesen von Scandaten
    - Auswertungsergebnisse des Lesefelds lesen
    - Verwendung einer wiederverwendbaren SOPAS-Hilfsfunktion

---

??? question "Wo finde ich weitere Informationen zur Integration?"

    Fortgeschrittene Themen zur Integration werden auf der Seite „Fortgeschrittene Themen“ behandelt.

    [Fortgeschritten](./lidar_advanced.md){ .md-button .button-small}

    Dazu gehören Informationen zu folgenden Themen:

    - protokollbasierte Integration
    - Verwendung des SDK
    - Verarbeitung von Scandaten
    - Integration externer Systeme
    - SICK Perception SDK

---

??? question "Wo finde ich vollständige Projektdateien oder den Quellcode?"

    Die GitHub.io-Dokumentation enthält Erläuterungen, Einrichtungsanleitungen und Projektübersichten.

    Die vollständigen Projektdateien und der Quellcode sollten über das GitHub.com-Projekt-Repository bereitgestellt werden.

    [GitHub](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank" .md-button .button-small}

    !!! note
        Der endgültige Link zum GitHub.com-Projekt-Repository muss möglicherweise angepasst werden, sobald die offizielle Repository-Struktur festgelegt ist.

---

## Verwandte Seiten

<div class="next-step-buttons" markdown>

[Leitfaden für den Einstieg](./lidar_getting_started.md){.md-button }

[Feldbewertung](./lidar_field_evaluation.md){ .md-button }

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[LiDAR-Code-Beispiele](./lidar_code_snippets.md){ .md-button }

[Fortgeschritten](./lidar_advanced.md){ .md-button }

[Häufig gestellte Fragen](../faq.md){ .md-button }

</div>

</div>