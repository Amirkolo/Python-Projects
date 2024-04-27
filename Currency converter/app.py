"""
Currency Converter Module

This module provides functions to fetch real-time exchange rates and perform currency conversion.
It includes the following functions:
- get_exchange_rates: Fetches real-time exchange rates for a base currency against various target currencies.
- convert_currency: Converts an amount from one currency to another using real-time exchange rates.
- main: Prompts the user for currency conversion, retrieves real-time rates, performs conversion,
        and displays the result with timestamps.

Created by: Mohammed Kolo Ibraim
"""

import requests
from datetime import datetime

def get_exchange_rates(base_currency="USD"):
    """
    Fetches real-time exchange rates for a base currency against various target currencies
    using a generic API provider (might have limitations).

    Args:
        base_currency (str, optional): The base currency for which rates are retrieved. Defaults to "USD".

    Returns:
        dict: A dictionary containing exchange rates for target currencies (if successful), or an empty dictionary (if API call fails).
    """

    # Replace with a free generic API endpoint (consider limitations)
    # This example uses a free, rate-limited API. Explore other options for broader coverage.
    api_url = f"https://api.exchangerate.host/latest?base={base_currency}"
    response = requests.get(api_url)

    if response.status_code == 200:
        try:
            data = response.json()
            return data["rates"]
        except KeyError:
            print(f"API response missing 'rates' key. Using empty rates.")
            return {}
    else:
        print(f"Error retrieving exchange rates: {response.status_code}")
        return {}

def convert_currency(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another using real-time exchange rates.

    Args:
        amount (float): The amount to convert.
        from_currency (str): The currency code of the amount to be converted.
        to_currency (str): The currency code of the desired output currency.

    Returns:
        float: The converted amount in the target currency, or None if an error occurs.
    """

    rates = get_exchange_rates(from_currency)

    if to_currency not in rates:
        print(f"Unsupported currency: {to_currency}")
        return None

    # Handle base currency conversion (no need for external rates)
    if from_currency == to_currency:
        return amount

    return amount * rates[to_currency]

def main():
    """
    Prompts the user for currency conversion, retrieves real-time rates,
    performs conversion, and displays the result with timestamps.
    """

    print("Welcome to the Currency Converter!")
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        from_currency = input("Enter the currency you have (e.g., USD, EUR, JPY): ").upper()
        to_currency = input("Enter the currency you want (e.g., USD, EUR, JPY): ").upper()

        amount = None
        while amount is None:
            try:
                amount = float(input("Enter the amount to convert: "))
                if amount <= 0:
                    print("Please enter a positive amount.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        converted_amount = convert_currency(amount, from_currency, to_currency)

        if converted_amount is not None:
            print(f"{amount} {from_currency} is equivalent to {converted_amount:.2f} {to_currency}.")
            print(f"Exchange rates retrieved on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        else:
            print("Conversion failed. Please check the currencies you entered.")

        choice = input("Do you want to convert again? (y/n): ").lower()
        if choice != "y":
            break

if __name__ == "__main__":
    main()
