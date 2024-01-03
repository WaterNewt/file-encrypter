from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64
import sys

def generate_key(password):
    password = password.encode()
    salt = b'salt_'  # Change this salt for better security
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key

def encrypt_text(text, password, key=None):
    if key == None:
        key = generate_key(password)
    fernet = Fernet(key)
    encrypted_text = fernet.encrypt(text)
    return encrypted_text

def decrypt_text(encrypted_text, password):
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted_text = fernet.decrypt(encrypted_text)
    return decrypted_text

def clean_exit(message: str):
    print(message)
    sys.exit(0)