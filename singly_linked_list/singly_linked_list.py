# Node
class SinglyLinkedNode:
  def __init__(self, value, next_node=None):
    self._value = value
    self._next = next_node

  def get_value(self):
    return self._value

  def get_next(self):
    return self._next

  def set_next(self, next_node):
    self._next = next_node

# Linked List
class SinglyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def append(self, value):
    node = SinglyLinkedNode(value)
    if self.head == None:
      self.head = node
      self.tail = node
    else:
      self.tail.set_next(node)
      self.tail = node

  def remove_last(self):
    last_node = self.tail
    if self.head == None:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      prev_to_last = self.head
      while not prev_to_last.get_next() == last_node:
        prev_to_last = prev_to_last.get_next()
      self.tail = prev_to_last
    return last_node.get_value()

  def remove_first(self):
    first_node = self.head
    if self.head == None:
      return None
    elif self.head == self.tail:
      self.head = None
      self.tail = None
    else:
      self.head = self.head.get_next()
    return first_node.get_value()

  def contains(self, data):
    node = self.head
    if self.head == None:
      return False
    while node != None:
      if node.get_value() == data:
        return True
      else:
        node = node.get_next()
    return False

  def get_max(self):
    if self.head == None:
      return None
    node = self.head
    max_value = node.get_value()
    while node.get_next() != None:
      node = node.get_next()
      if node.get_value() > max_value:
        max_value = node.get_value()
    return max_value

class LinkedList(SinglyLinkedList):

  def add_to_tail(self, data):
    super().append(data)

  def remove_tail(self):
    return super().remove_last()

  def remove_head(self):
    return super().remove_first()


