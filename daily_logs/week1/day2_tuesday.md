# Day 2 - Tuesday: Linked Lists

**Date:** 14/1/2026
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Linked Lists - Singly and Doubly

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Linked List Basics**
   - Understanding nodes and pointers
   - Difference between arrays and linked lists:
     - Arrays: Contiguous memory, O(1) access, O(n) insert/delete
     - Linked Lists: Non-contiguous, O(n) access, O(1) insert/delete at head
   - Dynamic size vs fixed size

2. **Singly Linked List**
   - Each node has value and next pointer
   - Operations:
     - Append: O(n)
     - Prepend: O(1)
     - Insert: O(n)
     - Delete: O(n)
     - Search: O(n)

### Code Written

- Created `data_structures/linked_lists/linked_list.py`
- Implemented `SinglyLinkedList` class with:
  - `append(value)` - Add at end
  - `prepend(value)` - Add at beginning
  - `insert_at(index, value)` - Insert at position
  - `delete(value)` - Delete by value
  - `delete_at(index)` - Delete at position
  - `search(value)` - Find value
  - `get(index)` - Get value at index
  - `reverse()` - Reverse in-place
  - `display()` - Show all values
  - `get_size()` - Get length
  - `is_empty()` - Check if empty

### Challenges Faced

- Understanding pointer manipulation
- Handling edge cases (empty list, single node)
- Reversing linked list without extra space

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Doubly Linked List**
   - Each node has value, next, and prev pointers
   - Can traverse in both directions
   - More memory overhead but more flexibility
   - Operations similar to singly but with prev pointer updates

2. **Linked List Algorithms**
   - Cycle detection using Floyd's algorithm (tortoise and hare)
   - Finding middle node using two pointers
   - Understanding fast and slow pointer technique

### Code Written

- Implemented `DoublyLinkedList` class with:
  - `append(value)` - Add at end
  - `prepend(value)` - Add at beginning
  - `delete(value)` - Delete by value
  - `display_forward()` - Show head to tail
  - `display_backward()` - Show tail to head

- Added helper functions:
  - `detect_cycle(head)` - Floyd's cycle detection
  - `find_middle(head)` - Two-pointer technique

### Tests Performed

- Created comprehensive test suite in `tests/test_linked_lists.py`
- Tested:
  - All singly linked list operations
  - All doubly linked list operations
  - Cycle detection algorithm
  - Middle node finding
- All tests passing ✓

### Test Results

```
test_linked_lists.py::TestSinglyLinkedList::test_append PASSED
test_linked_lists.py::TestSinglyLinkedList::test_prepend PASSED
test_linked_lists.py::TestSinglyLinkedList::test_insert_at PASSED
test_linked_lists.py::TestSinglyLinkedList::test_delete PASSED
test_linked_lists.py::TestSinglyLinkedList::test_delete_at PASSED
test_linked_lists.py::TestSinglyLinkedList::test_search PASSED
test_linked_lists.py::TestSinglyLinkedList::test_get PASSED
test_linked_lists.py::TestSinglyLinkedList::test_reverse PASSED
test_linked_lists.py::TestSinglyLinkedList::test_is_empty PASSED
test_linked_lists.py::TestDoublyLinkedList::test_append PASSED
test_linked_lists.py::TestDoublyLinkedList::test_prepend PASSED
test_linked_lists.py::TestDoublyLinkedList::test_delete PASSED
test_linked_lists.py::TestLinkedListAlgorithms::test_detect_cycle PASSED
test_linked_lists.py::TestLinkedListAlgorithms::test_find_middle PASSED
```

---

## Summary

- **Morning:** 5 hours (8 AM - 1 PM)
- **Lunch:** 1 hour (1 PM - 2 PM)
- **Afternoon:** 3 hours (2 PM - 5 PM)
- **Total:** 8 hours
- **Note that I start the afternoon at 12pm so that they are both 4 hours**

### Files Created
1. `data_structures/linked_lists/linked_list.py` - Main implementation
2. `tests/test_linked_lists.py` - Test suite

### Key Takeaways
- Linked lists are dynamic and memory-efficient for frequent insertions/deletions
- Two-pointer technique is powerful for many linked list problems
- Understanding pointers is crucial for linked list manipulation
- Doubly linked lists trade memory for bidirectional traversal

### Next Steps (Day 3)
- Study Stacks and Queues
- Understand LIFO and FIFO principles
- Implement using arrays and linked lists

---

## Notes
- Pointer manipulation requires careful attention
- Edge cases are critical in linked list operations
- Ready to move to Day 3: Stacks and Queues
