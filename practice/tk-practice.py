#we will start to use the graphics with tkinter

#as first you need to import the widgets
from tkinter import *

#the initial is to create a root object
root = Tk()
#we can start cutomizing the title of the window
root.title("GYM-RAT")
#also we can add an icon
root.iconbitmap('practice/files/image-cup.gif')
#using this code we can set an specific size and let the user re size it or not.
root.resizable(300,300)


#the term frame is where we will stablish the content so then we will use the next

#calling the frame object
frame = Frame(root,width=600,height=600) #you need to pass as argument in which root this frame will exist, w and h too
frame.pack()#after that you need to pack the frame in the root, so to do this 
frame.config(cursor="pirate")#we will use more the config property to give color, border and more
frame.config(bg="lightblue") #bg is the background
frame.config(bd=20) #the border size
frame.config(relief="sunken") #this is the shape of the border

#but you can also set the same properties of the frame to the root as is

root.config(cursor="arrow")#we will use more the config property to give color, border and more
root.config(bg="blue") #bg is the background
root.config(bd=20) #the border size
root.config(relief="ridge") #this is the shape of the border




#then we need to initialize the windows, this is like the start
root.mainloop()

