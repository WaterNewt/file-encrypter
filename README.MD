
# Encryption and Decryption Tool

This is a Python-based tool that offers both a Graphical User Interface (GUI) and a Command Line Interface (CLI) to encrypt and decrypt sensitive information within files.

## Features

- **Encryption:** Securely encrypt files using a chosen password.
- **Decryption:** Decrypt encrypted files with the correct password.
- **User-Friendly Interface:** Choose between a GUI or CLI based on your preference.

## Usage

### Command Line Interface (CLI)

The CLI supports various commands for encryption and decryption.
![enter image description here](https://i.imgur.com/0sld16c.gif)
#### Commands:


``python3 main.py <file> -e/-d -p <password>``

 - '-e' or '--encrypt' for Encryping the file
 - '-d' or '--decrypt' for Decrypting the file
 - '-p' or '--password' for specifying the password
 - '-g' or '--gui' for opening GUI window
#### Examples:
##### Encrypting:
``python3 main.py image.jpg -e -p password123``
##### Decrypting:
``python3 main.py image.jpg -d -p password123``

### Graphical User Interface (GUI)
The GUI offers an intuitive and user-friendly way to interact with the tool.

 - Encrypt/Decrypt: Pick between 'Encrypt'ing or 'Decrypt'ing the selected file
 - Password: The password which will be used to encrypt/decrypt the file
 - Output (Optional): The file that will be outputted to. If not specified, it will replace the original file.
 - Select File: A button that will open a file select dialog, to select the file

### Aditional Notes
- Always ensure the correct password is specified while decrypting the file
- Log files are created for debugging (`log.log`)
- If you recieve a `ModuleNotFoundError`, you might have to install the modules with command: ```pip3 install -r requirements.txt```