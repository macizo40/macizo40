#lets do some new test about the objects 
#a class is a template of objects that have some similar attributes

class Cake:

    #this like java we have a constructor method (called here init) that will assign the values recived in the call to their variables
    def __init__(self, flavour, size, form):
        self.flavour = flavour
        self.size = size
        self.form = form

    #this method was new for me, this is a way to return to screen in format string=str the content of the object usually with print   
    def __str__(self):
        return 'Cake details are {} {} {}'.format(self.flavour,self.size,self.form)
    
#now we can play with some characteristics of the cakes

red_velvet = Cake ("Chocolat","Big","Square")
addiction = Cake ("Strawberry","Big","Circle")
carrot = Cake ("Carrot","Big","Triangle")

#now lets use the __STR__ method:

print(red_velvet)
print(addiction)
print(carrot)



