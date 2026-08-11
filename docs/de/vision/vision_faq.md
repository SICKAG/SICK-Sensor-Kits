<div class="faq-page"markdown>

# FAQ – Vision-Starter-Kit

## Kurzbeschreibung

Diese FAQ beantwortet häufig gestellte Fragen zum Vision Starter Kit, zu SICK Nova, zur Bildaufnahme und zu KI-basierten Tools.

Bei allgemeinen Fragen zu den Starter-Kits, Support-Ressourcen oder zusätzlichem Schulungsmaterial besuchen Sie bitte den allgemeinen Abschnitt [FAQ](../faq.md).

---

??? question "Das Gerät läuft langsam. Wie kann ich die Leistung verbessern?"

    Im Abschnitt **Erfassung** können Sie den Schieberegler **Downsample** anpassen, um die Bildauflösung zu verringern und die Verarbeitungsgeschwindigkeit zu erhöhen.

    Dies kann die Leistung verbessern, insbesondere wenn KI-Tools oder mehrere Analysetools in einem Auftrag verwendet werden.

    !!! warning "Wichtig"
        Stellen Sie die Abtastratenreduzierung zu Beginn eines Projekts ein.  
        Bereits erstellte Regionen, beispielsweise für den Object Locator oder KI-Tools, werden anschließend möglicherweise nicht automatisch angepasst.

---

??? question "Das Bild ist zu dunkel, zu hell oder unscharf. Was kann ich tun?"

    Überprüfen Sie die Erfassungseinstellungen in SICK Nova.

    Zu den nützlichen Maßnahmen gehören:

    - **Auto-Setup** ausführen
    - Belichtungseinstellungen anpassen
    - die Lichtverhältnisse verbessern
    - Stellen Sie den Fokus manuell mit dem Fokus-Einstellwerkzeug ein.
    - Den Abstand zwischen Objekt und Sensor prüfen

    Bei schlechter Bildqualität können auch die KI-Klassifizierung und die Anomalieerkennung unzuverlässig werden.

---

??? question "Wo finde ich weitere Informationen zu den verfügbaren Tools?"

    In SICK Nova können Sie über den Abschnitt **Hilfe** direkt auf werkzeugspezifische Informationen zugreifen.

    Dies ist hilfreich, wenn Sie verstehen möchten, was ein bestimmtes Werkzeug bewirkt, welche Parameter verfügbar sind und wie das Werkzeug in einem Arbeitsablauf eingesetzt werden kann.

    Hier ist eine umfassende Online-Übersicht über die [SICK Nova](https://sicknova.documentation)-Tools geplant:


    !!! note
        Der Link zur Online-Dokumentation ist möglicherweise noch nicht verfügbar.

---

??? question "Wie kann ich Daten von SICK Nova in einer IDE wie Visual Studio Code oder Python verwenden?"

    Im Abschnitt **Ergebnisse** von SICK Nova können Sie Ergebnisdaten konfigurieren und versenden.

    Für erste Versuche können Sie auch die Seite [Vision-Code-Beispiele](./vision_code_snippets.md) nutzen.

    Zu den typischen Anwendungsfällen gehören:

    - Empfangen von Sensordaten in Python
    - Auslösen der Bildaufnahme
    - Auswertung der Klassifizierungsergebnisse
    - Daten an eine externe Anwendung senden

---

??? question "Die KI-Klassifizierung funktioniert nicht zuverlässig. Was kann ich verbessern?"

    Die Zuverlässigkeit der Klassifizierung hängt stark von der Qualität und Vielfalt der Trainingsbilder ab.

    Versuchen Sie Folgendes:

    - Weitere Trainingsbilder hinzufügen
    - verschiedene Objektpositionen verwenden
    - verschiedene Drehungen verwenden
    - die Lichtverhältnisse konstant halten
    - Stellen Sie sicher, dass das Objekt gut sichtbar ist.
    - Reflexionen oder Schatten reduzieren
    - Prüfen, ob die Klassen optisch voneinander zu unterscheiden sind

    Sollte die Klassifizierung noch instabil sein, beginnen Sie mit weniger Klassen und fügen Sie später weitere hinzu.

---

??? question "Die Anomalieerkennung funktioniert nicht zuverlässig. Was sollte ich überprüfen?"

    Die Anomalieerkennung hängt von einem stabilen Bild und in vielen Fällen von einem zuverlässigen Objektlokalisierer ab.

    Bitte überprüfen Sie Folgendes:

    - Das Objekt wird konsistent positioniert.
    - Das Bild ist scharf und gut ausgeleuchtet.
    - Der Object Locator verfolgt das Objekt zuverlässig
    - Der Referenzbereich ist korrekt platziert.
    - Es wurden genügend gute Bilder hinzugefügt.
    - Die Trainingsparameter sind für die Objektvariation geeignet.

    !!! warning "Abhängigkeit vom Objekt-Locator"
        Sollte der Object Locator fehlschlagen, kann auch die Anomalieerkennung fehlschlagen.  
        Stellen Sie sicher, dass der Object Locator zuverlässig funktioniert, bevor Sie die Anomalieerkennung optimieren.

---

??? question "Der Objekt-Locator verfolgt das Objekt nicht zuverlässig. Was kann ich tun?"

    Der Object Locator benötigt einen eindeutigen und stabilen Referenzbereich.

    Versuchen Sie Folgendes:

    - Wählen Sie einen Teil des Objekts mit deutlichen Kanten oder hohem Kontrast aus.
    - Vermeiden Sie einheitliche oder reflektierende Bereiche
    - Kantenstärke anpassen
    - Drehung zulassen, wenn sich das Objekt drehen lässt
    - Einstellungen für Spielstand und Winkel anpassen
    - Beleuchtung und Fokus verbessern

    Sollte die Verfolgung weiterhin instabil sein, wählen Sie einen anderen Referenzbereich aus.

---

??? question "Wo finde ich Beispielprojekte für das Vision Starter Kit?"

    Die Beispielprojekte des Vision Starter Kits sind auf der Seite [Beispielprojekte](./vision_example_projects.md) aufgeführt.

    Beginnen Sie mit einem geführten Projekt, wenn Sie das Vision Starter Kit noch nicht kennen.

---

??? question "Wo finde ich vollständige Projektdateien oder den Quellcode?"

    Die GitHub.io-Dokumentation enthält Erläuterungen, Einrichtungsanleitungen und Projektübersichten.

    Die vollständigen Projektdateien und der Quellcode sollten über das [GitHub.com](https://github.com/SICKAG/SICK-Sensor-Starter-Kits){:target="_blank"}-Projekt-Repository bereitgestellt werden.

---

## Verwandte Seiten

<div class="next-step-buttons" markdown>

[Erste Schritte](./vision_getting_started.md){ .md-button }

[Beispielprojekte](./vision_example_projects.md){ .md-button }

[Beispiele für Vision-Code](./vision_code_snippets.md){ .md-button }

[Häufig gestellte Fragen](../faq.md){ .md-button }

</div>

</div>