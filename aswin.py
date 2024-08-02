from tkinter import *
root=Tk()
et=Entry(root, width=50,font=('times',30))
et.pack()
et.insert(0," enter your name")
def click():
  
    message= "hey" + et.get() + "!!!"
    label=Label(root,text=message)
    label.pack()
bt=Button(root,text="ok",command=click)
bt.pack()
root.mainloop()