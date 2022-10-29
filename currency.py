
def main():

    print(f'This program convert us dollar to sterling pound')
    print()

    dollars = eval(input('Enter amount in dollars: '))

    pounds = convert_to_pounds(dollars)

    print(f'That is {pounds} pounds')


convert_to_pounds = lambda dollars: dollars * 0.82

main()
