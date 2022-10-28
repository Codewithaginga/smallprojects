import string

import random

characters = list(string.ascii_letters + string.digits + '!@#%$£&()')

def get_pass():

    password_length = int(input("How long does your password is: "))

    random.shuffle(characters)

    password = []

    for ps in range(password_length):
        password.append(random.choice(characters))

        random.shuffle(password)


        password = "".join(password)

        print(password)



option = input("Do you want to generate a password(Yes/No): ")

if option == "Yes":
    get_pass()

elif option == "No":
    print('program ended')
    quit()

else:
    print('Invalid input, try again')
    get_pass()
