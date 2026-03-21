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

#now lest start to use the meta character this is used to find none or more repetitions of the letter at its left

newtext = "cmd command coommmand cooooooommand"

new_filter_list = ['co','co*']

patterns_find(new_filter_list,newtext)
#the output of the previous command will give specific 'co' found three time and the second 4 times including the first one