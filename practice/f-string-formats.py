#now lets play with the f-string formats this will have the pourpose as the others to give some indentation

print(f"{'lets put 20 characters before this text':20}")

myText = "lets use a variable to avoid type"

#using same values as before to see that some are aligned to left, right or center
print(f"{myText}")
print(f"{myText:>40}")
print(f"{myText:^40}")

#lets now play with trunc same as others

print(f"{myText:.4}")
print(f"{myText:.8}")

#lets start using variables to set tne values for alignment and also for the trunc

myLimit=4
myLimit2=80

print(int(True))
print(f"{myText:.{myLimit}}")
print(f"{myText:^{myLimit2}}")

#lets play with aligmenetn and truc with variables

longitude=40
limit=4

print(f"{myText:^{longitude}.{limit}}")

#now lets also use the f-string with the techinque to add values to floats, or fill some spaces with some character

print(f"{1:6d}")   # aligment to six spaces to the right
print(f"{10:6d}")  # same as above
print(f"{100:6d}") # all should be to the right

print(f"{1:06d}")   # the 0 before the 6 is the character that we will include
print(f"{10:06d}")  # same as above
print(f"{100:06d}") # all should be to the right and filled

#now lets use the floats numbers to show and truncate using variables

floatNumber = 34.34334433
floatLenght = 7
floatLimitDecimal = 3
floatFillNumber = 0

print(f"{floatNumber:{floatFillNumber}{floatLenght}.{floatLimitDecimal}f}")
