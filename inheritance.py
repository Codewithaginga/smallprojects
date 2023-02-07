class Terminal1A:

    def __init__(self):
        print('in A init')

    def flight_one(self):

        print('From Nairobi to Johanesburg')

    def flight_two(self):

        print('From Nairobi to Dakar')


class Terminal1B(Terminal1A):

    def __init__(self):
        super().__init__()
        print('in B init')


    def flight_three(self):

        print('From Nairobi to London Heathrow')

    def flight_four(self):

        print('From Nairobi to Schiphol')

    def search(self):

        super().flight_two()


term = Terminal1B()

term.search()





