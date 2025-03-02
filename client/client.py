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

    # Get a username, email and password from the user.
    username = GetInput("username")
    email = GetInput("email")
    password = GetInput("password")

def GetCommand():
    # Create a boolean variable to determine whether a given command is valid.
    valid = False
    # Loop until a valid command has been provided.
    while not valid:
        # Retrieve the command.
        command = input("").split()

        # TODO: Add calls to functions for all the commands. 

        # Check whether a command has been provided.
        if len(command) > 0:
            # Check whether the command exists and the number of arguments is correct.
            # Set the boolean variable to True if the command is valid.
            # Call the corresponding function if the command is valid.
            if command[0] == "register" and len(command) == 1:
                valid = True
                Register()
            elif command[0] == "login" and len(command) == 2:
                valid = True
            elif command[0] == "logout" and len(command) == 1:
                valid = True
            elif command[0] == "list" and len(command) == 1:
                valid = True
            elif command[0] == "view" and len(command) == 1:
                valid = True
            elif command[0] == "average" and len(command) == 3:
                valid = True
            elif command[0] == "rate" and len(command) == 6:
                valid = True
            # The command does not exist or the number of arguments is incorrect.
            else:
                # Display a message to provide a valid command.
                print("Please provide a valid command.")
        # A command has not been provided.
        else:
            # Display a message to provide a valid command.
            print("Please provide a valid command.")

def main():
    # Run continuously.
    while True:
        # Get the command provided by the user.
        GetCommand()

if __name__=="__main__":
    main()
