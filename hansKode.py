alias = None
enemy = None
greeting = None

def getInput():
    user = input("What is your name, user? ")
    if user == "" or user == None:
        user = getInput()
    return user

def setUserVars(anAlias, anEnemy, aGreeting):
    global alias, enemy, greeting
    alias = anAlias
    enemy = anEnemy
    greeting = aGreeting

def greetUser():
    return "Greetings {}. {}. Good luck defeating{}!".format(alias, greeting, enemy)

user = getInput()

if user == "Bruce Wayne":
    setUserVars("Batman", "The Joker", "You are the hero Gothamdeserves, but not the one it needs right now")
elif user == "Katniss Everdeen":
    setUserVars("Mockingjay", "President Snow", "May the odds beever in your favour")
else:
    setUserVars("Programmer", "The Compiler", "You are the 5%")
