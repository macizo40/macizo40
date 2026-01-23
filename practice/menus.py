from tkinter import *
#we are now will be working with Menus this are the regular ones in any application
root  = Tk()

#there are some some non stablished rules but the common programming practices does suggest follow this

#we need to set a master menu, this is usually called
menubar = Menu(root)
root.config(menu=menubar)

#now it is time to create the menus inside menus and we create a tree of menus

filemenu = Menu(menubar, tearoff=0) # as you can see we add it as child of menubar which is the principal
#now it is time to add the options that each menu will have and they will be actions that will start a command
filemenu.add_command(Label="Open") #this case add command is different from cascade since we want an action
filemenu.add_command(Label="Save")
filemenu.add_command(Label="Close")
filemenu.add_separator() #this creates a line to separete a different section
filemenu.add_command(Label="Exit", command=root.quit) #this will be always the exit command

#now lets do the same as before for the next edit menu
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(Label="Copy")
editmenu.add_command(Label="Cut")
editmenu.add_command(Label="Paste")
editmenu.add_separator()
editmenu.add_command(Label="Select all")

#now lets give somce format to the help menu
helpmenu = Menu(menubar, tearoff=0) #tearoff does remove a kind of -- option that is showed when it does not contains any other menu
helpmenu.add_command(Label="Help")
helpmenu.add_separator()
helpmenu.add_command(Label="About...")


#now it is time to set the relation and the text that will be showing to the main menu, this case menubar like this
menubar.add_cascade(Label="File",menu=filemenu) #add cascade is adding a menu that is opened in cascade
menubar.add_cascade(Label="Edit",menu=editmenu) #label is the text to show in the menu
menubar.add_cascade(Label="File",menu=helpmenu) # menu= pointing out to the first element in the cascade


root.mainloop()
