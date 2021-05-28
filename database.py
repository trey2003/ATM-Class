#craete record
#update record
#read record
#delete record
#CRUD

#find user
import os
import validation

user_db_path = "data/user_record/"

def create(accountNumber ,user_details):
    
    completion_state = False
    try:
        f = open(user_db_path + str(accountNumber) + ".txt", "x")

    except FileExistsError:

        print("File user already exist")
        #delete the already created file, and print out the error, then return false
        #delete(accountNumber)

    else:

        f.write(str(user_details))
        completion_state = True

    finally:

        f.close()
        return completion_state

    #create a file
    # name of the file would be account_number.txt
    # add the user details to the file
    # RETURN TRUE
    # if saving to file failed, then delete created file


def read(user_account_number):
    is_valid_account_number = validation.account_number_validation(user_account_number)
    try:
        if is_valid_account_number:
            f = open(user_db_path + str(user_account_number) + ".txt", "r")
        else:
            f = open(user_db_path + user_account_number + ".txt", "r")

    except FileNotFoundError:
        print("user not found")
    except FileExistsError:
        print("user doesn't exist")
    except TypeError:
        print("Invalid account number format")
    else:
        return f.readline()

def update(user_account_number):
    print("Update user record")
    # find user with account number
    # fetch the content of the file
    # update the content of the file
    # save the file
    # return True


def delete(user_account_number):
    is_delete_successful = False

    if os.path.exists(user_db_path + str(user_account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(user_account_number) + ".txt")
            is_delete_successful = True
        except FileNotFoundError:
            print("User not found")
        finally:
            return is_delete_successful



def does_email_exist(accountNumber, email):
    all_users = os.listdir(user_db_path)

    for user in all_users:
        print(read(user))
        print("\n")

does_email_exist(8802855319, "treyharris617@gmail.com")