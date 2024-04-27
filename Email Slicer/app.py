def email_slicer():
    """
    Slices an email address into its components: username, domain, and extension.
    """
    print('Welcome to the Email Slicer!')
    print()

    email_input = input("Please enter your email address: ")

    try:
        username, domain = email_input.split('@')
        domain, extension = domain.split('.')
    except ValueError:
        print("Invalid email address format. Please provide a valid email address.")
        return

    print('Username:', username)
    print('Domain:', domain)
    print('Extension:', extension)

if __name__ == "__main__":
    email_slicer()
