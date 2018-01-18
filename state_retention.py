#!/usr/bin/env python3
from __future__ import print_function


# nonlocal 3.x
def tester(start):
    state = start

    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested


# nested global 2.x, 3.x
def tester1(start):
    global gstate
    gstate = start

    def nested(label):
        global gstate
        print(label, gstate)
        gstate += 1
    return nested


# with mutables
def tester2(start):
    state = [start]

    def nested(label):
        print(label, state[0])
        state[0] += 1
    return nested


# function attr
def tester3(start):

    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = 0
    return nested


# class
class tester4(object):

    def __init__(self, start):
        self.state = start

    def __call__(self, label):
        print(label, self.state)
        self.state += 1


if __name__ == '__main__':
    for test in (tester, tester1, tester2, tester3, tester4):
        f = test(0)
        f('name: %s, state:' % test.__name__)
        f('name: %s, state:' % test.__name__)
        f('name: %s, state:' % test.__name__)
        f('name: %s, state:' % test.__name__)
        print()
    print('done')
