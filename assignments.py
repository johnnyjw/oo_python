#!/usr/bin/python

class MaxSizeList(object):
    def __init__(self, maximum):
        self.MaximumList = maximum

    def push(self, value):
        mylist = []
        mylist = self.list
        mylist.append(value)
        while len(mylist) > self.MaximumList:
            mylist.pop(0)
        self.list = mylist


    def get_list(self):
        return self.list