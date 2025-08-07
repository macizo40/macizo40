#lets continue playing with some formats in the strings

#now lets try to trunc some strings using the format, with only the tree first letters

print("{:.3}".format("truncate"))

#now lets try to do some more values in the string like 5

print("{:.5}".format("truncate"))

#there are other exmaples that we can use and combine the trunc with the alignment, lets try center and trunc

print("{:>30.6}".format("center_alingment"))

#there are special cases where the user input in the case of numbers are different and you want to use the same format for all

#check the graphical representation of this
print("{}".format(10))
print("{}".format(100))
print("{}".format(1000))

#on screen the format will be
#10
#100
#1000

#but we want  better format in the screen, now lets give a 4 digits format to all
print("now the values are format in different way with spaces before the value 4d")
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

print("now lets play with that values are filled not with spaces instead are using 0")
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

print("finally we can play with reduce the float numbers this is a very general case")
print("{}".format(3.146576857))
print("now applyinf the special format .2f the value is:")
print("{:.2f}".format(3.146576857))
print("please note that the value not just got truncate also was move to the equilavent in float")