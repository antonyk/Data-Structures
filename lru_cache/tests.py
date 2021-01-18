class Link(object):
    __slots__ = 'prev', 'next', 'hello'


lnk = Link()
# print(lnk.prev)

lnk.prev, lnk.next, lnk.hello = 1, 2, 3

print(lnk.prev)
