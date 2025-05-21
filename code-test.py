import sys

#printing the values that are pass in the command line
print(sys.argv[1:])

for args in (sys.argv[1:]):
    print(args)

#Single iteration doing the values pass by the arguments
if len(sys.argv) == 3:
    for r in (sys.argv[1:]):
        print(sys.argv[1] * int(sys.argv[2]))
else:
    print("Not valid number of arguments")


#Reading values fron the sys instead of using some extra variables in the code

print ("Values in the chain {} are repeatable by this number {}".format(sys.argv[1],sys.argv[2]))

# using as same values that we have in a list but their index

print ("Values in the chain {1} are repeatable by this number {1}".format(sys.argv[1],sys.argv[2]))

# using variables defied inside the print

print("Vales now will be declared in the for as {value} and the other is the number {number}".format(value=sys.argv[1],number=sys.argv[2]))

#using format to do some alignment
print("Now the {:>10} will be moved to the right".format(sys.argv[1]))

#this is the center text
print ("This is a text that will be center at some spaces {:^10} after we send the info".format(sys.argv[1]))

#truncate the values of the text
print("Values now will be truncate them only 2 in {:.2}".format(sys.argv[1]))

#combine the use of aligment and the truncate in a same

print("This text {:^30.2} willbe only in the center and just have 2 letters".format(sys.argv[1]))

#another use of format values to provide a indentation

print("{:5d}".format(10))
print("{:5d}".format(100))
print("{:5d}".format(1000))


#another use of format values to provide fill of left spaces with any character, very good for number or references that require all values

print("{:05d}".format(10))
print("{:05d}".format(100))
print("{:05d}".format(1000))

#this also will work with the float numbers

print("{:.3f}".format(3433.12564584))

#we can also aligment of the current floats to the same number of positions

print("{:7.3f}".format(3.1256458454))
print("{:7.3f}".format(345.14))

