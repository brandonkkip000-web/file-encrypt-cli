import argparse
import os
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import secrets

def derive_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(path: str, password: str):
    with open(path, "rb") as f:
        data = f.read()

    salt = secrets.token_bytes(16)
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    nonce = secrets.token_bytes(12)
    ciphertext = aesgcm.encrypt(nonce, data, None)

    with open(path + ".enc", "wb") as f:
        f.write(salt + nonce + ciphertext)

    print(f"Encrypted -> {path}.enc")

def decrypt_file(path: str, password: str):
    with open(path, "rb") as f:
        raw = f.read()

    salt, nonce, ciphertext = raw[:16], raw[16:28], raw[28:]
    key = derive_key(password, salt)
    aesgcm = AESGCM(key)
    data = aesgcm.decrypt(nonce, ciphertext, None)

    out_path = path.replace(".enc", ".dec")
    with open(out_path, "wb") as f:
        f.write(data)

    print(f"Decrypted -> {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Encrypt/Decrypt CLI (AES-GCM)")
    parser.add_argument("mode", choices=["encrypt", "decrypt"])
    parser.add_argument("file", help="Path to file")
    parser.add_argument("--password", required=True, help="Password")

    args = parser.parse_args()
    if args.mode == "encrypt":
        encrypt_file(args.file, args.password)
    else:
        decrypt_file(args.file, args.password)
