#now lets practice including images, tkinter just accept two types we will try to insert gif and pgn

#regular import:

from tkinter import *
root = Tk()

myimage = PhotoImage(file="practice/files/image-cup.gif")
Label(root, image=myimage,bd=0).pack()

root.mainloop()
