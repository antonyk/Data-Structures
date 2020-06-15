Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
- O(1), using the tail of the list

2. What is the runtime complexity of `push` using a linked list?
- O(1), using the head of the list

3. What is the runtime complexity of `pop` using a list?
- O(1), using the tail of the list

4. What is the runtime complexity of `pop` using a linked list?
- O(1), using the head of the list

5. What is the runtime complexity of `len` using a list?
- O(1)

6. What is the runtime complexity of `len` using a linked list?
- O(1) as long as the list stores its size and O(n) if it doesn't

## Queue

1. What is the runtime complexity of `enqueue` using a list?
- O(1)

2. What is the runtime complexity of `enqueue` using a linked list?
- O(1) if it stores a tail pointer, O(n) if it doesn't

3. What is the runtime complexity of `dequeue` using a list?
- O(n)

4. What is the runtime complexity of `dequeue` using a linked list?
- O(1)

5. What is the runtime complexity of `len` using a list?
- O(1)

6. What is the runtime complexity of `len` using a linked list?
- O(1) as long as list stores its len, O(n) otherwise

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?
- O(1)

2. What is the runtime complexity of `ListNode.insert_before`?
- O(1)

3. What is the runtime complexity of `ListNode.delete`?
- O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
- O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
- O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
- O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
- O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
- O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
- O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
- O(1) for delete by node reference, O(n) for deleting by value from unsorted list 
    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
