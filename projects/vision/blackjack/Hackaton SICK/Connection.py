import socket
import time

class BlackjackClient:
    def __init__(self, ip="192.168.0.1", port=34170):
        self.ip = ip
        self.port = port
        self.client = None

    def connect(self):
        """Establishes connection to the server."""
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((self.ip, self.port))
            print(f"Connected to {self.ip}:{self.port}")
            return True
        except Exception as e:
            print(f"Connection failed: {e}")
            self.client = None
            return False

    def disconnect(self):
        """Closes the connection."""
        if self.client:
            try:
                self.client.close()
            except:
                pass
            self.client = None
            print("Disconnected")

    def trigger_and_receive(self):
        """
        Sends the trigger bytes \x02trigger\x03 and waits for a response.
        Expected response format: "Received: Dealer ; Player1 ; Player2"
        Returns: [dealer_card_str, p1_card_str, p2_card_str] or None on failure.
        """
        if not self.client:
            if not self.connect():
                return None

        try:
            # Send trigger
            trigger_msg = b"\x02trigger\x03"
            self.client.sendall(trigger_msg)

            # Receive response
            # Note: 1024 bytes should be enough for the short string.
            response = self.client.recv(1024)
            response = self.client.recv(1024)
            response = response.decode("utf-8")
            
            print(f"Raw Response: {response}")
            
            # Parse logic
            # Handle both "Received: 10 ; As ; 4" and raw "10 ; As ; 4"
            content = response
            if "Received:" in response:
                content = response.replace("Received:", "")
            
            content = content.strip()
            parts = [p.strip() for p in content.split(";")]
            
            if len(parts) >= 3:
                # Truncate to 3 logic parts (Dealer, P1, P2) in case of extra delimiters
                return parts[:3]
            else:
                print(f"Error: Expected at least 3 parts, got {len(parts)}: {parts}")
                return None

        except Exception as e:
            print(f"Communication error: {e}")
            self.disconnect()
            return None