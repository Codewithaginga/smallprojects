class Students:

    def __init__(self, name, rollno):

        self.name = name
        self.rollno = rollno

    def show(self):

        print(self.name, self.rollno)


    class Laptop:

        def __init__(self):

            self.brand = 'HP'
            self.cpu = 'I7'
            self.RAM = 8

        def show(self):

            print(self.brand, self.cpu, self.RAM)

s1 = Students('Aginga', 12)

lap1 = Students.Laptop()

s1.show()
lap1.show()
