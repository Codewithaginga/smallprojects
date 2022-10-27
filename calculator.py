#  Calculator

def add(a, b):

    answer =  a + b
    print(f'{a} + {b} = {answer:,}')

def sub(a, b):

    answer = a - b
    print(f'{a} - {b} = {answer:,}')

def mul(a, b):

    answer = a * b
    print(f'{a} * {b} = {answer:,}')

def div(a, b):
    answer = a / b
    print(f'{a} / {b} = {answer:,}')

def expo(a, b):
    answer = a ** b
    print(f'{a} ** {b} = {answer:,}')

def mod(a, b):

    answer = a % b
    print(f'{a} % {b} = {answer:,}')


while True:
    print('A. addition')
    print('B. substraction')
    print('C. division')
    print('E. exponential')
    print('D. modulus')
    print('M. Mulptiplication')
    print('F. quit')
    operate = input('Input your operator: ')

    if operate == "a" or "A":
        print('Addition')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        add(a, b)

    elif operate == "b" or "B":
        print('Subtractionn')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        sub(a, b)

    elif operate == "m" or "M":
        print('Multiplication')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        mul(a, b)

    elif operate == "c" or "C":
        print('division')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        div(a, b)

    elif operate == "d" or "D":
        print('Modulus')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        mod(a, b)

    elif operate == "e" or "E":
        print('Exponentail')
        a = int(input('Enter first Number: '))
        b = int(input('Enter second Number: '))
        expo(a, b)

    elif operate == "f" or "F":
        print('goodbye')
        quit()

    
    