import random
import validation
import database

#database = {
#    6462540594: ["treyharris617@gmail.com", "Trey", "Harris", "Trey18"]
# }

def init():
    isValidOptionSelected = False
    print("== ==== ====== ===== ==")
    print("Welcome to Bank Express")
    while not isValidOptionSelected:
        haveAccount = int(input("Do you have a account with us: 1 (yes) 2 (no) \n"))
        print("== ==== ====== ===== ==")
        if (haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif (haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print("You have selected invalid option")


def login():
    print("Login to existing account")
    isLoginSuccessful = False
    while isLoginSuccessful == False:
        accountNumberPut = input(str("What is your account number?\n"))
        account_number_valid = validation.account_number_validation(accountNumberPut)

        if account_number_valid:

            password = input("What is your password?\n")

            for accountNumber, userChoice in database.items():
                if accountNumber == int(accountNumberPut) and userChoice[3] == password:
                    (bankOperation(userChoice))
                else:
                    print("Invalid account  or password")
                    login()



def register():
    print("***** Register *****")
    print("== ==== ====== ===== ==")
    email = input("What is your email address?\n")
    first_name = input("What is your first name\n")
    last_name = input("What is your last name\n")
    password = input("Create a password for yourself \n")

    accountNumber = generationAccountNumber()

    is_user_created = database.create(accountNumber, [email, first_name, last_name, password, 0])

    if is_user_created:
        print("Your Account Has Been Created")
        print("== ==== ====== ===== ==")
        print("Your account number is:%d" % accountNumber)
        print("Keep account number secured")
        print("== ==== ====== ===== ==")

        login()

    else:
        print("Something went wrong, please try again")
        register()


def bankOperation(user):
    chosenOption = True
    while chosenOption == True:
        print("== ==== ====== ===== ==")
        print("Welcome %s%s" % (user[1], user[2]))
        chosenOption = int(input(
            "Main Menu\n == ==== ====== ===== ==\n 1. Withdraw:\n 2. Deposit:\n 3: Logout:\n 4: Exit:\n== ==== ====== ===== ==\n"))
        print("Choose one of the options above^")
        if chosenOption == 1:
            chosenOption = True
            operationWithdraw()
        if chosenOption == 2:
            chosenOption = True
            operationDeposit()
        if chosenOption == 3:
            chosenOption = True
            login()
        if chosenOption == 4:
            exit()

def operationWithdraw():
    print("Withdraw ")


def operationDeposit():
    print("Deposit ")


def generationAccountNumber():
    return random.randrange(1111111111, 9999999999)


init()