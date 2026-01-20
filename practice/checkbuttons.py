from tkinter import *
#now we will practice with a different kind of button the check ones, a check box can one or more, radio, is more to be only one
# we do neet the method to get the value

def selection ():
    #this will be an empty string
    myselection = ""

    #now lets manage the selection

    if (cream.get()):
        myselection += "with cream"
    else:
        myselection += "no cream"

    #same for the second value

    if (chocolat.get()):
        myselection += "with chocolat"
    else:
        myselection += "no chocolat"

    #finally we pass the text that we have generated
    monitor.config(text=myselection)


root = Tk()
root.title("Creppe")
root.config(bd=15)

#lets image that we want a creppe and we want some chocolat and cream

cream = IntVar() #values to be true or false are 1 or 0
chocolat = IntVar() #1 is for true and 0 for false

#we can play more adding as example an image

myimage = PhotoImage(file="image.gif")
Label(root, image=myimage).pack(side="left")

#remember giving more design to the GUI with a frame

frame = Frame(root)
frame.pack(side="right")

#instead of adding the label and the butto to root we add it to frame
Label(frame, text="Do you want some extras?").pack(anchor="w") #we define anchor to align all the objects
#the big difference here is that this has to different attributes to assign a value when is check or not, you will be able to play with it
Checkbutton(frame, text="yes cream",variable=cream, onvalue=1, offvalue=0, command=selection).pack(anchor="w")
Checkbutton(frame,text="yes chocolat",variable=chocolat, onvalue=1, offvalue=0, command=selection).pack(anchor="w")

#now we need to add the command that is the method that we will get the values of the check buttons

monitor = Label(frame)
monitor.pack()

root.mainloop()