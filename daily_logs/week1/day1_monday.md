# Day 1 - Monday: Arrays and Lists

**Date:** 12/01/2026 
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Arrays and Lists - Foundation

---

## Morning Session (8:00 AM - 12:00 PM)

### What I Learned

1. **Array Basics**
   - Understanding arrays as contiguous memory locations
   - Array operations: append, insert, delete
   - Time complexities:
     - Access: O(1)
     - Search: O(n)
     - Insert: O(n)
     - Delete: O(n)

2. **Array Operations Implementation**
   - Created `ArrayOperations` class with basic operations
   - Implemented append, insert, delete methods
   - Added utility methods: find_min, find_max, linear_search

### Code Written

- Created `data_structures/arrays/array_operations.py`
- Implemented ArrayOperations class with:
  - `append(value)` - Add element to end
  - `insert(index, value)` - Insert at specific position
  - `delete(index)` - Remove element at index
  - `find_min()` - Find minimum value
  - `find_max()` - Find maximum value
  - `linear_search(target)` - Search for element
  - `reverse()` - Reverse array in-place
  - `get_size()` - Get array length
  - `is_empty()` - Check if empty

### Challenges Faced

- Understanding in-place operations vs creating new arrays
- Handling edge cases (empty arrays, out of bounds)

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Array Algorithms**
   - Finding second largest element
   - Removing duplicates while preserving order
   - Array rotation
   - Two sum problem (using hash map for O(n) solution)

2. **Problem Solving**
   - Two sum: Used hash map to achieve O(n) time complexity
   - Array rotation: Used reverse technique for in-place rotation

### Code Written

- Added helper functions:
  - `find_second_largest(arr)` - O(n) solution
  - `remove_duplicates(arr)` - O(n) time, O(n) space
  - `rotate_array(arr, k)` - O(n) time, O(1) space
  - `two_sum(arr, target)` - O(n) time, O(n) space

### Tests Performed

- Created comprehensive test suite in `tests/test_arrays.py`
- Tested all methods with:
  - Normal cases
  - Edge cases (empty arrays, single element)
  - Boundary conditions
- All tests passing ✓

### Test Results

```
test_arrays.py::TestArrayOperations::test_append PASSED
test_arrays.py::TestArrayOperations::test_insert PASSED
test_arrays.py::TestArrayOperations::test_delete PASSED
test_arrays.py::TestArrayOperations::test_find_min PASSED
test_arrays.py::TestArrayOperations::test_find_max PASSED
test_arrays.py::TestArrayOperations::test_linear_search PASSED
test_arrays.py::TestArrayOperations::test_reverse PASSED
test_arrays.py::TestArrayOperations::test_get_size PASSED
test_arrays.py::TestArrayOperations::test_is_empty PASSED
test_arrays.py::TestArrayAlgorithms::test_find_second_largest PASSED
test_arrays.py::TestArrayAlgorithms::test_remove_duplicates PASSED
test_arrays.py::TestArrayAlgorithms::test_rotate_array PASSED
test_arrays.py::TestArrayAlgorithms::test_two_sum PASSED
```

---

## Summary

### Time Breakdown
- **Morning:** 4 hours (8 AM - 12 PM)
- **Lunch:** 1 hour (12 PM - 1 PM)
- **Afternoon:** 4 hours (1 PM - 5 PM)
- **Total:** 8 hours

### Files Created
1. `data_structures/arrays/array_operations.py` - Main implementation
2. `tests/test_arrays.py` - Test suite

### Key Takeaways
- Arrays are fundamental and understanding them is crucial
- Time complexity analysis is important for choosing the right approach
- Hash maps can optimize many array problems
- Writing tests helps verify correctness

### Next Steps (Day 2)
- Study Linked Lists
- Understand differences between arrays and linked lists
- Implement singly and doubly linked lists

---

## Notes
- All code is well-commented for future reference
- Tests ensure code correctness
- Ready to move to Day 2: Linked Lists
