#program to convert hours,minutes,seconds

def convertHours(n):#function to convert hours to minutes
    if n < 0:
        print("error!,time cannot be negative")
    else:
        minutes = n *60
        print("Minutes = ", minutes)

def convertminutes(minutes):#function to convert minutes to seconds
    seconds = minutes *60
    print("Seconds = ", seconds)

def convert(seconds):#function to convert seconds to minutes
    mins = seconds /60
    print("Minutes = ", mins)

def convertm(mins):#function to convert minutes to hours
    mins = mins /60
    print("Hours = ",mins)
    
#main driver code that gets input from user from keyboard 
n = int(input("Enter the hours you want to convert in minutes"))
hours = convertHours(n)
minutes = int(input("Enter the minutes you want to convert in seconds"))
minute = convertminutes(minutes)
seconds = int(input("Enter the seconds you want to convert in minutes"))
second = convert(seconds)
mins = int(input("Enter the minutes you want to convert in hours"))
hour = convertm(mins)
        
#open a textfile to write each output given from functions
with open("category2.txt", "w") as f:
    print(n,file = f)
    print(minutes,file = f)
    print(seconds,file = f)
    print(mins,file = f)
f.close()#close file after writing

#calls the main function to get conversion of hours/minutes/seconds and vice versa
