import module1
print('running module2.py')


def hello():
    print('module 2 says Hello!\nand...')
    module1.hello()
