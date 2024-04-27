def main():
    """
    This function serves as the entry point for the Monthly Loan Payment Calculator.
    It prompts the user for loan details, calculates the monthly payment, and offers the option to calculate another loan payment.
    """
    while True:
        print('This is a Monthly Loan payment calculator')
        print('')

        principal = float(input('Input the loan amount: '))
        apr = float(input('Input the annual interest rate: '))
        years = int(input('Input amount of years: '))

        monthly_interest_rate = apr / 1200
        number_of_months = years * 12
        monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-number_of_months))

        print('The monthly payment for this loan is: $%.2f' % monthly_payment)

        choice = input("Do you want to calculate another loan payment? (y/n): ")
        if choice.lower() != "y":
            break

if __name__ == "__main__":
    main()
