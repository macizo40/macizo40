#lets now test some popups windows in the GUI

from tkinter import *
from tkinter import messagebox

root = Tk()

#the objective is to have a button that will do an action, we need a method

def test():
    #now lets call here the messagebox
    messagebox.showinfo("My Test","Clicked") #this needs two values,first is the title in the window, second is the text inside the window
    messagebox.showwarning("Alert","Alarm is activated") #this kind does show a warning message
    messagebox.showerror("Error","Out of memory error") # this show an error box
    #this method does return a yes or no string value so you can save it to do an action
    result = messagebox.askquestion("Exit","Are you sure to exit?")
    #now that you got the message is time to do something
    if result == "yes":
        root.destroy() #this quits all the windows

    #there is another variant insted say yes or no, it says ok or cancel, this also needs to catch the result

    result = messagebox.askokcancel("Overwritte","Confirm overwritte the file?")

    #in this case result is a boolean, true or false, so we can directly used it 

    if result:
        root.destroy()



#define a button that will call the method
Button(root,text="Clickme", command=test).pack()

root.mainloop()