"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def get_prev(self):
        return self.prev
    def set_prev(self, node):
        self.prev = node
    
    def get_next(self):
        return self.next
    def set_next(self, node):
        self.next = node

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        node = ListNode(value, self, self.next)
        if self.next != None:
            self.next.prev = node
        self.next = node

        # current_next = self.next
        # self.next = ListNode(value, self, current_next)
        # if current_next:
        #     current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        node = ListNode(value, None, self.head)
        if self.length == 0:
            self.tail = node
        if self.head:
            self.head.set_prev(node)
        self.head = node
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.tail = None
        removed_node = self.head
        self.head = self.head.get_next()
        self.length -= 1
        return removed_node.value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        node = ListNode(value, self.tail, None)
        if self.length == 0:
            self.head = node
        if self.tail:
            self.tail.set_next(node)
        self.tail = node
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
        removed_node = self.tail
        self.tail = self.tail.get_prev()
        self.length -= 1
        return removed_node.value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
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

        # if length 2 or more:
        if self.length > 1 and node != self.head:
            # sets up next of previous node links
            node.prev.next = node.next
            # if node is tail => no next
            if self.tail == node:
                self.tail = node.prev
            # node not tail => has next
            else:
                # sets up previous of next node
                node.next.prev = node.prev

            # set up the new head node
            node.prev = None
            node.next = self.head
            self.head = node

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
    # check if list or node argument are valid for operation
        # if self.length
        # node.delete()
        # if self.tail:
        #     self.tail.insert_after(node.value)
        # self.tail = self.tail.next

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

        # if length 2 or more:
        if self.length > 1 and node != self.tail:
            # sets up next of previous node links
            node.next.prev = node.prev
            # if node is head => no prev
            if self.head == node:
                self.head = node.next
            # node not head => has prev
            else:
                # sets up next of prev node
                node.prev.next = node.next

            # set up the new tail
            node.next = None
            node.prev = self.tail
            self.tail = node

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
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

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            if node == self.head:
                self.head = self.head.next
            elif node == self.tail:
                self.tail = self.tail.prev
            else:
                node.delete()
        self.length -= 1
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        
        max_val = self.head.value
        current = self.head.next
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val


