#now lets continue working with the regular expressions 

#we need to import this:

import re

#we can start using patterns this ones will help to find in the text those 

mytext = "star start staaaar starrrrrrrt"

#we can find one text only as before

print("finding a single word:",re.findall('star',mytext))

#since the paters exist will give back the number of times, even the words does have more letters the pattern is true

#lets get some help with a method

def patterns_find(patterns,text):
    for pattern in patterns:
        print(re.findall(pattern,text))

#lets use a list that will search too the same pattern

mylist_patters_to_search = ['star','staa']

patterns_find(mylist_patters_to_search,mytext)

#now lest start to use the meta character this is used to find zero or more repetitions of the letter at its left 
# (0 or more, this can be 1 or many)

newtext = "cmd command coommmand cooooooommand"

new_filter_list = ['c','co*']

patterns_find(new_filter_list,newtext)
#the output of the previous command will give specific 'co' found three time and the second 4 times including the first one

#there is another special character that will find at least 1 or more, this is the +

plus_filter = ['co+']

patterns_find(plus_filter,newtext)

#the next special character is the ? is the none or one repetition of the letter at its left 

question_filter = ['co?','co?mm']

patterns_find(question_filter,newtext)

#there is character that will let us know an specific repetitive number in string {} always at the left also we can use a range

repetive_filter = ['co{2}','co{2}m','co{0,5}m']

patterns_find(repetive_filter,newtext)


