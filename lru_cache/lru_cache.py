# lru_cache.py

class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""

    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"{self.value}"

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
        after this node. Note that this node could already
        have a next node it is point to."""

        new_node = ListNode(value, self, self.next)
        if self.next != None:
            self.next.prev = new_node
        self.next = new_node

    def append_node(self, node):
        node.prev = self
        node.next = self.next
        if self.next != None:
            self.next.prev = node
        self.next = node

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
        before this node. Note that this node could already
        have a previous node it is point to."""

        new_node = ListNode(value, self.prev, self)
        if self.prev != None:
            self.prev.next = new_node
        self.prev = new_node

    def prepend_node(self, node):
        node.next = self
        node.prev = self.prev
        if self.prev != None:
            self.prev.next = node
        self.prev = node

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
        accordingly, effectively deleting this ListNode."""

        if self.prev:
            self.prev.next = self.next
            # self.prev = None
        if self.next:
            self.next.prev = self.prev
            # self.next = None


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def __str__(self):
        cur = self.head
        num = 0
        result = ''
        while cur:
            result += f"{', ' if num > 0 else ''}{num}: {str(cur)}"
            num += 1
            cur = cur.next

        if result == '':
            result = 'Empty'
        return result

    def initialize(self, value):
        node = ListNode(value)
        self.head = node
        self.tail = node
        self.length = 1

    def contains(self, node):
        if self.length == 0:
            return False

        current = self.head
        while current:
            if current is node:
                return True
            current = current.next
        return False

    def add_to_head(self, value):
        """Wraps the given value in a ListNode and inserts it 
        as the new head of the list. Don't forget to handle 
        the old head node's previous pointer accordingly."""

        if self.length == 0:
            self.initialize(value)
        else:
            self.head.insert_before(value)
            self.head = self.head.prev
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

    def move_to_front(self, node):
        """Removes the input node from its current spot in the 
        List and inserts it as the new head node of the List."""

        # check if list or node argument are valid for operation
        if not self.contains(node):
            raise Exception("Node argument not member of list")

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
        if not self.contains(node):
            raise Exception("Node argument not member of list")

        # only valid case for this to do something is
        # if length > 1 and passed node is not the tail
        if self.length > 1 and node != self.tail:
            if self.head == node:
                self.head = self.head.next
            node.delete()
            self.tail.append_node(node)
            self.tail = node

    def append(self, node):
        if self.length > 1:
            self.tail.append_node(node)
        self.tail = node
        self.length += 1

    def prepend(self, node):
        if self.length > 1:
            self.head.prepend_node(node)
        self.head = node
        self.length += 1

    def delete(self, node):
        """Removes a node from the list and handles cases where
        the node was the head or the tail"""

        if node:
            # check if list or node argument are valid for operation
            if not self.contains(node):
                raise Exception("Node argument not member of list")

            # check if list or node argument are valid for operation
            if node is self.head:
                self.head = self.head.next
            if node is self.tail:
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


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.store = {}  # key / value --
        self.top_id = 0
        self.old_id = 0
        self.recent = {}

    def __str__(self, order='list'):
        ret = '==== lru ====\n'

        # if order == 'dict':
        #     for k, v in self.store.items():
        #         ret += f"key: {str(k)}, value: {str(v.value[1])}\n"
        # elif order == 'list':
        #     node = self.order_list.head
        #     while node:
        #         print(node.value)
        #         # ret += f"key: {str(node.value[0])}, value: {str(node.value[1])}\n"
        #         node = node.next

        ret += '==== end ====\n'
        return ret

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """

        node = self.store.get(key, None)
        print('get: ', node)

        if node:
            self.priority_list.move_to_front(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """

        node = self.store.get(key, None)
        print('set: ', node)
        node_value = (key, value)

        if key not in
        if node:
            node.value = node_value
            self.priority_list.move_to_front(node)
        else:
            new_node = ListNode(node_value)
            self.priority_list.prepend(new_node)
            self.store[key] = new_node
            self.size += 1

        # cleanup if size > limit
        if self.size > self.limit:
            old_node = self.priority_list.tail
            print(self.priority_list)
            del self.store[old_node.value[0]]
            self.priority_list.remove_from_tail()
            self.size -= 1


class LRUCacheDDL:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.size = 0
        self.store = {}  # key / value --

        self.priority_list = DoublyLinkedList()

        # IMPLEMENTATION # 2 (USING DICT AND TRACKER)
        # self.order = {} # key =

        # each insert/update increments this tracker; use it as the key in order dict
        # self.last = 0

        # need a data structure to hold the order of the elements

    def __str__(self, order='list'):
        ret = '==== lru ====\n'

        # if order == 'dict':
        #     for k, v in self.store.items():
        #         ret += f"key: {str(k)}, value: {str(v.value[1])}\n"
        # elif order == 'list':
        #     node = self.order_list.head
        #     while node:
        #         print(node.value)
        #         # ret += f"key: {str(node.value[0])}, value: {str(node.value[1])}\n"
        #         node = node.next

        ret += '==== end ====\n'
        return ret

    def get(self, key):
        """
        Retrieves the value associated with the given key. Also
        needs to move the key-value pair to the end of the order
        such that the pair is considered most-recently used.
        Returns the value associated with the key or None if the
        key-value pair doesn't exist in the cache.
        """

        node = self.store.get(key, None)
        print('get: ', node)

        if node:
            self.priority_list.move_to_front(node)
            return node.value[1]
        else:
            return None

    def set(self, key, value):
        """
        Adds the given key-value pair to the cache. The newly-
        added pair should be considered the most-recently used
        entry in the cache. If the cache is already at max capacity
        before this entry is added, then the oldest entry in the
        cache needs to be removed to make room. Additionally, in the
        case that the key already exists in the cache, we simply
        want to overwrite the old value associated with the key with
        the newly-specified value.
        """

        node = self.store.get(key, None)
        print('set: ', node)
        node_value = (key, value)

        if node:
            node.value = node_value
            self.priority_list.move_to_front(node)
        else:
            new_node = ListNode(node_value)
            self.priority_list.prepend(new_node)
            self.store[key] = new_node
            self.size += 1

        # cleanup if size > limit
        if self.size > self.limit:
            old_node = self.priority_list.tail
            print(self.priority_list)
            del self.store[old_node.value[0]]
            self.priority_list.remove_from_tail()
            self.size -= 1


if __name__ == '__main__':

    lru = LRUCache()

    lru.set('a', 1)
    lru.set('b', 2)
    lru.set('c', 3)
    lru.set('d', 4)
    lru.set('e', 5)
    lru.set('f', 6)
    lru.set('g', 7)
    lru.set('h', 8)
    lru.set('i', 9)
    lru.set('j', 10)
    lru.set('k', 11)
    lru.set('l', 12)
    lru.set('m', 13)
    lru.set('n', 14)
    lru.get('j')

    print(lru)
    print(len(lru.store))
    print(len(lru.priority_list))

    # lru.set('c', 9)

    # print(lru)

    # print(lru.get('b'))
