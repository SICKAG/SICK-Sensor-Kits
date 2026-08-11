<!-- # Fortgeschrittene Anwendung des LiDAR-Starter-Kits
Das LiDAR-Starter-Kit ist ein leistungsstarkes Werkzeug für Entwickler und Forscher, die fortschrittliche Sensorfunktionen in ihre Projekte integrieren möchten. Dieser Leitfaden enthält detaillierte Anleitungen und Code-Beispiele, die Ihnen helfen, die Funktionen des Kits optimal zu nutzen.

Ausführlichere Informationen und Ressourcen zur Arbeit mit SICK-Geräten und deren Integration finden Sie im [Artikel „picoScan100: Protokolle und Integration“](https://support.sick.com/sick-knowledgebase/article/?code=KA-09481).


## SICK-Treiber sick_scan_xd
Für zusätzliche Funktionen und eine erweiterte Integration können Sie sich den [sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk)-Treiber ansehen. Dieser Treiber bietet erweiterte Unterstützung für SICK-LiDAR-Geräte und kann eine wertvolle Ressource für Ihre Projekte sein.

In der Welt von LiDAR sind präzise Messdaten nur so aussagekräftig wie die Software, die ihr Potenzial erschließt. Ein C++-SDK fungiert als unverzichtbares digitales Hilfsmittel, das Entwicklern direkten, leistungsstarken Zugriff auf Rohsensordaten und Konfigurationsoptionen für Echtzeitanwendungen ermöglicht.

**Funktionen**

- Empfang von Scan-, IMU- und Encoder-Daten im SICK-Datenformat „Compact“ über UDP oder TCP sowie Durchführung der Sensorkonfiguration über die REST-API
- Thread-sichere und ereignisgesteuerte Datenerfassung von mehreren Sensoren.
- Plattformübergreifendes Build-System mit CMake für Linux und Windows sowie Abhängigkeitsverwaltung über Conan 2 möglich.
- Kompatibel mit den Architekturen x86_64 und ARM64 (z. B. Raspberry Pi).
- Zahlreiche gebrauchsfertige Beispiele für schnelles Prototyping.
- Integrierte Diagnose- und Protokollierungsfunktionen.
- Umfassende Unit- und CI-Tests mit integrierten Testdaten aus der Praxis.
- Entwickelt, um die Anforderungen des EU-Gesetzes zur Cyber-Resilienz zu erfüllen.

-->

# Fortgeschrittene Anwendung des LiDAR-Starter-Kits

## Kurzbeschreibung

Diese Seite enthält fortgeschrittene Informationen zur Arbeit mit dem LiDAR-Starter-Kit.

Der Schwerpunkt liegt auf protokollbasierter Integration, Software Development Kits, erweitertem Datenzugriff und möglichen Integrationsszenarien für kundenspezifische LiDAR-Anwendungen.

## Übersicht über fortgeschrittene Themen

<table style="border-collapse: collapse; width: 100%;">
  <thead>
    <tr style="background-color: #005aff; color: white;">
      <th style="padding: 8px; text-align: left;">Thema</th>
      <th style="padding: 8px; text-align: left;">Zweck</th>
      <th style="padding: 8px; text-align: left;">Empfohlen für</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Protokolle und Integration</td>
      <td>Erfahren Sie, wie Sie auf LiDAR-Daten zugreifen und diese in externe Anwendungen integrieren können.</td>
      <td>Anwender, die auf Basis des LiDAR-Sensors eigene Software entwickeln möchten.</td>
    </tr>
    <tr>
      <td>SICK Perception SDK</td>
      <td>Verwenden Sie ein Software Development Kit für den erweiterten Zugriff auf SICK-Sensordaten.</td>
      <td>Entwickler, die an größeren oder leistungsorientierten Anwendungen arbeiten.</td>
    </tr>
    <tr>
      <td>Verarbeitung von Scandaten</td>
      <td>LiDAR-Scandaten für kundenspezifische Anwendungen empfangen und verarbeiten.</td>
      <td>Anwender, die Rohdaten oder verarbeitete Sensordaten analysieren möchten.</td>
    </tr>
    <tr>
      <td>Externe Integration</td>
      <td>Verbinden Sie LiDAR-Ergebnisse mit anderen Softwaresystemen, Dashboards oder Automatisierungslogik.</td>
      <td>Fortgeschrittene Anwender und Systemintegratoren.</td>
    </tr>
  </tbody>
</table>

<br>

## Weitere Informationen zu Produkten und Protokollen

Ausführlichere Informationen zur Arbeit mit SICK-LiDAR-Geräten, Protokollen und Integrationsmöglichkeiten finden Sie im folgenden Artikel der SICK-Knowledge-Base.

[Wissensdatenbank](https://support.sick.com/sick-knowledgebase/article/?code=KA-09481){ .md-button .button-small }

!!! note "Erweiterte Dokumentation"
    Der verlinkte Artikel enthält weitere Hintergrundinformationen zu Protokollen und Integrationsmöglichkeiten.  
    Das ist besonders nützlich, wenn Sie über die grundlegenden Beispiele des Starter-Kits hinausgehen möchten.

---

## SICK Perception SDK

Für zusätzliche Funktionen und eine erweiterte Integration können Sie sich das SICK Perception SDK ansehen.

[Sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk){ .md-button .button-small }

Das SDK bietet erweiterte Unterstützung für SICK-LiDAR-Geräte und kann eine wertvolle Ressource für anspruchsvolle Projekte sein.

Bei LiDAR-Anwendungen sind präzise Messdaten nur dann von Nutzen, wenn die Software zuverlässig auf diese Daten zugreifen, sie verarbeiten und integrieren kann.  
Ein Software Development Kit kann Entwicklern dabei helfen, auf Sensordaten zuzugreifen, Geräte zu konfigurieren und Echtzeitanwendungen zu erstellen.

---

## Wofür das SDK verwendet werden kann

Das SICK Perception SDK kann für Anwendungen nützlich sein, die über eine einfache browserbasierte Konfiguration oder einfache Code-Schnipsel hinausgehen.

Zu den typischen Anwendungsfällen gehören:

- Empfang von Scandaten
- Arbeiten mit kompakten SICK-Datenformaten
- Sensoren programmgesteuert konfigurieren
- Integration von LiDAR-Daten in benutzerdefinierte Anwendungen
- Entwicklung von Echtzeitanwendungen
- Verwendung von LiDAR-Daten auf Plattformen wie PCs oder eingebetteten Systemen

---

## Wichtigste Merkmale

<div class="requirement-box">

<h3>Core Capabilities</h3>

<ul>
  <li>Receive scan, IMU and encoder data in SICK data format Compact over UDP or TCP.</li>
  <li>Perform sensor configuration via REST API.</li>
  <li>Acquire data from multiple sensors in an event-driven and thread-safe way.</li>
  <li>Use a cross-platform build system based on CMake for Linux and Windows.</li>
  <li>Use dependency management via Conan 2.</li>
</ul>

</div>

<div class="requirement-box optional">

<h3>Additional Features</h3>

<ul>
  <li>Compatible with x86_64 and ARM64 architectures, for example Raspberry Pi.</li>
  <li>Includes ready-to-use examples for fast prototyping.</li>
  <li>Provides diagnostic and logging capabilities.</li>
  <li>Includes unit and CI tests with real-world test data.</li>
  <li>Designed to support cybersecurity-related requirements such as the EU Cyber Resilience Act.</li>
</ul>

</div>

---

## Wann sollten Sie das SDK verwenden?

Verwenden Sie das SDK, wenn Sie Anwendungen entwickeln möchten, die einen erweiterten Zugriff auf LiDAR-Daten erfordern.

<div class="strategy-grid">

  <div class="strategy-card">
    <h3>Use the Starter Kit UI</h3>
    <p>Use the browser-based user interface if you want to configure the sensor, create fields or test basic functionality.</p>
    <p>This is the best option for first demos and educational exercises.</p>
  </div>

  <div class="strategy-card">
    <h3>Use Code Examples</h3>
    <p>Use the LiDAR code examples if you want to send simple SOPAS commands or read basic measurement data with Python.</p>
    <p>This is useful for small scripts and first software experiments.</p>
  </div>

  <div class="strategy-card">
    <h3>Use the SDK</h3>
    <p>Use the SDK if you want to build more robust, scalable or performance-oriented applications.</p>
    <p>This is useful for advanced integration, sensor data processing and larger software projects.</p>
  </div>

</div>

---

## Typischer erweiterter Arbeitsablauf

Ein möglicher Arbeitsablauf für die fortgeschrittene LiDAR-Integration könnte wie folgt aussehen:

1. Führen Sie die Anleitung „Erste Schritte mit LiDAR“ durch.
2. Führen Sie eine einfache Demo zur Feldauswertung durch.
3. Testen Sie die grundlegenden LiDAR-Code-Beispiele.
4. Scan- oder Feldauswertungsdaten mit Python auslesen.
5. Entscheiden Sie, ob einfache Skripte ausreichen.
6. Sollte eine umfassendere Integration erforderlich sein, sehen Sie sich das SICK Perception SDK an.
7. Entwickeln Sie eine benutzerdefinierte Anwendung, die LiDAR-Daten verarbeitet oder visualisiert.

---

## Ideen zur Integration

Das LiDAR-Starter-Kit lässt sich je nach Anwendungsfall auf verschiedene Weise erweitern.

Mögliche Ideen für eine weitergehende Integration:

- Ein Dashboard für Live-LiDAR-Daten erstellen
- Scandaten in einer externen Anwendung anzeigen
- die Ergebnisse der Feldbewertung mit akustischem oder optischem Feedback kombinieren
- LiDAR-Daten für interaktive Installationen nutzen
- LiDAR-Daten mit einem Roboter, einer SPS oder einem Steuerungssystem verbinden
- Prozessabstandswerte für Mess- oder Überwachungsaufgaben
- Mehrere Sensoren in einer Anwendung kombinieren

---

## Bezug zu den Code-Beispielen

Auf der Seite „LiDAR-Code-Beispiele“ finden Sie kurze Python-Codeausschnitte für die grundlegende Kommunikation.

Nutzen Sie die Seite „Code-Beispiele“, wenn Sie Folgendes tun möchten:

- Eine TCP-Verbindung testen
- Gerätetyp auslesen
- Scandaten anfordern
- Ergebnisse der Feldauswertung lesen
- die grundlegende Handhabung von SOPAS-Befehlen verstehen

[LiDAR-Code-Beispiele](./lidar_code_snippets.md){ .md-button .button-small }

Bei größeren Softwareprojekten ist das SDK möglicherweise der bessere Ausgangspunkt.

---

## Zusammenfassung

Auf dieser Seite wurden erweiterte Anwendungsmöglichkeiten für das LiDAR-Starter-Kit vorgestellt.

Sie haben erfahren, wo Sie weitere Informationen zu Protokollen und zur Integration finden, in welchen Fällen das SICK Perception SDK nützlich sein kann und wie fortgeschrittene Anwender von einfachen Code-Beispielen zu robusteren LiDAR-Softwareanwendungen übergehen können.

Die fortgeschrittenen Themen sind besonders nützlich, wenn Sie über die grundlegenden Demos des Starter-Kits hinausgehen und LiDAR-Daten in Ihre eigene Software oder Systemumgebung integrieren möchten.

## Nächste Schritte

Weiter zu den Schulungsunterlagen, Beispielprojekten oder dem SICK Perception SDK.

<div class="next-step-buttons" markdown>

[Schulungsmaterial](./lidar_training_material.md){ .md-button }

[Beispielprojekte](./lidar_example_projects.md){ .md-button }

[Sick_perception_xd](https://github.com/SICKAG/sick_perception_sdk){ .md-button }

</div>