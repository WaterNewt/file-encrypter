import utils
import sys
import customtkinter as ct
from customtkinter import filedialog
from CTkMessagebox import CTkMessagebox as ctmsg
import subprocess
import logging
import argparse

max_args = 4
specificed_args = len(sys.argv)-1
filename = sys.argv[0]
logging.basicConfig(filename="log.log", encoding="utf-8", level=logging.DEBUG)

argument_err_message = f"Error:\n{str(specificed_args)}/{str(max_args)} arguments were specified\nUse -h for help"
password_err_message = "Error:\nIncorrect password"
help_message = f"""\nThis is a program, that is used to encrypt and decrypt files.\nCreated by Yunus Ruzmetov\n\n\n-h / --help: Show this help menu
\nRequired arguments:\n1st: filename: The file that will be encrypted or decrypted.\n\n -e: Encrypt the file\n -d: Decrypt the file\n -p / --password: The password that will be used to encrypt/decrypt the file.\n-g / --gui: Opens a user-friendly gui menu.\n\nExamples:\nEncrypting:\npython3 {filename} image.png -e -p testpass123\n\nDecrypting:\npython3 {filename} image.jpg -d -p testpass123"""
argument_err_message1 = help_message


def cli(args):
    file = args.file
    password = args.password

    if args.encrypt:
        text = open(file, 'rb').read()
        encrypted = utils.encrypt_text(text, password)
        open(file, 'wb').write(encrypted)
        print("Successfully encrypted file.")
        logging.info(f"Encrypted file '{file}'")
        return encrypted
    elif args.decrypt:
        encrypted = open(file, 'rb').read()
        decrypted = utils.decrypt_text(encrypted, password)
        open(file, 'wb').write(decrypted)
        print("Successfully decrypted file.")
        logging.info(f"Decrypted file '{file}'")
        return decrypted

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files")

    parser.add_argument('file', type=str, help="The file to be encrypted or decrypted")
    parser.add_argument('-e', '--encrypt', action='store_true', help="Encrypt the file")
    parser.add_argument('-d', '--decrypt', action='store_true', help="Decrypt the file")
    parser.add_argument('-p', '--password', type=str, required=True, help="Password for encryption/decryption")

    args = parser.parse_args()

    if args.encrypt and args.decrypt:
        parser.error("Either encrypt or decrypt, not both")

    if not (args.encrypt or args.decrypt):
        parser.error("Specify either -e/--encrypt or -d/--decrypt")

    cli(args)

class gui:
    ct.set_appearance_mode("system")
    ct.set_default_color_theme("blue")
    def submit(self):
        choice_value = self.choice.get()
        filename = self.file
        out = self.output.get()
        passw = self.password.get()
        if filename=="" or passw=="":
            logging.error(msg="Required entries can not be empty!")
            error = ctmsg(title="Error", message="Required entries can not be empty!", icon="cancel", option_1="Ok")
            if error.get()=="Ok":
                self.root.destroy()
                gui()
        if out=="":
            logging.info(msg="Empty output, the file will be replaced.")
            out = self.file
        if choice_value=="Encrypt":
            logging.info(msg=f"Encrypting file '{filename}'")
            text = open(self.file, 'rb').read()
            encrypted = utils.encrypt_text(text, passw)
            open(out, 'wb').write(encrypted)
            logging.info(msg=f"Encrypted file '{filename}'")
            success = ctmsg(title="Success", message="Successfully encrypted the file.", option_1="Ok", icon="check")
            if success.get()=="Ok":
                self.root.destroy()
                self.__init__()
        
        elif choice_value=="Decrypt":
            logging.info(msg=f"Decrypting file '{filename}'")
            try:
                encrypted = open(self.file, 'r').read()
            except UnicodeDecodeError:
                error = ctmsg(title="Error", message="You are attempting to decrypt a file which is not yet encrypted.", option_1="Ok")
                logging.error(msg="Tried to decrypt a file which is not yet encrypted.")
                if error.get()=="Ok":
                    self.root.destroy()
                    gui()
            decrypted = utils.decrypt_text(encrypted, passw)
            open(out, 'wb').write(decrypted)
            logging.info(msg=f"Decrypted file '{filename}'")
            success = ctmsg(title="Success", message="Would to open the file?", option_1="Yes", option_2="No", icon="check")
        try:
            if success.get()=='Yes':
                subprocess.call(['open', filename])
                sys.exit()
            elif success.get()=='No':
                sys.exit()
        except UnboundLocalError:
            pass
        
    def get_file(self):
        self.file = filedialog.askopenfilename()
        logging.info(msg=f"Selected file '{self.file}'")
        self.label.configure(text=self.file)
        
    def __init__(self):
        self.root = ct.CTk()
        self.root.geometry("500x400")
        self.root.title("File Encrypt")
        logging.info(msg=f"Opened GUI Window")

        self.frame = ct.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        self.choice = ct.CTkComboBox(self.frame, values=['Encrypt', 'Decrypt'])
        self.choice.pack(pady=12, padx=10)

        self.password = ct.CTkEntry(self.frame, placeholder_text="Password", show="•")
        self.password.pack(pady=12, padx=10)

        self.output = ct.CTkEntry(self.frame, placeholder_text="Output (Optional)")
        self.output.pack(pady=12, padx=10)

        self.file = ct.CTkButton(self.frame, text="Select File", command=self.get_file)
        self.file.pack(pady=12, padx=10)

        self.label = ct.CTkLabel(self.frame, text="No file selected")
        self.label.pack(pady=12, padx=10)

        self.submit = ct.CTkButton(self.root, text="Submit", command=self.submit)
        self.submit.pack(pady=12, padx=10)

        self.root.mainloop()
        logging.info(msg="Exiting software")
        
if __name__=="__main__":
    if "-h" in sys.argv or "--help" in sys.argv:
        utils.clean_exit(help_message)
    if "-g" in sys.argv or "--gui" in sys.argv:
        logging.info(msg="Selected interface GUI")
        gui()
    else:
        logging.info(msg="Selected interface CLI")
        main()