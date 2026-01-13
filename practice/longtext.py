from tkinter import *

root = Tk()

#we will be creating a long text field for descriptions

text = Text(root)
text.pack() #we have to pack the content always this is a basic rule
#here is the trick, with the widht 30 means that the text will have 30 characters, with the second value it means 10 lines
text.config(width=30,height=10,font=("Consolas",12),padx=20,pady=20)

root.mainloop()
