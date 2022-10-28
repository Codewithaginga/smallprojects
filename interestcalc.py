# collecy neccesary input; principal, apr, years
# calculate the monthly payment
# show to the use

def main():
    print('This is a monthly payment calculator')
    print("")

    principal = float(input("Enter the loan amount: "))

    apr = float(input("The annual interest rate: "))

    years = int(input('Amount of Years: '))


    monthly_interest_rate = apr / 1_200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate)) ** (-amount_of_months)

    print(f'The monthly payment for this loan is {monthly_payment:,}')



main()