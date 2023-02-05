class Computer:

    def config(self):
        print('16Gb', '4Gb Ram', 'Core I 7')


#com1 =  Computer()
#Computer.config(com1)

class Human:

    def __init__(self):

        self.age = 23
        self.name = 'Madiang'


    def compare(self, other):

        if self.age == other.age:
            return True

        else:
            return False


h1 = Human()
h2 = Human()
#h2.age = 33


#if h1.compare(h2):
    #print('The same')
   
#else:

   # print('Not the same')


class Car:

    wheel = 4

    def __init__(self):
        self.mil = 4
        self.make = 'AUDI'



c1 = Car()
c2 =  Car()

Car.wheel = 10

c1.make = 'Mercedez Benz'

#print(c1.make, c1.wheel)
#print(c2.make, c2.wheel)


class Student:

    school = 'Madiang Foundation'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avrg(self):
        return (self.m1 + self.m2 + self.m3) / 3

    @classmethod
    def get_school(cls):
        return cls.school

    @staticmethod
    def info():
        print('This is a python programming Tutorials')


s1 = Student(23, 56, 67)
s2 = Student(21, 55, 35)

print(s1.avrg())
print(s2.avrg())

print(Student.get_school())

Student.info()











