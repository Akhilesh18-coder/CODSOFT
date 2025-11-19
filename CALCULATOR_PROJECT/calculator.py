import tkinter as tk

# Function to update the expression in the screen
def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + value)

# Function to clear the screen
def clear_screen():
    entry.delete(0, tk.END)

# Function to calculate the result
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Creating the main window
window = tk.Tk()
window.title("GUI Calculator")
window.geometry("300x400")

# Display screen
entry = tk.Entry(window, width=20, font=("Arial", 20), borderwidth=2, relief="solid")
entry.pack(pady=10)

# Buttons frame
frame = tk.Frame(window)
frame.pack()

# Buttons list
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

# Adding buttons dynamically
row = 0
col = 0
for button in buttons:
    if button == "=":
        btn = tk.Button(frame, text=button, width=5, height=2, command=calculate)
    else:
        btn = tk.Button(frame, text=button, width=5, height=2,
                        command=lambda b=button: button_click(b))
    
    btn.grid(row=row, column=col, padx=5, pady=5)
    
    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
clear_button = tk.Button(window, text="Clear", width=15, height=2, command=clear_screen)
clear_button.pack(pady=10)

window.mainloop()
