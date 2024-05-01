#6.create a GUI using Tkinter module

from tkinter import *
import tkinter.messagebox
def message():
      tkinter.messagebox.showinfo("welcome to ","python lab")
window=Tk()
window.title("welcome note")
window.geometry("900x600")
lable=Label(window,text='NIEFGC',fg='red',bg='white').pack(fill='y')
button=Button(window,text='click here',fg='red',command=message).pack(expand='false')
window.mainloop()