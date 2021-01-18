# main.py
import sys

import module1
print('================================')
print(f'running main.py - module name: {__name__}')

print(module1)

module1.pprint_dict('main.globals', globals())

print(sys.path)
print(sys.modules['module1'])
print('================================')
