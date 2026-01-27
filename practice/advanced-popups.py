from tkinter import *
from tkinter import messagebox as MessageBox #this trick overrides the name of the class in any case that you want to play with it
from tkinter import colorchooser as ColorChooser
from tkinter import filedialog as FileDialog

root = Tk()

#to play with advanced popups we can continue call them from an oprdniadary button.
#some popups as example are the ones that can select, here is where we will use the color chooser class

def actionable():
    #this color chooser is the tipicall windows color palette where you can select the different colors and gradiants

    #the method to do this is askcolor and you pass a title and you need to save the value returned
    mycolor = ColorChooser.askcolor(title="Select a color")

    #you can print to the console to see what is the value his is a tuple consider that in the manage of the value
    print("Here is the selected color {}".format(mycolor)) #first value is a RGB code, second part is the same but in hexadecimal

def openfilepath():
    #on this method we will use another most common window, the file path, the one that we search for a file to open or save it

    #first lets play with the open file dialog, this will return a path
    #you can setup the initial start point, and which types of files to show in the window, you can select more than one with a tuple
    myfilepath = FileDialog.askopenfilename(title="Please open a file", initialdir="C:", filetypes=(("Text file","*.txt"),("Python file","*.py"))) 
    
    #we can also print it to the console
    print(f"this is the path of the open file {myfilepath}")

def savefileas ():
    #this method certainly will open the window to where you can save the file as
    #this method opens the file with property w, so cleans all, you can also set which is the default extension to save it.
    myfiletosave = FileDialog.asksaveasfile(title="Save the file as",defaultextension=".txt") 

    #in the case that you click save you can define the actions to this file as

    if myfiletosave is not None:
        #this returns a file type object so you can use the file methods
        myfiletosave.write("You save me!") #here is the whole content to save, this time we will just play with a single text
        myfiletosave.close()





#define a button that will call the method
Button(root,text="Clickme", command=actionable).pack()

root.mainloop()