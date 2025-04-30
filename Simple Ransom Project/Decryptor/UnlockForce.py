import os
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox
import time

# Target extension
EXTENSIONS = ['.txt', '.jpg', '.pdf', '.docx']

# Load key
def load_key():
    return open("key.key", "rb").read()

# Decrypt files
def decrypt_files(key):
    fernet = Fernet(key)
    folder_path = os.path.expanduser("~/Documents")
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if any(file_name.endswith(ext) for ext in EXTENSIONS):
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "rb") as file:
                        data = file.read()
                    decrypted_data = fernet.decrypt(data)
                    with open(file_path, "wb") as file:
                        file.write(decrypted_data)
                except Exception as e:
                    print(f"Error decrypting {file_path}: {e}")

# Delete ransom note
def delete_ransom_note():
    doc = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents')
    note_path = os.path.join(doc, "README_LOCKED.txt")
    if os.path.exists(note_path):
        os.remove(note_path)

# Popup notification
def popup():
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo("UnlockForce", "Files have been decrypted successfully!")

def main():
    key = load_key()
    decrypt_files(key)
    delete_ransom_note()
    popup()
    time.sleep(5)

if __name__ == "__main__":
    main()
