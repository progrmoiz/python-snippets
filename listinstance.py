#!/usr/bin/env python3
# File listinstance.py (2.x + 3.x)

from __future__ import print_function


class ListInstance:
    """
    Mix-in class that provides a formatted print() or str() of instances via
    inheritance of __str__ coded here; displays instance attrs only; self is
    instance of lowest class; __X names avoid clashing with client's attrs
    """

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__,
            id(self),
            self.__attrnames())


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

    tester(ListInstance)
