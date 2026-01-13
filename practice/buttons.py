from tkinter import *
#we do use the same methods to insert and run the objects 
root = Tk()

# we will use now a button that is clickable, with an action

#first lets define a quick method or function, which will be excuted when you click the button
def clickme ():
    print("You click me")

#as you can see the parameter command will call the method this output will be in the console due print is a console method
Button(root,text="Click me", command=clickme).pack()

root.mainloop()