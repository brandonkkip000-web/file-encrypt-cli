# 🔐 file-encrypt-cli

A lightweight command-line tool to **encrypt and decrypt files securely** using **AES-256-GCM** with a password.  
Perfect for protecting sensitive documents locally without relying on third-party software.

## ✨ Features
- 🔑 AES-256-GCM encryption (strong and modern)
- 🧂 Random salt & nonce for each encryption
- 📂 Works with any file type (text, images, PDFs, etc.)
- 🖥️ Simple CLI interface

## 🚀 Installation
Clone the repository and install dependencies:

    git clone https://github.com/YOUR_USERNAME/file-encrypt-cli.git
    cd file-encrypt-cli
    pip install -r requirements.txt

Create a **requirements.txt** file with:
    cryptography

## 🛠️ Usage

### Encrypt a file
    python file_encrypt.py encrypt secret.txt --password mypass
➡️ Produces secret.txt.enc

### Decrypt a file
    python file_encrypt.py decrypt secret.txt.enc --password mypass
➡️ Produces secret.txt.dec

## ⚠️ Security Notes
- Use a **strong password** (long, random, and unique).
- This tool is for **personal/educational use**. For enterprise security, consider well-audited solutions like GPG or OpenSSL.
- Encrypted files cannot be recovered if the password is lost.

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing
Pull requests are welcome! If you’d like to add features or fix bugs, fork the repo and submit a PR.

## 👤 Author
**Brandon**  
[GitHub Profile](https://github.com/brandonkkip000-web)
