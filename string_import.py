# you can use builtin __import__ function

modname = 'strings'
string = __import__(modname)
print(strings)

# Python official prefferred way

import importlib
modname = 'strings'
strings = importlib.import_module(modname)
print(strings)
