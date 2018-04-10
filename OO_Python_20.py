#!/usr/bin/python

import random

class Animal(object):

    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Elvis Dog', 'Bull Dog', 'Goulet Dog', 'Pug'])

    def fetch(self, thing):
        print '%s goes after the %s!' % (self.name, thing)

d= Dog('dogname')

print d.name
print d.breed


# now test static methods
class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = self.filterint(val)
        InstanceCounter.count += 1

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value


a = InstanceCounter(5)
b = InstanceCounter(76)
c = InstanceCounter('hello')

print a.val
print b.val
print c.val