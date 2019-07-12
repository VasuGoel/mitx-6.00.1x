import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthday = None
        self.lastName = name.split()[-1]

    def getLastName(self):
        return self.lastName

    def __str__(self):
        return self.name

    def __lt__(self, other):
        """
        Return True if self's name is lexicographically less than other's name and False otherwise
        """
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def setBirthday(self, month, day, year):
        self.birthday = datetime.date(year, month, day)

    def getAge(self):
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days



p1 = Person('Mark Zukerberg')
p1.setBirthday(day=14, month=5, year=1984)
p2 = Person('Drew Houston')
p2.setBirthday(day=4, month=3, year=1983)
p3 = Person('Bill Gates')
p3.setBirthday(day=28, month=10, year=1955)
p4 = Person('Andrew Gates')
p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

for p in personList:
    print(p)

print(f'\nMark Zuckerberg\'s age: {round(p1.getAge()/365, 2)} years\n')
