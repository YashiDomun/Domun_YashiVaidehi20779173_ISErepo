#category1partb
#identify whether numeric values are in a given string

def numbersfound(text):
    isnumber = False#assign flag isnumber to false outside of loop
    for character in text:
        if character.isdigit():#use isdigit() to check if there is any numeric values in the given string
            isnumber = True#assign flag isnumber to true in the loop
    print(isnumber)


text = str(input("Enter a string: "))#user input from keyboard
numbersfound(text)
