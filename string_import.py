# you can use builtin __import__ function

modname = 'string'
string = __import__(modname)
print(string)    #will print the 'string'

# Python official prefferred way

import importlib
modname = 'string'
string = importlib.import_module(modname)
print(string)
