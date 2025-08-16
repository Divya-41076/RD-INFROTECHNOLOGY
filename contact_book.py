import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# In-memory contact list
contacts = []

# Functions
def add_contact():
    name = name_var.get()
    phone = phone_var.get()
    email = email_var.get()

    if name and phone and email:
        contacts.append({'Name': name, 'Phone': phone, 'Email': email})
        refresh_contacts()
        clear_inputs()
    else:
        messagebox.showwarning("Input Error", "All fields are required.")

def clear_inputs():
    name_var.set("")
    phone_var.set("")
    email_var.set("")

def refresh_contacts():
    contact_list.delete(*contact_list.get_children())
    for i, contact in enumerate(contacts):
        contact_list.insert('', 'end', iid=i, values=(contact['Name'], contact['Phone'], contact['Email']))

def select_contact(event):
    selected = contact_list.focus()
    if selected:
        values = contact_list.item(selected, 'values')
        name_var.set(values[0])
        phone_var.set(values[1])
        email_var.set(values[2])

def update_contact():
    selected = contact_list.focus()
    if selected:
        contacts[int(selected)] = {
            'Name': name_var.get(),
            'Phone': phone_var.get(),
            'Email': email_var.get()
        }
        refresh_contacts()
        clear_inputs()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to update.")

def delete_contact():
    selected = contact_list.focus()
    if selected:
        del contacts[int(selected)]
        refresh_contacts()
        clear_inputs()
    else:
        messagebox.showwarning("Selection Error", "Select a contact to delete.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("650x450")

# Variables
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()

# Input Fields
tk.Label(root, text="Name").pack(pady=5)
tk.Entry(root, textvariable=name_var, width=50).pack()

tk.Label(root, text="Phone").pack(pady=5)
tk.Entry(root, textvariable=phone_var, width=50).pack()

tk.Label(root, text="Email").pack(pady=5)
tk.Entry(root, textvariable=email_var, width=50).pack()

# Buttons
tk.Button(root, text="Add Contact", command=add_contact, bg="lightgreen").pack(pady=5)
tk.Button(root, text="Update Contact", command=update_contact, bg="lightblue").pack(pady=5)
tk.Button(root, text="Delete Contact", command=delete_contact, bg="tomato").pack(pady=5)

# Contact List
contact_list = ttk.Treeview(root, columns=('Name', 'Phone', 'Email'), show='headings')
contact_list.heading('Name', text='Name')
contact_list.heading('Phone', text='Phone')
contact_list.heading('Email', text='Email')
contact_list.pack(pady=10, fill=tk.BOTH, expand=True)
contact_list.bind('<ButtonRelease-1>', select_contact)

# Run App
root.mainloop()
