# Menschliches Klavier / Luftklavier
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
      <td>Erstellen Sie mehrere Spielfelder und eine einfache Python-Anwendung, die bei Regelverstößen auf den Spielfeldern Töne abspielt.</td>
      <td>Fortgeschritten</td>
      <td>30–60 Minuten</td>
      <td>Mehrere Personen oder Gegenstände</td>
    </tr>
  </tbody>
</table>

![Klavier](../images/piano.jpg)

Ziel dieses Projekts ist es, die Tasten eines Klaviers zu simulieren, indem Felder gezeichnet werden, die unterschiedliche Töne erzeugen, wenn sie von Objekten berührt werden. Ein einfaches Python-Skript steuert die Logik der verschiedenen Töne.

## Anleitung

**Hinweis:** Die genannten Codeausschnitte dienen lediglich als Beispiele. Sie können gerne Ihren eigenen Code verwenden, um das Projekt auszuführen.

### Feldbewertung

- Schließen Sie Ihr Gerät wie unter [Erste Schritte](./lidar_getting_started.md) beschrieben an. Die Benutzeroberfläche sollte nun in etwa so aussehen:

![LiDAR 1](../images/LiDAR_1.png)

- Melden Sie sich als **Service** an, Passwort: **servicelevel**, und klicken Sie auf **Standardpasswort beibehalten**
- Wählen Sie **Anwendung** > **Feldauswertung** und zeichnen Sie ein Feld in geeigneter Größe ein.

![LiDAR 3](../images/LiDAR_3.png)

- Falls erforderlich, führen Sie ein **Teach-in** durch, um alle statischen Objekte zu ignorieren. Beenden Sie das Teach-in nach etwa 10 Sekunden.

![LiDAR 2](../images/LiDAR_2.png)

- Legen Sie die Feldparameter fest, z. B. die maximale Ausblendgröße, die der minimalen Objektgröße entspricht, die das Feld überschreitet.

![LiDAR 4](../images/LiDAR_4.png)

- Zeichnen Sie mehrere Felder direkt nebeneinander.

![LiDAR-Klavier](../images/lidar_piano.png)

- Sie können **Ausgabe** ignorieren

### Programmierung

- Öffnen Sie eine Programmierumgebung für Python, beispielsweise Visual Studio Code.
- Geben Sie den folgenden Code ein:

```python
import socket

HOST = "192.168.0.1"
PORT = 2111

def sopas(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        telegram = b"\x02" + cmd.encode("ascii") + b"\x03"
        s.sendall(telegram)
        return s.recv(1024).decode("ascii").strip("\x02\x03")

# Enable measurement
print(sopas("sMN SetAccessMode 03 F4724744"))
print(sopas("sMN LMCstartmeas"))

# Read field evaluation
response = sopas("sRN FieldEvaluationResult")
print("Field evaluation:", response)
```

- Das Ergebnis sollte in etwa so aussehen: 

![LiDAR 5](../images/LiDAR_5.png)

- **2** = Feld nicht verletzt, **4** = Feld verletzt
- Lesen Sie nun einen bestimmten Wert aus (Feld „verletzt“ oder „nicht verletzt“, z. B. um einen Ton abzuspielen oder ein Licht einzuschalten).

??? sickinfo "Code"
    ```python
    field1 = response[38:39]
    print(output)
    ```

- **38:39** bezieht sich auf die Position im Ergebnis (erste Ziffer 2 oder 4)
- Überprüfen Sie, ob das Ergebnis die richtige Position angibt (entweder 2 für „nicht verletzt“ oder 4 für „verletzt“).
- Bei einem Verstoß gegen die Feldgrenzen wird ein Ton abgespielt; andernfalls wird der Text „Fehler“ angezeigt. Wichtig: Gib in der zweiten Zeile des Codes (unterhalb des vorherigen „import socket“) den Befehl „import winsound“ ein.

??? sickinfo "Code"
    ```python
    import winsound


    if output == '4':
        winsound.Beep(200, 1000)
    else:  print('error')
    ```

- Um die Sensordaten kontinuierlich auszulesen, fügen Sie den Code in eine „while True“-Schleife ein.

??? sickinfo "Code"
    ```python
    import socket
    import winsound
    HOST = "192.168.0.1"
    PORT = 2111
    def sopas(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        telegram = b"\x02" + cmd.encode("ascii") + b"\x03"
        s.sendall(telegram)
        return s.recv(1024).decode("ascii").strip("\x02\x03")
    # Enable measurement
    print(sopas("sMN SetAccessMode 03 F4724744"))
    print(sopas("sMN LMCstartmeas"))

    while True:
    # Read field evaluation
    response = sopas("sRN FieldEvaluationResult")
    print("Field evaluation:", response)

    output= response[38:39]
    #print(output)

    if output == '4':
        winsound.Beep(200, 1000)
    else:  print('error')
    ```

- Füge alle Felder in deinen Code ein
- Wählen Sie die passenden Frequenzen für Ihre Noten aus.

??? sickinfo "Frequenzen"
    ![Frequenzen](../images/frequencies.png)

- **Vollständiger Code:**

??? sickinfo "Code"
    ```python
    import winsound

    if output == '4':
        x
        import socket
    import winsound

    HOST = "192.168.0.1"
    PORT = 2111

    def sopas(cmd):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(2)
        s.connect((HOST, PORT))
        telegram = b"\x02" + cmd.encode("ascii") + b"\x03"
        s.sendall(telegram)
        return s.recv(1024).decode("ascii").strip("\x02\x03")

    # Enable measurement
    print(sopas("sMN SetAccessMode 03 F4724744"))
    print(sopas("sMN LMCstartmeas"))

    #music notes
    noteC=262
    noteD=298
    noteE=330
    noteF=350
    noteG=392
    noteA=440

    fieldposition=37
    duration=300

    while True:
    # Read field evaluation
    response = sopas("sRN FieldEvaluationResult")
    print("Field evaluation:", response)

    field1= response[fieldposition:fieldposition+1]
    field2= response[fieldposition+4:fieldposition+5]
    field3= response[fieldposition+8:fieldposition+9]
    field4= response[fieldposition+12:fieldposition+13]
    field5= response[fieldposition+16:fieldposition+17]
    field6= response[fieldposition+20:fieldposition+21]
    #print(field1 +' '+ field2)


    if field1 == '4':
        winsound.Beep(noteC, duration)
    if field2 == '4':
        winsound.Beep(noteD, duration)
    if field3 == '4':
        winsound.Beep(noteE, duration)
    if field4 == '4':
        winsound.Beep(noteF, duration)
    if field5 == '4':
        winsound.Beep(noteG, duration)
    if field6 == '4':
        winsound.Beep(noteA, duration)
    else:  print('error')
    ```
- Versuche, einen Song abzuspielen, indem du die entsprechenden Felder falsch ausfüllst.

Möchtest du weitere Schwierigkeitsstufen?

- Note nur beim Wechseln der Noten abspielen
- Halbtöne einbeziehen, d. h. benachbarte Tasten