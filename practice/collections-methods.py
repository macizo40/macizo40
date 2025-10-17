#lets do play with some special methods that collections as strings, dictionaries and more does have by default

my_string = "Hello I am a simple string, you can play with me"
my_lower_case_string = "i am a lower case string"
my_repeated_string = "this is a lower lower lower, with many many many, repeated words words words"

#method upper will change all the string to uppe cases
print(my_string.upper())
#but with this you will see that after the method is used the string just remains as original not affecting the original value
print(my_string)

#method to make all lower case
print(my_string.lower()," ",my_string)

#method capitalize to set the first letter as capital
print(my_lower_case_string.capitalize()," ",my_lower_case_string)

#method to set all the first letters in capital as title
print(my_lower_case_string.title()," ",my_lower_case_string)

#method to count how many times a word or character does appear in the string
print(my_lower_case_string.count('a')," ",my_lower_case_string)

#or a entire word
print(my_lower_case_string.count('case')," ",my_lower_case_string)

#what about to know in which position of the string the word index start we use find
print(my_lower_case_string.find('lower')," ",my_lower_case_string)

#but the previous method will tell you only the first word found, with rfind you find the index of the latest word found
print(my_repeated_string.rfind('lower')," ",my_repeated_string)