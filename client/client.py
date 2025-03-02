import requests

# Create a Session object as a global variable.
s = requests.Session()

def GetInput(input_field):
    # Create a boolean variable to determine whether the user input is not empty.
    empty = True
    # Ask for the user input.
    while empty:
        # Retrieve the user input.
        user_input = input(input_field.capitalize() + ": ")
        # Check whether the user input is empty.
        if len(user_input) == 0:
            # Display a message to provide user input.
            print("Please provide a " + input_field + ".")
        else:
            # Set the boolean variable to False to indicate non-empty user input.
            empty = False

    return user_input

def Register():
    # Display a message to the user to provide the required details.
    print("Please provide a username, email and password to register.")

    username = GetInput("username")
    email = GetInput("email")
    password = GetInput("password")

def GetCommand():
    # Create a boolean variable to determine whether the command is valid.
    valid = False
    # Loop until a valid command has been provided.
    while not valid:
        # Retrieve the command.
        command = input("")
        # Check whether the command is empty.
        if len(command) == 0:
            # Display a message to provide a valid command.
            print("Please provide a valid command.")
        else:
            # Set the boolean variable to False to indicate non-empty user input.
            empty = False

    return command.split()

def RunClient():
    # Run continuously.
    while True:
        # Get a command from the user.
        command = GetCommand()

        # TODO: Add calls to the corresponding functions.
        # Check whether the command exists and the number of arguments is correct.
        # Call the corresponding function if the command is valid.
        if command == "register" and len(command) == 1:
            Register()
        elif command == "login" and len(command) == 2:
            pass
        elif command == "logout" and len(command) == 1:
            pass
        elif command == "list" and len(command) == 1:
            pass
        elif command == "view" and len(command) == 1:
            pass
        elif command == "average" and len(command) == 3:
            pass
        elif command == "rate" and len(command) == 6:
            pass
        # The command does not exist or the number of arguments is incorrect.
        else:
            # Display a message to provide a valid command.
            print("Please provide a valid command.")

if __name__=="__RunClient__":
    RunClient()