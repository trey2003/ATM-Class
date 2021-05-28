language = input("Select Language \nEnglish \nor \nEspañol \n")
languages = ["English", "Español"]
if language in languages:
    password = input("Password? \n")
    userID = languages.index(language)
    if language == languages[0]:
        print("Hello")
    if language == languages[1]:
        print("Hola")

else:
    print("Select English or Español")

insert = input("Insert Card code \n")
codes = ["4568", "6798", "8879"]
name = input("What is your name? \n")
allowedUsers = ["Trey", "Tyler", "Yung"]
allowedPasswords = ["Memphis03", "Memphis", "Connecticut"]

##All users have the same account balances
##All users have 5 million dollars

if insert in codes:
    print("Continue to Account")

    if name in allowedUsers:
        password = input("Password? \n")
        userID = allowedUsers.index(name)

        if password == allowedPasswords[userID]:
            print("Welcome %s!" % name)
            print("Here are your options")
            print("1. Withdraw:")
            print("2. Deposit:")
            print("3. Balance:")

            chosenOption = input(int("Insert chosen option \n"))

            if chosenOption == 1:
                print("Select amount \t Or enter another amount %s" % chosenOption)
            if chosenOption == 2:
                print("Insert cash or check into slot %s" % chosenOption)
            if chosenOption == 3:
                print("Balance is $5,000,000. %s" % chosenOption)

            else:
                print("Option not found, try again")


        else:
            print("Wrong Password, try again.")

    else:
        print("Name not recognized, try again.")

else:
    print("Wrong code, try again.")
