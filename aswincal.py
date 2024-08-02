import tkinter as tk

def append_to_display(value):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(tk.END, current + value)
    
def clear_display():
    display.delete(0, tk.END)

def calculate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(tk.END, str(result)) 
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
 
# Entry widget for display
display = tk.Entry(root, width=30, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text != '=':
        button = tk.Button(root, text=text, padx=30, pady=20, command=lambda t=text: append_to_display(t))
    else:
        button = tk.Button(root, text=text, padx=30, pady=20, command=calculate)
    button.grid(row=row, column=col, padx=5, pady=5)

# Clear button
clear_button = tk.Button(root, text="Clear", padx=20, pady=20, command=clear_display)
clear_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
