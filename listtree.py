#!/usr/bin/env python3
# File listtree.py (2.x + 3.x)


class ListTree:
    """
    Mix-in that returns an __str__ trace of the entire class and all
    its object's attrs at and above self; run by print(), str() returns
    constructed string; uses __X attr names to avoid impacting clients;
    recurses to superclasses explicitly, uses str.format() for clarity.
    """

    def __attrnames(self, obj, indent):
        spaces = ' ' * (indent + 1)
        result = ''
        for attr in sorted(obj.__dict__):
            if attr.startswith('__') and attr.endswith('__'):
                result += spaces + '{0}\n'.format(attr)
            else:
                result += spaces + '{0}={1}\n'.format(attr, getattr(obj, attr))
        return result

    def __listclass(self, aClass, indent):
        dots = '.' * indent
        if aClass in self.__visited:
            return '\n{0}<Class {1}:, address {2}: (see above)>\n'.format(
                dots,
                aClass.__name__,
                id(aClass))
        else:
            self.__visited[aClass] = True
            here = self.__attrnames(aClass, indent)
            above = ''
            for super in aClass.__bases__:
                above += self.__listclass(super, indent + 4)
            return '\n{0}<Class {1}:, address {2}:\n{3}{4}{5}'.format(
                dots,
                aClass.__name__,
                id(aClass),
                here, above,
                dots)

    def __str__(self):
        self.__visited = {}
        here = self.__attrnames(self, 0)
        above = self.__listclass(self.__class__, 4)
        return '<Instance of {0}, address {1}:\n{2}{3}>'.format(
            self.__class__.__name__,
            id(self),
            here, above)


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

    tester(ListTree)
