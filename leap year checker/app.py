"""
Module Name: leap_year_checker.py
Author: Mohammed Kolo Ibrahim
Date: 22/03/2024

Description:
This module provides a function to check whether a given year is a leap year or not.

Functions:
- is_leap_year: Checks if a given year is a leap year.
"""

def is_leap_year(year):
    """
    Checks if a given year is a leap year.

    Args:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int) or year < 0:
        raise ValueError("Year must be a positive integer")

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False

def main():
    try:
        year = int(input("Enter the year you want to check: "))
        if is_leap_year(year):
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    except ValueError:
        print("Invalid input. Please enter a valid year (a positive integer).")

# Call the main function when the script is executed
if __name__ == "__main__":
    main()