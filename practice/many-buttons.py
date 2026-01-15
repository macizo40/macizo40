from tkinter import *

#lets start doing some actions like what is we have a simple calculation in the buttons

def operation ():
    #this operation will be kind different due is managing in the GUI
    result.set (float(number1.get()) + float(number2.get()))
    clean_values() #calling clean to set text values to nothing

#lets define a method that cleand the text values after the button is clicked

def clean_values():
    #we will net just to set the values to nothing
    number1.set("")
    number2.set("")
    #now this need to be called in the operation method

root = Tk()
#lets use borders to give more presentation to this code
root.config(bd=15) #this are the spaces that we will set to the elements.

#create the calculations variables, since they need to exist to be used in the calculations.
number1 = StringVar()
number2 = StringVar()
result = StringVar()

#now lets create the entry fields in the GUI
#we can set labels to identify the values that we will input
Label(root, text="First value").pack()
Entry (root, justify="Center", textvariable=number1).pack() #you can see that in the textvariable you point 
Label(root, text="Second value").pack()
Entry (root, justify="Center", textvariable=number2).pack() #this is the second value
Label(root, text="Result").pack()
Entry (root, justify="Center", textvariable=result, state="disabled").pack() #this is final result



#we do define the button and the method that will do the actions, the method need to exist before this
Button (root,text="Operation",command=operation).pack()



root.mainloop()
