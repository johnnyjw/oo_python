class Date(object):
    def get_date(self):
        return '2014-10-13'

class Time(Date):
    def get_time(self):
        return '08:13:07'

aa = Time()
print(aa.get_time())
print(aa.get_date())




class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print ('%s is eating %s.' % (self.name, food))

class Dog(Animal):
    def fetch(self, thing):
        print ('%s goes after the %s!' % (self.name, thing))

class Cat(Animal):
    def swatstring(self):
        print ('%s shreds the string!' % (self.name))


r = Dog('Rover')
f = Cat('Fluffy')

r.fetch('paper')
f.swatstring()
r.eat('dog food')
f.eat('cat food')
r.swatstring()


# Polymorphism!
class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print ('{0} eats {1}'.format(self.name, food))


class Dog(Animal):

    def fetch(self, thing):
        print ('{0} goes after the {1}'.format(self.name, thing))

    def show_affection(self):
        print ('{0} wags tail'.format(self.name))


class Cat(Animal):

    def swatstring(self):
        print ('{0} shreds the string!'.format(self.name))

    def show_affection(self):
        print ('{0} purrs'.format(self.name))


for a in (Dog('Rover'), Cat('Fluffy'), Cat('Elvis'), Dog('Michael')):
    a.show_affection()