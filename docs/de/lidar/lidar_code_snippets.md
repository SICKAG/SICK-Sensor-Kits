# Code-Schnipsel LiDAR

Im Folgenden finden Sie einige Beispiel-Codeausschnitte, die Ihnen den Einstieg in die Arbeit mit dem LiDAR-Sensor-Kit erleichtern sollen:

## Gerätetyp auslesen
Das LiDAR-Starter-Kit bietet Entwicklern erweiterte Funktionen zur Anpassung und Optimierung ihrer Anwendungen. In diesem Leitfaden wird erläutert, wie Sie programmgesteuert mit dem Gerät interagieren und es für bestimmte Anwendungsfälle konfigurieren können.
```python
import socket
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"\x02sRN DItype\x03")
    data = s.recv(1024)
 
print(f"Received {data}")
```

## Scandaten lesen
Um Scandaten vom LiDAR-Starter-Kit abzurufen, können Sie das folgende Python-Skript verwenden. Dieses Skript veranschaulicht, wie man einen Befehl an das Gerät sendet und die entsprechende Antwort mit den Scandaten empfängt.
```python
import socket
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"\x02sRN LMDscandata\x03")
    data = s.recv(1024)
 
print(f"Received {data}")
```

## Scandaten kontinuierlich lesen
Um kontinuierlich Scandaten vom LiDAR-Starter-Kit auszulesen, können Sie das folgende Python-Skript verwenden. Dieses Skript ermöglicht es dem Gerät, Scandaten in Echtzeit zu senden, die dann je nach Bedarf für Ihre Anwendung verarbeitet werden können.
```python
import socket
import time
 
HOST = "192.168.0.1" 
PORT = 2111
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b"\x02sEN LMDscandata 1\x03")
         
    while True:
        data = s.recv(2048)
        print(data)
```