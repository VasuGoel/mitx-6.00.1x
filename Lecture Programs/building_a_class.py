import datetime

class Person(object):
    def __init__(self, name):
        self.name = name
        self.birthdate = None
        self.lastName = name.split()[-1]

    def getLastName(self):
        return self.lastName

    def __str__(self):
        return self.name
