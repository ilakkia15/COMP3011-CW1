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

def main():
    Register()

if __name__=="__main__":
    main()