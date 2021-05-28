print("== ==== ====== ===== ==")
from datetime import datetime
now = datetime.now()
date = now.strftime("\n%x")
time = now.strftime("%I:%M %p")
print(time, date)
print("Welcome to ATM!")
print("== ==== ====== ===== ==")

name = input("What is your name? \n")
allowedUsers = ["Trey", "Tyler", "Yung"]
allowedPasswords = ["Memphis03", "Memphis", "Connecticut"]
amountBalance = [10000000, 3000000, 0]

##All users have the same account balances
##All users have 5 million dollars

attempts = 0
while True:
    if name in allowedUsers:
        password = input("Password? \n")
        userID = allowedUsers.index(name)

        attempt = 0
        while True:
            if password == allowedPasswords[userID]:
                currentBalance = amountBalance[userID]
                while True:
                    print("== ==== ====== ===== ==")
                    from datetime import datetime
                    now = datetime.now()
                    current_date = now.strftime("%c")
                    print(current_date)
                    print("=====Welcome %s!=====" % name)
                    print("Main Menu")
                    print("1. Withdraw:")
                    print("2. Deposit:")
                    print("3. Complaint:")
                    print("4. Cancel:")
                    print("== ==== ====== ===== ==")

                    chosenOption = int(input("Insert chosen option above ^ \n"))
                    while True:
                        if chosenOption == 1:
                            print(currentBalance)
                            amount = int(input("====Type amount you want to withdraw==== \n"))
                            word = str("$ has been withdrawn")
                            currentBalance = currentBalance - amount
                            amountBalance[userID] = currentBalance
                            print("{0}{1}".format(amount, word))
                            print(currentBalance)
                            exitkey = int(input("press 2 to go back to main menu \npress 3 to cancel\n"))
                            print(exitkey)
                            if exitkey == 2:
                                break
                            if exitkey == 3:
                                print("Have a nice day!")
                                quit()
                        if chosenOption == 2:
                            print(currentBalance)
                            insert = int(input("====Insert cash or check into slot====\n"))
                            cash = str("$ has been deposited into your account")
                            currentBalance = currentBalance + insert
                            amountBalance[userID] = currentBalance
                            print(f"{insert}{cash}")
                            print(currentBalance)
                            exitkey2 = int(input("press 2 to go back to main menu \npress 3 to cancel\n"))
                            print(exitkey2)
                            if exitkey2 == 2:
                                break
                            if exitkey2 == 3:
                                print("Have a nice day!")
                                quit()
                        if chosenOption == 3:
                            print("====To issue a complaint, contact us at treyharris617@gmail.com====")
                            exitkey3 = int(input("press 2 to go back to main menu \npress 3 to cancel\n"))
                            print(exitkey3)
                            if exitkey3 == 2:
                                break
                            if exitkey3 == 3:
                                print("Have a nice day!")
                                quit()
                        if 4 == chosenOption:
                            print("Have a nice day!")
                            quit()

                        else:
                            print("Option not found, try again")

            else:
                while password != allowedPasswords[userID] and attempt < 2:
                    attempt = attempt + 1
                    password = input("Wrong Password, try again\n" + "you've tried %s" % attempt + " times\n")

                    if password == allowedPasswords[userID]:
                        print("That's correct!")
                    if attempt == 2:
                        print("You've exceeded your number of attempts.")
                        break

    else:
        while name not in allowedUsers and attempts < 2:
            attempts = attempts + 1
            name = input("Name not recognized, try again\n" + "you've tried %s" % attempts + " times\n")

            if name in allowedUsers:
                print("Next")
                break
            if attempts == 2:
                print("You've exceeded your number of attempts")
                quit()


