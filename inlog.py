import os



def login():
    """gives the login menu"""
    print("." * 40)
    print("Logging in...")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    return login_check(username, password)


def login_check(username, password):
    """checks the input given in the login function"""
    try:
        with open(os.path.join("accounts",f"{username}.txt"), "r") as file:
            saved_password = file.read()
            if password == saved_password:
                print(f"Welcome {username}!")
                return True
            else:
                print("password incorrect")
                return False
    except FileNotFoundError:
        print("user not found")
        return False


def signup():
    """creates account based on the input given"""
    print("." * 40)
    print("Signing up ...")
    new_user = input("Enter your username: ")
    new_password = input("Enter your password: ")
    acc_save(new_user, new_password)
    print("your account has been created")
    login()
    return new_user, new_password

def acc_save(new_user, new_password):
    """saves the account created in the signup function"""
    folder_name = "accounts"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filename = os.path.join(folder_name,f"{new_user}.txt")
    if os.path.exists(filename):
        overwrite = input(f"the username {new_user} already exists, do you want to overwrite? (y/n): ")
        if overwrite != "y":
            print("account is not saved")
            return
    with open(filename, "w") as file:
        file.write(new_password)



def guest_signin():
    """prints welcome message to guests"""
    print("Welcome guest!")





















