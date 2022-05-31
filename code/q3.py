#identify whether a given string is valid number or not

def checknumbers(text):
    isnumber = False#assign flag isnumber to false outside of loop
    for character in text:
        if character.isnumeric():#use isnumeric() to check if there is any numeric values  are valid in the given string
            isnumber = True#assign flag isnumber to true in the loop
    print("Flag: ",isnumber)


text = str(input("Enter a string: "))#functionality - user input from keyboard
checknumbers(text)
