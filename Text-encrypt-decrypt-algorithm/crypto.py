import tkinter as tk
from tkinter import messagebox

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shifted = ord(char) + shift
            print(shifted+26)
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26

            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            print(shifted)
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char  # Keep non-alphabetic characters unchanged
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def encrypt_text():
    plaintext = entry_text.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())
    encrypted_text = caesar_encrypt(plaintext, shift)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", encrypted_text)

def decrypt_text():
    ciphertext = entry_text.get("1.0", tk.END).strip()
    shift = int(entry_shift.get())
    decrypted_text = caesar_decrypt(ciphertext, shift)
    text_output.delete("1.0", tk.END)
    text_output.insert("1.0", decrypted_text)

# Create the main window
window = tk.Tk()
window.title("Caesar Cipher Encryptor/Decryptor")

# Create widgets
label_text = tk.Label(window, text="Enter text:")
label_text.grid(row=0, column=0, padx=10, pady=5)

entry_text = tk.Text(window, height=5, width=50)
entry_text.grid(row=0, column=1, padx=10, pady=5)

label_shift = tk.Label(window, text="Enter shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=5)

entry_shift = tk.Entry(window)
entry_shift.grid(row=1, column=1, padx=10, pady=5)

button_encrypt = tk.Button(window, text="Encrypt", command=encrypt_text)
button_encrypt.grid(row=2, column=0, padx=10, pady=10)

button_decrypt = tk.Button(window, text="Decrypt", command=decrypt_text)
button_decrypt.grid(row=2, column=1, padx=10, pady=10)

label_output = tk.Label(window, text="Result:")
label_output.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)

text_output = tk.Text(window, height=5, width=50)
text_output.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

# Start the GUI main loop
window.mainloop()
