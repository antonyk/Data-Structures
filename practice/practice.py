from types import ModuleType
import types
import calendar
import sys
import fractions
import math

print(math)


print(fractions)

print(globals())

print(globals()['math'])

mod_math = globals()['math']

print(mod_math.sqrt(2))


print(type(globals()))

print(type(math))

print(id(math))


print(type(sys.modules))

print(sys.modules)

print(math.__name__)

print(sys.modules['fractions'].__spec__)

print(calendar)


print(types)

print(isinstance(fractions, types.ModuleType))


mod = types.ModuleType('test', 'This is a test module')


print(isinstance(mod, ModuleType))

mod.pi = 3.14

mod.hello = lambda: print('Hello')

print(mod.__dict__)

hello = mod.hello

print('hello' in globals())
print('mod' in globals())

hello()
