class MyDict(dict):
    def __setitem__(self, key, value):
        print "Doing a setitem"
        dict.__setitem__(self, key, value)

dd = MyDict()
dd['a'] = 5
dd['b'] = 6

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key]))


class MyList(list):

    def __getitem__(self, index):
        if index == 0:  raise IndexError
        if index > 0: index = index - 1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:  raise IndexError
        if index > 0: index = index - 1
        list.__setitem__(self, index, value)


x = MyList(['a', 'b', 'c'])

print x

x.append('spam');

print x[1]

print x[4]

y = ['a', 'b', 'c']

print y[1]

