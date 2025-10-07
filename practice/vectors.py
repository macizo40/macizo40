import math

#lets do a more robust excersise that will use the maps of x,y diagrama

class Dot:

    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        print("New dot is created in x={},y={}".format(self.x,self.y))
    

    def __str__(self):
        return("Dot values ({},{})".format(self.x,self.y))

    def quadrant (self):
        if self.x > 0 and self.y > 0:
            print ("Dot is in the first quadrant")
        elif self.x < 0 and self.y > 0:
            print ("Dot in the second quadrant")
        elif self.x < 0 and self.y < 0:
            print ("Dot is in the third quadrant")
        elif self.x > 0 and self.y < 0:
            print ("Dot is in the fourth quadrant")
        elif self.x == 0 and self.y == 0:
            print ("Dot is in the origin")

    def vector (self,d):
        print("Vector of dots {} and {} is ({},{})".format(self,d,d.x-self.x,d.y-self.y))

    def distance (self,d):
        r = math.sqrt((d.x-self.x)**2 + (d.y-self.y)**2)
        print("Distance of dots {} and {} is ({})".format(self,d,r))

a = Dot(2,3)
b = Dot(5,5)
c = Dot(-3,-1)
d = Dot()

a.quadrant()
c.quadrant()
d.quadrant()

a.vector(b)
b.vector(a)

a.distance(b)
b.distance(a)

class Rectangle:

    def __init__(self,b=Dot(),h=Dot()):
        self.b = b
        self.h = h
        print(f"Rectangle created with b={self.b} and h={self.h}")
    
    def base (self):
        base_result = abs(self.h.x-self.b.x)
        print(f"base is {base_result}")
        return base_result
    
    def high (self):
        high_result = abs(self.h.y - self.b.y)
        print(f"high is {high_result}")
        return high_result

    def area (self):
        print(f"base is {self.base()} and high is {self.high()}, area is equal to {(self.base() * self.high())}")

r = Rectangle(a,b)
r.base()
r.high()
r.area()





        

        
        