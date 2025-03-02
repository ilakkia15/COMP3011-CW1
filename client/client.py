import requests

# Create a Session object as a global variable.
s = requests.Session()

def Register():
    # Display a message to the user to provide the required details.
    print("Please provide a username, email and password to register.")

    # Create a boolean variable to determine if the username is valid.
    valid_username = False
    # Ask for a valid username.
    while not valid_username:
        # Retrieve a username from the user.
        username = input("Username: ")
        # Check whether the username is empty.
        if len(username) == 0:
            # Display a message to provide a username.
            print("Please provide a username.")
        else:
            # Set the boolean variable to True to indicate a valid username.
            valid_username = True

    # Create a boolean variable to determine if the email is valid.
    valid_email = False
    # Ask for a valid email.
    while not valid_email:
        # Retrieve a email from the user.
        email = input("Email: ")
        # Check whether the email is empty.
        if len(email) == 0:
            # Display a message to provide an email.
            print("Please provide an email.")
        else:
            # Set the boolean variable to True to indicate a valid email.
            valid_email = True

    # Create a boolean variable to determine if the password is valid.
    valid_password = False
    # Ask for a valid password.
    while not valid_password:
        # Retrieve a password from the user.
        password = input("Password: ")
        # Check whether the password is empty.
        if len(password) == 0:
            # Display a message to provide an password.
            print("Please provide an password.")
        else:
            # Set the boolean variable to True to indicate a valid password.
            valid_password = True
