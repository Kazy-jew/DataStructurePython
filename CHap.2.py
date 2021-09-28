# for change
from dategen import Calendar
class FirstClass:
    name = 'A'
    sex = 'Bi'
    def setyear(self, year):
        self.year = year
    def setdate(self, date):
        self.date = date
    def setdata(self, data):
        self.data = data
    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print("Current value = {}".format(self.data))

class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __str__(self):
        return '[ThirdClass: {}]'.format(self.data)
    def mul(self, other):
        self.data *= other


a = ThirdClass('abc')
a.mul(3)
