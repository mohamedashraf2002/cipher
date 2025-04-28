
import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if mode == "encrypt":
               new_char = chr(((ord(char.lower()) - 97 + shift_amount) %26) + 97)
            elif mode == "decrypt":
                new_char = chr(((ord(char.lower()) - 97 - shift_amount) %26) + 97)

            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result
def monoalphabetic_cipher(text, key, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for char in text:
        if char.isalpha():
            if mode == "encrypt":
                new_char = key[alphabet.index(char.lower())]
            elif mode == "decrypt":
                 new_char = alphabet[key.index(char.lower())]

            result += new_char.upper() if char.isupper() else new_char
        else:
            result += char
    return result
def vigenere_cipher(text, key, mode):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  result = ""
  key_index = 0
  for char in text:
      if char.isalpha():
         shift = alphabet.index(key[key_index % len(key)].lower())
         if mode == "encrypt":
             new_char = chr(((ord(char.lower()) - 97 + shift) % 26) +97)

         elif mode == "decrypt":
             new_char = chr(((ord(char.lower()) - 97 - shift) % 26) +97)

         result += new_char.upper() if char.isupper() else new_char
         key_index += 1
      else:
       result += char

  return result

  # Cipher functions from the previous response go here
def encrypt_decrypt():
        text = input_text.get("1.0", tk.END).strip()
        key = key_entry.get()
        mode = mode_var.get()
        if mode == "caesar":
           shift = int(key)
           result = caesar_cipher(text, shift, operation_var.get())
        elif mode == "monoalphabetic":
             result = monoalphabetic_cipher(text, key, operation_var.get())
        elif mode == "vigenere":
            result = vigenere_cipher(text, key, operation_var.get())
        output_text.delete("1.0", tk.END)
        output_text.insert("1.0", result)

root = tk.Tk()
root.title("Ciphers")
root.configure(background='#ffffff')
style = ttk.Style()
style.theme_use('clam')
style.configure('TLabel', foreground='#000000', background='#ffffff',
font=('Helvetica', 10))
style.configure('TEntry', foreground='#000000', background='#ffffff',
font=('Helvetica', 10))
style.configure('TButton', foreground='#ffffff', background='#800000',
font=('Helvetica', 10), padding=10)
style.map('TButton', background=[('active', '#640000')])
mainframe = ttk.Frame(root, padding="10")
mainframe.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
mode_var = tk.StringVar()
operation_var = tk.StringVar()
ttk.Label(mainframe, text="Cipher:").grid(row=0, column=0, sticky=tk.W)
ttk.OptionMenu(mainframe, mode_var, "caesar", "caesar","monoalphabetic","vigenere").grid(row=0, column=1, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Operation:").grid(row=1, column=0, sticky=tk.W)
ttk.OptionMenu(mainframe, operation_var, "encrypt", "encrypt","decrypt").grid(row=1, column=1, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Key:").grid(row=2, column=0, sticky=tk.W)
key_entry = ttk.Entry(mainframe)
key_entry.grid(row=2, column=1, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Input text:").grid(row=4, column=0,sticky=tk.W)
input_text = tk.Text(mainframe, wrap=tk.WORD, width=40, height=5)
input_text.grid(row=4, column=1, sticky=(tk.W, tk.E))
ttk.Label(mainframe, text="Output text:").grid(row=8, column=0,sticky=tk.W)
output_text = tk.Text(mainframe, wrap=tk.WORD, width=40, height=10)
output_text.grid(row=8, column=1, sticky=(tk.W, tk.E))
ttk.Button(mainframe, text="Generate",command=encrypt_decrypt).grid(row=6, column=1, sticky=tk.N, pady=10)
root.mainloop()
