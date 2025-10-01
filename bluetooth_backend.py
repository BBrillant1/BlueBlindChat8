import threading
import time
from crypto import encrypt_message

class BluetoothManager:
    def __init__(self):
        self.devices = []
        self.callback = None
        self.running = False

    def start_scan(self, callback):
        self.callback = callback
        self.running = True
        threading.Thread(target=self.scan_loop, daemon=True).start()

    def scan_loop(self):
        while self.running:
            time.sleep(15)
            if self.callback:
                # Simuler un message chiffré réel pour démo (message "Hello" envoyé par Utilisateur1)
                encrypted = encrypt_message("Hello")
                self.callback(encrypted, "Utilisateur1")

    def send(self, encrypted_text):
        # Simuler l'envoi Bluetooth (à compléter avec pyjnius ou plyer si matériel réel)
        pass