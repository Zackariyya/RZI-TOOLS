from tkinter import *
import time
window = Tk()
root = tk.Tk()
window.title("RZI SERVICES")
window.geometry('350x200')

lbl = Label(window, text="STOPPED")
lbl.grid(column=0, row=0)
def c():
    btn2.destroy()
    btn.destroy()
    lbl.destroy()
    
    
btn2 = Button(window, text="Start GUI", command=c)



def clicked():
    lbl.configure(text="RZI.exe is running")
    btn2.grid(column=2, row=1)
    window.title("GUI")


btn = Button(window, text="Run RZI services", command=clicked)
btn.grid(column=2, row=0)


window.mainloop()
