import socket
import time

# --- CONFIGURATION ---
SENSOR_IP = "192.168.0.1"
SENSOR_PORT = 2111
BUFFER_SIZE = 4096

# Codes de contrôle CoLa A
STX = b'\x02'
ETX = b'\x03'

def send_command(sock, command_str):
    """Encapsule la commande avec STX/ETX et l'envoie."""
    # CoLa A : <STX> commande <ETX>
    full_payload = STX + command_str.encode('ascii') + ETX
    print(f"Sending : {command_str}")
    sock.send(full_payload)

def receive_response(sock):
    """Lit le socket jusqu'à trouver le caractère ETX."""
    data = b""
    try:
        while ETX not in data:
            chunk = sock.recv(BUFFER_SIZE)
            if not chunk:
                break
            data += chunk
    except socket.timeout:
        print("Timed out")
        return None
    
    # Nettoyage des balises STX/ETX
    clean_data = data.replace(STX, b'').replace(ETX, b'')
    return clean_data.decode('ascii', errors='ignore')

def parse_sick_hex_signed(hex_str):
    """
    Convertit un hexadécimal (complément à deux 32 bits) en entier Python.
    Gère correctement les nombres négatifs (ex: FFFFFFAD -> -83).
    """
    try:
        val = int(hex_str, 16)
        # Si le bit de signe (32ème bit) est 1, c'est un nombre négatif
        if val & 0x80000000:
            val = -0x100000000 + val
        return val
    except ValueError:
        return 0


def get_computed_distance():
    # Initialisation de la variable à retourner pour éviter les erreurs si le calcul échoue
    computed_dist = None

    try:
        # Connexion TCP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2.0) # Timeout de 2 secondes
        print(f"Connexion to {SENSOR_IP}:{SENSOR_PORT}...")
        sock.connect((SENSOR_IP, SENSOR_PORT))
        print("Connected")

        # Login (Authorized Client)
        # D'après page 81 <STX>sMN SetAccessMode 3 F4724744<ETX>
        login_cmd = "sMN SetAccessMode 3 F4724744"
        send_command(sock, login_cmd)
        response = receive_response(sock)
        print(f"Login response : {response}")
        
        if response and "sAN SetAccessMode 1" in response:
            print("=> Login succesful")
        else:
            print("=> Login failed, unexpected response.")
            

        # Requête de la Distance Perpendiculaire (Page 194-196).
        # 'sRN' (Read by Name) pour lire la valeur une fois.
        data_cmd = "sRN perpendicularDistanceResult" 
        send_command(sock, data_cmd)
        
        raw_response = receive_response(sock)
        print(f"Raw response : {raw_response}")

        # Décodage de la trame
        # Format attendu : 
        # sRA perpendicularDistanceResult <timestamp> <Number of evaluation> <Evaluation ID> <MinDistance> ...
        if raw_response and "sRA perpendicularDistanceResult" in raw_response:
            parts = raw_response.split(' ')
            
            # Exemple de réponse : <STX>sRA{SPC}perpendicularDistanceResult{SPC}230BDCE0{SPC}1{SPC}1{SPC}20C{SPC}324{SPC}20C{SPC}FFFFFFAD{SPC}41{SPC}32{SPC}FFFFFF54{SPC}1E<ETX>
            # parts[0] = "sRA"
            # parts[1] = "perpendicularDistanceResult"
            # parts[2] = time-stamp
            # parts[3] = Number of evaluations (ex : X )
            # parts[4] = Evaluation 1 ID
            # parts[5] = Min distance
            # parts[6] = Max distance
            # parts[7] = Min distance X
            # parts[8] = Min distance Y
            # parts[9] = Min distance Z
            # parts[10] = Max distance X
            # parts[11] = Max distance Y
            # parts[12] = Max distance Z
            # parts[13] = Evaluation 2 ID (si X>=2)
            # .
            # .
            # .
            # parts[X+3] = Evaluation X ID

            if len(parts) > 4:
                
                # SICK encode souvent en Hex ASCII dans CoLa A
                val_min_hex = parts[5]
                val_max_hex = parts[6]
                val_min_x_hex = parts[7]
                val_min_y_hex = parts[8]
                val_min_z_hex = parts[9]
                
                dist_min = parse_sick_hex_signed(val_min_hex)
                dist_max = parse_sick_hex_signed(val_max_hex)
                val_min_x = parse_sick_hex_signed(val_min_x_hex)
                val_min_y = parse_sick_hex_signed(val_min_y_hex)
                val_min_z = parse_sick_hex_signed(val_min_z_hex)

                # Le calcul est effectué ici et stocké dans la variable locale
                computed_dist = (val_min_x**2 + val_min_y**2 + val_min_z**2)**0.5
                
                print("-" * 30)
                print(f"Decoded data :")
                # print(f"Min Distance: {dist_min} mm")
                # print(f"Max Distance: {dist_max} mm")
                print (f"X Min : {val_min_x} mm")
                print (f"Y Min : {val_min_y} mm")
                print (f"Z Min : {val_min_z} mm")
                print(f"Min Distance computed : {computed_dist:.2f} mm")
                print("-" * 30)
            else:
                print("Too short frame, cannot decode automaticly .")
        else:
            print("Unexpected response or unfound variable.")

    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        # Vérification que sock existe avant de fermer (au cas où l'erreur survient à la création)
        if 'sock' in locals():
            print("Fermeture de la connexion.")
            sock.close()
    
    # Retour de la valeur calculée (ou None si erreur) pour le programme appelant
    return computed_dist

# Bloc main pour exécution autonome
if __name__ == "__main__":
    # Appel de la fonction
    resultat = get_computed_distance()
    
    # Vérification et utilisation de la variable
    if resultat is not None:
        print(f"SUCCES : Fetched value : {resultat}")
    else:
        print("FAIL : Not value returned.")