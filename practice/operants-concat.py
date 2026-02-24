#now lets start doing some other operants usage, python and other languages does accept subsecuent operands to work on those

#lest do an if with two validations

if 1 < 2 and 2 < 3:
    print("Expresion is true") 

#but the previous one can be easy changes to have a single expresion like this since the single values in common is 2
if 1 < 2 < 3:
    print("This is also true")

#lets do another explame with two operants and then we will see how they get changed

number = 23

if number >= 0 and number <= 100:
    print(f"the number {number} is in the range before 100")
else:
    print(f"number {number} does not belogn to the range of 100")

#now lets change it in the way that we will use a sinlge expresion with out and
if 0 <=  number <= 100:
    print(f"the number {number} is in the range before 100")
else:
    print(f"number {number} does not belogn to the range of 100")