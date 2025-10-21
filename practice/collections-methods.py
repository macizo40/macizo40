#lets do play with some special methods that collections as strings, dictionaries and more does have by default

my_string = "Hello I am a simple string, you can play with me"
my_lower_case_string = "i am a lower case string"
my_repeated_string = "this is a lower lower lower, with many many many, repeated words words words"
my_cvs_text = "Helo,5,value,58687,special,comma,sepparated,values,with,no,spaces"
my_spaces_text = "   this is a text with space and begining and the end     "
my_characters_text = "------this is a text with characters and begining----end-----"
my_text_to_replace = "My name name name name is repeated, also want to read only e"

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

#there more methods to validate if this string does have a number

my_number = "100"
#this will return a tru or false
print("this string is a number",my_number,"=",my_number.isdigit())

#lets use some validations to confirm that string does not contains special characters
my_alphanum = "ADFB2938364rtbdkgid"

my_special = "mskdhksjhd$ksdkjf1001"

print("this string is a does contains special characters",my_alphanum,"=",my_alphanum.isalnum())

print("this string is a does not contains special characters",my_special,"=",my_special.isalnum())

#we can also validate that if the string only contain letters

print(my_string.isalpha()," ",my_string)

print(my_lower_case_string.isalpha()," ",my_lower_case_string)

#validating types or writing
print(my_lower_case_string.istitle()," ",my_lower_case_string)


print(my_lower_case_string.islower()," ",my_lower_case_string)

print(my_lower_case_string.isupper()," ",my_lower_case_string)

print(my_lower_case_string.isspace()," ",my_lower_case_string)

#in another types of methods we can validate the starts of a string

print(my_lower_case_string.startswith("I")," ",my_lower_case_string)

#also with a word we can see if start or end

print(my_string.startswith("Hello")," ",my_string)

print(my_string.endswith("me")," ",my_string)

#lets try now manage and change the string with more advanced methods

#split method with every space will separate the words and will create a list

print(my_string.split()," ",my_string)

#or we can save it to a new variable

my_split_list = my_string.split()
#I can now add a new item in the list and the original string will not be affected
my_split_list.append("bye")

print(my_split_list," ",my_string)

#another good stuff with split I can maybe want to create a list with the last item or the first one using an index value

print(my_string.split()[0]," ",my_string) #index 0 the first item that finds before an space
print(my_string.split()[-1]," ",my_string) #index -1 last item found after the last space

#methid split is also well used to parse comma separated values and have a list, we need to specify the character to use also can be any 

print(my_cvs_text.split(','))

#on the other hand there is a process to add a character to split an string, as example this

print(my_alphanum," is moved to "," ".join(my_alphanum)) #this will separate each character with an space

#another useful methiod commnly used to remove spaces or characters from begining or end of string

print(my_spaces_text," is moved to ",my_spaces_text.strip())


print(my_characters_text," is moved to ",my_characters_text.strip('-')) #notice that if there are characters between words those are not removed

#and one of the most common ones, replace, this will replace the character by another or can be used to remove too

print(my_text_to_replace,"-is moved to-",my_text_to_replace.replace('a','10')) #this will replace all letters a with a 10

print(my_text_to_replace,"-is moved to-",my_text_to_replace.replace('name','',2)) #this will remove the word name 2 times, leaves spaces

print(my_text_to_replace,"-is moved to-",my_text_to_replace.replace(' name','',3)) #this will remove the word name 3 times an space at the begining of the word 