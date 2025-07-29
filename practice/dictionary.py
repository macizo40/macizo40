#there is a other type very common the dictionaries , this can be easy to match the equilavencies in different areas a simple way maybe to translate some words

myColors = {'green':'verde','blue':'azul','yellow':'amarillo'}

print("this is the empy dictionary that is now avaialable: {} and type is {} ".format(myColors,type(myColors)))

#now lets reference the values to a simple translation excersice in this way there will be a simple question and since is linked to a value the return will be his translation

print("now the spanish translation of yellow is {}".format(myColors['yellow']))

#one other combination and use can be when we do manage keys for some constans very useful for DB and save the value based on key

myKeys = {10:'Mexico',22:'USA',55:'Canada'}

print("if I select the value 22 in the list the value will be {}".format(myKeys[22]))


#now lets try to use the reverse instead of key lets find the value and see what gives us

#print("now I will point our to the value amarillo and see if this work here {}".format(myColors['amarillo']))

#now you can see that you can only point out to the keys only