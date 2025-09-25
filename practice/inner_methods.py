#lets work with some of the special methods that are reserved by default, some of them are very popular in most of the proggamming languages 

#now lets use a previous example that at the beining it was not not clear for me but now is different

class Automobile:

    #the constructor of this will be things that we can classify, we need to pass yes self first.

    def __init__(self,brand,year,color,model):
        #lets assign the values to self
        self.brand = brand
        self.year = year
        self.color = color
        self.model = model
        #lets add a text that will help to confirm that constructor has run based on the model
        print("New automobile '{}' was created".format(model))

    #now a new specila method as other know as garbage collector, we can have a destrcutor methid known as "del"
    #this method always happens when the object is deleted during the program, running now will show ar the end of the program a deletion
    def __del__(self):
        print("We are deleting automobile '{}' color '{}'".format(self.model,self.color))

    #a method that was previously used was str we can redefine the method to be more custom

    def __str__(self):
        #we just sue a return
        return "{} brand {} launched in {}".format(self.model,self.brand,self.year)
    
    #now lets do a simple method that will change the color of automobile, this methid will be called paint

    def paint_automobile(self,new_color):
        self.color = new_color
        return self


forteHB = Automobile("kia",2022,"white","forte HB")

#now lets see the value of color first

print ("Color of {} currently is {}".format(forteHB.model,forteHB.color))

#now lets call the methid paint

forteHB.paint_automobile("Black")


print ("Color of {} currently is {}".format(forteHB.model,forteHB.color))

#we can call the destrcutor by calling the methid del

#del(forteHB)

#using a simple str methid with a number

print(str(10))

#now with our object

print(str(forteHB))

        
