#lets play a little with the dictionaries and do a method that read a text from input and transform it to aviation code

nato_alphabet = {
    # Letters
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliett",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "X-ray",
    "Y": "Yankee",
    "Z": "Zulu",

    # Numbers
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Tree",     
    "4": "Fower",    
    "5": "Fife",     
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Niner"     
}

mytext = input("Type a text that you want to code to aviation alphabet:")

text = "Flight A3"
for c in mytext.upper():
    if c in nato_alphabet:
        print(f"{c}: {nato_alphabet[c]}")

