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
