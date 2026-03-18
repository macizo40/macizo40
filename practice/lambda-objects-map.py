#now lets do some maps with objects, there is no limited to list only

#we will use the same class method of the filter practice

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

#a normal way to change the age of each people is to create a method that reads the people and change his age

def change_age(person):
    person.age += 1
    return person

#now using a single map will be 

peoples = map(change_age,people_list)

for x in peoples:
    print(x)

#now be careful wiuth you add this with lambda is not just add the value is more to use a new object

newpeoples = map(lambda subject: People(subject.name,subject.age+1),people_list)

for y in newpeoples:
    print(y)
