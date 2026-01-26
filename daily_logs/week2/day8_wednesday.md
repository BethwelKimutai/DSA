# Day 8 - Wednesday: Sorting Algorithms

**Date:** 21/01/2026
**Time:** 8:00 AM - 5:00 PM  
**Topic:** Sorting Algorithms

---

## Morning Session (8:00 AM - 1:00 PM)

### What I Learned

1. **Basic Sorting Algorithms**
   - **Bubble Sort:**
     - Compare adjacent elements, swap if needed
     - Time: O(n²), Space: O(1)
     - Stable, in-place
   - **Selection Sort:**
     - Find minimum, swap with current position
     - Time: O(n²), Space: O(1)
     - Not stable, in-place
   - **Insertion Sort:**
     - Build sorted array one element at a time
     - Time: O(n²) worst, O(n) best, Space: O(1)
     - Stable, in-place, good for small arrays

2. **Comparison-Based Sorting**
   - All comparison-based sorts have Ω(n log n) lower bound
   - Can't do better than O(n log n) with comparisons

### Code Written

- Created `algorithms/sorting/sorting_algorithms.py`
- Implemented basic sorts:
  - `bubble_sort(arr)` - Bubble sort with early termination
  - `selection_sort(arr)` - Selection sort
  - `insertion_sort(arr)` - Insertion sort

### Challenges Faced

- Understanding when to use each algorithm
- Optimizing bubble sort with early termination
- Understanding stability concept

---

## Afternoon Session (2:00 PM - 5:00 PM)

### What I Learned

1. **Efficient Sorting Algorithms**
   - **Merge Sort:**
     - Divide and conquer
     - Time: O(n log n), Space: O(n)
     - Stable, not in-place
   - **Quick Sort:**
     - Divide and conquer with pivot
     - Time: O(n log n) average, O(n²) worst, Space: O(log n)
     - Not stable, in-place
   - **Heap Sort:**
     - Uses heap data structure
     - Time: O(n log n), Space: O(1)
     - Not stable, in-place

2. **Non-Comparison Sorts**
   - **Counting Sort:**
     - For integers in small range
     - Time: O(n + k), Space: O(k)
   - **Radix Sort:**
     - Sort by digits
     - Time: O(d * n), Space: O(n)

3. **Algorithm Selection**
   - Small arrays: Insertion sort
   - General purpose: Quick sort or Merge sort
   - Stable needed: Merge sort
   - Integer sorting: Counting/Radix sort

### Code Written

- Implemented efficient sorts:
  - `merge_sort(arr)` - Merge sort
  - `quick_sort(arr)` - Quick sort (functional)
  - `quick_sort_inplace(arr)` - In-place quick sort
  - `partition(arr, low, high)` - Partition helper
  - `heap_sort(arr)` - Heap sort
  - `heapify(arr, n, i)` - Heapify helper
  - `counting_sort(arr, max_val)` - Counting sort
  - `radix_sort(arr)` - Radix sort
  - `counting_sort_by_digit(arr, exp)` - Helper for radix

### Tests Performed

- Created test suite in `tests/test_sorting.py`
- Tested all sorting algorithms
- Verified correctness with various inputs
- All tests passing ✓

### Test Results

```
test_sorting.py::TestSortingAlgorithms::test_bubble_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_selection_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_insertion_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_merge_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_quick_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_heap_sort PASSED
test_sorting.py::TestSortingAlgorithms::test_counting_sort PASSED
```

---

## Summary

### Files Created
1. `algorithms/sorting/sorting_algorithms.py` - All sorting algorithms

### Key Takeaways
- Different sorts for different scenarios
- O(n log n) is optimal for comparison-based sorts
- Merge sort is stable, Quick sort is fast
- Non-comparison sorts can be O(n) for special cases
- Understanding trade-offs helps choose the right algorithm
- In-place vs extra space is important consideration

### Next Steps (Day 9)
- Study Searching Algorithms
- Understand binary search variations
- Learn when to use each search method

---

## Notes
- Sorting is fundamental to many algorithms
- Understanding complexity helps choose right algorithm
- Ready to move to Day 9: Searching Algorithms
