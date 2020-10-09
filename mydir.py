#!python
"""
mydir.py: a module that list the namespaces of other modules
"""
from __future__ import print_function

seplen = 60
sepchr = '-'

def listing(module, verbose=True):
    sepline = sepchr * seplen
    if verbose:
        print(sepline)
        print('name:', module.__name__, 'file:', module.__file__)
        print(sepline)

    count = 0
    for attr in sorted(module.__dict__):  # Scan namespace keys (or enumerate)
        print('%02d) %s' % (count, attr), end=' ')
        if attr.startswith('__'):
            print('<built-in name>')  # Skip __file__, etc
        else:
            print(getattr(module, attr))  # Same as .__dict__[attr]
        count += 1

    if verbose:
        print(sepline)
        print(module.__name__, 'has following %d names' % count)
        print(sepline)

if __name__ == '__main__':
    import mydir
    listing(mydir)
