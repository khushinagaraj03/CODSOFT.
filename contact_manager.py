import tkinter as tk
from tkinter import messagebox, simpledialog
import csv
import os

filename = 'contacts.csv'

# Initialize file if it doesn't exist
if not os.path.isfile(filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Phone", "Email", "Address"])

# Functions
def add_contact():
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if name and phone:
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, phone, email, address])
        clear_fields()
        load_contacts()
        messagebox.showinfo("Success", "Contact added successfully.")
    else:
        messagebox.showerror("Error", "Name and Phone are required.")

def load_contacts():
    listbox.delete(0, tk.END)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def search_contact():
    query = entry_search.get().lower()
    listbox.delete(0, tk.END)
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if query in row[0].lower() or query in row[1]:
                listbox.insert(tk.END, f"{row[0]} - {row[1]}")

def delete_contact():
    selected = listbox.curselection()
    if selected:
        name_phone = listbox.get(selected[0])
        name = name_phone.split(" - ")[0]

        rows = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for row in rows:
                if row and row[0] != name:
                    writer.writerow(row)

        load_contacts()
        messagebox.showinfo("Deleted", "Contact deleted successfully.")
    else:
        messagebox.showwarning("Select", "Please select a contact to delete.")

def update_contact():
    selected = listbox.curselection()
    if selected:
        old_name = listbox.get(selected[0]).split(" - ")[0]
        with open(filename, 'r') as file:
            reader = list(csv.reader(file))
        for row in reader:
            if row and row[0] == old_name:
                name = simpledialog.askstring("Update", "Enter new name:", initialvalue=row[0])
                phone = simpledialog.askstring("Update", "Enter new phone:", initialvalue=row[1])
                email = simpledialog.askstring("Update", "Enter new email:", initialvalue=row[2])
                address = simpledialog.askstring("Update", "Enter new address:", initialvalue=row[3])
                row[:] = [name, phone, email, address]

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(reader)

        load_contacts()
        messagebox.showinfo("Updated", "Contact updated successfully.")
    else:
        messagebox.showwarning("Select", "Please select a contact to update.")

def clear_fields():
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Contact Management System")
root.geometry("500x600")

# Input Fields
tk.Label(root, text="Name").pack()
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Phone").pack()
entry_phone = tk.Entry(root)
entry_phone.pack()

tk.Label(root, text="Email").pack()
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root, text="Address").pack()
entry_address = tk.Entry(root)
entry_address.pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact).pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact).pack(pady=5)

tk.Label(root, text="Search Contact").pack()
entry_search = tk.Entry(root)
entry_search.pack()
tk.Button(root, text="Search", command=search_contact).pack(pady=5)

# Listbox to show contacts
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Load contacts on startup
load_contacts()

root.mainloop()
