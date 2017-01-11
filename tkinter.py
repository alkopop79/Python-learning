from Tkinter import *

def prnt():
	print "errrr"

root=Tk(className="My first GUI")
root.geometry("500x500")
bttn=Button(root,text="button",command=prnt)
bttn.pack()

root.mainloop() 
