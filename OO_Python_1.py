myint = 5
mystr = 'hello'

print type(myint)
print type(mystr)

dir(myint)

## test concepts of methods from 'primary' objects
var = 'hello, world!'
print type(var)
print var.upper()

## class with nothing in it!!
class MyClass(object):
    pass

this_obj = MyClass()

print this_obj

that_obj = MyClass()

print that_obj

### redoing the class including a variable
class MyClass(object):
    var = 10

this_obj = MyClass()
that_obj = MyClass()

print this_obj.var
print that_obj.var

#### New class
class Joe(object):
    greeting = 'hello, Joe'

thisjoe = Joe()

print thisjoe.greeting

#### redefined, but with a method!
class Joe(object):
    def callme(self):
        print('calling "callme" method with instance:  ')
        print self

thisjoe = Joe()

thisjoe.callme()

print thisjoe

## Another Class
class MyClass(object):
    def dothis(self):
        print('doing this')

myinst = MyClass()
myinst.dothis()

## Revise this class!
import random

class MyClass(object):
    def dothis(self):
        self.rand_val = random.randint(1,10)

myinst = MyClass()
myinst.dothis()
print(myinst.rand_val)
