#this practice is almost the same of the previous buttons.py but now lets put the out put in the window
from tkinter import *
#we do use the same methods to insert and run the objects 
root = Tk()

# we will use now a button that is clickable, with an action

#first lets define a quick method or function, which will be excuted when you click the button
def clickme ():
    print("You click me")

#to do something in the window, lets first define a method example create a label

def create_label ():
    #this need to follow the same process as any other graphic object
    Label(root,text="Dynamic label creation").pack()

#as you can see the parameter command will call the method this output will be in the console due print is a console method
Button(root,text="Click me", command=create_label).pack()

root.mainloop()