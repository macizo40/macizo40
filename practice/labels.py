#now lets start using the labels inside the root

from tkinter import *

root = Tk()

#lets start using a dynamic var 
text = StringVar()
text.set("A text added via var")

#we will now use a new widget called label

#this way is to save a line of declaration
Label(root,text="GYM-RAT 1.0").pack()

Label(root,text="Checked in").pack()

#now lets do more things with label, but for this we need yes a var 

label = Label(root,text="Users")
label.pack()
label.config(bg="blue",fg="white",font=("Verdana",24))

#the string var created before need to be
label.config(textvariable=text) #in this way we do refer to the stream var

root.mainloop()