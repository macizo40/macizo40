import math

#lets do a more robust excersise that will use the maps of x,y diagrama

class Dot:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print("New dot is created in x={},y={}".format(self.x,self.y))
    

    def __str__(self):
        print("Dot values ({},{})".format(self.x,self.y))

def cuadrant (Dot=None):
    if Dot.x is True and Dot.y is True:
        print ("Dot is in the first quadrant")
    elif Dot.x is True and Dot.y is False:
        print ("Dot in the second quadrant")
    elif Dot.x is False and Dot.y is False:
        print ("Dot is in the third quadrant")
    elif Dot.x is False and Dot.y is True:
        print ("Dot is in the fourth quadrant")    


def vector (dot1=Dot,dot2=Dot):
    print("Vector is ({},{})".format(dot2.x-dot1.x,dot2.y-dot1.y))

        

        

        
        