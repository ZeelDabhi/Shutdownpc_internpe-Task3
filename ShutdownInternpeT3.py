from tkinter import *
import os

win = Tk()
win.title("writed by ZD")
win.geometry("300x200")
win.resizable(0,0)

def shut():
		os.system("shutdown /s /t 1")
def res():
		os.system("shutdown /r /t 1")
def log():
		os.system("shutdown -1")
def Ret():
	  os.system("shutdown /r /t 20")

l = Label(win,text="Click On Button:",font=("Lucida Console",20,))
l.grid()

b = Button(win,text="shutdown",command=shut,bg="yellow")
b.grid(ipadx=10)

b2 = Button(win,text="restart",command=res,bg="red")
b2.grid(ipadx=10)

b3 = Button(win,text="log-out",command=log,bg="blue")
b3.grid(ipadx=10)

b4 = Button(win,text="Restart-time",command=Ret,bg="Orange")
b4.grid(ipadx=10)


win.mainloop()