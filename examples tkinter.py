import tkinter as tk
root=tk.Tk()
root.title("interface")
label=tk.Label(root, text="Hello,world!", bg="red")
label.grid(row=0,column=0)
label.pack()
def button_function():
    print("Button Clicked!")
button=tk.Button(root, text="click me",command=button_function)
root.mainloop()

