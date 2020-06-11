"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
        else:
            if self.right:
                return self.right.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    def get(self, value):
        pass

    # Call the function `fn` on the value of each node
    def for_each(self, fn, method='order', left=True):
        # iterate over the elements of a sorted binary tree
        if method == 'order':
            if self.left:
                self.left.for_each(fn, method)
            fn(self.value)
            if self.right:
                self.right.for_each(fn, method)

        elif method == 'pre-order':
            fn(self.value)
            if self.left:
                self.left.for_each(fn, method)
            if self.right:
                self.right.for_each(fn, method)

        elif method == 'post-order':
            if self.left:
                self.left.for_each(fn, method)
            if self.right:
                self.right.for_each(fn, method)
            fn(self.value)

        elif method == 'iter-dft':
            pending_stack = []
            pending_stack.append(self)
            while len(pending_stack) > 0:
                node = pending_stack.pop()
                if node.left:
                    pending_stack.append(node.left)
                if node.right:
                    pending_stack.append(node.right)
                fn(node.value)

        elif method == 'iter-bft':
            pending_queue = []
            pending_queue.append(self)
            while len(pending_queue) > 0:
                node = pending_queue.pop(0)
                if node.left:
                    pending_queue.append(node.left)
                if node.right:
                    pending_queue.append(node.right)
                fn(node.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, 'order')

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, 'iter-bft')

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node=None):
        if node == None:
            node = self
        node.for_each(print, "iter-dft")

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # if node == None:
        #     node = self
        node.for_each(print, "pre-order")

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node == None:
            node = self
        node.for_each(print, "post-order")


def test():
    bst = BSTNode(1)
    bst.insert(8)
    bst.insert(5)
    bst.insert(7)
    bst.insert(6)
    bst.insert(3)
    bst.insert(4)
    bst.insert(2)

    print('=== in order ===')
    bst.in_order_print()
    print('=== bft order ===')
    bst.bft_print()
    print('=== dft order ===')
    bst.dft_print()


test()

def demo():
    import random

    tree = BSTNode(0)
    for i in range(20):
        tree.insert(random.randint(0, 50))

    val = int(input("Enter an integer from 0-49"))

