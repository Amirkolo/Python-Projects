"""
This module provides a simple site connectivity checker program
for Python 2. It checks the connectivity to a user-provided URL
and displays information about the connection attempt.
"""

import urllib.request as urllib

def main(url):
    """
    This function checks the connectivity to a given URL.

    Args:
        url (str): The URL of the website to check.

    Returns:
        None
    """

    print('Checking connectivity to', url)

    try:
        response = urllib.urlopen(url)
        print('Connected to', url, 'successfully')
        print("The response code was", response.getcode())
        print("Server:", response.info().get('Server'))  # Example: print server type
    except Exception as e:
        print("Error connecting to the URL:", e)
        return

print('Welcome to the site connectivity checker!')

while True:
    input_url = input('Input the url of the site you want to check (or "exit" to quit): ')
    if input_url.lower() == "exit":
        break
    main(input_url)

print('Thank you for using the site connectivity checker!')
