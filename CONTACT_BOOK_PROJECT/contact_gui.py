import tkinter as tk
from tkinter import messagebox

# Contact list (stored as a list of dictionaries)
contacts = []

# Add contact function
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    messagebox.showinfo("Success", "Contact added successfully!")
    clear_inputs()
    view_contacts()

# View all contacts
def view_contacts():
    listbox.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        listbox.insert(tk.END, f"{idx+1}. {contact['name']} - {contact['phone']}")

# Search contacts
def search_contact():
    query = search_entry.get().lower()
    listbox.delete(0, tk.END)

    for idx, contact in enumerate(contacts):
        if query in contact["name"].lower() or query in contact["phone"]:
            listbox.insert(tk.END, f"{idx+1}. {contact['name']} - {contact['phone']}")

# Update selected contact
def update_contact():
    try:
        index = listbox.curselection()[0]
        selected_contact = contacts[index]

        selected_contact["name"] = name_entry.get()
        selected_contact["phone"] = phone_entry.get()
        selected_contact["email"] = email_entry.get()
        selected_contact["address"] = address_entry.get()

        messagebox.showinfo("Updated", "Contact updated successfully!")
        view_contacts()
        clear_inputs()
    except:
        messagebox.showerror("Error", "Select a contact to update!")

# Delete selected contact
def delete_contact():
    try:
        index = listbox.curselection()[0]
        contacts.pop(index)
        messagebox.showinfo("Deleted", "Contact deleted!")
        view_contacts()
        clear_inputs()
    except:
        messagebox.showerror("Error", "Select a contact to delete!")

# Load selected contact into input fields
def load_contact(event):
    try:
        index = listbox.curselection()[0]
        contact = contacts[index]

        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)

        name_entry.insert(0, contact["name"])
        phone_entry.insert(0, contact["phone"])
        email_entry.insert(0, contact["email"])
        address_entry.insert(0, contact["address"])
    except:
        pass

# Clear input fields
def clear_inputs():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


# Tkinter window
window = tk.Tk()
window.title("Contact Book - GUI")
window.geometry("450x550")

# Title
title = tk.Label(window, text="Contact Book", font=("Arial", 18))
title.pack(pady=10)

# Input fields
frame = tk.Frame(window)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Address").grid(row=3, column=0)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1)

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack()

tk.Button(btn_frame, text="Add", width=10, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", width=10, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", width=10, command=delete_contact).grid(row=0, column=2, padx=5)

# Search box
tk.Label(window, text="Search Contact").pack()
search_entry = tk.Entry(window, width=30)
search_entry.pack()
tk.Button(window, text="Search", command=search_contact).pack(pady=5)

# Contact list view
listbox = tk.Listbox(window, width=50, height=10)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", load_contact)

tk.Button(window, text="Show All Contacts", command=view_contacts).pack()

window.mainloop()
