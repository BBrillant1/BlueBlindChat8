from cryptography.fernet import Fernet
import os

KEY_FILE = "fernet.key"

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

key = load_key()
cipher = Fernet(key)

def encrypt_message(msg):
    return cipher.encrypt(msg.encode())

def decrypt_message(encrypted):
    return cipher.decrypt(encrypted).decode()