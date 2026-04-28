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

#another common useage if the escape characters this ones need an special way 

validating_escape_character = 'this project did start in the 2025'

#now lets try to test the scape list by number, this will find the numbers in the previous text

find_just_numbers = [r'\d']

#now lest use the method and see the result 
patterns_find(find_just_numbers,validating_escape_character)#will print ['2', '0', '2', '5']

#if we want to have just find numbers that are together like a year by 1 or more times

one_or_more_numbers = [r'\d+']

patterns_find(one_or_more_numbers,validating_escape_character) #this will print ['2025']

#what about that we want to separate from the text all the letters and not numbers

just_letters = [r'\D']

#this will print 't', 'h', 'i', 's', ' ', 'p', 'r', 'o', 'j', 'e', 'c', 't', ' ', 'd', 'i', 'd', ' ', 's', 't', 'a', 'r', 't', ' ', 'i', 'n', ' ', 't', 'h', 'e', ' ']
patterns_find(just_letters,validating_escape_character)

#same way if we want to get non numbers that does repeate at least one more time, will give all the string

letters_more_than_one_time = [r'\D+']

#this will print['this project did start in the '], check the last space before the number
patterns_find(letters_more_than_one_time,validating_escape_character)

#lets do the same example before but with numbers in the middle like

letters_numbers_text = 'this project version 1 started in the 2025'

#this will print ['this project version ', ' started in the '], check that are spaces in the print
patterns_find(letters_more_than_one_time,letters_numbers_text)

#something not very common just to find th spaces

find_just_spaces = [r'\s']

patterns_find(find_just_spaces,letters_numbers_text)


