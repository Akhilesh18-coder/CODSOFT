import tkinter as tk
import random

# List of choices
choices = ["Rock", "Paper", "Scissors"]

# Scores
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    # Determine winner
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer's Choice: {computer_choice}")
    result_label.config(text=f"Result: {result}")
    score_label.config(text=f"Score → You: {user_score}   Computer: {computer_score}")


# Tkinter Window
window = tk.Tk()
window.title("Rock Paper Scissors - GUI")
window.geometry("400x400")

title_label = tk.Label(window, text="Rock, Paper, Scissors Game", font=("Arial", 16))
title_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(window)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, height=2, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, height=2, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Labels for displaying results
user_label = tk.Label(window, text="Your Choice: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(window, text="Computer's Choice: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(window, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

score_label = tk.Label(window, text="Score → You: 0   Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

window.mainloop()
