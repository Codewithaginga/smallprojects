# python dictionary with aa key value pair
# collect import from the user

def dictionary():

    aginga_dict = {
        'novice': 'unexperince or a begginer person',
        'Morass': 'something that is complicated',
        'Nebulous': 'somthing that is unclear'
    }

    word = input('Enter a word to search: ')

    while True:
        if word == "":
            break

        if word in aginga_dict:
            print(word ':' aginga_dict[word])

dictionary()