# from stack import Stack
# from singly_linked_list import SinglyLinkedList
import sys

sys.path.append('../singly_linked_list')
sys.path.append('../stack')

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order.

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when
   implementing a Queue?

Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""


# class ListQueue:
# pass
class Queue:

    def __init__(self):
        # self.size = 0
        self.storage = []

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.append(value)

    def dequeue(self):
        return self.storage.pop(0) if len(self) > 0 else None


class SinglyListQueue:
    pass
# class Queue:

    # def __init__(self):
    #     # self.size = 0
    #     self.storage = SinglyLinkedList()

    # def __len__(self):
    #     return len(self.storage)

    # def enqueue(self, value):
    #     self.storage.append(value)

    # def dequeue(self):
    #     return self.storage.remove_first()


class StackQueue:
    pass
# class Queue:

#    def __init__(self):
#         # self.size = 0
#         self.storage = Stack()

#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.push(value)
#         # self.storage.append(value)

#     def dequeue(self):
#         newstack = Stack()
#         cur = self.storage.pop()
#         while cur != None:
#             newstack.push(cur)
#             cur = self.storage.pop()
#         top = newstack.pop()
#         cur = newstack.pop()
#         while cur != None:
#             self.storage.push(cur)
#             cur = newstack.pop()
#         return top
