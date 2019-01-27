existing_users = []

class Account():
    username = ""

    password = ""

    admin = False

    def __init__(self, username, password, admin):
        self.username = username
        self.password = password
        self.admin = admin

# Lets the user create an account
def create_account():
    username = str(input("Please provide a username: "))
    
    for user in existing_users:
        if username == user.username:
            print("This user already exists.")
            return

    password = input("Please provide a passowrd: ")
    existing_users.append(Account(username, password, False))

    print(username + " has been added!")

# Lets a user delete an account
def delete_account():
    for user in existing_users:
        print("User -> " + user.username)
    user_to_delete = input("Please type in the username of a user to be deleted: ")
    for user in existing_users:
        if user.username == user_to_delete:
            existing_users.remove(user)
            print(user_to_delete + " was deleted!")

# Lets a user login
def login():
    while(1):
        provided_username = input("Please provide your username: ")
        provided_password = input("Please provide your password: ")

        for user in existing_users:
           if provided_username == user.username:
               if provided_password == user.password:
                   print("You've logged in!")
                   if user.admin:
                       deleting = input("Type delete if you'd like to delete an account: ")
                       if deleting == "delete":
                           delete_account()
                           return
                   return

        retry = input("The credentials were invalid, would you like to try again?\n(Type yes to cominue)")
        if retry != "yes":
            return

# Runs the program
existing_users.append(Account("admin", "admin", True))
while(1):
    next_function = input("What would you like to do?\n1) Create Account\n2) Login\ninput: ")
    if next_function == "1":
        create_account()
    elif next_function == "2":
        login()
    else:
        print("The provided function could not be recognized")
