# main.

# declare var:
fluidvelocity = 0;
fluidvorticity = 0;
inflowrate = 0;
outflowrate = 0;
diametervortex = 0;
spinrate = 0;
heightvortex = 0;
volume = 0;


# layout panel
x = 100
y = 100
z = 100

# user log-in via terminal
name = input("What is your name? - ")
password = "1789"
owner = False;
ownername = "Allen"
inputYes = "Yes"
inputNo = "No"


if (name.casefold() == ownername.casefold()):
    print("User: " + name)
    trueness = True  
    ownerness = True
    checker = True
    execution = True
    repeating = True

    while trueness == True:
        
        while repeating == True:
            ownerboolean = input("Are you Owner? (Yes/No) - ")
            if (ownerboolean.casefold() == inputYes.casefold()):
                trueness = True
                checker = True
                repeating = False
            elif (ownerboolean.casefold() == inputNo.casefold()):
                trueness = False
                checker = False
                repeating = False
            else:
                repeating = True
                print("Please enter Yes or No.")

        if (checker == True):
            passwordinput = input("Password - ")
            if (passwordinput == password):
                print("This user has owner privledge now.")
                owner = True;
                trueness = False;
            else:    
                print("Password is wrong.")
                again = input("Try Again? (Yes/No) - ")
                
                if (again.casefold() == inputYes.casefold()):
                    trueness = True
                elif (again.casefold() == inputNo.casefold()):
                    trueness = False
                else:
                    trueness = True
                    print("Please enter Yes or No.")
        else:   
            execution = False          
else:
    print("User: " + name)

# Owner Privledge:

# Data Set Input from User:


