class GetSet(object):

    def __init__(self, value):
        self.attrval = value

    @property
    def var(self):
        print 'getting the "var" attribute'
        return self.attrval

    @var.setter
    def var(self, value):
        print 'setting the "var"'
        self.attrval = value

    @var.deleter
    def var(self):
        print 'deleting the "var"'
        self.attrval = None

me = GetSet(5)

me.var = 1000
print me.var
del me.var
print me.var


class GetSet2(object):

    def __init__(self, value):
        self.attrval = value

    @property
    def goulet(self):
        print 'getting the "goulet" attribute'
        return self.attrval

    @goulet.setter
    def goulet(self, value):
        print 'setting the "goulet"'
        self.attrval = value

    @goulet.deleter
    def goulet(self):
        print 'deleting the "goulet"'
        self.attrval = None

me = GetSet2(5)

me.goulet = 1000
print me.goulet
del me.goulet
print me.goulet
