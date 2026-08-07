# Fortgeschrittene Anwendung des LiDAR-Starter-Kits
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