#there will be some areas where regular expressions will be used for sure to find matches.

#we need to import this:

import re

#now lets try to find an expression

text = "here is the largest text even and the code should find the three letters MMM"

#this will print a regular expression object
print("now running the regular expression object:",re.search('MMM',text))

#we can use the regular expression to validate with a single if

found_item = re.search('three',text)

if found_item is not None:
    print("I found you")
else:
    print("Not found my friend")

#but certainly just saying true or false is not all magic here, you can also find the location

print("here is firs element location of the expression: {}".format(found_item.start()))

#but there is also a method to find where the expression does end

print("this is the end location of the expression: {}".format(found_item.end()))

#to avoid having the start and the end, well we can use the span method

print("now lets get a tuple with the both start and end : {}".format(found_item.span()))

#in any case that you want to see the original string, this object does have a copy of it

print("recovering the entire string:{}".format(found_item.string))

#in the case that you want to know if the string does start with a expression you can use match

print("check is this starts with 'here'",re.match('here',text))

#with the method split, you can cut in different elements the text, what about the space character is the common

print("split the original text and get:{}".format(re.split(" ",text)))

#now what about if I want to substitute that character or word from the text

print("substitition of spaces with a '-' gives a result:{}".format(re.sub(" ","-",text)))

#if we want to find the number of times that a word, element repeats in a string we can use findall
#but certainly this does work better if we count the times
#this will return a list of the words
print("find the word 'the' in the string:{}".format(re.findall('the',text)))

#but certainly we may need the leng and you can try
print("now same but now how many times does repeat: {}".format(len(re.findall('the',text))))

#but what about if you want to find two different words in the expression you can and this will tell you that is valid

print("here is the use of the '|' symbol : {}".format(re.findall("(the|code)",text)))

#and what about the len of the previous exercise

print("using len with the '|' symbol : {}".format(len(re.findall("(the|code)",text))))

#note that in the result of the previous example the numbers is the total, is not telling that found 3 and 1, is a total