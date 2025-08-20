import tkinter as tk
import random
from tkinter import messagebox

# Initialize scores
user_score = 0
comp_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play a round
def play(user_choice):
    global user_score, comp_score

    comp_choice = random.choice(choices)
    result = ""

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Scissors" and comp_choice == "Paper") or \
         (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    result_label.config(text=f"Your choice: {user_choice}\nComputer's choice: {comp_choice}\n\n{result}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

# Reset the game
def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text="Score - You: 0 | Computer: 0")

# Exit game
def exit_game():
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.config(bg="lightblue")

# Title
tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 20, "bold"), bg="lightblue").pack(pady=10)

# Result display
result_label = tk.Label(root, text="Make your move!", font=("Arial", 14), bg="lightblue")
result_label.pack(pady=20)

# Buttons for choices
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack()

tk.Button(button_frame, text="Rock", font=("Arial", 12), width=10, command=lambda: play("Rock")).grid(row=0, column=0, padx=10, pady=5)
tk.Button(button_frame, text="Paper", font=("Arial", 12), width=10, command=lambda: play("Paper")).grid(row=0, column=1, padx=10, pady=5)
tk.Button(button_frame, text="Scissors", font=("Arial", 12), width=10, command=lambda: play("Scissors")).grid(row=0, column=2, padx=10, pady=5)

# Score display
score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 12), bg="lightblue")
score_label.pack(pady=20)

# Reset & Exit buttons
tk.Button(root, text="Play Again", command=reset_game, bg="green", fg="white", font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Exit", command=exit_game, bg="red", fg="white", font=("Arial", 12)).pack(pady=5)

# Start the GUI loop
root.mainloop()