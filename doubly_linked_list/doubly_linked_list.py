
class ListNode:
    """
    Each ListNode holds a reference to its previous node
    as well as its next node in the List.
    :type prev: ListNode
    """

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    # def get_prev(self):
    #     return self.prev
    # def set_prev(self, node):
    #     self.prev = node

    # def get_next(self):
    #     return self.next
    # def set_next(self, node):
    #     self.next = node

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""

        node = ListNode(value, self, self.next)
        if self.next != None:
            self.next.prev = node
        self.next = node

    def append_node(self, node):
        node.next = self.next
        if node.next:
            node.next.prev = node
        node.prev = self
        self.next = node

        # current_next = self.next
        # self.next = ListNode(value, self, current_next)
        # if current_next:
        #     current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""

        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def prepend_node(self, node):
        node.prev = self.prev
        if node.prev:
            node.prev.next = node
        node.next = self
        self.prev = node

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""

        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def initialize(self, value):
        node = ListNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly."""

        if self.length == 0:
            self.initialize(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
        # node = ListNode(value, None, self.head)
        # if self.length == 0:
        #     self.tail = node
        # if self.head:
        #     self.head.set_prev(node)
        # self.head = node
            self.length += 1

    def remove_from_head(self):
        """Removes the List's current head node, making the
        current head's next node the new head of the List.
        Returns the value of the removed Node."""

        if self.length == 0:
            return None
        removed_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            removed_node.delete()
        self.length -= 1
        return removed_node.value

    def add_to_tail(self, value):
        """Wraps the given value in a ListNode and inserts it 
        as the new tail of the list. Don't forget to handle 
        the old tail node's next pointer accordingly."""

        if self.length == 0:
            self.initialize(value)
        else:
            self.tail.insert_after(value)
            self.tail = self.tail.next
        # node = ListNode(value, self.tail, None)
        # if self.length == 0:
        #     self.head = node
        # if self.tail:
        #     self.tail.set_next(node)
        # self.tail = node
            self.length += 1

    def remove_from_tail(self):
        """Removes the List's current tail node, making the 
        current tail's previous node the new tail of the List.
        Returns the value of the removed Node."""

        if self.length == 0:
            return None
        removed_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            removed_node.delete()
        self.length -= 1
        return removed_node.value

        # if self.length == 0:
        #     return None
        # if self.length == 1:
        #     self.head = None
        # removed_node = self.tail
        # self.tail = self.tail.get_prev()
        # self.length -= 1
        # return removed_node.value

    def move_to_front(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List."""

        # check if list or node argument are valid for operation
        if self.length == 0:
            raise Exception("Cannot perform on empty list")
        contains = False
        current = self.head
        while current:
            if current == node:
                contains = True
                break
            else:
                current = current.next
        if not contains:
            raise Exception('Node argument not member of list')

        # only valid case for this to do something is
        # if length > 1 and passed node is NOT the HEAD
        if self.length > 1 and node != self.head:
            if self.tail == node:
                self.tail = self.tail.prev
            node.delete()
            self.head.prepend_node(node)
            self.head = node

    def move_to_end(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new tail node of the List."""

        # check if list or node argument are valid for operation
        if self.length == 0:
            raise Exception("Cannot perform on empty list")
        contains = False
        current = self.head
        while current:
            if current == node:
                contains = True
                break
            else:
                current = current.next
        if not contains:
            raise Exception('Node argument not member of list')

        # only valid case for this to do something is
        # if length > 1 and passed node is not the tail
        if self.length > 1 and node != self.tail:
            if self.head == node:
                self.head = self.head.next
            node.delete()
            self.tail.append_node(node)
            self.tail = node

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""

        if self.length == 0:
            raise Exception("Cannot perform on empty list")
        contains = False
        current = self.head
        while current:
            if current == node:
                contains = True
                break
            else:
                current = current.next
        if not contains:
            raise Exception('Node argument not member of list')

        # check if list or node argument are valid for operation
        if node == self.head:
            self.head = self.head.next
        if node == self.tail:
            self.tail = self.tail.prev
        node.delete()
        self.length -= 1

    def get_max(self):
        """Returns the highest value currently in the list"""

        if not self.head:
            return None

        max_val = self.head.value
        current = self.head.next
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val
