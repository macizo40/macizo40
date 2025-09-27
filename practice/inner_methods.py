from datetime import date

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
        #lets add a parameter that will tell us that this auto was changed from his original color
        self.wasPainted = True
        return self
    
    #lets play with other actions that this class can have maybe repair car, this will need just get the object as is
    #and we will add some values that explain now the repair

    def repair_automobile(self):
        self.isRepaired = True
        self.newParts = ["door","windshiled","bumper","tires"]
        return self
    
    #another can be maybe adding customs to this ride

    def add_custom_parts(self,newPart):
        self.hasCustomParts = True
        self.newPart = newPart
        return self
    
    #waht about that a car need service and we want to track the record of services in the shop

    def do_maintenance_service(self,kilometers):
        self.current_kilometers = kilometers
        self.next_service = kilometers + 10000
        self.parts_changed = []
        self.date_of_service = date.today()
        return self


forteHB = Automobile("kia",2022,"white","forte HB")

#now lets see the value of color first

print ("Color of {} currently is {}".format(forteHB.model,forteHB.color))

#now lets call the methid paint

forteHB.paint_automobile("Black")


print ("Color of {} currently is {}".format(forteHB.model,forteHB.color))

#now lets see that after the methid is apply it, the object has a new value called wasPainted

print ("Was this {} painted: {}".format(forteHB.model,forteHB.wasPainted))

#now lets play that we do repair this auto

forteHB.repair_automobile()

#lets now see that new values are here

print ("Was this {} repaired: {} with parts {}".format(forteHB.model,forteHB.isRepaired,forteHB.newParts))

forteHB.add_custom_parts("ring")

print ("Was this {} add custom parts: {} with parts {}".format(forteHB.model,forteHB.isRepaired,forteHB.newPart))

#now lets give a service to this car

forteHB.do_maintenance_service(1000)

print("Was this {} had a service of {}kms and next service is {}kms".format(forteHB.model,forteHB.current_kilometers,forteHB.next_service))

print(str(forteHB))

        
