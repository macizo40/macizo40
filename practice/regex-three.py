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

