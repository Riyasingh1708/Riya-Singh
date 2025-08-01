import tkinter as tk

# Function to update the expression
def press(num):
    entry_text.set(entry_text.get() + str(num))

# Function to evaluate the final expression
def equalpress():
    try:
        total = str(eval(entry_text.get()))
        entry_text.set(total)
    except:
        entry_text.set("Error")

# Function to clear the input field
def clear():
    entry_text.set("")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.configure(bg="lightgray")

# Entry field
entry_text = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_text, font=('Arial', 20), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=20)

# Button layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('.',4,1), ('=',4,2), ('+',4,3),
    ('C',5,0)
]

# Create and place buttons
for (text, row, col) in buttons:
    if text == '=':
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="green", fg="white", command=equalpress)
    elif text == 'C':
        btn = tk.Button(root, text=text, padx=140, pady=20, font=('Arial', 14), bg="red", fg="white", command=clear)
        btn.grid(row=row, column=col, columnspan=4)
        continue
    else:
        btn = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Run the application
root.mainloop()