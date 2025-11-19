import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        tasks.pop(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# GUI Window
window = tk.Tk()
window.title("To-Do List App")
window.geometry("300x400")

# Title
title = tk.Label(window, text="To-Do List", font=("Arial", 16))
title.pack(pady=10)

# Task Entry Box
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

# Add Button
add_btn = tk.Button(window, text="Add Task", command=add_task)
add_btn.pack(pady=5)

# Listbox to show tasks
listbox = tk.Listbox(window, width=25, height=10, font=("Arial", 12))
listbox.pack(pady=10)

# Delete Button
delete_btn = tk.Button(window, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

window.mainloop()
