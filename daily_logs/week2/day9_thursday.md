# Day 9 - Thursday: Searching Algorithms

**Date:** 22/01/2025
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Searching Algorithms

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Basic Searching**
   - **Linear Search:**
     - Check each element sequentially
     - Time: O(n), Space: O(1)
     - Works on unsorted arrays
   - **Binary Search:**
     - Divide and conquer on sorted array
     - Time: O(log n), Space: O(1)
     - Requires sorted array
     - Iterative and recursive implementations

2. **Binary Search Variations**
   - Standard binary search
   - Finding first occurrence
   - Finding last occurrence
   - Counting occurrences

### Code Written

- Created `algorithms/searching/searching_algorithms.py`
- Implemented basic searches:
  - `linear_search(arr, target)` - Linear search
  - `binary_search(arr, target)` - Iterative binary search
  - `binary_search_recursive(arr, target)` - Recursive binary search
  - `find_first_occurrence(arr, target)` - First occurrence
  - `find_last_occurrence(arr, target)` - Last occurrence
  - `count_occurrences(arr, target)` - Count occurrences

### Challenges Faced

- Understanding binary search edge cases
- Handling duplicate elements
- Implementing first/last occurrence correctly

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Advanced Searching Algorithms**
   - **Interpolation Search:**
     - Uses value distribution
     - Time: O(log log n) average, O(n) worst
     - Better than binary for uniformly distributed data
   - **Jump Search:**
     - Jump ahead by fixed steps
     - Time: O(√n), Space: O(1)
     - Between linear and binary
   - **Exponential Search:**
     - Find range, then binary search
     - Time: O(log n), Space: O(1)
     - Good for unbounded arrays

2. **Search Algorithm Selection**
   - Unsorted: Linear search
   - Sorted, random access: Binary search
   - Sorted, uniform distribution: Interpolation search
   - Sorted, unbounded: Exponential search

### Code Written

- Implemented advanced searches:
  - `interpolation_search(arr, target)` - Interpolation search
  - `jump_search(arr, target)` - Jump search
  - `exponential_search(arr, target)` - Exponential search
  - `binary_search_range(arr, target, left, right)` - Range search

### Tests Performed

- Created test suite in `tests/test_searching.py`
- Tested all searching algorithms
- Verified with various test cases
- All tests passing ✓

### Test Results

```
test_searching.py::TestSearchingAlgorithms::test_linear_search PASSED
test_searching.py::TestSearchingAlgorithms::test_binary_search PASSED
test_searching.py::TestSearchingAlgorithms::test_binary_search_recursive PASSED
test_searching.py::TestSearchingAlgorithms::test_interpolation_search PASSED
test_searching.py::TestSearchingAlgorithms::test_jump_search PASSED
test_searching.py::TestSearchingAlgorithms::test_exponential_search PASSED
test_searching.py::TestSearchingAlgorithms::test_find_first_occurrence PASSED
test_searching.py::TestSearchingAlgorithms::test_find_last_occurrence PASSED
test_searching.py::TestSearchingAlgorithms::test_count_occurrences PASSED
```

---

## Summary

### Files Created
1. `algorithms/searching/searching_algorithms.py` - All searching algorithms

### Key Takeaways
- Linear search: Simple, works on any array
- Binary search: Fast, requires sorted array
- Different searches for different scenarios
- Understanding data distribution helps choose algorithm
- First/last occurrence variations are useful
- Search algorithms are fundamental building blocks

### Next Steps (Day 10)
- Study Dynamic Programming
- Understand memoization and tabulation
- Learn common DP patterns

---

## Notes
- Searching is fundamental to many algorithms
- Binary search is powerful for sorted data
- Ready to move to Day 10: Dynamic Programming
