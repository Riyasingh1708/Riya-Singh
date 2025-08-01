import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    contacts.append(f"{name} - {phone}")
    update_listbox()
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "No contact selected.")

def update_listbox():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact)

# GUI setup
root = tk.Tk()
root.title("Simple Contact Book")
root.geometry("400x400")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone:").pack(pady=5)
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)
tk.Button(root, text="Delete Selected", command=delete_contact).pack(pady=5)

contact_list = tk.Listbox(root, width=50)
contact_list.pack(pady=20)

root.mainloop()