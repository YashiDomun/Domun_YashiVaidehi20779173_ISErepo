#category 1 part d
#remove any numeric values in a given string and then convert the string to upper or lower case

import re
#use of regex
#print stateent used as a menu for the user to choose from
def lists():
    print("Enter 1 to convert the string to upper case")
    print("Enter 2 to convert the string to lowercase")
def removingnumbers(string):
    regex = "[0-9]"#assign digit to the regex variable
    return (re.sub(regex, "",string))#slicing numeric values from string obtained from the user

def menu(choice):
    if choice == '1':
        print("Lowercase: ",case.lower())#.lower() converts remaining string to lowercase

    if choice == '2':
        print("Uppercase: ",case.upper())#.upper() converts remaining string to uppercase

lists()
string = str(input("Enter a string: "))#functionality - user input from keyboard
case = removingnumbers(string)
choice = str(input("Make your selection"))
menu(choice)



