#we do import tinker

from tkinter import *

root = Tk()

frame = Frame (root,width=600,height=600)
frame.pack()
frame.config(background="white")

#we will now use a new widget called label

label = Label(frame,text="GYM-RAT 1.0") #we need to include it in the specific frame
label.place(x=100,y=100)

root.mainloop()