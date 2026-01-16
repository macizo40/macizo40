#we will use now a new model of buttons the radio which are just one selectable of different options
from tkinter import *


root = Tk()

#this variable will be used to store the option selected

option = IntVar()


#this will create the different ration buttons, but still this need to be part of a set of groups
Radiobutton (root, text="Option 1", variable=option, value=1).pack()
Radiobutton (root, text="Option 2", variable=option, value=2 ).pack()
Radiobutton (root, text="Option 3", variable=option, value=3).pack()

root.mainloop()
