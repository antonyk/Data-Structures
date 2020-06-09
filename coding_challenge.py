import collections
import inspect
myarr = ['Joe', '2', 'Ted', '4.98', '14', 'Sam', 'void *', '42', 'float', 'pointers', '5006']

# for item in myarr:
#   print(item)

newarr = ['Bob', 'Slack', ('a', 'b'), ['reddit', '89', 101, ['alacritty', '(brackets)', 5, 375]], 0, ['{slice, owned}'], 22]

# tuples, lists, dictionaries

def printel(element):
  # isIter = False
  # try:
  #   _ = iter(element)
  #   isIter = True
  # except:
  #   pass

  if getattr(element, '__iter__', None) != None and not isinstance(element, str):
    for item in element:
      printel(item)
  else:
    print(element)


for item in newarr:
  printel(item)
