# Day 3 - Wednesday: Stacks and Queues

**Date:** [Date]  
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Stacks and Queues - LIFO and FIFO

---

## Morning Session (8:00 AM - 12:00 PM)

### What I Learned

1. **Stacks (LIFO - Last In First Out)**
   - Operations: push, pop, peek
   - Can be implemented using arrays or linked lists
   - Time complexities:
     - Push: O(1)
     - Pop: O(1)
     - Peek: O(1)
   - Applications:
     - Function call stack
     - Expression evaluation
     - Parentheses matching
     - Undo operations

2. **Stack Implementations**
   - Array-based: Simple, but may need resizing
   - Linked list-based: Dynamic, no size limit

### Code Written

- Created `data_structures/stacks/stack.py`
- Implemented `ArrayStack` class:
  - `push(value)` - Add to top
  - `pop()` - Remove from top
  - `peek()` - View top element
  - `is_empty()` - Check if empty
  - `size()` - Get size
  - `display()` - Show all elements

- Implemented `LinkedStack` class:
  - Same operations as ArrayStack
  - Uses linked list for dynamic sizing

### Challenges Faced

- Understanding LIFO principle
- Handling empty stack exceptions
- Deciding between array and linked list implementation

---

## Afternoon Session (1:00 PM - 5:00 PM)

### What I Learned

1. **Queues (FIFO - First In First Out)**
   - Operations: enqueue, dequeue, front, rear
   - Time complexities:
     - Enqueue: O(1)
     - Dequeue: O(1) for linked list, O(n) for array
   - Applications:
     - Task scheduling
     - Breadth-first search
     - Print queue
     - Message queues

2. **Queue Variants**
   - Standard Queue: Basic FIFO
   - Circular Queue: Efficient array-based queue
   - Deque (Double-ended Queue): Can add/remove from both ends
   - Priority Queue: (Will cover later)

3. **Stack Applications**
   - Parentheses matching
   - Postfix expression evaluation
   - String reversal

### Code Written

- Created `data_structures/queues/queue.py`
- Implemented `ArrayQueue` class:
  - `enqueue(value)` - Add to rear
  - `dequeue()` - Remove from front
  - `front()` - View front element
  - `rear()` - View rear element
  - `is_empty()` - Check if empty
  - `size()` - Get size

- Implemented `LinkedQueue` class:
  - Same operations, O(1) dequeue

- Implemented `CircularQueue` class:
  - Fixed capacity
  - Efficient use of space
  - Circular array implementation

- Implemented `Deque` class:
  - `add_front(value)` - Add to front
  - `add_rear(value)` - Add to rear
  - `remove_front()` - Remove from front
  - `remove_rear()` - Remove from rear
  - `peek_front()` - View front
  - `peek_rear()` - View rear

- Added stack algorithms:
  - `is_balanced_parentheses(s)` - Check balanced parentheses
  - `evaluate_postfix(expression)` - Evaluate postfix notation
  - `reverse_string(s)` - Reverse using stack

### Tests Performed

- Created test suites:
  - `tests/test_stacks.py` - All stack tests
  - `tests/test_queues.py` - All queue tests
- Tested:
  - All stack operations
  - All queue operations
  - Stack algorithms
  - Edge cases (empty stacks/queues)
- All tests passing ✓

### Test Results

```
test_stacks.py::TestArrayStack::test_push_pop PASSED
test_stacks.py::TestArrayStack::test_peek PASSED
test_stacks.py::TestArrayStack::test_is_empty PASSED
test_stacks.py::TestArrayStack::test_size PASSED
test_stacks.py::TestLinkedStack::test_push_pop PASSED
test_stacks.py::TestLinkedStack::test_peek PASSED
test_stacks.py::TestLinkedStack::test_is_empty PASSED
test_stacks.py::TestStackAlgorithms::test_balanced_parentheses PASSED
test_stacks.py::TestStackAlgorithms::test_evaluate_postfix PASSED
test_stacks.py::TestStackAlgorithms::test_reverse_string PASSED

test_queues.py::TestArrayQueue::test_enqueue_dequeue PASSED
test_queues.py::TestArrayQueue::test_front_rear PASSED
test_queues.py::TestArrayQueue::test_is_empty PASSED
test_queues.py::TestLinkedQueue::test_enqueue_dequeue PASSED
test_queues.py::TestLinkedQueue::test_front PASSED
test_queues.py::TestCircularQueue::test_enqueue_dequeue PASSED
test_queues.py::TestCircularQueue::test_is_full PASSED
test_queues.py::TestDeque::test_add_remove_front PASSED
test_queues.py::TestDeque::test_add_remove_rear PASSED
test_queues.py::TestDeque::test_peek PASSED
```

---

## Summary

### Time Breakdown
- **Morning:** 4 hours (8 AM - 12 PM)
- **Lunch:** 1 hour (12 PM - 1 PM)
- **Afternoon:** 4 hours (1 PM - 5 PM)
- **Total:** 8 hours

### Files Created
1. `data_structures/stacks/stack.py` - Stack implementations
2. `data_structures/queues/queue.py` - Queue implementations
3. `tests/test_stacks.py` - Stack tests
4. `tests/test_queues.py` - Queue tests

### Key Takeaways
- Stacks are LIFO, perfect for recursion and backtracking
- Queues are FIFO, essential for BFS and scheduling
- Circular queues efficiently use fixed-size arrays
- Deques provide flexibility for both ends
- Stack-based algorithms solve many parsing problems

### Next Steps (Day 4)
- Study Trees
- Understand binary trees and binary search trees
- Learn tree properties and terminology

---

## Notes
- LIFO vs FIFO is fundamental to many algorithms
- Choosing the right data structure depends on access patterns
- Ready to move to Day 4: Trees
