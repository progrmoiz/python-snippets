#!/usr/bin/env python3
"""
reloadall.py: transitively reload nested module (2.x + 3.x)
Call reload_all with one or more import module module objects
"""

import types
from imp import reload  # from required in 3.x


def status(module):
    print('reloading ' + module.__name__)


def tryreload(module):
    try:
        reload(module)
    except:
        print('FAILED: %s' % module)


def transitive_reload(module, visited):
    if not module in visited:  # Trap cycles, duplicates
        status(module)  # Reload this module
        tryreload(module)  # And visit children
        visited[module] = True
        for attrobj in module.__dict__.values():  # For all attrs
            if type(attrobj) == types.ModuleType:  # Recur if module
                transitive_reload(attrobj, visited)


def reload_all(*args):
    visited = {}  # Main entry point
    for arg in args:  # For all passed in
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)


def tester(reloader, modname):  # Self-test code
    import importlib
    import sys  # Import on tests only
    if len(sys.argv) > 1:
        modname = sys.argv[1]  # command line (or passed)
    module = importlib.import_module(modname)  # Import by name string
    reloader(module)  # Test passed-in reloade


if __name__ == '__main__':
    tester(reload_all, 'reloadall')
