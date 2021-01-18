import sys
import importer
import module2

module1 = importer.import_('module1', 'module1_source.py', '.')


print('sys says:', sys.modules.get('module1', 'module not found'))


module2.hello()