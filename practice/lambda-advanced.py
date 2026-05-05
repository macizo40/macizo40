#now lets use more the strong of the filter looking for objects there is where the real thing happens

#lets work with class again

class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return "{} with age {}".format(self.name,self.age)
    

#now lets create a new list with the people object

people_list = [
    People("Ukyo",25),
    People("Ahomaru",15),
    People("Galford",34),
    People("Nim",78),
    People("Nakuru",12),
]

#lets take a look about what it is in the list:
print("people list is ",people_list)

#now we should be able to do this change with a lambda to find underage people
"""
This lambda will help us to set the list of users in the class that are under age, this does not use methods.
"""
underage = filter(lambda person:person.age <18,people_list)

#now lets loop in the list that it was returned

for i in underage:
    print(i)
