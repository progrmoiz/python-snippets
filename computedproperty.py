ng computed property and setting


class operators(object):
    def __getattr__(self, name):
        if name == 'age':
            return 40
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        print('set: %s %s' % (name, value))
        if name == 'age':
            self.__dict__['_age'] = value
        else:
            self.__dict__[name] = value


# OR BETTER WAY


class properties(object):
    def getage(self):
        return 40

    def setage(self, value):
        self._age = value

    age = property(getage, setage, None, None)


if __name__ == '__main__':
    x, y = operators(), properties()
    for ins in (x, y):
        print(ins.age)
        ins.age = 20
        print(ins._age)

