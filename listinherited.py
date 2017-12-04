#!/usr/bin/env python3
# File listinherited.py (2.x + 3.x)


class ListInherited:
    """
    Use dir() to collect both instance attr and names inherited from
    its classes; Python 3.x shows more name than 2.x because of the
    implied object superclass in the new-style class model; getattr()
    fetches inherited names not in self.__dict__; user __str__, not
    __repr__, or else the loops when printing bound method!
    """

    def __attrname(self):
        result = ''
        for attr in dir(self):  # instance dir
            if attr[:2] == '__' and attr[-2:] == '__':
                result += '\t%s\n' % attr
            else:
                result += '\t%s=%s\n' % (attr, getattr(self, attr))
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),           # My address
            self.__attrname())  # name=value list


def tester(listerclass, sept=False):

    class Super:

        def __init__(self):
            self.data1 = 'spam'

        def ham(self):
            pass

    class Sub(Super, listerclass):

        def __init__(self):
            Super.__init__(self)
            self.data2 = 'eggs'
            self.data3 = 42

        def spam(self):
            pass

    instance = Sub()
    print(instance)
    if sept:
        print('-' * 80)


if __name__ == '__main__':

    tester(ListInherited)
