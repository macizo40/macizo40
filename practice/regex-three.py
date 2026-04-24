# lets then start to produce some patterns with some characters 
#lets get some help with a method
import re
def patterns_find(patterns,text):
    for pattern in patterns:
        print(re.findall(pattern,text))

mynewtext = 'hala hela hila hola hula'

# from the previous text I want to find any word that contains either 'ou' and the 'la'
newlist = ['h[ou]la','h[aio]la']

patterns_find(newlist,mynewtext)

# the result will tell you that hola and hula does apply to the pattern also the second pattern does show the result with aio previously

# now lets try to find that contains any vocals and then the final word like la
allletters = ['h[aeiou]la']

patterns_find(allletters,mynewtext)

# what we can do also is to try to find the repetitions like the previous example

repetitivetext = 'caar ceear ciiiar coooooar cuar'

repetitions = ['c[ae]ar','c[ae]*ar'] #the asterisk says cero or more times the same character

patterns_find(repetitions,repetitivetext)

# we can now use the combination of the two areas, the character and the range

rangepatterns = ['c[io]{3,9}ar']

patterns_find(rangepatterns,repetitivetext)

# now we will use a different object this will be the negation wich will be use the ^ charatect 

#lets use a previos example but now let see the values that will not be found

mynewtext2 = 'hala hela hila hola hula'

# from the previous text I want to find any word that contains either 'ou' and the 'la'
newlist2 = ['h[o]la','h[^o]la']

#at the first pass the hola will be there but in the second one the hola will be excluded and the rest showed
patterns_find(newlist2,mynewtext2)

#now lets try to use another functionality which will be the range, this wi commonly used to find alpha num values

my_alpha_text = 'hi h1 Hello hEllo h0 Cart c4rt pen p3n flow Fl0W'

alpha_list = ['h[a-z]llo'] # this will serach to any plaha not capital

capital_list = ['h[A-Z]llo'] #this will search for the ones that only use capital letters.

numbers_letters_list = ['c[0-9]rt'] #this will find the word that contains a number

#this is very interesting, any letter not matter capital o not but the content have at least 4 
limited_characters = ['[A-z]{4}'] 

#this is the very common pattern and is that should contains with a capital letter always

first_letter_caital = ['[A-Z][A-z0-9]{3}']

patterns_find(alpha_list, my_alpha_text)
patterns_find(capital_list,my_alpha_text)
patterns_find(numbers_letters_list, my_alpha_text)
patterns_find(limited_characters,my_alpha_text)
patterns_find(first_letter_caital,my_alpha_text)
