#Converting a given string to uppercase or lowercase

def menu():#menu to choose from 
    print("Convert string lower or upper")
    print("Enter 1 for string conversion for lowercase")
    print("Enter 2 for string conversion for uppercase")
    
def lowerconversion(teststring):
    teststring = str(input("Enter a string"))
    teststring.lower()
    
def upperconversion(teststring):
    teststring = str(input("Enter a string"))
    teststring.upper()

def menuinput(choice):
    teststring = "yaShI"
    if choice == '1':
        string = str(input("Enter a string")) #get a string input from user
        print("Lowercase of the string: ",string.lower())#.lower() to convert the string to lowercase
        print("Lowercase of the string: ",teststring.lower())

    if choice == '2':
        string2 = str(input("enter a string")) #get a string input from user
        print("Uppercase of the string: ",string2.upper())#.upper() to convert the string to uppercase
        print("Uppercase of the string: ",teststring.upper())

menu()#call function menu so that the user can choose from it
choice = str(input("Make your selection"))#get choice from user
menuinput(choice)#trigger the menu according to the user's choice 
