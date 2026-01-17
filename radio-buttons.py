#we will use now a new model of buttons the radio which are just one selectable of different options
from tkinter import *

#but also like other areas the most importat part is to select an action that will happen when the radio is selected

def selection ():
    #this need to get the value of option and print it, since is a 
    monitor.config(text="Value is {}".format(option.get()))

def reset():
    option.set(None) #this makes that the value of the radio does not contains the last one
    monitor.config(text="") # we also reset the value of the label 

root = Tk()

#this variable will be used to store the option selected

option = IntVar()


#this will create the different ration buttons, but still this need to be part of a set of groups
Radiobutton (root, text="Option 1", variable=option, value=1,command=selection).pack()
Radiobutton (root, text="Option 2", variable=option, value=2,command=selection).pack()
Radiobutton (root, text="Option 3", variable=option, value=3,command=selection).pack()

#this label will be used to show the value selected, in this case the integer, but we will show it after the command happens.
monitor = Label(root)
monitor.pack()

#lets now play with reset all the values on the screen, let's create a button
#you need to create the reset method of course
Button(root,text='Reset', command=reset).pack()

root.mainloop()
