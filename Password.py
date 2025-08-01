import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password:-
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid positive number for password length.")

# Create main window:-
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

# Title label:-
title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Password length input:-
length_label = tk.Label(root, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10, justify="center")
length_entry.pack(pady=5)

# Generate button:-
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
generate_btn.pack(pady=10)

# Result display:-
result_label = tk.Label(root, text="Generated Password:", font=("Arial", 12), bg="#f0f0f0")
result_label.pack()
result_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=5)

# Run the GUI loop:-
root.mainloop()