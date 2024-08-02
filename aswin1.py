***
import tkinter as tk
root=tk .Tk()
root.title("Interface")
label=tk.Label(root,text ="Hello,world!",bg="red")
label.grid(row=0,column=1)
label1=tk.Label(root,text ="Hello,aswin!",bg="blue")
label1.grid(row=3,column=1)
def button_function():
   print("Button clicked!")
button = tk.Button(root, text="Click me",command=button_function)
button.grid(row=3,column=2)
button1 = tk.Button(root, text="submit",command= button_function)
button1.grid(row=4,column=0)
***  
from tkinter import*
root=tk()
et=Entry(root, width=50,font=('times',30))
entry.grid(row=5,column=0)
et.insert(0," enter your name")
def click():
 message= "hey" + et.get() + "!!!"
label=Label(root,text=message)
label.grid(row=6,column=1)
bt=Button(root,text="ok",command=click)
button.grid(row=7,column=2)
root.mainloop()