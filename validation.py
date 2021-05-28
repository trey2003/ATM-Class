def account_number_validation(accountNumber):
    if accountNumber:
        if len(str(accountNumber)) == 10:

            try:
                if int(accountNumber):
                    return True
            except ValueError:
                print("This option can only be a integer")
                return False
            except TypeError:
                print("Invalid account type")
                return False
        else:
            print("Can only be 10 digits")
    else:
        print("Account number is required")



